新聞

- SiFive Announces E20 and E21 RISC-V Cores for IoT and Wearables <https://www.cnx-software.com/2018/06/26/sifive-e20-e21-risc-v-cores-iot-wearables/>

  E20/E21 的定位為 Cortex-M0+/M4, 但 E20/E21 的 Interrupt Latency 只有 6 cycle.
  E2x 不使用 RISC-V 公定的 PLIC 作為 external interrupt controller, 而是使用 SiFive 自定的 CLIC controller.

SiFive 已公開資料

1. SiFive Proposal for a RISC-V Core-Local Interrupt Controller (CLIC) <https://github.com/sifive/clic-spec/blob/master/clic.adoc#inline-interrupt-handlers-and-interrupt-attribute-for-c>

ARM 官方對於 Interrupt Latency 的解釋.

1. A Beginner’s Guide on Interrupt Latency - and Interrupt Latency of the Arm Cortex-M processors <https://community.arm.com/processors/b/blog/posts/beginner-guide-on-interrupt-latency-and-interrupt-latency-of-the-arm-cortex-m-processors>
2. What is the true interrupt latency of Cortex-M3 and Cortex-M4 for interrupt entry and exit? <http://infocenter.arm.com/help/index.jsp?topic=/com.arm.doc.faqs/ka16366.html>
