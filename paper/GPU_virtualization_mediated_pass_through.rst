- paper name: A Full GPU Virtualization Solution with Mediated Pass-Through
- link: https://www.usenix.org/system/files/conference/atc14/atc14-paper-tian.pdf

Outline
-------

Note
----
1. 4 GPU virtualization technique

  - Slow to Fast

    - Device Emulation (trap-and-emulate)
    - API Forwarding (ex. OpenGL API)
    - Mediate Pass-Through 
    - Direct Pass-Through

  - Device Emulation (trap-and-emulate)

    - too slow
    - complete sharing and feature

  - Direct Pass-Through
    
    - nearly 100% performance
    - no sharing, only 1 VM can use

  - API Forwarding (ex. OpenGL API)

    - slow than Mediated Pass-Through, sharing better than Pass-Through
    - hard to support full feature
      
      - complexity of guest graphic stack
      - API compatibility between different OSes.

  - Mediated Pass-Through

    - pass performance-critical resources, emulate privileged instruction
    - only sharing 7 VM for good performance

2. GPU model

   - Intel Graphic

     - rendering engine and display engine
     - use system memory
     - memory: page table

       - Global Graphic Memory: 2GB virtual address space, accessed by CPU and GPU
       - Local Graphic Memory: Multiple 2GB virtual address space, only accessed by render engine
     
     - CPU fetch commands to ring buffer for GPU (needed for supplement)
     - 4 critical interface

       - frame buffer
       - command buffer
       - GPU Page Table Entries (PTE)
         - GPU Page Table
         - Memory-Mapped I/O && Port Mapped I/O registers
       - PCI configuration space register 
