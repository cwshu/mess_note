Prepare:

   - cmake, ninja-build, dtc

Prepare Toolchains:

   1. zephyr sdk
   2. custom (e.g. from distro)

Build::
   
   cd <zephyr_source>
   source zephyr-env.sh

   # custom toolchain
   (fish) set -x ZEPHYR_TOOLCHAIN_VARIANT cross-compile
   (fish) set -x CROSS_COMPILE /usr/bin/arm-none-eabi-

   cd samples/hello_world/
   mkdir build
   cd build/
   cmake -GNinja -DBOARD=qemu_cortex_m3 ..

   # build
   ninja
   # run
   ninja run

reference
---------

Toolchain:

  - Use Custom Cross Compilers: http://docs.zephyrproject.org/getting_started/getting_started.html#using-custom-cross-compilers
  - Install zephyr sdk: http://docs.zephyrproject.org/getting_started/installation_linux.html

Build and Run:

  - Building and Running an Application: http://docs.zephyrproject.org/getting_started/getting_started.html#building-a-sample-application
  - ARM Cortex-M3 Emulation (QEMU): http://docs.zephyrproject.org/boards/arm/qemu_cortex_m3/doc/board.html
  - RISCV32 Emulation (QEMU): http://docs.zephyrproject.org/boards/riscv32/qemu_riscv32/doc/board.html

Zephyr Demos:

  - Samples and Demos: http://docs.zephyrproject.org/samples/samples.html
