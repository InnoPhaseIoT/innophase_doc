MQTT Demo Application
=====================

The HAPI APIs residing in the host microcontroller (STM32) connects to
Talaria TWO module via UART/SPI. Using these HAPI APIs, users can write
applications to perform multiple functions with Talaria TWO. This series
of Host Application Notes discusses more on using these APIs to perform
specific functions.

This document provides details on how to use the HAPI APIs to create the
MQTT demo application to:

1. Initialize the HAPI interface

2. Select the interface

3. Enable/disable the scramble on the interface

4. Create/destroy a Wi-Fi network interface

5. Scan for Wi-Fi networks

6. Connect to a Wi-Fi network

7. Create MQTT connection

8. Publish a dummy message to the broker

9. Subscribe for a topic to receive data from the broker

Connection Set-up
=================

Host processor communicates with Talaria TWO via a SPI or UART
interface. The connection set-up used to test the application is as
shown in Figure 1.

|image1|

Figure 1: Connection set-up for application testing

STM32L433RC-P as Host Controller
--------------------------------

STM32L433RC-P is the host controller which will have the MQTT demo
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

1. Open any console (serial terminal) on STM32 MCU with a baudrate of
   115200

2. Reset the STM32 and check the MCU console. MCU will boot, the Wi-Fi
   connection is established and MQTT Module starts as follows:

   a. Initializes the MQTT network and connects to MQTT Server

   b. Initializes the MQTT Client and opens a new connection with MQTT
      Broker

   c. MQTT Client publishes message to topic group and receives the
      messages from subscribed topic group

   d. MQTT Client unsubscribes to topic group and disconnects

   e. MQTT Network disconnects from the MQTT Server

**Note**:

1. To make certain appropriate HAL operation, the application must
   ensure that the HAL time base is always set to 1 millisecond. The
   FreeRTOS heap size configTOTAL_HEAP_SIZE as defined in
   FreeRTOSConfig.h is set as per the OS resources’ memory requirements
   of the application with a +10% margin and rounded to the upper Kbyte
   boundary.

2. For more details on the FreeRTOS implementation on STM32Cube, please
   refer to UM1722 - Developing Applications on STM32Cube with RTOS.

3. MQTT demo application supports the following secured modes:

   a. 0 (unsecured) on port 1883.

   b. 1 (secured without certificate) on port 8883 and 2 (secured with
      certificate validation) on port 8884.

.. _mqtt-demo-application-1:

MQTT Demo Application
=====================

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

The application uses the default SSID and passphrase. These can be
modified as per user AP settings.

+-----------------------------------------------------------------------+
| /\* Connect wifi \*/                                                  |
|                                                                       |
| char\* ssid = "innotest";                                             |
|                                                                       |
| char\* passphrase = "innophase123";                                   |
+=======================================================================+
+-----------------------------------------------------------------------+

+-----------------------------------------------------------------------+
| if(true == hapi_wcm_network_profile_add(hapi_wcm, ssid, NULL,         |
| passphrase, NULL))                                                    |
|                                                                       |
| {                                                                     |
|                                                                       |
| if(false == hapi_wcm_autoconnect(hapi_wcm, 1))                        |
|                                                                       |
| {                                                                     |
|                                                                       |
| banner="hapi_wcm_autoconnect : failed..\\r\\n";                       |
|                                                                       |
| }                                                                     |
|                                                                       |
| }                                                                     |
+=======================================================================+
+-----------------------------------------------------------------------+

Create a MQTT Network Interface
-------------------------------

+-----------------------------------------------------------------------+
| struct hapi_mqtt\* hapi_mqtt;                                         |
|                                                                       |
| hapi_mqtt = hapi_mqtt_nw_init(hapi, &sockId, &stat);                  |
+=======================================================================+
+-----------------------------------------------------------------------+

MQTT Network Connect
--------------------

+-----------------------------------------------------------------------+
| bool status = false;                                                  |
|                                                                       |
| status = hapi_mqtt_nw_connect(hapi, hapi_mqtt, MQTT_SERVER, 1883);    |
+=======================================================================+
+-----------------------------------------------------------------------+

MQTT Network Disconnect
-----------------------

+-----------------------------------------------------------------------+
| bool status = false;                                                  |
|                                                                       |
| status = hapi_mqtt_nw_disconnect(hapi, hapi_mqtt);                    |
+=======================================================================+
+-----------------------------------------------------------------------+

MQTT Client Initialization
--------------------------

+-----------------------------------------------------------------------+
| bool status = false;                                                  |
|                                                                       |
| status = hapi_mqtt_client_init(hapi, hapi_mqtt, timeout_ms);          |
+=======================================================================+
+-----------------------------------------------------------------------+

MQTT Protocol Connect
---------------------

+-----------------------------------------------------------------------+
| bool status = false;                                                  |
|                                                                       |
| status = hapi_mqtt_connect(hapi, hapi_mqtt, MQTT_VERSION,             |
| MQTT_CLIENTID, MQTT_USERNAME, MQTT_PASSWORD);                         |
+=======================================================================+
+-----------------------------------------------------------------------+

MQTT Protocol Disconnect
------------------------

+-----------------------------------------------------------------------+
| bool status = false;                                                  |
|                                                                       |
| status = hapi_mqtt_disconnect(hapi, hapi_mqtt);                       |
+=======================================================================+
+-----------------------------------------------------------------------+

