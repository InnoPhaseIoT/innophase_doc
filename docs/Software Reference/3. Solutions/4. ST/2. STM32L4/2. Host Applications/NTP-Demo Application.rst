NTP-Demo Application
====================

The HAPI APIs residing in the host microcontroller (STM32) connects to
Talaria TWO module via UART/SPI. Using these HAPI APIs, users can write
applications to perform multiple functions with Talaria TWO. This series
of Host Application Notes discusses more on using these APIs to perform
specific functions.

This document provides details on how to use the HAPI APIs to create the
NTP demo application to:

1.  Initialize the HAPI interface

2.  Select the interface

3.  Enable/Disable the scramble on the interface

4.  Create/destroy a Wi-Fi network interface

5.  Scan for Wi-Fi networks

6.  Connect to a Wi-Fi network

7.  Create the NTP interface and fetch the time

8.  Set the RTC system time with the NTP time

9.  Execute the operations in a loop

10. 

**Connection Set-up**

Host processor communicates with Talaria TWO via a SPI or UART
interface. The connection set-up used to test the application is as
shown in Figure 1.

|image1|

Figure 1: Connection set-up for application testing

STM32L433RC-P as Host Controller
--------------------------------

STM32L433RC-P is the host controller which will have the NTP demo
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

1. Open any console (serial terminal) on STM32 MCU with a baudrate of
   115200

2. Reset the STM32 and check the MCU console. MCU will boot, the Wi-Fi
   connection is established and starts the NTP connection

3. The application gets the NTP data and sets the same to the local
   time, where the time is also displayed.

**Note**:

To make certain appropriate HAL operation, the application must ensure
that the HAL time base is always set to 1 millisecond. The FreeRTOS heap
size configTOTAL_HEAP_SIZE as defined in FreeRTOSConfig.h is set as per
the OS resources’ memory requirements of the application with a +10%
margin and rounded to the upper Kbyte boundary.

For more details on the FreeRTOS implementation on STM32Cube, please
refer to UM1722 - Developing Applications on STM32Cube with RTOS.

.. _ntp-demo-application-1:

**NTP Demo Application**

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
    {
        if(true == hapi_wcm_network_profile_add(hapi_wcm, ssid, NULL, passphrase, NULL))
        {
            if(false == hapi_wcm_autoconnect(hapi_wcm, 1))
        {
        banner="hapi_wcm_autoconnect : failed..\\r\\n";
    }

NTP Time Fetch
--------------

The application creates an NTP connection and fetch the current time
from NTP server.


.. code-block:: shell

    int loop, timeOut = 3;

    /* Provide suitable time zone to get local time offset
    * Few local time zone examples are,
    * for IST (Indian Standard Time) - UTC+05:30
    * for BST (British Summer Time) - UTC+01:00
    * for USA (Alaska) - UTC-09:00
    */

    offset = getTimeZoneoffset("UTC+05:30");
    if (-1 == offset) {
        return status;
    }
    for (loop = 0; loop < 100; loop++) {
        currentTime = 0;
        status = hapi_nw_misc_app_time_get(hapi, timeOut, &currentTime);
        if (false == status) {
            sprintf(print_arr,"\r\n Failed to get time from ntp server, reading again after %d seconds \r\n",duration);



From the NTP code snippet:

.. code-block:: shell

    int loop, timeOut = 3;

By default, timeout in NTP Module is set at 3 seconds. If the NTP time
is received within 3 seconds from the NTP server, then the time (based
on UTC) is updated to the user. Else, the following error message is
displayed:

.. code-block:: shell

    sprintf(print_arr,"\\r\\n Failed to get time from ntp server, reading again after %d seconds \\r\\n",duration);

Again after 10 seconds, an attempt to get time is initiated. This
iteration will continue for 100 times and then the NTP program
terminates.

.. code-block:: shell

    offset = getTimeZoneoffset("UTC+05:30");

The local function getTimeZoneoffset will get the local time offset for
the local time zone passed as parameter.

Currently, IST time zone (UTC+05:30) is programmed as default and for
quick reference, two other example local time zones are provided in the
comment section. Converted local time from UTC time is programmed into
STM32 RTC registers.

The list of local time zones currently handled in NTP Module are as
follows:

.. code-block:: shell

    UTC−12:00, UTC−11:00, UTC−10:00, UTC−09:30, UTC−09:00, UTC−08:00,
    UTC−07:00, UTC−06:00, UTC−05:00, UTC−04:00, UTC−03:30, UTC−03:00,
    UTC−02:00, UTC−01:00, UTC±00:00,
    UTC+01:00, UTC+02:00, UTC+03:00, UTC+03:30, UTC+04:00, UTC+04:30,
    UTC+05:00, UTC+05:30, UTC+05:45, UTC+06:00, UTC+06:30, UTC+07:00,
    UTC+08:00, UTC+08:45, UTC+09:00, UTC+09:30, UTC+10:00, UTC+10:30,
    UTC+11:00, UTC+12:00, UTC+12:45, UTC+13:00, UTC+14:00


**Expected Output**

The MCU will connect to the AP specified by the SSID and passphrase. On
successful connection, MCU will get the latest time from the NTP server
at regular intervals (currently, the interval is set to 10 seconds) and
this time will be converted to statable format required by the MCU and
stored in the RTC module. Once time is stored, the same will be read
back to make sure that time set is executed correctly.

Currently this test runs up to 100 times (configurable) post which the
application terminates.

The serial prints on the MCU are as follows:

|Text Description automatically generated|

Figure 2: Expected Output

**Application Files and Functions**

.. table:: Table 1: Application files and functions

    +-----------------------------------------+----------------------------+
    | **File**                                | **Function**               |
    +=========================================+============================+
    | I                                       | Main Program               |
    | nnoPhase_HAPI/T2-HAN-012/Src/HAPI/app.c |                            |
    +-----------------------------------------+----------------------------+
    | InnoP                                   | Code for configuring the   |
    | hase_HAPI/T2-HAN-012/Src/HAPI/app_ntp.c | RTC Module and setting the |
    |                                         | NTP time (suitably         |
    |                                         | converted as required by   |
    |                                         | MCU) in RTC Module         |
    +-----------------------------------------+----------------------------+
    | Middlewares/Third_Part                  | HAPI module to get time    |
    | y/InnoPhase_HAPI/Src/hapi_nw_misc_app.c | from NTP server            |
    +-----------------------------------------+----------------------------+
    | InnoPhase                               | Get NTP time header file   |
    | _HAPI\\T2-HAN-012\\Src\\HAPI\\include\\ |                            |
    | hapi_nw_misc_app.h                      |                            |
    +-----------------------------------------+----------------------------+
    | InnoPhase                               | NTP support header file    |
    | _HAPI\\T2-HAN-012\\Src\\HAPI\\include\\ |                            |
    | api\\nw_misc_app.h                      |                            |
    +-----------------------------------------+----------------------------+
    | InnoPhase_HAPI                          | Header file to enable RTC  |
    | \\T2-HAN-012\\inc\\stm32l4xx_hal_conf.h | Module                     |
    +-----------------------------------------+----------------------------+


.. |image1| image:: media/image1.png
.. |Text Description automatically generated| image:: media/image2.png
   :width: 7.72441in
   :height: 6.03621in
