TLS Demo Application
====================

The HAPI APIs residing in the host microcontroller (STM32) connects to
Talaria TWO module via UART/SPI. Using these HAPI APIs, users can write
applications to perform multiple functions with Talaria TWO. This series
of Host Application Notes discusses more on using these APIs to perform
specific functions.

This document provides details on how to use the HAPI APIs to create the
TLS demo application to:

1.  Initialize the HAPI interface

2.  Select the interface

3.  Enable/disable the scramble on the interface

4.  Create/destroy a Wi-Fi network interface

5.  Scan for Wi-Fi networks

6.  Connect to a Wi-Fi network

7.  Create TLS socket by using TLS HAPI APIs

8.  Upload TLS certificate

9.  Perform TLS handshake and send TLS request

10. Receive data on TLS socket

**Connection Set-up**

Host processor communicates with Talaria TWO via a SPI or UART
interface. The connection set-up used to test the application is as
shown in Figure 1.

|image1|

Figure 1: Connection set-up for application testing

STM32L433RC-P as Host Controller
--------------------------------

STM32L433RC-P is the host controller which will have the TLS demo
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

STM32L4A6ZG is the host controller which will have the TLS demo
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

**Set-up & Usage**

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

**Testing**

Sample application
------------------

The sample application discussed in this application note runs
specifically on STM32L4A6ZG/STM32L433RC-P devices. This example has been
tested with NUCLEO-L4A6ZG/NUCLEO-L433RC-P board and can be easily
tailored to any other supported device and development board.

1. Reset the STM32 and check the MCU console. MCU will boot and the
   Wi-Fi connection is established.

2. The requested TLS data is printed on the console (serial terminal).

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

.. _tls-demo-application-1:

**TLS Demo Application**

This section describes the application details along with code snippets.
The application uses HAPI APIs to achieve the functionality. HAPI APIs
presumes that the platform related initialization and clock settings are
completed by default.

HAPI Interface Initialization
-----------------------------

.. code-block:: shell

    struct hapi *hapi;
    #ifdef HAPI_INTERFACE_UART_ENABLED
    /* Register the uart, and baud rate to hapi */
    hapi = hapi_uart_init(hapi_uart, hapi_uart_tx, hapi_uart_rx);
    #endif
    #ifdef HAPI_INTERFACE_SPI_ENABLED
    /* Register the SPI */
    hapi = hapi_spi_init(hapi_spi, hapi_spi_cs_high, hapi_spi_cs_low, hapi_spi_tx, hapi_spi_rx);
    #endif


HAPI Interface Start and Disable Sleep Mode in Configuration
------------------------------------------------------------

.. code-block:: shell

    hapi_start(hapi);
    hapi_config(hapi, 0, 0, 0, 0, 0);

Check HAPI Communication with Talaria TWO EVB
---------------------------------------------

.. code-block:: shell

    hapi_hio_query(hapi,&hio_query_rsp);

Create a Wi-Fi Network Interface and Register the Link Status Callback 
-----------------------------------------------------------------------

.. code-block:: shell

    struct hapi_wcm \* hapi_wcm = hapi_wcm_create(hapi);
    hapi_wcm_set_link_cb(hapi_wcm, wcm_link_cb, NULL);

Connecting to a Wi-Fi network
-----------------------------

The application uses the default SSID and passphrase. These can be
modified as per user AP settings.

.. code-block:: shell

    /\* Connect wifi \*/
    char\* ssid = "innotest";
    char\* passphrase = "innophase123";

    if(true == hapi_wcm_network_profile_add(hapi_wcm, ssid, NULL, passphrase, NULL))
    {
        if(false == hapi_wcm_autoconnect(hapi_wcm, 1))
        {
            banner="hapi_wcm_autoconnect : failed..\r\n";
        }
    }


HAPI TLS Socket Create
----------------------

.. code-block:: shell

    char* port = "443";
    char* server = "www.example.com";
    struct hapi_TLS *hapi_TLS = hapi_TLS_create(hapi, server, port, 16384, sizeof(root_ca_pem), 0, 0);


HAPI TLS Data Ready Callback
----------------------------

.. code-block:: shell

    hapi_tls_set_notification_cb(hapi_tls, dataready_cb, NULL);

TLS Certificate Upload
----------------------

