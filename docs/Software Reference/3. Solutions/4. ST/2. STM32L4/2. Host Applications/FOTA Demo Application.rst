FOTA Demo Application
=====================

The HAPI APIs residing in the host microcontroller (STM32) connects to
Talaria TWO module via UART/SPI. Using these HAPI APIs, users can write
applications to perform multiple functions with Talaria TWO. This series
of Host Application Notes discusses more on using these APIs to perform
specific functions.

This document provides details on how to use the HAPI APIs to create
FOTA (Firmware Over-The-Air) of the Talaria TWO firmware. Following are
the major steps involved:

1. Initialize the HAPI interface

2. Create WCM interface

3. Connect to Wi-Fi Network

4. Trigger FOTA

Connection Set-up
=================

Host processor communicates with Talaria TWO via a SPI or UART
interface. The connection set-up used to test the application is as
shown in Figure 1.

|image1|

Figure 1: Connection set-up for application testing

STM32L433RC-P as Host Controller
--------------------------------

STM32L433RC-P is the host controller which will have the FOTA demo
application running on it. This host is in-turn connected to the
InnoPhase Talaria TWO board through SPI/UART interface. The serial to
Wi-Fi application (stw_multi_proto) firmware should be run on the
Talaria TWO board.

SPI Interface
~~~~~~~~~~~~~

Refer section: *SPI Interface* of the document:
QSG_T2_STM32CubeL4_L433RC-P.pdf
*(Documentation\\STM32CubeL4_Getting_Started*) for more details on the
Hardware setup and connections for testing the application using SPI
interface.

UART Interface
~~~~~~~~~~~~~~

Refer section: *UART Interface* of the document:
QSG_T2_STM32CubeL4_L433RC-P.pdf
*(Documentation\\STM32CubeL4_Getting_Started*) for more details on the
Hardware setup and connections for testing the application using UART
interface.

STM32L4A6ZG as Host Controller
------------------------------

STM32L4A6ZG is the host controller which will have the FOTA demo
application running on it. This host is in-turn connected to the
InnoPhase Talaria TWO board through SPI/UART interface. The serial to
Wi-Fi application (stw_multi_proto) firmware should be run on the
Talaria TWO board.

.. _spi-interface-1:

SPI Interface
~~~~~~~~~~~~~

Refer section: *SPI Interface* of the document:
QSG_T2_STM32CubeL4_L4A6ZG.pdf
*(Documentation\\STM32CubeL4_Getting_Started*) for more details on the
Hardware setup and connections for testing the application using SPI
interface.

.. _uart-interface-1:

UART Interface
~~~~~~~~~~~~~~

Refer section: *UART Interface* of the document:
QSG_T2_STM32CubeL4_L4A6ZG.pdf
*(Documentation\\STM32CubeL4_Getting_Started*) for more details on the
Hardware setup and connections for testing the application using UART
interface.

Set-up & Usage
==============

Pre-set-up on Talaria TWO
-------------------------

Refer section: *Setup & Usage* of the document:
QSG_T2_STM32CubeL4_L433RC-P.pdf
*(Documentation\\STM32CubeL4_Getting_Started*) for details on Pre-set-up
on Talaria TWO.

Boot Arguments 
---------------

Refer section: *Boot Arguments* of the document:
QSG_T2_STM32CubeL4_L433RC-P.pdf
*(Documentation\\STM32CubeL4_Getting_Started*) for details on the boot
arguments to be passed for SPI and UART interface.

Testing
=======

Sample Application
------------------

The sample application discussed in this application note runs
specifically on STM32L4A6ZG/STM32L433RC-P devices. This example has been
tested with NUCLEO-L4A6ZG/NUCLEO-L433RC-P board and can be easily
tailored to any other supported device and development board.

1. Start the application.

2. This will trigger FOTA on Talaria TWO.

3. If FOTA is a success, the setup will be rebooted. The changed
   Firmware version is an indication of the new firmware being booted .

For details on testing the application with SPI and UART interface,
refer sections: *Testing the Basic Operation on setup with SPI
interface* and *Testing the Basic Operation on setup with UART
interface* of the document: QSG_T2_STM32CubeL4_L433RC-P.pdf
*(Documentation\\STM32CubeL4_Getting_Started*).

