QEMU TCG and KVM mode
---------------------
code 切成 2 個 part，根據 kvm/tcg mode 決定跑哪一份 (`kvm_enabled()/tcg_enabled()`)

note: TCG - Tiny Code Generator, the JIT binary translator in qemu for emulation.


QEMU programming technique/architecture
---------------------------------------
1. qemu mainloop:

    - `qemu/main-loop.h`, `main-loop.c`
    - `qemu_set_fd_handler, qemu_set_fd_handler2`

2. qemu coroutine: http://blog.vmsplice.net/2014/01/coroutines-in-qemu-basics.html

    ::

        qemu_coroutine_create(process_incoming_migration_co);
        qemu_coroutine_enter(co, f);


3. QEMUFile struct

    ::

        qemu_loadvm_state(QEMUFile* f);
        qemu_fclose(QEMUFile* f);

        // 使用 qemu_fopen_ops() 函數註冊此 struct (assign many function pointer)
        qemu_fopen_ops()
            QEMUFile* f
            f = qemu_mallocz(sizeof(QEMUFile))
            assign(opaque, put_buffer, get_buffer, close, rate_limit, set_rate_limit, get_rate_limit) from function parameter.
            f->buf_max_size = IO_BUF_SIZE;
            f->buf = qemu_malloc(sizeof(uint8_t) * f->buf_max_size);

        struct QEMUFile {
            // six function pointer (put_buffer ... etc).
            void *opaque;
            int is_write;             

            int64_t buf_offset; /* start of buffer when writing, end of buffer
                                   when reading */
            int buf_index;            
            int buf_size; /* 0 when writing */ 
            int buf_max_size;
            uint8_t *buf;             
            
            int has_error;            
        };  

4. bdrv

    感覺跟 block device 有關.
    ::

        bdrv_snapshot

        bdrv_read/bdrv_write
        bdrv_aio_readv/bdrv_aio_writev

5. loadvm/savevm

    ::

        # qemu shapshot: http://www.xuebuyuan.com/2192772.html
        A) bdrv_snapshots()
        B) vm_stop()
        C) qemu_savevm_state()
        D) bdrv_snapshot_create()
        E) vm_start()

        qemu_savevm_state()
           A) qemu_savevm_state_begin()
           B) qemu_savevm_state_iterate()
           C) qemu_savevm_state_complete()

6. data structure 

    - ``include/qapi/qmp/qdict.h``

        - 根據 ``DictEntry``, 猜測是 linked list based map.

reference
---------
1. http://people.cs.nctu.edu.tw/~chenwj/slide/QEMU/KVM-introduction-01.txt
2. http://people.cs.nctu.edu.tw/~chenwj/slide/QEMU/KVM-introduction-02.txt
3. http://people.cs.nctu.edu.tw/~chenwj/slide/QEMU/KVM-introduction-03.txt
4. https://www.kernel.org/doc/Documentation/virtual/kvm/api.txt
5. QEMU source code notes: http://chenyufei.info/notes/qemu-src.html
