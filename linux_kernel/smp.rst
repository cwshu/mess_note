Linux SMP
=========

trace code
----------

use Linux 4.9.0 as example.

``struct call_single_data``::

    // CSD
    struct call_single_data {
        struct llist_node llist;
        smp_call_func_t func;
        void *info;
        unsigned int flags;
    }
    smp_call_func_t
    flags: CSD_FLAG_XXX
    csd_lock/csd_unlock: serialize access to per-cpu csd resources

    // CFD
    struct call_function_data = CSD + cpumask
    smpcfd APIs: smpcfd_*

``smp_call_function_many()``::

    // platform independent code: kernel/smp.c

    smp_call_function_many()
        // fast path
        smp_call_function_single()
            generic_exec_single()
                // on this cpu
                func() # run function pointer
                // on other cpu
                csd->func = func
                llist_add(&csd->llist, &per_cpu(call_single_queue, cpu))
                arch_send_call_function_single_ipi(cpu)
        // slow path
        arch_send_call_function_ipi_mask()

    // platform dependent code
    arch_send_call_function_single_ipi()
    arch_send_call_function_ipi_mask()

x86::

    // 1. struct smp_ops
    arch_send_call_function_single_ipi()
        smp_ops.send_call_func_single_ipi()
    arch_send_call_function_ipi_mask()
        smp_ops.send_call_func_ipi()

    // only 1 smp_ops
    smp_ops.send_call_func_ipi = native_send_call_func_ipi
    smp_ops.send_call_func_single_ipi = native_send_call_func_single_ipi

    native_send_call_func_ipi()
        apic->send_IPI_mask() or apic->send_IPI_allbutself()
    native_send_call_func_single_ipi()
        apic->send_IPI()

    // 2. struct apic

    // there are 2 struct apic
    struct apic apic_default // arch/x86/kernel/apic/probe_32.c
    struct apic apic_flat    // arch/x86/kernel/apic/apic_flat_64.c

    // apic_default in arch/x86/kernel/apic/probe_32.c
    apic_default.send_IPI_mask() = default_send_IPI_mask_logical()
    default_send_IPI_mask_logical()
        __default_send_IPI_dest_field()
            __xapic_wait_icr_idle()
            native_apic_mem_write(APIC_ICR2, cfg);
            native_apic_mem_write(APIC_ICR, cfg);  // send IPI

ARM64::

    // 1. smp_cross_call()

    arch_send_call_function_single_ipi(int cpu)
        smp_cross_call(cpumask_of(cpu), IPI_CALL_FUNC);
    arch_send_call_function_ipi_mask(const struct cpumask *mask)
        smp_cross_call(mask, IPI_CALL_FUNC);

    // smp_cross_call() calls __smp_cross_call(), and __smp_cross_call() is depends on irqchip driver.

    __init set_smp_cross_call(fn)
         __smp_cross_call = fn;

    // drivers/irqchip/irq-gic.c
    __gic_init_bases()
        set_smp_cross_call(gic_raise_softirq);
    // drivers/irqchip/irq-gic-v3.c
    gic_smp_init()
        set_smp_cross_call(gic_raise_softirq);

    // 2. irqchip's __smp_cross_call()
        // drivers/irqchip/irq-gic.c:gic_raise_softirq()
        // drivers/irqchip/irq-gic-v3.c:gic_raise_softirq()

    // GICv3: drivers/irqchip/irq-gic-v3.c:gic_raise_softirq()
    gic_raise_softirq()
        gic_send_sgi()
            gic_write_sgi1r()
                msr_s to System Register ICC_SGI1R_EL1

        // GICv3 register interface:
        // from GICv3 and GICv4 Software Overview - Ch3.5 Programmer Model
        1. Distributor interface: GICD_*
        2. Redistributors interface: GICR_*
        3. CPU interfaces: ICC_*_ELn
