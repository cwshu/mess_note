kvm
---
- cpu 

vm => regular linux process, scheduled by standard linux scheduler
more precisely, each vcpu appear as single linux process.

- security

SVirt: SELinux and kvm virtualization

- memory management

  - Intel Extended Page Table(EPT)
  - AMD Rapid Virtualization Indexing
  - kernel feature: Kernel Same-page Merging (KSM)

    - 把 VM 間的 same memory page merge 到同一個 physical page, 用於節省 memory, 同時開啟更多 VM.
    - ksmd(daemon) 定期掃描比對跟 merge
    - 比對法: http://blog.csdn.net/summer_liuwei/article/details/6013255, http://www.ibm.com/developerworks/linux/library/l-kernel-shared-memory/index.html
    - source: ``./mm/ksm.c``
    - in other system

      - ESXi: Transparent Page Sharing
      - XEN: Memory COW


- reading

  - http://www.ibm.com/developerworks/cloud/library/cl-hypervisorcompare-kvm/

- unread

  - `IBM developer - Anatomy of Linux hypervisor <http://www.ibm.com/developerworks/linux/library/l-hypervisor>`_
