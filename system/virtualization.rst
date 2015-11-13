virtualization basic
--------------------
- Virtualization Theory (Formal Requirements for Virtualizable Third Generation Architecture (1974))

  - sensitive instruction

    - mode referencing instruction
    - sensitive register/memory access instruction
    - storage protection system referencing instruction
    - all I/O instruction (guess: memory-mapped + port-mapped I/O)

  - privileged instruction

intel VT series
---------------
- intel VT-x and VT-i: VT for x86 and itanium(IA 64)
- intel VT-d: Virtualization of Direct IO

- VT-x

  - two forms
  - VMX root operation and non-root operation
  - EPT(Extended Page Tables): page table virtualization
  - VMCS(Virtual machine control structure) shadowing accelerates nested virtualization

- VT-d 
  
  - DMA remapping
  - DMA 相關問題
  
      DMA 發出的中斷為 MSI(message signaled interrupt), MSI 中要含有 device 的 memory address.
      如果要虛擬化, DMA 就要可以 access host + all vm 的 memory address, 隔離效果不好.
      解法: interrupt remapping: MSI 改成放 message id, 維護一個 message id to VM 區域的 table

- More

  - Page Table Virtualization

    - VPIDs(vcpu id), EPT.

- trap in Hardware Assisted Virtualization
  
  - http://pages.cs.wisc.edu/~remzi/OSTEP/vmm-intro.pdf

ref
+++
- intel VT instructions: 

  - http://linasm.sourceforge.net/docs/instructions/vme.php
  - http://virtualizationtechnologyvt.blogspot.tw/2009/04/vmx-instructions-in-x86.html

- Advanced x86: Intel Hardware Assisted Virtualization Slides
  
  - https://drive.google.com/folderview?pli=1&ddrp=1&id=0B25hHW4ATym7Z1pTUUs0cEhOMHc
