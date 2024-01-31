Hardware Setup and PIN Configuration
====================================

Topology
--------

The topology of the setup used to test the application is as shown in
Figure 1.

|A diagram of a different way Description automatically generated with
medium confidence|

Figure 1: Setup topology

Connection Setup
----------------

Host MCU communicates with Talaria TWO via the SPI interface.

SPI Interface
~~~~~~~~~~~~~

Figure 2 below shows the hardware setup for testing the application
using SPI interface.

1. Mount the Talaria TWO EVB on the STM32 board on Arduino connector.

2. Connect GPIO04 of Talaria TWO (J1 Connector) to PC8 (PIN2 of CN12 on
   NUCLEO-U575ZI-Q). Talaria TWO uses GPIO4 PIN to interrupt the host
   MCU when Talaria TWO wants to send data/notification to Host MCU.

3. Connect GPIO4 of Talaria TWO (J1 Connector) to PE4 (PIN48 of CN11 on
   NUCLEO-U575ZI-Q). The NUCLEO-U575ZI-Q Host MCU is configured to use
   this GPIO to be woken-up from STOP3 mode.

4. Connect GPI03 of Talaria TWO (J1 Connector) to PB11 (PIN18 of CN12 on
   NUCLEO-U575ZI-Q). The NUCLEO-U575ZI-Q Host MCU is configured to use
   this GPIO to wake-up Talaria TWO from suspend mode.

|A circuit board with many small components Description automatically
generated with medium confidence|

Figure 2: Hardware setup for testing Talaria TWO with STMU575-ZI-Q using
SPI

.. |A diagram of a different way Description automatically generated with medium confidence| image:: media/image1.png
   :width: 5.51181in
   :height: 3.25181in
.. |A circuit board with many small components Description automatically generated with medium confidence| image:: media/image2.png
   :width: 7.48031in
   :height: 4.08301in
