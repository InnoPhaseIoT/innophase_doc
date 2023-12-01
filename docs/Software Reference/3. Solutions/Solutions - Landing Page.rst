.. _solutions:

Solutions
#########

Talaria TWO works by communicating with a host application through a
series of message exchanges back and forth. In this case, the host
application contains the logic to execute a sequence of the events.

-  AT Commands

   -  Interface with native commands to communicate with the Talaria TWO
      module.

-  Serial-to-Wireless Multi-Proto (SMP)

   -  The SMP application resides on Talaria TWO and communicates with
      the application being executed on the Host MCU

-  Low-power Dual-Stack solution

   -  Host package can be run on a Linux-based platform

   -  Linux host for data application, and Talaria TWO for low
      power/sleep, and router and cloud keep alive mechanism.

   -  UART (2W/4W), SDIO and SPI interface.

   -  Wi-Fi/BLE User Space C library (HAPI) host package.


AT Commands
-----------
.. toctree::
   :maxdepth: 1

   1. AT Commands/ATCommands_Landing_Page.rst
   
STW Multi-Proto
------------------------

.. toctree::
   :maxdepth: 1

   2. STW Multi-Proto/STW Multi-Proto - Landing Page.rst

Dual stack
---------------

.. toctree::
   :maxdepth: 1

   3. Dual-Stack/Dual-Stack - Landing Page.rst
