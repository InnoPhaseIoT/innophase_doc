BLE Central Demo
================

The HAPI APIs residing in the host microcontroller (STM32) connects to
Talaria TWO module via UART/SPI. Using these HAPI APIs, users can write
applications to perform multiple functions with Talaria TWO. This series
of Host Application Notes discusses more on using these APIs to perform
specific functions.

This document provides details on how to use the HAPI APIs to create the
BLE central demo application to:

1. Initialize the HAPI interface

2. Select the interface

3. Enable/disable the scramble on the interface

4. Create/destroy BLE interface

5. Set custom BLE address

6. Add the BLE indication handler for connection events and
   characteristics access

7. Start the peripheral BLE device scan and connection

8. In a loop to read and write characteristics supported on peripheral
   devices

**Connection Set-up**

Host processor communicates with Talaria TWO via a SPI or UART
interface. The connection set-up used to test the application is as
shown in Figure 1.

|A diagram of different types of communication Description automatically
generated with medium confidence|

Figure 1: Connection set-up for application testing

STM32L433RC-P as Host Controller
--------------------------------

STM32L433RC-P is the host controller which will have the BLE central
demo application running on it. This host is in-turn connected to the
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

1. Setup another Talaria TWO board as BLE Peripheral. Program Talaria
   TWO with ble_server.elf (path:
   *Utilities/PC_Software/TalariaTwo_Binaries*).

2. Once the setup is successful, create a BLE Central using HAPI APIs on
   DUT.

**Note**: x and y in sdk_x.y refer to the SDK package release version.

For details on testing the application with SPI and UART interface,
refer sections: *Testing the Basic Operation on setup with SPI
interface* and *Testing the Basic Operation on setup with UART
interface* of the document: QSG_T2_STM32CubeL4_L433RC-P.pdf
*(Documentation\\STM32CubeL4_Getting_Started*).

BLE Central on DUT is created and will connect to Talaria TWO BLE
peripheral and read the characteristics five times and prints the data.
Data can be observed in BLE test peripheral.

BLE central device will write the characteristics five times and the
data can be seen on STM console and on the test peripheral.

**Note**:

To make certain appropriate HAL operation, the application must ensure
that the HAL time base is always set to 1 millisecond. The FreeRTOS heap
size configTOTAL_HEAP_SIZE as defined in FreeRTOSConfig.h is set as per
the OS resources’ memory requirements of the application with a +10%
margin and rounded to the upper Kbyte boundary.

For more details on the FreeRTOS implementation on STM32Cube, please
refer to UM1722 - Developing Applications on STM32Cube with RTOS.

**BLE Central Demo Application**

This section describes the application details along with code snippets.
The application uses HAPI APIs to achieve the functionality. HAPI APIs
presumes that the platform related initialization and clock settings are
completed by default.

HAPI Interface Initialization
-----------------------------

.. code-block:: shell

    struct hapi \*hapi
    #ifdef HAPI_INTERFACE_UART_ENABLED /\* Register the uart, and baud rate to hapi \*/
    hapi = hapi_uart_init(hapi_uart, hapi_uart_tx, hapi_uart_rx);
    #endif
    #ifdef HAPI_INTERFACE_SPI_ENABLED
    /\* Register the SPI \*/
    hapi = hapi_spi_init(hapi_spi, hapi_spi_cs_high, hapi_spi_cs_low,hapi_spi_tx, hapi_spi_rx);
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

Create/Destroy the BLE Interface
--------------------------------

.. code-block:: shell

    struct hapi_bt_host \*hapi_bt_host;
    hapi_bt_host = hapi_bt_host_create(hapi);
    if(hapi_bt_host == NULL)
    {
        console_print("alloc fail\\r\\n");
        goto end;
    }


Add Indicator Handler for Connection Events
-------------------------------------------

.. code-block:: shell

    hapi_add_ind_handler(hapi, HIO_GROUP_BT_HOST, BT_HOST_GAP_EVENT_IND,api_bt_host_gapp_ind_handler, hapi_bt_host);


Add Indicator Handler for Characteristic Access
-----------------------------------------------

.. code-block:: shell

    hapi_add_ind_handler(hapi,HIO_GROUP_BT_HOST,HOST_GATT_READ_CHARACTERISTIC_VALUE_IND,hapi_bt_rd_wr_chr_ind_handler, hapi_bt_host);
    hapi_add_ind_handler(hapi, HIO_GROUP_BT_HOST,BT_HOST_GATT_WRITE_CHARACTERISTIC_VALUE_RSP,hapi_bt_rd_wr_chr_ind_handler, hapi_bt_host);


Set BLE Address
---------------

.. code-block:: shell

    uint8_t addr[] = {0xaa, 0x2, 0x3, 0x1, 0xbb, 0xcc};
    hapi_bt_host_gap_addr_set(hapi_bt_host, 1, addr);

