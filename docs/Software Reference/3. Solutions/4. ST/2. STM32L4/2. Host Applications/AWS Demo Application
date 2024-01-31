AWS Demo Application
====================

The HAPI APIs residing in the host microcontroller (STM32) connects to
Talaria TWO module via UART/SPI. Using these HAPI APIs, users can write
applications to perform multiple functions with Talaria TWO. This series
of Host Application Notes discusses more on using these APIs to perform
specific functions.

This document provides details on how to use the HAPI APIs to create the
AWS demo application to:

1. Initialize the HAPI interface

2. Select the interface

3. Enable/disable the scramble on the interface

4. Create/destroy a Wi-Fi network interface

5. Scan for Wi-Fi networks

6. Connect to a Wi-Fi network

7. Create an AWS connection using HAPI APIs

8. Subscribe for AWS IoT messages from the AWS server

9. Publish data to the AWS server

**Connection Set-up**

Host processor communicates with Talaria TWO via a SPI or UART
interface. The connection set-up used to test the application is as
shown in Figure 1.

|image1|

Figure 1: Connection set-up for application testing

STM32L433RC-P as Host Controller
--------------------------------

STM32L433RC-P is the host controller which will have the AWS demo
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

STM32L4A6ZG is the host controller which will have the AWS demo
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

**AWS IoT Application**


This section describes the application details along with code snippets.
The application uses HAPI APIs to achieve the functionality. HAPI APIs
presumes that the platform related initialization and clock settings are
completed by default.

HAPI Interface Initialization
-----------------------------

.. code-block:: c

    struct hapi *hapi;
    #ifdef HAPI_INTERFACE_UART_ENABLED
    /* Register the uart, and baud rate to hapi */
    hapi = hapi_uart_init(hapi_uart, hapi_uart_tx, hapi_uart_rx);
    #endif
    #ifdef HAPI_INTERFACE_SPI_ENABLED
    /* Register the SPI */
    hapi = hapi_spi_init(hapi_spi, hapi_spi_cs_high, hapi_spi_cs_low, hapi_spi_tx, hapi_spi_rx);
    #endif


HAPI Interface Start and Disable Sleep Mode in configuration
------------------------------------------------------------

.. code-block:: shell

    hapi_start(hapi);
    hapi_config(hapi, 0, 0, 0, 0, 0);


Check HAPI Communication with Talaria TWO EVB
---------------------------------------------

.. code-block:: shell

    hapi_hio_query(hapi,&hio_query_rsp);

Create a Wi-Fi Network Interface and Register Link Status Callback 
-------------------------------------------------------------------

.. code-block::

    struct hapi_wcm \* hapi_wcm = hapi_wcm_create(hapi);
    hapi_wcm_set_link_cb(hapi_wcm, wcm_link_cb, NULL);


Connecting to a Wi-Fi network
-----------------------------



The application uses the default SSID and passphrase. These can be
modified as per user AP settings.

.. code-block:: c

    /\* Connect wifi \*/
    char\* ssid = "innotest";
    char\* passphrase = "innophase123";

.. code-block:: c

    if(true == hapi_wcm_network_profile_add(hapi_wcm, ssid, NULL, passphrase, NULL))
    {
        if(false == hapi_wcm_autoconnect(hapi_wcm, 1))
        {
            banner="hapi_wcm_autoconnect : failed..\\r\\n";
        }
    }


Create an AWS Connection
------------------------

.. code-block::

    if(init_and_connect_aws_iot())
    {
        banner="AWS connecting failed\\r\\n";
    }

Subscribe Data from AWS
-----------------------

.. code-block:: c

    int retval;
    if(retval = start_receiving_message_from_aws())
    {
        banner="\\r\\nfailed subscribing..\\r\\n";
    }
    else{
        banner="\\r\\nsubscribing done..\\r\\n";
    }

Publish Data to AWS
-------------------

.. code-block:: c

    if(start_sending_messages_to_aws(pub_msg,strlen(pub_msg)))
    {
        banner="failed publising\\r\\n";
    }
    else{
        banner="publishing done\\r\\n";
    }

**Expected Output**

The MCU will connect to the AP specified by the SSID and passphrase and
creates the AWS IoT connection with the certificate and URL. The publish
and subscribe on the topic occurs with MQTT protocol. The publishing is
done in every 3 seconds and the same data is received which gets
printed. The same data can be observed in the AWS portal as well.

|Text Description automatically generated|

Figure 2: Expected Output

**Application Files and Functions**

.. table:: Table 1: Application files and functions

    +-----------------------------------------------+----------------------+
    | **File**                                      | **Function**         |
    +===============================================+======================+
    | Inn                                           | Main Program         |
    | oPhase_HAPI/InnoPhase_HAPI_awsdemo/Src/main.c |                      |
    +-----------------------------------------------+----------------------+
    | InnoPhase_HAPI/InnoPhase_                     | HAL time-base file   |
    | HAPI_awsdemo/Src/stm32l4xx_hal_timebase_tim.c |                      |
    +-----------------------------------------------+----------------------+
    | InnoPhase_H                                   | Interrupt handlers   |
    | API/InnoPhase_HAPI_awsdemo/Src/stm32l4xx_it.c |                      |
    +-----------------------------------------------+----------------------+
    | InnoPhase_HAPI/                               | STM32L4xx system     |
    | InnoPhase_HAPI_awsdemo/Src/system_stm32l4xx.c | clock configuration  |
    |                                               | file                 |
    +-----------------------------------------------+----------------------+
    | InnoPhas                                      | Code for free RTOS   |
    | e_HAPI/InnoPhase_HAPI_awsdemo/Src/freertose.c | application          |
    +-----------------------------------------------+----------------------+
    | InnoPhase_HAPI/I                              | Code for MSP         |
    | nnoPhase_HAPI_awsdemo/Src/stm32l4xx_hal_msp.c | initializat          |
    |                                               | ion/deinitialization |
    +-----------------------------------------------+----------------------+
    | InnoPha                                       | System calls file    |
    | se_HAPI/InnoPhase_HAPI_awsdemo/Src/syscalls.c |                      |
    +-----------------------------------------------+----------------------+
    | InnoP                                         | System Memory calls  |
    | hase_HAPI/InnoPhase_HAPI_awsdemo/Src/sysmem.c | file                 |
    +-----------------------------------------------+----------------------+
    | InnoPhase_HAPI/InnoPhase_HAPI_awsdemo/Src/    | System startup file  |
    | startup_stm32l433rctxp.s                      |                      |
    +-----------------------------------------------+----------------------+
    | Inn                                           | Main program header  |
    | oPhase_HAPI/InnoPhase_HAPI_awsdemo/Inc/main.h | file                 |
    +-----------------------------------------------+----------------------+
    | InnoPhase_HAPI/In                             | HAL Library          |
    | noPhase_HAPI_awsdemo/Inc/stm32l4xx_hal_conf.h | Configuration file   |
    +-----------------------------------------------+----------------------+
    | InnoPhase_H                                   | Interrupt handler’s  |
    | API/InnoPhase_HAPI_awsdemo/Inc/stm32l4xx_it.h | header file          |
    +-----------------------------------------------+----------------------+
    | InnoPhase_HAP                                 | FreeRTOS             |
    | I/InnoPhase_HAPI_awsdemo/Inc/FreeRTOSConfig.h | Configuration file   |
    +-----------------------------------------------+----------------------+


.. |image1| image:: media/image1.png
.. |Text Description automatically generated| image:: media/image2.png
   :width: 7.72431in
   :height: 6.20208in
