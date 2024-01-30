.. _solutions:

Solutions
#########

Talaria TWO works by communicating with a host application through a
series of message exchanges back and forth. In this case, the host
application contains the logic to execute a sequence of the events.

-  AT Commands
   Interface with native commands to communicate with the Talaria TWO module.

-  Serial-to-Wireless Multi-Proto (SMP)
   The SMP application resides on Talaria TWO and communicates with
      the application being executed on the Host MCU

-  Low-power Dual-Stack solution
   -  Host package can be run on a Linux-based platform
   -  Linux host for data application, and Talaria TWO for low power/sleep, and router and cloud keep alive mechanism.
   -  UART (2W/4W), SDIO and SPI interface.
   -  Wi-Fi/BLE User Space C library (HAPI) host package.


AT Commands
-----------
.. toctree::
   :maxdepth: 1

   1. AT Commands/1. Prerequisites/Prerequisites.rst


Set-up and Usage
````````````````

.. toctree::
   :maxdepth: 1

   1. AT Commands/2. Set-up and Usage/1. Pre-setup on Talaria TWO.rst
   1. AT Commands/2. Set-up and Usage/2. Programming the Application.rst
   1. AT Commands/2. Set-up and Usage/3. Pre-setup on Host.rst
   1. AT Commands/2. Set-up and Usage/4. Configure the Serial Port.rst
   1. AT Commands/2. Set-up and Usage/5. Run the Application.rst

AT Commands
`````````

.. toctree::
   :maxdepth: 1

   1. AT Commands/3. AT Commands/AT Commands.rst

Command Response Description
`````````

.. toctree::
   :maxdepth: 1

   1. AT Commands/4. Command Response Description/Command Response Description.rst

FOTA Configuration
`````````

.. toctree::
   :maxdepth: 1

   1. AT Commands/5. FOTA Configuration and Environment Set-up/FOTA Configuration and Environment Set-up.rst

UseCases
`````````

.. toctree::
   :maxdepth: 1

   1. AT Commands/6. UseCases/1. Usecases - Landing Page
   1. AT Commands/6. UseCases/2. Wireless Operations
   1. AT Commands/6. UseCases/3. Network Protocol
   1. AT Commands/6. UseCases/4. Application Protocol and Data Transfer
   1. AT Commands/6. UseCases/5. Advanced Services
   1. AT Commands/6. UseCases/6. Miscellaneous

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
