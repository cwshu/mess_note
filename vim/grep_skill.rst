General
-------

- function call::

    grep -e ' <funcname>('
    grep -e ' inet_\w*('

- C struct member and member method(function pointer member in fact)::

    greps -e '[.>]<method>'
    greps -e '[.>]region_add'

Linux Kernel
------------

- system call::

    grep -e 'SYSCALL_DEFINE' | grep -e 'sendfile'
    grep -e 'SYSCALL_DEFINE[0-9](.*sendfile'

- file system syscall::

    grep -e 'file_operations'

- kthread::

    # kthread name:
    grep -e 'kswapd'
    
    grep -e 'kthread_\(run\|create\|thread\)(.*)'
