Azure IoT Application
=====================

The HAPI APIs residing in the host microcontroller (STM32) connects to
Talaria TWO module via UART/SPI. Using these HAPI APIs, users can write
applications to perform multiple functions with Talaria TWO. This series
of Host Application Notes discusses more on using these APIs to perform
specific functions.

This document provides details on how to use the HAPI APIs to create the
Azure IoT application to:

1. Initialize the HAPI interface

2. Select the interface

3. Enable/disable scrambling on the interface

4. Scan for Wi-Fi networks

5. Connect to a Wi-Fi network

6. Initialize and connect to the Azure IoT cloud

7. Subscribe for messages from the Azure IoT cloud

8. Publish data to the Azure IoT cloud

9. Disconnect from Azure IoT cloud

**Connection Set-up**

Host processor communicates with Talaria TWO via a SPI or UART
interface. The connection set-up used to test the application is as
shown in Figure 1.

|image1|

Figure 1: Connection set-up for application testing

STM32L433RC-P as Host Controller
--------------------------------

STM32L433RC-P is the host controller which will have the Azure IoT
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

STM32L4A6ZG is the host controller which will have the Azure IoT
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

**Note**:

To make certain appropriate HAL operation, the application must ensure
that the HAL time base is always set to 1 millisecond. The FreeRTOS heap
size configTOTAL_HEAP_SIZE as defined in FreeRTOSConfig.h is set as per
the OS resources’ memory requirements of the application with a +10%
margin and rounded to the upper Kbyte boundary.

For more details on the FreeRTOS implementation on STM32Cube, please
refer to UM1722 - Developing Applications on STM32Cube with RTOS.

.. _azure-iot-application-1:

**Azure IoT Application**

This section describes the application details along with code snippets.
The application uses HAPI APIs to achieve the functionality. HAPI APIs
presumes that the platform related initialization and clock settings are
completed by default.

HAPI Interface Initialization
-----------------------------

.. code-block:: shell

    struct hapi \*hapi;
    #ifdef HAPI_INTERFACE_UART_ENABLED
    /\* Register the uart, and baud rate to hapi \*/
    hapi = hapi_uart_init(hapi_uart, hapi_uart_tx, hapi_uart_rx);
    #endif
    #ifdef HAPI_INTERFACE_SPI_ENABLED
    /\* Register the SPI \*/
    hapi = hapi_spi_init(hapi_spi, hapi_spi_cs_high, hapi_spi_cs_low,
    hapi_spi_tx, hapi_spi_rx);
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


Create a Wi-Fi Network Interface and Register Link Status Callback 
-------------------------------------------------------------------

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

    if(true == hapi_wcm_network_profile_add(hapi_wcm, ssid, NULL,passphrase, NULL))
    {
        if(false == hapi_wcm_autoconnect(hapi_wcm, 1))
        {
            banner="hapi_wcm_autoconnect : failed..\\r\\n";
        }
    }


Create and Connect Azure IoT cloud
----------------------------------

.. code-block:: shell

    int rc;
    rc = init_and_connect_ms_azure_iot(&mqtt_credentials);

Subscribe Azure IoT Cloud Messages
----------------------------------

.. code-block:: shell

    int rc;
    rc = ms_azure_iot_mqtt_subscribe_for_cloud_to_device_messages(gpclient, mqtt_credentials.client_id,on_new_subscribe_message_from_ms_azure, NULL);

Publish Messages to Azure IoT Cloud
-----------------------------------

.. code-block:: shell

    char msg_payload[100];
    start_sending_messages_to_ms_azure(publish_topic, msg_payload, len);

Disconnect Azure IoT Cloud
--------------------------

.. code-block:: shelll

    ms_azure_iot_mqtt_disconnect(gpclient);


**Expected Output**


The MCU will connect to the AP specified by the SSID and passphrase.
This demo project connects to Azure, executes a handshake, and runs the
MQTT. Once MQTT is successful, it periodically does device to cloud
message method, and pushes data to Azure cloud. These messages can be
observed in the plugin. Right click on the device and click on send C2D
data to enter the data. This entered data will be received at the device
and printed on the serial terminal.

|Text Description automatically generated|

Figure 2: Expected Output

**Application Files and Functions**

.. table:: Table 1: Application files and functions

    +---------------------------------------------+------------------------+
    | **File**                                    | **Function**           |
    +=============================================+========================+
    | InnoPha                                     | Main Program           |
    | se_HAPI/InnoPhase_HAPI_azuredemo/Src/main.c |                        |
    +---------------------------------------------+------------------------+
    | InnoPhase_HAPI/InnoPhase_HAPI               | HAL time-base file     |
    | _azuredemo/Src/stm32l4xx_hal_timebase_tim.c |                        |
    +---------------------------------------------+------------------------+
    | InnoPhase_HAPI/                             | Interrupt handlers     |
    | InnoPhase_HAPI_azuredemo/Src/stm32l4xx_it.c |                        |
    +---------------------------------------------+------------------------+
    | InnoPhase_HAPI/Inno                         | STM32L4xx system clock |
    | Phase_HAPI_azuredemo/Src/system_stm32l4xx.c | configuration file     |
    +---------------------------------------------+------------------------+
    | InnoPhase_HA                                | Code for free RTOS     |
    | PI/InnoPhase_HAPI_azuredemo/Src/freertose.c | application            |
    +---------------------------------------------+------------------------+
    | InnoPhase_HAPI/InnoP                        | Code for MSP           |
    | hase_HAPI_azuredemo/Src/stm32l4xx_hal_msp.c | initializ              |
    |                                             | ation/deinitialization |
    +---------------------------------------------+------------------------+
    | InnoPhase_H                                 | System calls file      |
    | API/InnoPhase_HAPI_azuredemo/Src/syscalls.c |                        |
    +---------------------------------------------+------------------------+
    | InnoPhase                                   | System Memory calls    |
    | _HAPI/InnoPhase_HAPI_azuredemo/Src/sysmem.c | file                   |
    +---------------------------------------------+------------------------+
    | I                                           | System startup file    |
    | nnoPhase_HAPI/InnoPhase_HAPI_azuredemo/Src/ |                        |
    | startup_stm32l433rctxp.s                    |                        |
    +---------------------------------------------+------------------------+
    | InnoPha                                     | Main program header    |
    | se_HAPI/InnoPhase_HAPI_azuredemo/Inc/main.h | file                   |
    +---------------------------------------------+------------------------+
    | InnoPhase_HAPI/InnoPh                       | HAL Library            |
    | ase_HAPI_azuredemo/Inc/stm32l4xx_hal_conf.h | Configuration file     |
    +---------------------------------------------+------------------------+
    | InnoPhase_HAPI/                             | Interrupt handler’s    |
    | InnoPhase_HAPI_azuredemo/Inc/stm32l4xx_it.h | header file            |
    +---------------------------------------------+------------------------+
    | InnoPhase_HAPI/In                           | FreeRTOS Configuration |
    | noPhase_HAPI_azuredemo/Inc/FreeRTOSConfig.h | file                   |
    +---------------------------------------------+------------------------+


.. |image1| image:: media/image1.png
.. |Text Description automatically generated| image:: media/image2.png
   :width: 5.90556in
   :height: 5.22847in


