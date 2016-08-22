- source code

  - kvm-related source code in QEMU
  - kvm source code (Linux Kernel)

- QEMU interaction with kvm (ioctl)

  - ioctl wrapper detail trace

- QEMU-kvm/guest OS in linux kernel (and scheduling)
- enter/exit in kvm

Source Code
-----------

- kvm-related QEMU ource code

  - ``kvm-all.c``
  - ``target-arm/kvm.c``

- kvm source code (Linux kernel module)

  - `virt/kvm/*`
  - `arch/arm/kvm/*`
  - `include/linux/kvm_*.h`
  - `arch/arm/include/asm/kvm_*.h`
  - `Documentation/virtual/kvm/api.txt`

QEMU interaction with kvm(ioctl)
--------------------------------
kvm 為 linux kernel module, 把功能藉由擴充 ioctl system call 來 pass through 給 userspace 的 QEMU.

QEMU 藉由對 kvm device 作 ioctl, 對 kvm 發出 request.

- detail 

    - `Documentation/virtual/kvm/api.txt`
    - kvm API is set of ioctls in three kinds

        - System ioctls: `/dev/kvm`
        - VM ioctls
        - vcpu ioctls

    - example, one VM with 2 vcpu

        ::

            # file descriptors
            QEMU    1888 susu    8u      CHR             10,232        0t0      330 /dev/kvm
            QEMU    1888 susu    9u  a_inode                0,9          0     7626 kvm-vm
            QEMU    1888 susu   12u  a_inode                0,9          0     7626 kvm-vcpu
            QEMU    1888 susu   13u  a_inode                0,9          0     7626 kvm-vcpu

    - QEMU functions (`kvm_all.c`, `tar`)
        
        - doing system call to specific fd
        - three kinds ioctl

            - `int kvm_ioctl(KVMState *s, int type, ...)`
            - `int kvm_vm_ioctl(KVMState *s, int type, ...)`
            - `int kvm_vcpu_ioctl(CPUState *s, int type, ...)`
            - `int kvm_device_ioctl(int fd, int type, ...)`

    - kvm functions (`virt/kvm/kvm_all.c`)
        
        - system call implementation.
        - three kinds ioctl: `kvm_dev_ioctl`, `kvm_vm_ioctl`, `kvm_vcpu_ioctl`
        - architecture dependent system call: `kvm_arch_vm_ioctl`

QEMU 會替每一個虛擬 CPU (VCPU) 維護一個 CPUState 的資料結構.

在引入 KVM 之後, QEMU 在 ``CPU_COMMON`` 這個巨集 (cpu-defs.h) 裡的 CPUState 裡面加了幾個 KVM 需要的欄位.

::

    #define CPU_COMMON
        struct KVMState *kvm_state;                                         \
        struct kvm_run *kvm_run;                                            \
        int kvm_fd; // VCPU fd                                              \
        int kvm_vcpu_dirty;

QEMU call kvm ioctl trace code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- kvm_arch_vm_ioctl

  - arch-dependent kvm feature
  - detail::

      int kvm_vm_ioctl(KVMState *s, int type, ...)
      long kvm_arch_vm_ioctl(struct file *filp, unsigned int ioctl, unsigned long arg)

      when does kvm_vm_ioctl() calls kvm_arch_vm_ioctl()?

      if type is architecture type
      where filp = s.vmid
            ioctl = type
            arg = vargs( ... )
        
            return value = return value, for value != -1
                       = errno, for value == -1

- function prototype

    - `[QEMU][args] int kvm_vm_ioctl(KVMState *s, int type, ...) (in kvm-all.c)`
    - `[glibc/syscall][argv] int ioctl (int __fd, unsigned long int __request, ...)`
    - `[kvm] long kvm_vm_ioctl(struct file *filp, unsigned int ioctl, unsigned long arg) (virt/kvm/kvm_main.c)`
    - `[kvm] long kvm_arch_vm_ioctl(struct file *filp, unsigned int ioctl, unsigned long arg) (arch/arm/kvm/arm.c)`

- real function call

    - `[QEMU] save_s2_pgd( ... ) (in target-arm/kvm.c)` 
    - `[QEMU] s2_size = kvm_vm_ioctl(s, KVM_ARM_GET_S2_PGD_SIZE);`
    - `[libc call/syscall] ret = ioctl(s->vmfd, type, arg);`
    - `[kvm] ret = kvm_vm_ioctl(s->vmfd, type, arg);`
    - `[kvm] r = kvm_arch_vm_ioctl(filp, ioctl, arg);`
    - `[kvm] return PTRS_PER_S2_PGD * sizeof(pgd_t);`

