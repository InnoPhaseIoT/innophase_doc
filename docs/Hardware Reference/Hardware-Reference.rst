.. _hardware reference:

Talaria TWO Hardware
##################

The INP1010/INP1011/INP1012/INP1013/INP1014/INP1015 Talaria TWO modules
are complete solutions with integrated wireless connectivity plus
microcontroller for edge-of-network IoT designs.

Talaria TWO modules have either a printed PCB antenna (INP1010/INP1014),
a U.FL antenna connector (INP1011/INP1015), an RF pin connector
(INP1012), or a ceramic antenna (INP1013). The modules will include
Wi-Fi Alliance, Bluetooth SIG, FCC, IC (Canada), CE, and TELEC\*.

Each module has an associated EVB-A evaluation board
(INP3010/INP3011/INP3012/INP3013/INP3014/INP3015 respectively), designed
as an evaluation platform for the INP101x modules.

.. table:: Table 1: Talaria TWO modules overview

   +-----------+-------------------------------------+-------------------+
   | **Module**| **Antenna**                         | **Dimensions(mm)**|
   +===========+=====================================+===================+
   | INP2045   | QFN42 SoC                           | 5x6               |
   +-----------+-------------------------------------+-------------------+
   | INP1010   | Integrated PCB antenna module       | 21.6x19.1         |
   +-----------+-------------------------------------+-------------------+
   | INP1011   | u.Fl external antenna module        | 21.6x19.1         |
   +-----------+-------------------------------------+-------------------+
   | INP1012   | RF Pin external antenna mini module | 15x12.8           |
   +-----------+-------------------------------------+-------------------+
   | INP1013   | Integrated ceramic antenna mini     | 20x12.8           |
   |           | module                              |                   |
   +-----------+-------------------------------------+-------------------+
   | INP1014   | Integrated PCB antenna mini module  | 20x12.8           |
   +-----------+-------------------------------------+-------------------+
   | INP1015   | u.Fl external antenna mini module   | 17x12.8           |
   +-----------+-------------------------------------+-------------------+

For more details on the Talaria TWO modules and SoCs, refer: Talaria TWO
Module and SoC Datasheet (https://innophaseiot.com/portal/portal-hub/).

INP3000 programmer board provides a programming interface for the
Talaria TWO modules. It can be used with scripts provides in the Talaria
TWO SDK package.


**Design Guidelines**

Design guidelines can be broadly categorized into the following sections:

    - Power supply
    - Reset
    - Peripheral interfacing
    - Production programming
    - RF/Antenna section

Power supply, Reset & Peripheral interfacing remain same for all variations of the Talaria TWO module family.

    - Production Programming
    - Module Placement Guidelines
    - Power supply to the model
    - Reset
    - Module Peripherals
    - Hibernate Mode
    - Thermal Ground Pad

Design Guidelines
------------------
.. toctree::
   :hidden:
   :maxdepth: 1

   1. Design Guidelines/5. Production Programming/1. Production Programming-Landing
   1. Design Guidelines/7. Module Placement Guidelines/1. Module Placement Guidelines - INP1010_INP1013_INP1014
   1. Design Guidelines/2. Power Supply to the Module
   1. Design Guidelines/3. Reset
   1. Design Guidelines/4. Module Peripherals
   1. Design Guidelines/6. Hibernate Mode
   1. Design Guidelines/8. Thermal Ground Pad.rst


INP 301x
--------
.. toctree::
   :hidden:
   :maxdepth: 1

   2. INP301x/INP301x Development Board.rst


INP 3000
--------

INP 3000 Programmer Boards
==========================

.. toctree::
   :hidden:
   :maxdepth: 1

   3. INP3000/1. INP3000 Programmer Boards/3. INP3000 Programmer Board_2.1
   3. INP3000/1. INP3000 Programmer Boards/2. INP3000 Programmer Board_3.0
   3. INP3000/1. INP3000 Programmer Boards/1. INP3000 Programmer Board_4.0


Programming Using INP 3000
==========================

.. toctree::
   :hidden:
   :maxdepth: 1


   3. INP3000/2. Programming using INP3000/Prerequisites3000.rst
   3. INP3000/2. Programming using INP3000/2. Generating the Application Image
   3. INP3000/2. Programming using INP3000/3. Generating the Data FS Image.rst
   3. INP3000/2. Programming using INP3000/4. Installing Dependencies for JTAG_SWD Programming.rst
   3. INP3000/2. Programming using INP3000/5. Programming Talaria TWO over UART.rst
   3. INP3000/2. Programming using INP3000/6. Programming Talaria TWO over SWD.rst
