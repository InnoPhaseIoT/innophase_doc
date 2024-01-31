Wi-Fi Demo Application
======================

The HAPI APIs residing in the host microcontroller (STM32) connects to
Talaria TWO module via UART/SPI. Using these HAPI APIs, users can write
applications to perform multiple functions with Talaria TWO. This series
of Host Application Notes discusses more on using these APIs to perform
specific functions.

This document provides details on how to use the HAPI APIs to create the
Wi-Fi demo application to:

1. Initialize the HAPI interface

2. Select the interface

3. Enable/disable the scramble on the interface

4. Create/destroy a Wi-Fi network interface

5. Scan for Wi-Fi networks

6. Connect to a Wi-Fi network

7. Create a server socket

8. Wait for client connection and data

9. Send and receive data on the socket

Connection Set-up
=================

Host processor communicates with Talaria TWO via a SPI or UART
interface. The connection set-up used to test the application is as
shown in Figure 1.

|image1|

Figure 1: Connection set-up for application testing

STM32L433RC-P as Host Controller
--------------------------------

STM32L433RC-P is the host controller which will have the Wi-Fi demo
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

STM32L4A6ZG is the host controller which will have the Wi-Fi demo
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

1. Start TCP client on a PC that connects to the same network, with
   server IP as the IP printed on the STM32 serial console and port as
   9000

For example, TCP client: netcat on PC

+-----------------------------------------------------------------------+
| #nc <ip address of T2> 9000                                           |
+=======================================================================+
+-----------------------------------------------------------------------+

2. Send any data from the TCP client. The same data is received on the
   client from ST32-Talaria TWO device.

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

.. _wi-fi-demo-application-1:

Wi-Fi Demo Application
======================

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

|A close-up of a white background Description automatically generated|

Figure 2: Security types

The SSID, passphrase and other parameters can be modified as per the
security type selected as shown in Figure 3.

|A screenshot of a computer code Description automatically generated|

Figure 3: Modifying parameters as per AP settings

Write CA certificate only on Talaria TWO data partition using the
Download Tool for Enterprise_PEAP and edit app.c to include the
following parameters:

|image2|

Figure 4: Modifying parameters for Enterprise PEAP

|Text Description automatically generated|

Figure 5: Connecting Wi-Fi parameters - Enterprise PEAP

Write CA cert, Client cert & Client key on Talaria TWO data partition
using the Download Tool for Enterprise_TLS and edit app.c to include the
following parameters:

|A screenshot of a computer Description automatically generated|

Figure 6: Modifying parameters for Enterprise TLS

|image3|

Figure 7: Connecting Wi-Fi parameters - Enterprise TLS

For Enterprise_PSK, edit app.c to include the following parameters:

|image4|

Figure 8: Modifying parameters for Enterprise PSK

|A screenshot of a computer screen Description automatically generated|

Figure 9: Connecting Wi-Fi parameters - Enterprise PSK

Create a server socket
----------------------

The application creates a TCP server socket on port 9000 and wait for
client connection.

+-----------------------------------------------------------------------+
| uint32_t listen_sock;                                                 |
|                                                                       |
| listen_sock = socket_create(hapi, HIO_SOCK_TCP_SERVER,                |
| "255.255.255.255", "9000")                                            |
+=======================================================================+
+-----------------------------------------------------------------------+

Incoming Socket Connection Registration
---------------------------------------

This code registers a handler that get called when the server receives a
client connection .

+-----------------------------------------------------------------------+
| /\* Register indication handlers \*/                                  |
|                                                                       |
| hapi_add_ind_handler(hapi, HIO_GROUP_SOCK,                            |
|                                                                       |
| SOCK_CONNECTION_IND, client_connected_ind_handler, NULL);             |
|                                                                       |
| hapi_add_ind_handler(hapi, HIO_GROUP_SOCK,                            |
|                                                                       |
| SOCK_CLOSE_IND, socket_close_ind_handler, NULL);                      |
+=======================================================================+
+-----------------------------------------------------------------------+

Available Socket Data
---------------------

+-----------------------------------------------------------------------+
| int available;                                                        |
|                                                                       |
| available = hapi_sock_getavailable(hapi, socket);                     |
+=======================================================================+
+-----------------------------------------------------------------------+

Receive Data on the Socket 
---------------------------

+-----------------------------------------------------------------------+
| char rx_data[50];                                                     |
|                                                                       |
| hapi_sock_receive(hapi, socket, rx_data, available);                  |
+=======================================================================+
+-----------------------------------------------------------------------+

Send Data on the Socket
-----------------------