QEMU-kvm/guest OS and linux kernel scheduling
---------------------------------------------
example, one VM with 2 vcpu
::

    # QEMU process view
    1888 susu       20   0 1104M  301M 28088 S  0.0  2.5  3:55.18 QEMU -enable-kvm

    # QEMU thread view
    1888 susu       20   0 1104M  301M 28088 S  0.0  2.5  3:55.18 QEMU -enable-kvm
    1891 susu       20   0 1104M  301M 28088 S  0.0  2.5  0:12.45 ├─ QEMU -enable-kvm
    1890 susu       20   0 1104M  301M 28088 S  0.0  2.5  0:30.49 └─ QEMU -enable-kvm

[guess] QEMU 的 3 thread 應該是 QEMU main thread, 2 個 vcpu 各分一個 thread

host OS/QEMU/guest OS
~~~~~~~~~~~~~~~~~~~~~


:: 
    +----------------------------------------------------------+
    |                                                          |
    |  +-----------+    +--------------------+                 |
    |  |           |    |                    |                 |
    |  |           |    |  +--------------+  |                 |
    |  |           |    |  |              |  |                 |
    |  |           |    |  |   guest OS   <---------+          |
    |  |           |    |  |              |  |      |          |
    |  |           |    |  +--------------+  |      | VM enter |
    |  |           |    |                    |      |          |
    |  |           |    | QEMU --enable-kvm  |      |          |
    |  |   Host    |    |                    |      |          |
    |  |  process  |    |   Host process     |      |          |
    |  |           |    |                    |      |          |
    |  +-------+---+    +---------^------+---+      |          |
    |          |                  |      |          |          |
    |          |  context switch  |      |  syscall |          |
    |          |                  |      |  ioctl() |          |
    |      +---v------------------+----+-v----------++         |
    |      |                           |             |         |
    |      |    Host OS(linux kernel)  |     kvm     |         |
    |      |                           |             |         |
    |      +---------------------------+-------------+         |
    |                                                          |
    +----------------------------------------------------------+

enter && exit from kvm
----------------------

- `int kvm_cpu_exec(CPUArchState *env) in kvm_all.c`

    - 負責 VMEnter 以及 handling VMExit 需做的操作.

flow chart
::

     QEMU (user mode)       KVM (kernel mode)        Guest VM (guest mode)

        Issue Guest
  -->                 -------------
 |    Execution ioctl              |
 |                                 |
 |          (1)                    |
 |                                 v
 |
 |                        --> Enter Guest Mode ---------------
 |                       |                                    |
 |                       |                                    |
 |                       |                                    |
 |                       |                                    v
 |                       |              
 |                       |                             Execute natively
 |                       |           
 |                       |                               in Guest Mode
 |                       |              
 |                       |                                    |
 |                       |                                    |
 |                       |                                    |
 |                       |    Handle Exit     <--------------- 
 |                       |
 |                       |        |              
 |                       |        |
 |                       |        |
 |                       |        v 
 |                    Y  |
 |           ------------------- I/O?
 |          |            |
 |          |            |        |
 |          |            |        | N
 |          v            |        |
 |                       |   Y    v
  ----  Handle I/O <----------- Signal
                         |
           (2)           |     Pending?
                         | 
                         |        |
                         |        | N
                         |        |
                         --------- 

address translation
-------------------

- QEMU without virtualization

  ::

    GVA -----------> GPA ------------> HVA -------------> HPA
          Guest OS           QEMU             Host OS
         page table         KVMSlot         page table

  - GVA: Guest Virtual Address
  - GPA: Guest Physical Address
  - HVA: Host Virtual Address
  - HPA: Host Physical Address

- 當使用 Hardware Assisted Virtualization 時, GPA -> HPA 用 HAV 支援的 page table 做轉換??

  - in x86, yes: http://people.cs.nctu.edu.tw/~chenwj/slide/QEMU/KVM-mmu.txt 
  - in arm?

reference
---------

1. http://people.cs.nctu.edu.tw/~chenwj/slide/QEMU/KVM-introduction-01.txt
2. http://people.cs.nctu.edu.tw/~chenwj/slide/QEMU/KVM-introduction-02.txt
3. http://people.cs.nctu.edu.tw/~chenwj/slide/QEMU/KVM-introduction-03.txt
4. https://www.kernel.org/doc/Documentation/virtual/kvm/api.txt
5. QEMU source code notes: http://chenyufei.info/notes/QEMU-src.html
