qemu -enable-kvm -hda <image> -vga std -cpu host -smp 2 -m 512MB \
-net nic,vlan=0 \
-net user,hostfwd=tcp:127.0.0.1:50022-:22 \
-monitor telnet:0.0.0.0:60023,server,nowait 

network
-------
http://en.wikibooks.org/wiki/QEMU/Networking
- usermode (default)
- redirection
- TAP networking
- VDE networking

redirection example::

    -net user,hostfwd=tcp:127.0.0.1:2522-:22
    # host(127.0.0.1):2522 -> guest:22
    # hostfwd=[<host_ip>]:<host_port>-[<guest_ip>]:<guest_port>

monitor mode
------------
control the running VM.

- redirect monitor to host OS tcp socket::

  -monitor telnet:0.0.0.0:60023,server,nowait # qemu command line option

http://wiki.qemu.org/download/qemu-doc.html#pcsys_005fmonitor
http://en.wikibooks.org/wiki/QEMU/Monitor#Devices

examples::

    info network
    help hostfwd_add
    hostfwd_add tcp:127.0.0.1:8000-:8000

monitor mode 下的 ``hostfwd_add tcp:127.0.0.1:8000-:8000`` command 似乎無效, 待尋找原因.
