- memory types & cache control.
- x86 use MTRR(Memory Type and Range Registers) and PAT(Page Attribute Table) to control memory type.

----

- x86 memory types: UC, WC, WT, WB

  .. image:: img/x86_mem_type.png

- cache control registers and bits

  - MTRR register
  - PAT
    
    - PAT, PCD, PWT bit in page table entry
    - IA32_PAT MSR

  - G bit in page table entry
  - CR0's CD, NW bit
  - CR3's PCD, PWT bit
  - CR4's PGE bit

  .. image:: img/x86_cache_control_regs_bits.png

Linux usage::
    
    -------------------------------------------------------------------
    API                    |    RAM   |  ACPI,...  |  Reserved/Holes  |
    -----------------------|----------|------------|------------------|
    ioremap                |    --    |    UC      |       UC         |
    ioremap_cache          |    --    |    WB      |       WB         |
    ioremap_nocache        |    --    |    UC      |       UC         |
    ioremap_wc             |    --    |    --      |       WC         |
    set_memory_uc          |    UC    |    --      |       --         |
     set_memory_wb         |          |            |                  |
    set_memory_wc          |    WC    |    --      |       --         |
     set_memory_wb         |          |            |                  |
                           |          |            |                  |
    pci sysfs resource     |    --    |    --      |       UC         |
    pci sysfs resource_wc  |    --    |    --      |       WC         |
     is IORESOURCE_PREFETCH|          |            |                  |
    pci proc               |    --    |    --      |       UC         |
     !PCIIOC_WRITE_COMBINE |          |            |                  |
    pci proc               |    --    |    --      |       WC         |
     PCIIOC_WRITE_COMBINE  |          |            |                  |
                           |          |            |                  |
    /dev/mem               |    --    |    UC      |       UC         |
     read-write            |          |            |                  |
    /dev/mem               |    --    |    UC      |       UC         |
     mmap SYNC flag        |          |            |                  |
    /dev/mem               |    --    |  WB/WC/UC  |    WB/WC/UC      |
     mmap !SYNC flag       |          |(from exist-|  (from exist-    |
     and                   |          |  ing alias)|    ing alias)    |
     any alias to this area|          |            |                  |
    /dev/mem               |    --    |    WB      |       WB         |
     mmap !SYNC flag       |          |            |                  |
     no alias to this area |          |            |                  |
     and                   |          |            |                  |
     MTRR says WB          |          |            |                  |
    /dev/mem               |    --    |    --      |    UC_MINUS      |
     mmap !SYNC flag       |          |            |                  |
     no alias to this area |          |            |                  |
     and                   |          |            |                  |
     MTRR says !WB         |          |            |                  |
    ------------------------------------------------------------------

example memory types setting:

    .. image:: img/set_mem_type.png


Example
-------
- 如何知道在 Windbg 中得到 Memory type(也叫做caching type): http://www.cnblogs.com/aoaoblogs/archive/2009/11/19/1606067.html 
- Cache Attribute Virtualization in Xen: http://www-archive.xenproject.org/files/xensummitboston08/Cache-Virtualization.pdf
- Copying Accelerated Video Decode Frame Buffers: https://software.intel.com/en-us/articles/copying-accelerated-video-decode-frame-buffers/

  - Fast USWC(Uncachable Speculative Write Combine) to WB(Write Back) Memory Copy

Reference
---------

- LWN - ``Documentation/x86/pat.txt:`` https://lwn.net/Articles/278994/
- ``Documentation/x86/pat.txt:`` https://www.kernel.org/doc/Documentation/x86/pat.txt
- LWN - x86: Full support of PAT: https://lwn.net/Articles/618811/
- ``Documentation/x86/mtrr.txt`` http://lxr.free-electrons.com/source/Documentation/x86/mtrr.txt?v=4.8
- Intel Manual Vol3 

  - Ch11.3 Methods of Caching Available
  - Ch11.5 Cache Controls
  - Ch11.11 Memory Type Range Registers (MTRRS)
  - Ch11.12 Page Attribute Table(PAT)