MQTT Publish
------------

+-----------------------------------------------------------------------+
| bool status = false;                                                  |
|                                                                       |
| status = hapi_mqtt_publish(hapi, hapi_mqtt, MQTT_TOPIC, TOPIC);       |
+=======================================================================+
+-----------------------------------------------------------------------+

MQTT Subscribe
--------------

+-----------------------------------------------------------------------+
| bool status = false;                                                  |
|                                                                       |
| status = hapi_mqtt_subscribe(hapi, hapi_mqtt, MQTT_TOPIC1, QOS0);     |
+=======================================================================+
+-----------------------------------------------------------------------+

MQTT Un-Subscribe
-----------------

+-----------------------------------------------------------------------+
| bool status = false;                                                  |
|                                                                       |
| status = hapi_mqtt_unsubscribe(hapi, hapi_mqtt, MQTT_TOPIC1);         |
+=======================================================================+
+-----------------------------------------------------------------------+

Expected Output
===============

The MCU will connect to the AP specified by the SSID and passphrase. On
successful connection, it creates the MQTT connection to the broker with
the credentials provided and, in a loop, publish dummy data on topic
PUBMSG. This application is also subscribed to the topic SUBMSG1. The
received messages on this topic are printed on the console.

**Note**: If data more than 2KB needs to be sent, the following changes
need to be implemented:

1. Program Talaria TWO with an appropriate value for hio.maxsize

For example, to send 7KB of data, program Talaria TWO with the following
boot arguments:

+-----------------------------------------------------------------------+
| hio.transport=1, hio.irq_min_gap=1000, **hio.maxsize=8000**           |
+=======================================================================+
+-----------------------------------------------------------------------+

2. Change the value of RX_MAX_SIZE and TX_MAX_SIZE to the appropriate
   data length in the application configuration file (app_config.h) at:
   *<Project Path>\\T2-HAN-011\\Src\\HAPI\\app_config.h*:

*#define RX_MAX_SIZE = 2*1024;*

*#define TX_MAX_SIZE = 2*1024;*

For example, to send 7KB of data, change RX_MAX_SIZE and TX_MAX_SIZE to:

*#define RX_MAX_SIZE = 7*1024;*

*#define TX_MAX_SIZE = 7*1024;*

|A screenshot of a computer Description automatically generated|

Figure 2: Expected Output

Application Files and Functions
===============================

+-------------------------------------------+--------------------------+
| **File**                                  | **Function**             |
+===========================================+==========================+
| Free                                      | Main Program             |
| RTOS/FreeRTOS_INP2045_wifidemo/Src/main.c |                          |
+-------------------------------------------+--------------------------+
| FreeRTOS/FreeRTOS_INP2045_                | HAL time-base file       |
| wifidemo/Src/stm32l4xx_hal_timebase_tim.c |                          |
+-------------------------------------------+--------------------------+
| FreeRTOS/Fre                              | Interrupt handlers       |
| eRTOS_INP2045_wifidemo/Src/stm32l4xx_it.c |                          |
+-------------------------------------------+--------------------------+
| FreeRTOS/FreeRTO                          | STM32L4xx system clock   |
| S_INP2045_wifidemo/Src/system_stm32l4xx.c | configuration file       |
+-------------------------------------------+--------------------------+
| FreeRTOS/                                 | Code for free RTOS       |
| FreeRTOS_INP2045_wifidemo/Src/freertose.c | application              |
+-------------------------------------------+--------------------------+
| FreeRTOS/FreeRTOS                         | Code for MSP             |
| _INP2045_wifidemo/Src/stm32l4xx_hal_msp.c | initial                  |
|                                           | ization/deinitialization |
+-------------------------------------------+--------------------------+
| FreeRTOS                                  | System calls file        |
| /FreeRTOS_INP2045_wifidemo/Src/syscalls.c |                          |
+-------------------------------------------+--------------------------+
| FreeRT                                    | System Memory calls file |
| OS/FreeRTOS_INP2045_wifidemo/Src/sysmem.c |                          |
+-------------------------------------------+--------------------------+
| FreeRTOS/FreeRTOS_INP2045_wifidemo/Src/   | System startup file      |
| startup_stm32l433rctxp.s                  |                          |
+-------------------------------------------+--------------------------+
| Free                                      | Main program header file |
| RTOS/FreeRTOS_INP2045_wifidemo/Inc/main.h |                          |
+-------------------------------------------+--------------------------+
| FreeRTOS/FreeRTOS_                        | HAL Library              |
| INP2045_wifidemo/Inc/stm32l4xx_hal_conf.h | Configuration file       |
+-------------------------------------------+--------------------------+
| FreeRTOS/Fre                              | Interrupt handler’s      |
| eRTOS_INP2045_wifidemo/Inc/stm32l4xx_it.h | header file              |
+-------------------------------------------+--------------------------+
| FreeRTOS/FreeR                            | FreeRTOS Configuration   |
| TOS_INP2045_wifidemo/Inc/FreeRTOSConfig.h | file                     |
+-------------------------------------------+--------------------------+

Table 1: Application files and functions

.. |image1| image:: media/image1.png
.. |A screenshot of a computer Description automatically generated| image:: media/image2.png
   :width: 7.28346in
   :height: 4.5461in
