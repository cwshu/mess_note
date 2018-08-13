debian multiarch
================

- install path: /usr/lib/<GNU triplet>/
- usage
        
  - cross compilation: In multiarch, build-time library path and runtime library path is same for cross compilation.
  - QEMU emulate environment (binfmt-misc)
  - install 32-bit proprietary program dependencies on 64-bit system

- "Multi-Arch" field in package

  - same
  - foreign
  - allowed

Multiarch and lib32/lib64
-------------------------

example: zlib

- amd64 package: /lib/x86_64-linux-gnu/libz.so.1.2.8
- amd64 lib32 package: /usr/lib32/libz.so.1.2.8
- i386 package: /lib/i386-linux-gnu/libz.so.1.2.8

zlib is "Multi-Arch: same" package::

  $ apt-cache show zlib1g:amd64 | grep "Multi-Arch"
  Multi-Arch: same
  Multi-Arch: same

  $ apt-cache show zlib1g:i386 | grep "Multi-Arch"
  Multi-Arch: same
  Multi-Arch: same

reference
---------

- `FOSDEM: Multiarch on Debian and Ubuntu <https://lwn.net/Articles/482952/>`_
- `Debian: Multiarch HOWTO <https://wiki.debian.org/Multiarch/HOWTO>`_
- `Debian: Multiarch LibraryPathOverview - Multiarch and multilib <https://wiki.debian.org/Multiarch/LibraryPathOverview#Multiarch_and_multilib>`_
