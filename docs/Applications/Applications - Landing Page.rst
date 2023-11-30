.. applications:

Applications
############

The FreeRTOS SDK software package provides software APIs with
ready-to-run firmware examples to support quick evaluation and
development with Talaria TWO.

Applications: Production ready example applications which the user can
run on Talaria TWO. Following applications are available in the release
package:

+------------+---------------------------------------------------------+
| **         | **Description**                                         |
| Protocol** |                                                         |
+============+=========================================================+
| alarm      | Describes alarm functionality in Talaria TWO            |
+------------+---------------------------------------------------------+
| helloworld | Basic helloworld application                            |
+------------+---------------------------------------------------------+
| ssbl       | Demonstrates running and switching between multiple     |
|            | applications on Talaria TWO using SSBL                  |
+------------+---------------------------------------------------------+
| stw_m      | Serial to Wi-Fi application used in hosted mode of      |
| ulti_proto | operation                                               |
+------------+---------------------------------------------------------+
| gordon.elf | Flashing utility using UART interface                   |
+------------+---------------------------------------------------------+
| fota       | Demonstrates the FOTA (Firmware Over The Air) process   |
+------------+---------------------------------------------------------+
| iot_aws    | Demonstrates using Talaria TWO board and the SDK with   |
|            | Amazon Web Services (AWS) IoT                           |
+------------+---------------------------------------------------------+


Examples: Demo/sample applications that the user can run on Talaria TWO
firmware. Following examples are available:

+----------------+-----------------------------------------------------+
| **Protocol**   | **Description**                                     |
+================+=====================================================+
| alexa_ready    | Demonstrates the use of AWS IoT Embedded C Device   |
|                | SDK available on Talaria TWO to interact with the   |
|                | Device Shadow Service on AWS IoT Core               |
+----------------+-----------------------------------------------------+
| adc            | Example for using the Analog to Digital Convertor   |
|                | (ADC) peripheral of Talaria TWO modules             |
+----------------+-----------------------------------------------------+
| at_custom_cmd  | Demonstrates custom AT commands which the user can  |
|                | use apart from the standard commands                |
+----------------+-----------------------------------------------------+
| ble_beacons    | Example codes describing the basic concept of       |
|                | Eddystone Beacon                                    |
|                |                                                     |
|                | -  Eddystone UID                                    |
|                |                                                     |
|                | -  Eddystone URL                                    |
|                |                                                     |
|                | -  Eddystone TLM                                    |
+----------------+-----------------------------------------------------+
| b              | Example code for receiving a text message from a    |
| le_wifi_bridge | connected BLE client and publishing it to a         |
|                | CloudMQTT broker                                    |
+----------------+-----------------------------------------------------+
| chip_monitor   | Describes the application for fetching the changes  |
|                | in the values of device core temperature, Voltage   |
|                | of VBAT, external ADC and estimated current         |
|                | consumption of Talaria TWO device                   |
+----------------+-----------------------------------------------------+
| crash_handling | Example code for using the crash handler API to     |
|                | handle and debug error cases                        |
+----------------+-----------------------------------------------------+
| gpio           | Example codes to use the GPIO interface. the        |
|                | interface for GPIO                                  |
+----------------+-----------------------------------------------------+
| http_client    | Example codes for using HTTP client APIs to connect |
|                | to HTTP servers in secured (HTTPS) and non-secured  |
|                | way                                                 |
+----------------+-----------------------------------------------------+
| i2c            | Demonstrates usage of I2C on Talaria TWO            |
+----------------+-----------------------------------------------------+
| i2s_audio      | Example codes for using I2S peripheral of           |
|                | INP1010/INP1011/INP1012/INP1013 Talaria TWO modules |
|                | for playing audio                                   |
+----------------+-----------------------------------------------------+
| ifttt          | Example application for using Talaria TWO with      |
|                | IFTTT                                               |
+----------------+-----------------------------------------------------+
| lp_scan        | Demonstrates the basics of the Low Power Wi-Fi scan |
|                | feature                                             |
+----------------+-----------------------------------------------------+
| lp_uart        | Example codes describing the use of UART APIs       |
+----------------+-----------------------------------------------------+
| mdns           | Demonstrates using the mDNS APIs provided by the    |
|                | mDNS module                                         |
+----------------+-----------------------------------------------------+
| mqtt           | Example codes for using the publish/subscribe       |
|                | operation of MQTT in both secured and non-secured   |
|                | modes                                               |
+----------------+-----------------------------------------------------+
| prov           | A demo Provisioning application using BLE for       |
|                | provisioning AP credentials at Talaria TWO from a   |
|                | mobile application                                  |
+----------------+-----------------------------------------------------+
| pwm            | Demonstrates usage of Pulse Width Modulation        |
|                | peripheral of INP1010/INP1011/INP1012/INP1013       |
|                | Talaria TWO modules                                 |
+----------------+-----------------------------------------------------+
| radio          | Describes using the Radio and Module parameters on  |
| _module_params | the Talaria TWO module                              |
+----------------+-----------------------------------------------------+
| secure_files   | Example application for reading and writing         |
|                | encrypted files from/to the filesystem              |
+----------------+-----------------------------------------------------+
| socket_wakeup  | Demonstrates the basics of sleep management         |
|                | (Talaria TWO wake-up from sleep mode)               |
+----------------+-----------------------------------------------------+
| spi            | Demonstrates the usage of the Software SPI Master   |
|                | (SSM) on Talaria TWO                                |
+----------------+-----------------------------------------------------+
| unassoc        | Example codes describing Wi-Fi un-associated mode   |
|                | transmission APIs available in the SDK, call-back   |
|                | events, notifications and associated data           |
|                | structures                                          |
+----------------+-----------------------------------------------------+
| using_ble      | Introduction to BLE APIs through code samples       |
|                | consisting of a server and client application       |
+----------------+-----------------------------------------------------+
| us             | Demonstrates using the filesystem APIs to show case |
| ing_filesystem | the filesystem functionalities on the Talaria TWO   |
|                | EVK                                                 |
+----------------+-----------------------------------------------------+
| using_sntp     | Demonstrates fetching time from NTP server using    |
|                | SNTP                                                |
+----------------+-----------------------------------------------------+
| using_wifi     | Example codes describing the Wi-Fi connection       |
|                | manager APIs                                        |
+----------------+-----------------------------------------------------+
| watchdog_timer | Demonstrates managing Talaria TWO watchdog timer    |
|                | using the functions provided by the watchdog driver |
+----------------+-----------------------------------------------------+
| wcm_multi_ap   | Demonstrates the application example of Wi-Fi       |
|                | Connection with Multi-Access Point (WCM_MULTI_AP)   |
+----------------+-----------------------------------------------------+
| wcm_pm         | Demonstrates the Wi-Fi Connection Manager power     |
|                | management APIs                                     |
+----------------+-----------------------------------------------------+
| websocket      | Demonstrates using the WebSocket client APIs        |
|                | provided by the WebSocket module                    |
+----------------+-----------------------------------------------------+



