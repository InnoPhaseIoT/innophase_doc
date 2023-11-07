Socket Wakeup
---------------------


This application note describes the basics of sleep management with an
example illustrating Talaria TWO wake-up from sleep mode.

System Sleep Enable & Disable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

System Sleep APIs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

os_suspend_enable()
~~~~~~~~~~~~~~~~~~~

Suspends the system when idle.

+-----------------------------------------------------------------------+
| void os_suspend_enable(void)                                          |
+=======================================================================+
+-----------------------------------------------------------------------+

Calling os_suspend_enable() will suspend the system or enable deep
sleep, when the processor is idle. Enabling and disabling suspend mode
takes additional time, which will affect the real-time response of the
system. When an interrupt occurs, the system will wake up even if it is
in a suspended state. However, the latency will be more as compared to
when the system operates in a non-suspended mode.

os_suspend_disable()
~~~~~~~~~~~~~~~~~~~~

Disables system suspend.

+-----------------------------------------------------------------------+
| void os_suspend_disable(void)                                         |
+=======================================================================+
+-----------------------------------------------------------------------+

When the system is idle, the kernel will place the CPU in low-power
mode, ready to swiftly resume execution if an interrupt occurs.

Code Walkthrough 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sock_wake.c
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Overview
~~~~~~~~

The sample code is the path: examples/socket_wakeup/src/sock_wake.c is a
simple application which demonstrates socket wake-up in sleep mode.

Connect to a Wi-Fi network 
~~~~~~~~~~~~~~~~~~~~~~~~~~~

To connect to a Wi-Fi network the following APIs from the Wi-Fi
Connection Manager are used:

1. wcm_create()

..

   This function creates the Wi-Fi network interface using the
   wcm_handle pointer.

2. wcm_notify_enable()

..

   Enables callbacks of the link and IP address changes.

3. wcm_add_network_profile ()

..

   Asynchronously adds a Wi-Fi network to connect. Currently only one
   network can be added.

4. wcm_auto_connect ()

..

   Enables start or stop auto connection of the device with Wi-Fi.

+-----------------------------------------------------------------------+
| static int                                                            |
|                                                                       |
| wifi_connection(void)                                                 |
|                                                                       |
| {                                                                     |
|                                                                       |
| int rval;                                                             |
|                                                                       |
| struct network_profile \*profile;                                     |
|                                                                       |
| const char \*np_conf_path = os_get_boot_arg_str("np_conf_path") ?:    |
| NULL;                                                                 |
|                                                                       |
| my_wcm_handle = wcm_create(NULL);                                     |
|                                                                       |
| if (my_wcm_handle != NULL) {                                          |
|                                                                       |
| wcm_notify_enable(my_wcm_handle, wcm_notifier, NULL);                 |
|                                                                       |
| if (np_conf_path != NULL) {                                           |
|                                                                       |
| /\* Create a Network Profile from a configuration file in             |
|                                                                       |
| \*the file system \*/                                                 |
|                                                                       |
| rval = network_profile_new_from_file_system(&profile, np_conf_path);  |
|                                                                       |
| } else {                                                              |
|                                                                       |
| /\* Create a Network Profile using BOOT ARGS \*/                      |
|                                                                       |
| rval = network_profile_new_from_boot_args(&profile);                  |
|                                                                       |
| }                                                                     |
|                                                                       |
| if (rval < 0) {                                                       |
|                                                                       |
| pr_err("could not create network profile %d\\n", rval);               |
|                                                                       |
| return rval;                                                          |
|                                                                       |
| }                                                                     |
|                                                                       |
| rval = wcm_add_network_profile(my_wcm_handle, profile);               |
|                                                                       |
| if (rval < 0) {                                                       |
|                                                                       |
| pr_err("could not associate network profile to wcm %d\\n", rval);     |
|                                                                       |
| return rval;                                                          |
|                                                                       |
| }                                                                     |
|                                                                       |
| rval = wcm_auto_connect(my_wcm_handle, 1);                            |
|                                                                       |
| if (rval != WCM_SUCCESS) {                                            |
|                                                                       |
| pr_err("could enable auto connect for wcm %d\\n", rval);              |
|                                                                       |
| return rval;                                                          |
|                                                                       |
| }                                                                     |
|                                                                       |
| xSemaphoreTake(connect_lock, portMAX_DELAY);                          |
|                                                                       |
| vTaskDelay(1000);                                                     |
|                                                                       |
| }                                                                     |
|                                                                       |
| return WCM_SUCCESS;                                                   |
|                                                                       |
| }                                                                     |
+=======================================================================+
+-----------------------------------------------------------------------+

