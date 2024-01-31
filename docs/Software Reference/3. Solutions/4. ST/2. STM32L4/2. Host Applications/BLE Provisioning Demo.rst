BLE Provisioning Demo
=====================

The HAPI APIs residing in the host microcontroller (STM32) connects to
Talaria TWO module via UART/SPI. Using these HAPI APIs, users can write
applications to perform multiple functions with Talaria TWO. This series
of Host Application Notes discusses more on using these APIs to perform
specific functions.

This document provides details on how to use the HAPI APIs to create the
BLE Provisioning demo application to:

1.  Initialize the HAPI interface

2.  Select the interface

3.  Enable/disable the scramble on the interface

4.  Create/destroy BLE interface

5.  Create GATT server

6.  Add services

7.  Start the server for provisioning

8.  Read the provisioning data

9.  Scan for Wi-Fi networks

10. Connect to a Wi-Fi network

Connection Set-up
=================

Host processor communicates with Talaria TWO via a SPI or UART
interface. The connection set-up used to test the application is as
shown in Figure 1.

|A diagram of different types of communication Description automatically
generated with medium confidence|

Figure 1: Connection set-up for application testing

STM32L433RC-P as Host Controller
--------------------------------

STM32L433RC-P is the host controller which will have the BLE
Provisioning demo application running on it. This host is in-turn
connected to the InnoPhase Talaria TWO board through SPI/UART interface.
The serial to Wi-Fi application (stw_multi_proto) firmware should be run
on the Talaria TWO board.

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

**Note**:

Write the part.json file to the Talaria TWO filesystem.

a. Write files: Follow the instructions described in section: *Write
   Files* of the document User_Guide_for_Talaria_TWO_Download_Tool.pdf
   (path:
   *I-CUBE-T2-STW-lib_x.y\\STM32CubeExpansion_T2-HostAPI-lib_vx.y\\Documentation\\Download_Tool_UG*)

b. part.json file path: *sdk_x.y\\examples\\prov\\data*

x and y in x.y refers to the software package release version.

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

1. Download and install the Android or iOS mobile application from the
   play store using the following links:

a. **Android**:https://play.google.com/store/apps/details?id=com.innophase.provisioning&hl=en&gl=US

b. **iOS**: https://apps.apple.com/in/app/ble-provisioning/id1627682345

..

   |A screenshot of a phone Description automatically generated|

Figure 2: Android mobile app in the play store

   |Screenshot of a phone screen Description automatically generated|

Figure 3: iOS mobile app in the app store

2. Open the provisioning mobile app on an Android phone

|image1|

   Figure 4: Provisioning mobile app - home screen

3. Open any console (serial terminal) on STM32 MCU with a baudrate of
   115200

4. Reset the STM32 and check the MCU console. The Talaria TWO starts the
   BLE advertisement in peripheral mode.

5. The mobile app will be able to scan the Talaria TWO BLE device and
   once connected to the device, a window to enter the passphrase of the
   selected AP appears.

|Graphical user interface, text, application Description automatically
generated|

   Figure 5: Entering SSID and passphrase

6. On entering the passphrase, press the send button. Talaria TWO
   receives this information and tries to connect to the specified AP
   and the success/failure of the connection is communicated back to the
   mobile app.

|A white box with black text Description automatically generated|

   Figure 6: Successful connection

**Note**: For BLE Provisioning, it is recommended to use the Talaria TWO
provisioning app.

To make certain appropriate HAL operation, the application must ensure
that the HAL time base is always set to 1 millisecond. The FreeRTOS heap
size configTOTAL_HEAP_SIZE as defined in FreeRTOSConfig.h is set as per
the OS resources’ memory requirements of the application with a +10%
margin and rounded to the upper Kbyte boundary.

For more details on the FreeRTOS implementation on STM32Cube, please
refer to UM1722 - Developing Applications on STM32Cube with RTOS.

BLE Provisioning Application
============================

This section describes the application details along with code snippets.
The application uses HAPI APIs to achieve the functionality. HAPI APIs
presumes that the platform related initialization and clock settings are
completed by default.

1. 

2. 

3. 

4. 

5. 

6. 

7. 

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

Create Common GATT Server
-------------------------

+-----------------------------------------------------------------------+
| hapi_bt_host_common_server_create(hapi_bt_host, "tname", 0,           |
| "tmanuf");                                                            |
+=======================================================================+
+-----------------------------------------------------------------------+

Create Custom BLE Service
-------------------------

+-----------------------------------------------------------------------+
| void \*service;                                                       |
|                                                                       |
| service = hapi_bt_host_gatt_create_service_128(hapi_bt_host,          |
| UUID_CUSTOM_SERVICE);                                                 |
+=======================================================================+
+-----------------------------------------------------------------------+

Add BLE Services
----------------

+-----------------------------------------------------------------------+
| hapi_bt_host_gatt_add_service(hapi_bt_host, service);                 |
+=======================================================================+
+-----------------------------------------------------------------------+

Configure BLE Advertisements
----------------------------

+-----------------------------------------------------------------------+
| hapi_bt_host_gap_cfg_adv(hapi_bt_host, 10240, 0, 160, 480, 0, 7);     |
+=======================================================================+
+-----------------------------------------------------------------------+

Add BLE Indication Handler for Read/Write Characteristics
---------------------------------------------------------