+-----------------------------------------------------------------------+
| const char teststring[] = "Hello world!";                             |
|                                                                       |
| hapi_sock_send_tcp(hapi, socket, teststring, available);              |
+=======================================================================+
+-----------------------------------------------------------------------+

Expected Output
===============

The MCU will connect to the AP specified by the SSID and passphrase. On
successful connection, it creates the TCP server socket wait for client
connection. Once the client gets connected, it waits for the data from
client and sends the same received data after changing the case (upper
to lower or lower to upper). The serial prints on the MCU are as shown
in Figure 10:

|image5|

Figure 10: Expected output

Application Files and Functions
===============================

+----------------------------------------+-----------------------------+
|    File                                |    Function                 |
+========================================+=============================+
|    InnoPhase_H                         |    Main Program             |
| API/InnoPhase_HAPI_wifidemo/Src/main.c |                             |
+----------------------------------------+-----------------------------+
|    InnoPhase_HAPI/InnoPhase_HAPI_wif   |    HAL time-base file       |
| idemo/Src/stm32l4xx_hal_timebase_tim.c |                             |
+----------------------------------------+-----------------------------+
|    InnoPhase_HAPI/Inno                 |    Interrupt handlers       |
| Phase_HAPI_wifidemo/Src/stm32l4xx_it.c |                             |
+----------------------------------------+-----------------------------+
|    InnoPhase_HAPI/InnoPhas             |    STM32L4xx system clock   |
| e_HAPI_wifidemo/Src/system_stm32l4xx.c |    configuration file       |
+----------------------------------------+-----------------------------+
|    InnoPhase_HAPI/I                    |    Code for free RTOS       |
| nnoPhase_HAPI_wifidemo/Src/freertose.c |    application              |
+----------------------------------------+-----------------------------+
|    InnoPhase_HAPI/InnoPhase            |    Code for MSP             |
| _HAPI_wifidemo/Src/stm32l4xx_hal_msp.c |    init                     |
|                                        | ialization/deinitialization |
+----------------------------------------+-----------------------------+
|    InnoPhase_HAPI/                     |    System calls file        |
| InnoPhase_HAPI_wifidemo/Src/syscalls.c |                             |
+----------------------------------------+-----------------------------+
|    InnoPhase_HAP                       |    System memory calls file |
| I/InnoPhase_HAPI_wifidemo/Src/sysmem.c |                             |
+----------------------------------------+-----------------------------+
|    InnoPhase_HAPI/InnoPhase_HAPI       |    System startup file      |
| _wifidemo/Src/startup_stm32l433rctxp.s |                             |
+----------------------------------------+-----------------------------+
|    InnoPhase_H                         |    Main program header file |
| API/InnoPhase_HAPI_wifidemo/Inc/main.h |                             |
+----------------------------------------+-----------------------------+
|    InnoPhase_HAPI/InnoPhase_           |    HAL Library              |
| HAPI_wifidemo/Inc/stm32l4xx_hal_conf.h |    Configuration file       |
+----------------------------------------+-----------------------------+
|    InnoPhase_HAPI/Inno                 |    Interrupt handler’s      |
| Phase_HAPI_wifidemo/Inc/stm32l4xx_it.h |    header file              |
+----------------------------------------+-----------------------------+
|    InnoPhase_HAPI/InnoPh               |    FreeRTOS Configuration   |
| ase_HAPI_wifidemo/Inc/FreeRTOSConfig.h |    file                     |
+----------------------------------------+-----------------------------+

Table 1: Application files and functions

.. |image1| image:: media/image1.png
.. |A close-up of a white background Description automatically generated| image:: media/image2.png
   :width: 4.72441in
   :height: 1.76007in
.. |A screenshot of a computer code Description automatically generated| image:: media/image3.png
   :width: 4.72441in
   :height: 1.79528in
.. |image2| image:: media/image4.png
   :width: 4.72441in
   :height: 1.98658in
.. |Text Description automatically generated| image:: media/image5.png
   :width: 4.72393in
   :height: 2.19167in
.. |A screenshot of a computer Description automatically generated| image:: media/image6.png
   :width: 4.72441in
   :height: 1.91978in
.. |image3| image:: media/image7.png
   :width: 4.72441in
   :height: 2.74734in
.. |image4| image:: media/image8.png
   :width: 4.72441in
   :height: 1.91145in
.. |A screenshot of a computer screen Description automatically generated| image:: media/image9.png
   :width: 4.72441in
   :height: 2.50628in
.. |image5| image:: media/image10.png
   :width: 5.90556in
   :height: 3.88264in
