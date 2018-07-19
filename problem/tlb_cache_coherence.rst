
:date: 2016-11-28 00:00

We need to do TLB cache coherence by software in SMP environment

The common method is including send IPI and do TLB invalidation in other cpu.

some search:

- http://forum.osdev.org/viewtopic.php?p=190926#p190926
- TLB and Pagewalk Coherence: http://blog.stuffedcow.net/2015/08/pagewalk-coherence/

papers:

- (2017, Nadav) Optimizing the TLB Shootdown Algorithm with Page Access Tracking

  - `paper <https://www.usenix.org/system/files/conference/atc17/atc17-amit.pdf>`_, `slide <https://www.usenix.org/sites/default/files/conference/protected-files/atc17_slides_amit.pdf>`_
  - `source code <http://nadav.amit.to/publications/tlb>`_

- HW approach

  - (2006) A comprehensive study of hardware/software approaches to improve TLB performance for java applications on embedded systems

- SW approaches

  - (1989) Translation lookaside buffer consistency: a software approach.
  - (1988) Translation lookaside buffer synchronization in a multiprocessor system
  - (1987, Patricia) TLB consistency on highly-parallel shared-memory multiprocessors.
  - (1990, Patricia) Translation-lookaside buffer consistency
  - (2011) DiDi: Mitigating the performance impact of TLB shootdowns using a shared TLB directory


my code trace (in the progress):

- ./tlb_shootdown_linux.rst


