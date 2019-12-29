::

    lsmod                       # list all loaded kernel modules
    modinfo <module_name>       # list info of one kernel module
    systool -v -m <module_name>

    # add and remove kernel module
    insmod/rmmod

      # modprobe also process dependency of kernel modules
    modprobe -c | grep <module_name>
    modprobe --show-depends <module_name>