.. code-block:: shell

    hapi_TLS_upload_cert(hapi_TLS, HAPI_TLS_ROOT_CERT, root_ca_pem, sizeof(root_ca_pem));

TLS Handshake
-------------

.. code-block:: shell

    hapi_TLS_handshake(hapi_TLS, HAPI_TLS_AUTH_MODE_OPTIONAL));


TLS Data Send
-------------

.. code-block:: shell

    static const char get_request[] = "GET / HTTP/1.0\\r\\n\\r\\n";
    hapi_TLS_write(hapi_TLS, get_request, sizeof(get_request));


TLS Data Read
-------------

.. code-block:: shell

    char rx_data[1024];
    ssize_t size = hapi_TLS_read(hapi_TLS, rx_data, buf_size-1);

TLS Socket Close
----------------

.. code-block:: shell

    hapi_TLS_close(hapi_TLS));


**Expected Output**

The MCU will connect to the AP specified by the SSID and creates the TLS
socket to send and receive data.

|Text Description automatically generated|

Figure 2: Expected Output

**Application Files and Functions**

.. table:: Table 1: Application files and functions

    +-----------------------------------------------+----------------------+
    |    File                                       |    Function          |
    +===============================================+======================+
    |    Inn                                        |    Main Program      |
    | oPhase_HAPI/InnoPhase_HAPI_TLSdemo/Src/main.c |                      |
    +-----------------------------------------------+----------------------+
    |    InnoPhase_HAPI/InnoPhase_                  |    HAL time-base     |
    | HAPI_TLSdemo/Src/stm32l4xx_hal_timebase_tim.c |    file              |
    +-----------------------------------------------+----------------------+
    |    InnoPhase_H                                |    Interrupt         |
    | API/InnoPhase_HAPI_TLSdemo/Src/stm32l4xx_it.c |    handlers          |
    +-----------------------------------------------+----------------------+
    |    InnoPhase_HAPI/                            |    STM32L4xx system  |
    | InnoPhase_HAPI_TLSdemo/Src/system_stm32l4xx.c |    clock             |
    |                                               |    configuration     |
    |                                               |    file              |
    +-----------------------------------------------+----------------------+
    |    InnoPhas                                   |    code for free     |
    | e_HAPI/InnoPhase_HAPI_TLSdemo/Src/freertose.c |    RTOS application  |
    +-----------------------------------------------+----------------------+
    |    InnoPhase_HAPI/I                           |    code for MSP      |
    | nnoPhase_HAPI_TLSdemo/Src/stm32l4xx_hal_msp.c |    initializat       |
    |                                               | ion/deinitialization |
    +-----------------------------------------------+----------------------+
    |    InnoPha                                    |    System calls file |
    | se_HAPI/InnoPhase_HAPI_TLSdemo/Src/syscalls.c |                      |
    +-----------------------------------------------+----------------------+
    |    InnoP                                      |    System Memory     |
    | hase_HAPI/InnoPhase_HAPI_TLSdemo/Src/sysmem.c |    calls file        |
    +-----------------------------------------------+----------------------+
    |    InnoPhase_HAPI/InnoPhase_HAPI_TLSdemo/Src/ |    System startup    |
    |    startup_stm32l433rctxp.s                   |    file              |
    +-----------------------------------------------+----------------------+
    |    Inn                                        |    Main program      |
    | oPhase_HAPI/InnoPhase_HAPI_TLSdemo/Inc/main.h |    header file       |
    +-----------------------------------------------+----------------------+
    |    InnoPhase_HAPI/In                          |    HAL Library       |
    | noPhase_HAPI_TLSdemo/Inc/stm32l4xx_hal_conf.h |    Configuration     |
    |                                               |    file              |
    +-----------------------------------------------+----------------------+
    |    InnoPhase_H                                |    Interrupt         |
    | API/InnoPhase_HAPI_TLSdemo/Inc/stm32l4xx_it.h |    handler’s header  |
    |                                               |    file              |
    +-----------------------------------------------+----------------------+
    |    InnoPhase_HAP                              |    FreeRTOS          |
    | I/InnoPhase_HAPI_TLSdemo/Inc/FreeRTOSConfig.h |    Configuration     |
    |                                               |    file              |
    +-----------------------------------------------+----------------------+

.. |image1| image:: media/image1.png
.. |Text Description automatically generated| image:: media/image2.png
   :width: 7.72441in
   :height: 7.28077in