Apps
-------------
.. toctree::
    :maxdepth: 1

    1. Apps/1. Alexa_Ready_Application_with_AWS_IoT_Embedded_C_Device_SDK
    1. Apps/2. Alarm
    1. Apps/3. IoT_AWS
    1. Apps/4. SSBL
    1. Apps/5. Firmware_Over-The-Air-Upgrade

Examples
-------------
.. toctree::
    :maxdepth: 1

    2. Examples/Example_for_Analog_to_Digital_Converter
    2. Examples/Example_for_Audio_over_I2S
    2. Examples/Example_for_BLE_WiFi_Bridge
    2. Examples/Example_for_Crash_handling
    2. Examples/Example_for_I2C
    2. Examples/Example_for_LPScan
    2. Examples/Example_for_MQTT
    2. Examples/Example_for_Pulse_Width_Modulation
    2. Examples/Example_for_Radio_and_Module_Parameters
    2. Examples/Example_for_Secure_Files
    2. Examples/Example_for_Socket_Wakeup
    2. Examples/Example_for_Software_SPI_Master
    2. Examples/Example_for_using_Chip_Monitor
    2. Examples/Example_for_using_Filesystem
    2. Examples/Example_for_using_GPIO
    2. Examples/Example_for_using_SNTP
    2. Examples/Example_for_using_WiFi
    2. Examples/Example_for_WiFi_Power_Management
    2. Examples/Example_using_BLE_5_0
    2. Examples/Example_using_BLE_Beacons
    2. Examples/Example_using_Custom_ATCMDLIB
    2. Examples/Example_using_HTTP_Client
    2. Examples/Example_using_IFTTT
    2. Examples/Example_using_Low_Power_UART
    2. Examples/Example_using_mDNS
    2. Examples/Example_using_Provisioning
    2. Examples/Example_using_Unassociated_Mode
    2. Examples/Example_using_Watchdog_Timer
    2. Examples/Example_using_WCM_Multi_AP
    2. Examples/Example_using_Websock_Client
