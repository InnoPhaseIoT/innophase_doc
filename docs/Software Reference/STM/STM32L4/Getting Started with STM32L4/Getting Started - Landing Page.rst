.. _stm32l4:

STM32L4
========

**STM32L4A6ZG/L433RC-P Host controller**

This section provides a detailed walkthrough of the steps to set-up
Talaria TWO hosted solution demo using STM32 NUCLEO (L4A6ZG/L433RC-P).

STM32L4A6ZG/L433RC-P is a Host controller which has the HAPI APIs
running on it. HAPI is a portable library of “c” functions that wraps
HIO data structs and resides on the host processor. Using these HAPI
APIs, users can write applications to perform multiple functions with
Talaria TWO.

**Prerequisites**

1. Talaria TWO Evaluation Board

2. Serial Cable (USB to Micro-USB)

3. Windows/Linux PC

4. Wi-Fi Access Point

5. Minicom/Tera Term VT Utility installed on PC

6. STM32L4A6ZG/L433RC-P Nucleo board

7. EVK package

8. STM32CubeIDE


**Download the Evaluation Software Package (EVK)**

Download the software package from the InnoPhase website:
https://innophaseiot.com/talaria-two-modules/#product-availability.

|A screenshot of a computer Description automatically generated|

Figure 1: Download the Software Package

**Package Contents**

I-CUBE-T2-STW software package provides software APIs running on STM32
for STM's NUCLEO-STM32L4A6ZG or NUCLEO-STM32L433RC-P. It provides
ready-to-run firmware examples to support quick evaluation and
development of MQTT/HTTP/AWS/AZURE and HTTPS IoT Cloud applications on
STM32L4 Nucleo boards with InnoPhase Talaria TWO Wi-Fi add-on boards.

Folder details are as follows:

1. Documentation: This folder includes all applications related to
   Talaria TWO and STMCubeL4.

2. Drivers: This folder includes BSP files for STM32L4 Nucleo boards.
   Refer to release notes for further details

3. Middleware: This folder includes Middleware FreeRTOS and third-Party
   Middleware InnoPhase-HAPI to act as a host interface for Talaria TWO
   Modules (INP101X) Wi-Fi devices

4. Projects: This folder includes the applications to demonstrate the
   INP101X features such as Wi-Fi, BLE, cloud apps on modules
   32L4A6ZG-NUCLEO and 32L433RC-P-NUCLEO. Refer to release notes for
   further details.

5. Path to access the applications:
   *I-CUBE-T2-STW-src_x.y\\STM32CubeExpansion_T2-HostAPI-src_vx.y\\Projects\\NUCLEO-L433RC-P\\Applications\\InnoPhase_HAPI*

**Note**: x and y refer to the package release version.

6. Utilities: This folder includes Download tool GUI and the firmware
   binary for Talaria TWO EVB(INP301x)


Getting Started
---------------
.. toctree::
    :maxdepth: 1

    Hardware Setup and PIN Configuration.rst
    Set-up and Usage.rst
    Set-up Host Machine.rst
    Testing Basic Operations on Set-up.rst

Host Applications
-----------------
.. toctree::
    :maxdepth: 1

    ../Host Applications/AWS Demo Application.rst
    ../Host Applications/Azure IoT Application.rst
    ../Host Applications/BLE Central Demo.rst
    ../Host Applications/BLE Peripheral Demo.rst
    ../Host Applications/BLE Provisioning Demo.rst
    ../Host Applications/FOTA Demo Application.rst
    ../Host Applications/HTTP-Demo Application.rst
    ../Host Applications/Low Power Demo Application.rst
    ../Host Applications/MQTT Demo Application.rst
    ../Host Applications/NTP-Demo Application.rst
    ../Host Applications/TLS Demo Application.rst
    ../Host Applications/Unassoc-Demo Application.rst
    ../Host Applications/Wi-Fi Demo Application.rst
    ../Host Applications/Wi-Fi Demo Application with Scramble Enable.rst


.. |A screenshot of a computer Description automatically generated| image:: media/image1.png
   :width: 7.48031in
   :height: 4.49373in
