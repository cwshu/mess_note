新聞

- SiFive Announces E20 and E21 RISC-V Cores for IoT and Wearables <https://www.cnx-software.com/2018/06/26/sifive-e20-e21-risc-v-cores-iot-wearables/>

  E20/E21 的定位為 Cortex-M0+/M4, 但 E20/E21 的 Interrupt Latency 只有 6 cycle.
  E2x 不使用 RISC-V 公定的 PLIC 作為 external interrupt controller, 而是使用 SiFive 自定的 CLIC controller.

SiFive 已公開資料

1. SiFive Proposal for a RISC-V Core-Local Interrupt Controller (CLIC) <https://github.com/sifive/clic-spec/blob/master/clic.adoc#inline-interrupt-handlers-and-interrupt-attribute-for-c>

ARM 官方對於 Interrupt Latency 的解釋.

1. A Beginner’s Guide on Interrupt Latency - and Interrupt Latency of the Arm Cortex-M processors <https://community.arm.com/processors/b/blog/posts/beginner-guide-on-interrupt-latency-and-interrupt-latency-of-the-arm-cortex-m-processors>
2. What is the true interrupt latency of Cortex-M3 and Cortex-M4 for interrupt entry and exit? <http://infocenter.arm.com/help/index.jsp?topic=/com.arm.doc.faqs/ka16366.html>


Note
----

1. A Beginner’s Guide on Interrupt Latency - and Interrupt Latency of the Arm Cortex-M processors <https://community.arm.com/processors/b/blog/posts/beginner-guide-on-interrupt-latency-and-interrupt-latency-of-the-arm-cortex-m-processors>


- Interrupt Latency 的計算: IRQ signal 進入的 cycle 到 ISR 1st instr 進入 pipeline execution stage 的 cycle count.

  - 一些 assumptions, 滿重要的是 M4F 有 FPU lazy stacking 的優化. 
  - M3/M4 Interrupt Latency 示意圖.

- Interrupt Latency 常有的問題

  - jitter
  - ...

- ARM Cortex-M 其他的 Interrupt optimization

  - Tail Chaining
  - Late Arrival
  - Stack-Pop Preemption
  - Sleep-on-Exit
  - Wait-for-Event (WFE) sleep
  - Zero jitter support on Cortex-M0/M0+

- Cortex-M4F lazy FPU stacking

  - Cortex-M4(F) Lazy Stacking and Context Switching Application Note 298 <http://infocenter.arm.com/help/index.jsp?topic=/com.arm.doc.dai0298a/index.html>
  - https://stackoverflow.com/questions/38614776/cortex-m4f-lazy-fpu-stacking

2. What is the true interrupt latency of Cortex-M3 and Cortex-M4 for interrupt entry and exit? <http://infocenter.arm.com/help/index.jsp?topic=/com.arm.doc.faqs/ka16366.html>

- 更細的提到 M3/M4 12 cycle latency 的原因跟硬體設計的限制 (e.g. memory system 不能影響 parallel register save)
- 非常多 interrupt latency 的要素, 跟硬體相關的內容也很多.


3. NXP Application Note - Measuring Interrupt Latency <https://www.nxp.com/docs/en/application-note/AN12078.pdf>

- Cause of interrupt latency: 影響 interrupt latency 的 factors. 還有一些潛在的 factors.
- 實測 interrupt latency (Cortex-M7)

  - Timer IRQ
  - GPIO IRQ
  - wait RTOS event latency

4. Digikey - Real Time: Some Notes on Microcontroller Interrupt Latency <https://www.digikey.com/en/articles/techzone/2011/jul/real-time-some-notes-on-microcontroller-interrupt-latency>

- 簡述 ARM7 跟 Cortex-M3 的 interrupt latency
- 簡述 Microchip PIC 系列的 interrupt latency
- 簡述 Atmel AVR XMEGA  的 interrupt latency

