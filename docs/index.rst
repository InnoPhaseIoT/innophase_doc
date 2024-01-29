

InnoPhase IoT Programming Guide
================================

Welcome to the InnoPhase IoT Programming Guide. This guide provides information on programming for InnoPhase IoT devices. The Overview section provides a high-level introduction to InnoPhase IoT devices and the programming guide's structure.

Getting Started
===============

InnoPhase IoT is a fabless wireless semiconductor platform company specializing in extreme low power wireless radio solutions. InnoPhase IoT is focused on developing wireless semiconductor SoCs and Modules for high volume, battery-based consumer, commercial, medical, and industrial wireless IoT products.
InnoPhase offers two types of solution architectures:
    • ``Hostless (Stand-alone) Solution``
    • ``Hosted Solution``


Hostless (Stand-alone) Solution:
-------
* In this case, there is no external host involved and the application runs on the internal MCU of the Talaria TWO.
* Available as part of the SDK release package. For example: sdk_x.y.zip.
``Note``: x and y in sdk_x.y refers to the SDK version of the release package.
* Beneficial for development of integrated applications on Talaria TWO with InnoOS RTOS, lwIP network stack and GCC compiler-based SDK.
* Enables application, networking and wireless (BLE/Wi-Fi) functionality on Talaria TWO.

Hosted Solution:
----------

Talaria TWO works by communicating with a host application through a series of message exchanges back and forth. In this case, the host application contains the logic to execute a sequence of the events. There are two variants of the Hosted architecture:
    * ``MCU-based (Hosted MCU)``
    * ``Linux CPU-based (Hosted CPU)``

MCU-based (Hosted MCU):
~~~~~~~~~~
•	Available as part of the ST and LPS release packages.
        The release package for ST (MCU from STM) is available on the website. Contact InnoPhase IoT for the LPS solution (Low Power Sensor – MCU from Nuvoton). These packages contain the required libraries and examples that run on the host MCU and communicate with Talaria TWO.
•	MCU serves as the master and sends commands to Talaria TWO to perform any of the following operations: Wi-Fi, BLE, Socket, FoTA, Provisioning and so on).
•	Talaria TWO provides all Wi-Fi, BLE, Socket, MQTT/HTTP, TLS, FoTA, Provisioning.
•	Supported interfaces:
•	AT Commands: UART
•	HAPI (STM): UART, SPI
•	Wi-Fi/BLE C library (HAPI) host package or AT Commands (native on Talaria TWO).
•	BLE can also be supported via HCI interface.

Linux CPU-based (Hosted CPU):
~~~~~~~~~~
* The host package can be run on a Linux based platform
* The package can be made available on request (proprietary).
* Low Power, Dual-Stack architecture.
* Linux host for data application, and Talaria TWO for low power/sleep, and router and cloud keep alive mechanism.
* UART (2W/4W), SDIO and SPI interface.
* Wi-Fi/BLE User Space C library (HAPI) host package.

.. toctree::
   :hidden:
   :maxdepth: 2
   :caption: Contents

   Getting Started/Introduction


.. toctree::
   :hidden:
   :maxdepth: 2

   Hardware Reference/Hardware-Reference

.. toctree::
   :hidden:
   :maxdepth: 2

   Software Reference/Software_Reference_Landing_Page.rst

.. toctree::
   :hidden:
   :maxdepth: 2

   Development Environments/Development Environments - Landing Page

.. toctree::
   :hidden:
   :maxdepth: 2

   Tools/Tools-landing page

.. toctree::
   :hidden:
   :maxdepth: 2

   Applications/Applications - Landing Page

.. toctree::
   :hidden:
   :maxdepth: 2

   Regulatory Notices/Regulatory Notices

.. toctree::
   :hidden:
   :maxdepth: 2

   Security/Security - Landing Page

.. toctree::
   :hidden:
   :maxdepth: 2

   Porting Guide/Porting-Guide

.. toctree::
   :hidden:
   :maxdepth: 2

   Support/Support

.. toctree::
   :hidden:
   :maxdepth: 2

   Disclaimers/Disclaimers

.. toctree::
   :hidden:
   :maxdepth: 2

   Appendix/Appendix-Landing_Page

.. toctree::
   :hidden:
   :maxdepth: 2

   glossary

.. toctree::
   :hidden:
   :maxdepth: 2
   :caption: About

   about