+-----------------------------------------------------------------------+
| hapi_add_ind_handler(hapi, HIO_GROUP_BT_HOST,                         |
| BT_HOST_GATT_CHAR_RD_IND, bt_data_rd_req, hapi_bt_host);              |
|                                                                       |
| hapi_add_ind_handler(hapi, HIO_GROUP_BT_HOST,                         |
| BT_HOST_GATT_CHAR_WR_IND, bt_data_wr_req, hapi_bt_host);              |
+=======================================================================+
+-----------------------------------------------------------------------+

Start BLE Advertisement
-----------------------

+-----------------------------------------------------------------------+
| hapi_bt_host_gap_connectable(hapi_bt_host,                            |
| GAP_CONNECTABLE_MODE_UNDIRECT, bt_hci_addr_type_random,               |
| addr_type_zero, address_zero);                                        |
+=======================================================================+
+-----------------------------------------------------------------------+

Create WCM Interface
--------------------

+-----------------------------------------------------------------------+
| hapi_wcm_create(hapi);                                                |
+=======================================================================+
+-----------------------------------------------------------------------+

Connecting to a Wi-Fi Network 
------------------------------

+-----------------------------------------------------------------------+
| hapi_wcm_autoconnect(hapi_wcm, 1, ssid, pw);                          |
+=======================================================================+
+-----------------------------------------------------------------------+

Set WCM Indication Handler
--------------------------

+-----------------------------------------------------------------------+
| hapi_wcm_set_link_cb(hapi_wcm, wcm_link_cb, NULL);                    |
+=======================================================================+
+-----------------------------------------------------------------------+

Expected Output
===============

The provided android application should be able to connect to the BLE
device on Talaria TWO and configure the SSID and passphrase. On
successful connection, the Talaria TWO board will associate to the AP as
specified by the SSID and passphrase.

| 
| |A screenshot of a computer Description automatically generated|

Figure 7: Expected output

Application Files and Functions
===============================

+-------------------------------------+--------------------------------+
| **File**                            | **Function**                   |
+=====================================+================================+
| /T2-HAN-010/Src/main.c              | Main Program                   |
+-------------------------------------+--------------------------------+
| /T2-HAN-0                           | HAL time-base file             |
| 10/Src/stm32l4xx_hal_timebase_tim.c |                                |
+-------------------------------------+--------------------------------+
| /T2-HAN-010/Src/stm32l4xx_it.c      | Interrupt handlers             |
+-------------------------------------+--------------------------------+
| /T2-HAN-010/Src/system_stm32l4xx.c  | STM32L4xx system clock         |
|                                     | configuration file             |
+-------------------------------------+--------------------------------+
| /T2-HAN-010/Src/freertose.c         | Code for free RTOS application |
+-------------------------------------+--------------------------------+
| /T2-HAN-010/Src/stm32l4xx_hal_msp.c | Code for MSP                   |
|                                     | i                              |
|                                     | nitialization/deinitialization |
+-------------------------------------+--------------------------------+
| /T2-HAN-010/Src/syscalls.c          | System calls file              |
+-------------------------------------+--------------------------------+
| /T2-HAN-010/Src/sysmem.c            | System Memory calls file       |
+-------------------------------------+--------------------------------+
| /T                                  | System startup file            |
| 2-HAN-010/Src/startup_stm32l4a6xx.s |                                |
+-------------------------------------+--------------------------------+
| /T2-HAN-010/Inc/main.h              | Main program header file       |
+-------------------------------------+--------------------------------+
| /                                   | HAL Library Configuration file |
| T2-HAN-010/Inc/stm32l4xx_hal_conf.h |                                |
+-------------------------------------+--------------------------------+
| /T2-HAN-010/Inc/stm32l4xx_it.h      | Interrupt handler’s header     |
|                                     | file                           |
+-------------------------------------+--------------------------------+
| /T2-HAN-010/Inc/FreeRTOSConfig.h    | FreeRTOS Configuration file    |
+-------------------------------------+--------------------------------+
| /T2-HAN-010/Src/HAPI/app.c          | Application file               |
+-------------------------------------+--------------------------------+
| /T2-HAN-010/Src/HAPI/app_bt.c       | BLE application file           |
+-------------------------------------+--------------------------------+
| /T2-HA                              | BLE provisioning application   |
| N-010/Src/HAPI/app_bt_provisioing.c | file                           |
+-------------------------------------+--------------------------------+
| /T2-HAN-010/Src/HAPI/bt_att.h,      | BLE application header files   |
| /T2-HAN-010/Src/HAPI/bt_gatt.h,     |                                |
| /T2-HAN-010/Src/HAPI/uuid.h         |                                |
+-------------------------------------+--------------------------------+

Table 1: Application files and functions

.. |A diagram of different types of communication Description automatically generated with medium confidence| image:: media/image1.png
   :width: 6.29921in
   :height: 3.65325in
.. |A screenshot of a phone Description automatically generated| image:: media/image2.jpeg
   :width: 2.75591in
   :height: 5.53126in
.. |Screenshot of a phone screen Description automatically generated| image:: media/image3.png
   :width: 2.75591in
   :height: 4.36454in
.. |image1| image:: media/image4.jpeg
   :width: 2.75591in
   :height: 5.68863in
.. |Graphical user interface, text, application Description automatically generated| image:: media/image5.jpeg
   :width: 2.75591in
   :height: 5.84195in
.. |A white box with black text Description automatically generated| image:: media/image6.png
   :width: 2.55906in
   :height: 5.35166in
.. |A screenshot of a computer Description automatically generated| image:: media/image7.png
   :width: 7.48031in
   :height: 5.45854in
