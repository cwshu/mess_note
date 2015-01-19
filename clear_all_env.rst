[備份]

clear all environment variable

glibc 2.0 以上有 clearenv() 支援, 根據下面的資料 bionic 應該也有實作.
不過其他平台應該如何實作這個功能?

查了一些現有的實作來參考.

- glibc(__gnat_clearenv): 

  - https://github.com/gcc-mirror/gcc/blob/master/gcc/ada/env.c

- bionic:

  - https://code.google.com/p/android-source-browsing/source/browse/libc/bionic/clearenv.c?repo=platform--bionic&r=fc10b24accd082fb33c8f92ff8b92481c22fe3dc

- cpython(實作 keys, dumps 出來在各自 unsetenv):

  - http://blog.labix.org/2007/10/17/pythons-osenviron
