Unassoc-Demo Application
========================

The HAPI APIs residing in the host microcontroller (STM32) connects to
Talaria TWO module via UART/SPI. Using these HAPI APIs, users can write
applications to perform multiple functions with Talaria TWO. This series
of Host Application Notes discusses more on using these APIs to perform
specific functions.

This document provides details on how to use the HAPI APIs to create the
unassoc demo application to:

1. Initialize the HAPI interface

2. Select the interface

3. Create the unassoc interface with MAC address

4. Configure the unassoc tx params

5. Start unassoc transmission

Connection Set-up
=================

Host processor communicates with Talaria TWO via a SPI or UART
interface. The connection set-up used to test the application is as
shown in Figure 1.

|A black and blue rectangles with black text Description automatically
generated|

Figure 1: Connection set-up for application testing

STM32L433RC-P as Host Controller
--------------------------------

STM32L433RC-P is the host controller with Wi-Fi demo application running
on it. This host is in-turn connected to the InnoPhase Talaria TWO board
through SPI/UART interface. The serial to Wi-Fi application
(stw_multi_proto) firmware should be run on the Talaria TWO board.

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

For details on testing the application with SPI and UART interface,
refer sections: *Testing the Basic Operation on setup with SPI
interface* and *Testing the Basic Operation on setup with UART
interface* of the document: QSG_T2_STM32CubeL4_L433RC-P.pdf
*(Documentation\\STM32CubeL4_Getting_Started*).

1. Open any console (serial terminal) on STM32 MCU with a baud rate of
   115200.

2. Reset the STM32 and check the MCU console.

3. Application creates, configures, and starts unassoc transmission.

**Note**:

This application use default values for unassoc frame. Please update the
values as per requirement.

To make certain appropriate HAL operation, the application must ensure
that the HAL time base is always set to 1 millisecond. The FreeRTOS heap
size configTOTAL_HEAP_SIZE as defined in FreeRTOSConfig.h is set as per
the OS resources’ memory requirements of the application with a +10%
margin and rounded to the upper Kbyte boundary.

For more details on the FreeRTOS implementation on STM32Cube, please
refer to UM1722 - Developing Applications on STM32Cube with RTOS.

.. _unassoc-demo-application-1:

Unassoc Demo Application
========================

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

HAPI Interface Start & Disable Sleep Mode in Configuration
----------------------------------------------------------

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

Create Unassoc Interface with Desired MAC Address
-------------------------------------------------

+-----------------------------------------------------------------------+
| bool hapi_unassoc_create(struct hapi \*hapi, uint8_t \*addr)          |
+=======================================================================+
+-----------------------------------------------------------------------+

Configure the Unassoc Parameters
--------------------------------

The application uses the default values for unassoc tx. These can be
modified as per user AP settings.

+-----------------------------------------------------------------------+
| char target_ssid[] = "TEST_AP";                                       |
|                                                                       |
| uint8_t ie[]= {                                                       |
|                                                                       |
| 0x11 /\* ie tag \*/,0x02 /\* ie len \*/,0x33,0x44 /\* ie data \*/,    |
|                                                                       |
| 0x12 /\* ie tag \*/,0x04 /\* ie len \*/,0x77,0x88,0x99,0xaa /\* ie    |
| data \*/,                                                             |
|                                                                       |
| 0x13 /\* ie tag \*/,0x07 /\* ie len                                   |
| \*/,0xa0,0xa1,0xa2,0xa3,0xa4,0xa5,0xa6 /\* ie data \*/                |
|                                                                       |
| };                                                                    |
|                                                                       |
| status = hapi_unassoc_config(hapi,                                    |
|                                                                       |
| 0, /\* num_probes. 0=infinate \*/                                     |
|                                                                       |
| 500, /\* interval_ms \*/                                              |
|                                                                       |
| 1, /\* verbose \*/                                                    |
|                                                                       |
| target_ssid, /\* ssid \*/                                             |
|                                                                       |
| RATE_6, /\* RATE \*/                                                  |
|                                                                       |
| 0, /\* suspend_en \*/                                                 |
|                                                                       |
| sizeof(ie), /\* ie_len \*/                                            |
|                                                                       |
| ie /\* ie \*/                                                         |
|                                                                       |
| );                                                                    |
|                                                                       |
| if(status == false) {                                                 |
|                                                                       |
| sprintf(print_arr,"hapi_unassoc_config fail\\r\\n");                  |
|                                                                       |
| console_print(print_arr);                                             |
|                                                                       |
| printf("%s",print_arr);                                               |
|                                                                       |
| }                                                                     |
+=======================================================================+
+-----------------------------------------------------------------------+

Start Unassoc Transmission & Verify Status 
-------------------------------------------

Start the unassoc transmission, and verify status:

+-----------------------------------------------------------------------+
| status = hapi_unassoc_start(hapi);                                    |
|                                                                       |
| if(status == false) {                                                 |
|                                                                       |
| sprintf(print_arr,"hapi_unassoc_start fail\\r\\n");                   |
|                                                                       |
| console_print(print_arr);                                             |
|                                                                       |
| printf("%s",print_arr);                                               |
|                                                                       |
| }                                                                     |
+=======================================================================+
+-----------------------------------------------------------------------+

Expected Output
===============

The MCU will configure Talaria TWO to send unassoc frames. Following
output can be observed in MCU console.

|Text Description automatically generated|

Figure 2: Expected Output

Application Files and Functions 
================================

+---------------------------------------------+------------------------+
|    File                                     |    Function            |
+=============================================+========================+
|    InnoPhase_HAPI/T2-HAN-013/Src/HAPI/app.c |    Main Program        |
+---------------------------------------------+------------------------+

Table 1: Application files and functions

.. |A black and blue rectangles with black text Description automatically generated| image:: media/image1.png
   :width: 4.80694in
   :height: 2.81389in
.. |Text Description automatically generated| image:: media/image2.png
   :width: 5.90551in
   :height: 2.05985in