Wi-Fi Connection Callback Function
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The app_wcm_notify_cb() function enables the callbacks of link and IP
address.

+-----------------------------------------------------------------------+
| void                                                                  |
|                                                                       |
| wcm_notifier(void \*ctx, struct os_msg \*msg)                         |
|                                                                       |
| {                                                                     |
|                                                                       |
| switch (msg->msg_type) {                                              |
|                                                                       |
| case WCM_NOTIFY_MSG_CONNECTED:                                        |
|                                                                       |
| os_printf("wcm_notify_cb to App Layer -                               |
| WCM_NOTIFY_MSG_CONNECTED\\n");                                        |
|                                                                       |
| xSemaphoreGive(connect_lock);                                         |
|                                                                       |
| break;                                                                |
|                                                                       |
| default:                                                              |
|                                                                       |
| break;                                                                |
|                                                                       |
| }                                                                     |
|                                                                       |
| os_msg_release(msg);                                                  |
|                                                                       |
| }                                                                     |
+=======================================================================+
+-----------------------------------------------------------------------+

Server Socket Function 
~~~~~~~~~~~~~~~~~~~~~~~

On successfully connecting to the Wi-Fi, the device creates a UDP server
in Talaria TWO with server port number 8000. The server will initially
be in sleep mode. Here, we register a call- back function to wake up
Talaria TWO from sleep mode.

+-----------------------------------------------------------------------+
| static void                                                           |
|                                                                       |
| udp_server()                                                          |
|                                                                       |
| {                                                                     |
|                                                                       |
| struct netconn \*conn                                                 |
|                                                                       |
| = netconn_new_with_callback(NETCONN_UDP, sock_event_cb);              |
|                                                                       |
| assert(conn);                                                         |
|                                                                       |
| if (netconn_bind(conn, IP_ADDR_ANY, UDP_SERVER_PORT) == ERR_OK) {     |
|                                                                       |
| netconn_set_nonblocking(conn, 1);                                     |
|                                                                       |
| os_printf("udp server started at port %d\\n", UDP_SERVER_PORT);       |
|                                                                       |
| } else {                                                              |
|                                                                       |
| pr_err("udp server at %d failed\\n", UDP_SERVER_PORT);                |
|                                                                       |
| }                                                                     |
|                                                                       |
| }                                                                     |
+=======================================================================+
+-----------------------------------------------------------------------+

Socket Event Callback Function
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is the callback function, where Talaria TWO is enabled from sleep
and put back to sleep after a brief period of 500ms.

+-----------------------------------------------------------------------+
| static void                                                           |
|                                                                       |
| sock_event_cb(struct netconn \*conn, enum netconn_evt event, u16_t    |
| len)                                                                  |
|                                                                       |
| {                                                                     |
|                                                                       |
| if (event == NETCONN_EVT_RCVPLUS) {                                   |
|                                                                       |
| os_printf("NETCONN_EVT_RCVPLUS\\n");                                  |
|                                                                       |
| os_printf("Waking up\\n");                                            |
|                                                                       |
| os_suspend_disable();                                                 |
|                                                                       |
| vTaskDelay(500);                                                      |
|                                                                       |
| os_printf("sleeping\\n");                                             |
|                                                                       |
| os_suspend_enable();                                                  |
|                                                                       |
| } }                                                                   |
+=======================================================================+
+-----------------------------------------------------------------------+

Running the Application 
~~~~~~~~~~~~~~~~~~~~~~~~

Program sock_wake.elf *(freertos_sdk_x.y\\examples\\socket_wakeup\\bin)*
using the Download tool:

1. Launch the Download tool provided with InnoPhase Talaria TWO FreeRTOS
   SDK.

2. In the GUI window:

   a. Boot Target: Select the appropriate EVK from the drop-down

   b. ELF Input: Load the sock_wake.elf by clicking on Select ELF File.

   c. AP Options: Provide the SSID and Passphrase under AP Options to
      connect to an Access Point.

   d. Programming: Prog RAM or Prog Flash as per requirement.

Launch the Hercules tool for Windows and provide the port number along
with the IP address and send the data.

|Graphical user interface, application Description automatically
generated|

Figure : Hercules Tool - Data transfer

Expected Output
~~~~~~~~~~~~~~~

sock_wake.elf is created when the code is compiled. Following is the
console output when the ELF is programmed onto Talaria TWO.

+-----------------------------------------------------------------------+
| Y-BOOT 208ef13 2019-07-22 12:26:54 -0500 790da1-b-7                   |
|                                                                       |
| ROM yoda-h0-rom-16-0-gd5a8e586                                        |
|                                                                       |
| FLASH:PWWWWWWAE                                                       |
|                                                                       |
| Build $Id: git-831e563 $                                              |
|                                                                       |
| Flash detected. flash.hw.uuid: 39483937-3207-0061-00a2-ffffffffffff   |
|                                                                       |
| Bootargs: ssid=test passphrase=12345678                               |
|                                                                       |
| $App:git-5a9f591                                                      |
|                                                                       |
| SDK Ver: FREERTOS_SDK_1.0                                             |
|                                                                       |
| Wake From Sock App                                                    |
|                                                                       |
| addr e0:69:3a:00:15:a8                                                |
|                                                                       |
| network profile created for ssid: test                                |
|                                                                       |
| [2.906,467] DISCONNECTED                                              |
|                                                                       |
| [3.020,421] CONNECT:72:d7:92:3a:8a:71 Channel:6 rssi:-41 dBm          |
|                                                                       |
| [3.070,394] MYIP 192.168.122.64                                       |
|                                                                       |
| [3.070,558] IPv6 [fe80::e269:3aff:fe00:15a8]-link                     |
|                                                                       |
| wcm_notify_cb to App Layer - WCM_NOTIFY_MSG_CONNECTED                 |
|                                                                       |
| URI: udp://192.168.122.64:8000                                        |
|                                                                       |
| udp server started at port 8000                                       |
|                                                                       |
| NETCONN_EVT_RCVPLUS                                                   |
|                                                                       |
| Waking up                                                             |
|                                                                       |
| sleeping                                                              |
|                                                                       |
| NETCONN_EVT_RCVPLUS                                                   |
|                                                                       |
| Waking up                                                             |
|                                                                       |
| sleeping                                                              |
|                                                                       |
| NETCONN_EVT_RCVPLUS                                                   |
|                                                                       |
| Waking up                                                             |
|                                                                       |
| sleeping                                                              |
|                                                                       |
| NETCONN_EVT_RCVPLUS                                                   |
|                                                                       |
| Waking up                                                             |
|                                                                       |
| sleeping                                                              |
|                                                                       |
| NETCONN_EVT_RCVPLUS                                                   |
|                                                                       |
| Waking up                                                             |
|                                                                       |
| sleeping                                                              |
|                                                                       |
| NETCONN_EVT_RCVPLUS                                                   |
|                                                                       |
| Waking up                                                             |
|                                                                       |
| sleeping                                                              |
+=======================================================================+
+-----------------------------------------------------------------------+

.. |Graphical user interface, application Description automatically generated| image:: media/image1.png
   :width: 6.29921in
   :height: 5.47816in