Start BLE Connection 
---------------------

.. code-block:: shell

    uint8_t peer_addr[] = {0x02, 0x03, 0x04, 0x05, 0x06, 0x07}
    hapi_bt_host_gap_connection(hapi_bt_host,GAP_CONNECTION_MODE_DIRECT,bt_hci_addr_type_random, 1, peer_addr);


Read BLE Characteristics Value from Peripheral
----------------------------------------------

.. code-block:: shell

    hapi_bt_host_gatt_read_characteristic_value(hapi_bt_host, VALUE_HANDLE_READ);

Write BLE Characteristics Value to Peripheral
---------------------------------------------

.. code-block:: shell

    hapi_bt_host_gatt_write_characteristic_value(hapi_bt_host, VALUE_HANDLE_WRITE, (uint8_t\*)msg, strlen(msg));

**Expected Output**

BLE Central on DUT is created and will connect to Talaria TWO BLE
peripheral. It reads the characteristics five times and prints the data.
Data can be observed in the BLE test peripheral. BLE central device will
write the characteristics five times and data can be seen on STM console
and on the test peripheral.

|A screenshot of a computer program Description automatically generated|

|A computer screen with white text Description automatically generated|

Figure 2: Expected output

**Application Files and Functions**

.. table:: Table 1: Application files and functions

    +------------------------------------------+---------------------------+
    | **File**                                 | **Function**              |
    +==========================================+===========================+
    | /T2-HAN-009 /Src/main.c                  | Main Program              |
    +------------------------------------------+---------------------------+
    | /T2-HAN-009                              | HAL time-base file        |
    | /Src/stm32l4xx_hal_timebase_tim.c        |                           |
    +------------------------------------------+---------------------------+
    | /T2-HAN-009 /Src/stm32l4xx_it.c          | Interrupt handlers        |
    +------------------------------------------+---------------------------+
    | /T2-HAN-009 /Src/system_stm32l4xx.c      | STM32L4xx system clock    |
    |                                          | configuration file        |
    +------------------------------------------+---------------------------+
    | /T2-HAN-009 /Src/freertose.c             | Code for free RTOS        |
    |                                          | application               |
    +------------------------------------------+---------------------------+
    | /T2-HAN-009 /Src/stm32l4xx_hal_msp.c     | Code for MSP              |
    |                                          | initia                    |
    |                                          | lization/deinitialization |
    +------------------------------------------+---------------------------+
    | /T2-HAN-009 /Src/syscalls.c              | System calls file         |
    +------------------------------------------+---------------------------+
    | /T2-HAN-009 /Src/sysmem.c                | System Memory calls file  |
    +------------------------------------------+---------------------------+
    | /T2-HAN-009                              | System startup file       |
    | /Src/startup_stm32l433rctxp.s            |                           |
    +------------------------------------------+---------------------------+
    | /T2-HAN-009 /Inc/main.h                  | Main program header file  |
    +------------------------------------------+---------------------------+
    | /T2-HAN-009 /Inc/stm32l4xx_hal_conf.h    | HAL Library Configuration |
    |                                          | file                      |
    +------------------------------------------+---------------------------+
    | /T2-HAN-009 /Inc/stm32l4xx_it.h          | Interrupt handler’s       |
    |                                          | header file               |
    +------------------------------------------+---------------------------+
    | /T2-HAN-009 /Inc/FreeRTOSConfig.h        | FreeRTOS Configuration    |
    |                                          | file                      |
    +------------------------------------------+---------------------------+
    | /T2-HAN-009/Src/HAPI/app.c               | Application file          |
    +------------------------------------------+---------------------------+
    | /T2-HAN-009/Src/HAPI/bt_app.c            | BLE application file      |
    +------------------------------------------+---------------------------+
    | /T2-HAN-009/Src/HAPI/peripheral_bt_app.c | Peripheral BLE            |
    |                                          | application files         |
    +------------------------------------------+---------------------------+
    | /T2-HAN-009/Src/HAPI/bt_att.h,           | BLE application header    |
    | /T2-HAN-009/Src/HAPI/bt_gatt.h,          | files                     |
    | /T2-HAN-009/Src/HAPI/bt_hci.h,           |                           |
    | /T2-HAN-009/Src/HAPI/bt_uuid.h           |                           |
    +------------------------------------------+---------------------------+


.. |A diagram of different types of communication Description automatically generated with medium confidence| image:: media/image1.png
   :width: 5.90551in
   :height: 3.42492in
.. |A screenshot of a computer program Description automatically generated| image:: media/image2.png
   :width: 7.48031in
   :height: 7.2487in
.. |A computer screen with white text Description automatically generated| image:: media/image3.png
   :width: 7.48031in
   :height: 1.82852in
