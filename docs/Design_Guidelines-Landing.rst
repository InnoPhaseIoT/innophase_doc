
.. _Design_Guidelines:

Hibernate mode
==============

In the Hibernate mode, EN_CHIP/RST PIN must be held LOW (less than 0.6V)
and the VDD must be ON (VDD 3V). In this mode, SRAM memory is not
retained and the RTC will be OFF. Host connected to this PIN can put the
module in Hibernate mode by a GPIO to save power. When released from the
Hibernate mode, the module will work with a default software application
stored in Flash. In this mode, the module consumes less than 1uA.


Module Peripherals
==============
.. toctree::
   :maxdepth: 3

   Module_Peripheral/Module_Peripherals_Landing


Module Placement Guidelines
==============
.. toctree::
   :maxdepth: 3
    
   Module_Placement_Guidelines/Module_and_Antenna_Placement_Guidelines–INP1012
   Module_Placement_Guidelines/Module_Placement_Guidelines-INP1010_INP1013_INP1014
   Module_Placement_Guidelines/Module_Placement_Guidelines–INP1011_INP1015


Power Supply to the Module
==========================
.. toctree::
   :maxdepth: 3
    
   Power_Supply_to_the_Module/Power_Supply_to_the_Module


Production Programming 
==========================

Production programming of Talaria TWO module can be done in the
following three ways:

    1. PC-based programming 
    2. Host-based programming
    3. Programming Over the Air

**Note**: The schematics and the user guide for the programmer board
INP3000 are available in the *Documentation* section of the customer
portal on the InnoPhase IoT website:
https://innophaseiot.com/portal/portal-hub/.

To obtain access to the customer portal, contact InnoPhase IoT sales
team: sales@innophaseiot.com.

.. toctree::
   :maxdepth: 3
    
   Production_Programming/Host-based/Production_Programming-Host_based
   Production_Programming/PC-based/Production_Programming-PC_based
   Production_Programming/Programming_Over_the_Air/Production_Programming-Programming_Over_the_Air
