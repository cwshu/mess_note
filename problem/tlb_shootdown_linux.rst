- [RFC PATCH 2/2] ARMv7: Invalidate the TLB before freeing page tables: http://lists.infradead.org/pipermail/linux-arm-kernel/2011-February/043050.html

  - ``include/asm-generic/tlb.h``, ``arch/x86/include/asm/tlb.h``: how other arch handle this stuff
  - TLB shootdown code is supposed to make this more efficient than 
    having to issue a broadcasted TLB invalidate for every page as we remove each one in sequence?
  - tlb_remove_page(), zap_pte_range(), tlb_end_vma()

- linux-patches/tlb-shootdown-measurement: https://github.com/x-y-z/linux-patches/blob/master/tlb-shootdown-measurement/0003-tracing-add-a-reason-for-tracing-tlb-shootdown-initi.patch

- ``arch/arm/include/asm/tlb.h`` 寫說, 有三種方法使用 TLB shootdown 的 code
  
  a. unmap range of vmas: unmap_region(), zap_page_range()
  b. unmap all vmas: exit_mmap()
  c. unmap argument pages: shift_arg_pages()

- ``arch/arm64/include/asm/tlbflush.h``: http://lxr.free-electrons.com/source/arch/arm64/include/asm/tlbflush.h?v=4.8#L28

  - arm64 TLB management code?

unmap_region()::

    - unmap_region()
      - tlb_gather_mmu() => __tlb_reset_range()
      - free_pgtables()
      - tlb_finish_mmu()
        - tlb_flush_mmu()
          - tlb_flush_mmu_tlbonly(): flush tlb entry
            - tlb_flush()
            - mmu_notifier_invalidate_range()
            - __tlb_reset_range()
          - tlb_flush_mmu_free(): free pages

    - [x86] tlb_flush()
    - [x86] flush_tlb_mm_range()
    - [x86] flush_tlb_others() = native_flush_tlb_others() // trace_tlb_flush(TLB_REMOTE_SEND_IPI)
    - smp_call_function_many() + flush_tlb_func

    // mmu_notifier, mmu_notifier_op // implemented in ./drivers/iommu/{intel-svm.c, amd_iommu_v2.c}