**Note**:

To make certain appropriate HAL operation, the application must ensure
that the HAL time base is always set to 1 millisecond. The FreeRTOS heap
size configTOTAL_HEAP_SIZE as defined in FreeRTOSConfig.h is set as per
the OS resources’ memory requirements of the application with a +10%
margin and rounded to the upper Kbyte boundary.

For more details on the FreeRTOS implementation on STM32Cube, please
refer to UM1722 - Developing Applications on STM32Cube with RTOS.

.. _fota-demo-application-1:

FOTA Demo Application
=====================

This section describes the application details along with code snippets.
The application uses HAPI APIs to achieve the functionality. HAPI APIs
presumes that the platform related initialization and clock settings are
completed by default.

HAPI Interface Initialization
-----------------------------

+-----------------------------------------------------------------------+
| struct hapi \*hapi;                                                   |
|                                                                       |
| #ifdef HAPI_INTERFACE_UART_ENABLED                                    |
|                                                                       |
| /\* Register the uart, and baud rate to hapi \*/                      |
|                                                                       |
| hapi = hapi_uart_init(hapi_uart, hapi_uart_tx, hapi_uart_rx);         |
|                                                                       |
| #endif                                                                |
|                                                                       |
| #ifdef HAPI_INTERFACE_SPI_ENABLED                                     |
|                                                                       |
| /\* Register the SPI \*/                                              |
|                                                                       |
| hapi = hapi_spi_init(hapi_spi, hapi_spi_cs_high, hapi_spi_cs_low,     |
| hapi_spi_tx, hapi_spi_rx);                                            |
|                                                                       |
| #endif                                                                |
+=======================================================================+
+-----------------------------------------------------------------------+

HAPI Interface Start and Disable Sleep Mode in Configuration
------------------------------------------------------------

+-----------------------------------------------------------------------+
| hapi_start(hapi);                                                     |
|                                                                       |
| hapi_config(hapi, 0, 0, 0, 0, 0);                                     |
+=======================================================================+
+-----------------------------------------------------------------------+

Check HAPI Communication with Talaria TWO EVB
---------------------------------------------

+-----------------------------------------------------------------------+
| hapi_hio_query(hapi,&hio_query_rsp);                                  |
+=======================================================================+
+-----------------------------------------------------------------------+

Create a Wi-Fi Network Interface and Register Link Status Callback 
-------------------------------------------------------------------

+-----------------------------------------------------------------------+
| struct hapi_wcm \* hapi_wcm = hapi_wcm_create(hapi);                  |
|                                                                       |
| hapi_wcm_set_link_cb(hapi_wcm, wcm_link_cb, NULL);                    |
+=======================================================================+
+-----------------------------------------------------------------------+

Connecting to a Wi-Fi network
-----------------------------

The application uses different parameters which can be modified as per
user AP settings. The SECURITY_TYPE macro must be updated with the WPA
security type, which can be chosen from one of following depending on
the AP settings.

|A close-up of a computer code Description automatically generated|

Figure 2: Modifying parameters as per AP settings

In app_config file, configure the SSID and passphrase for a Wi-Fi
connection as mentioned below:

+-----------------------------------------------------------------------+
| #define WIFI_SSID "InnoAP"                                            |
|                                                                       |
| /comment this macro for open security/                                |
|                                                                       |
| #define WIFI_PASSPHRASE "inno123456"                                  |
+=======================================================================+
+-----------------------------------------------------------------------+

Trigger FOTA
------------

The application triggers FOTA using the following HAPI API:

+-----------------------------------------------------------------------+
| bool                                                                  |
|                                                                       |
| hapi_fota_start(struct hapi \*hapi_p,                                 |
|                                                                       |
| uint32_t check_for_update,                                            |
|                                                                       |
| uint32_t auto_reset);                                                 |
+=======================================================================+
+-----------------------------------------------------------------------+

Usage:

+-----------------------------------------------------------------------+
| status = hapi_fota_start(hapi, 1, 0);                                 |
|                                                                       |
| if(!status){                                                          |
|                                                                       |
| /\*Fota failed*/                                                      |
|                                                                       |
| console_print("\\nFOTA Failed");                                      |
|                                                                       |
| goto err_exit;                                                        |
|                                                                       |
| }                                                                     |
|                                                                       |
| /\*FOTA is Success*/                                                  |
+=======================================================================+
+-----------------------------------------------------------------------+

The host application can set auto_reset as 1 or 0. If set to 1, Talaria
TWO will be reset after successful completion of FOTA. If FOTA fails,
the API will return with the failure code.

However, it is recommended to set the parameter to 0. With this, the API
will return success/failure. The host needs to reset the system if the
API return is a success. The new firmware will take effect in Talaria
TWO only after reset.

Expected Output
===============

On successful FOTA download and commit, FOTA Success can be observed on
the serial terminal.

|A screenshot of a computer Description automatically generated|

Figure 3: Expected output

Application Files and Functions
===============================

+----------------------------------------------+-----------------------+
|    File                                      |    Function           |
+==============================================+=======================+
|    InnoP                                     |    Main Program       |
| hase_HAPI/InnoPhase_HAPI_wifidemo/Src/main.c |                       |
+----------------------------------------------+-----------------------+
|    InnoPhase_HAPI/InnoPhase_HA               |    HAL time-base file |
| PI_wifidemo/Src/stm32l4xx_hal_timebase_tim.c |                       |
+----------------------------------------------+-----------------------+
|    InnoPhase_HAP                             |    Interrupt handlers |
| I/InnoPhase_HAPI_wifidemo/Src/stm32l4xx_it.c |                       |
+----------------------------------------------+-----------------------+
|    InnoPhase_HAPI/In                         |    STM32L4xx system   |
| noPhase_HAPI_wifidemo/Src/system_stm32l4xx.c |    clock              |
|                                              |    configuration file |
+----------------------------------------------+-----------------------+
|    InnoPhase_                                |    Code for free RTOS |
| HAPI/InnoPhase_HAPI_wifidemo/Src/freertose.c |    application        |
+----------------------------------------------+-----------------------+
|    InnoPhase_HAPI/Inn                        |    Code for MSP       |
| oPhase_HAPI_wifidemo/Src/stm32l4xx_hal_msp.c |    initializa         |
|                                              | tion/deinitialization |
+----------------------------------------------+-----------------------+
|    InnoPhase                                 |    System calls file  |
| _HAPI/InnoPhase_HAPI_wifidemo/Src/syscalls.c |                       |
+----------------------------------------------+-----------------------+
|    InnoPha                                   |    System memory      |
| se_HAPI/InnoPhase_HAPI_wifidemo/Src/sysmem.c |    calls file         |
+----------------------------------------------+-----------------------+
|    InnoPhase_HAPI/InnoPhas                   |    System startup     |
| e_HAPI_wifidemo/Src/startup_stm32l433rctxp.s |    file               |
+----------------------------------------------+-----------------------+
|    InnoP                                     |    Main program       |
| hase_HAPI/InnoPhase_HAPI_wifidemo/Inc/main.h |    header file        |
+----------------------------------------------+-----------------------+
|    InnoPhase_HAPI/Inno                       |    HAL Library        |
| Phase_HAPI_wifidemo/Inc/stm32l4xx_hal_conf.h |    Configuration file |
+----------------------------------------------+-----------------------+
|    InnoPhase_HAP                             |    Interrupt          |
| I/InnoPhase_HAPI_wifidemo/Inc/stm32l4xx_it.h |    handler’s header   |
|                                              |    file               |
+----------------------------------------------+-----------------------+
|    InnoPhase_HAPI/                           |    FreeRTOS           |
| InnoPhase_HAPI_wifidemo/Inc/FreeRTOSConfig.h |    Configuration file |
+----------------------------------------------+-----------------------+

Table 1: Application files and functions

.. |image1| image:: media/image1.png
.. |A close-up of a computer code Description automatically generated| image:: media/image2.png
   :width: 3.93701in
   :height: 0.97967in
.. |A screenshot of a computer Description automatically generated| image:: media/image3.png
   :width: 5.90551in
   :height: 2.65816in
