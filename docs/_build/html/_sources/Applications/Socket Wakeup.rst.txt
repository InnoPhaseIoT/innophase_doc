Introduction 
=============

This application note describes the basics of sleep management in
InnoOS™ with an example illustrating Talaria TWO wake-up from sleep
mode.

System Sleep Enable & Disable
=============================

System Sleep APIs
-----------------

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

os_avail_heap()
~~~~~~~~~~~~~~~

Returns size of the remaining heap.

+-----------------------------------------------------------------------+
| size_t os_avail_heap(void)                                            |
+=======================================================================+
+-----------------------------------------------------------------------+

This is the total size including internal overhead. However, this may
not represent the amount that can be allocated by an application.

Code Walkthrough 
=================

Sock_wake.c
-----------

Overview
~~~~~~~~

The sample code is the path: examples/socket_wakeup/src/sock_wake.c is a
simple application which demonstrates sleep mode.

Sample Code Walkthrough 
~~~~~~~~~~~~~~~~~~~~~~~~

While programming the ELF to Talaria TWO using boot.py, bootargs is used
to pass the SSID and Passphrase parameters to the program:

+-----------------------------------------------------------------------+
| ssid = os_get_boot_arg_str("ssid");                                   |
|                                                                       |
| passphrase = os_get_boot_arg_str("passphrase") ?: "";                 |
+=======================================================================+
+-----------------------------------------------------------------------+

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
| my_wcm_handle = wcm_create(NULL);                                     |
|                                                                       |
| if(my_wcm_handle != NULL)                                             |
|                                                                       |
| {                                                                     |
|                                                                       |
| wcm_notify_enable(my_wcm_handle, my_wcm_notify_cb, NULL);             |
|                                                                       |
| if (np_conf_path != NULL) {                                           |
|                                                                       |
| /\* Create a Network Profile from a configuration file in             |
|                                                                       |
| \*the file system*/                                                   |
|                                                                       |
| rval = network_profile_new_from_file_system(&profile, np_conf_path);  |
|                                                                       |
| } else {                                                              |
|                                                                       |
| /\* Create a Network Profile using BOOT ARGS*/                        |
|                                                                       |
| rval = network_profile_new_from_boot_args(&profile);                  |
|                                                                       |
| }                                                                     |
|                                                                       |
| if (rval < 0) {                                                       |
|                                                                       |
| pr_err("could not create network profile %d\\n", rval);               |
|                                                                       |
| return 0;                                                             |
|                                                                       |
| }                                                                     |
|                                                                       |
| rval = wcm_add_network_profile(my_wcm_handle, profile);               |
|                                                                       |
| if (rval < 0) {                                                       |
|                                                                       |
| pr_err("could not associate network profile to wcm %d\\n", rval);     |
|                                                                       |
| return 0;                                                             |
|                                                                       |
| }                                                                     |
|                                                                       |
| wcm_cnt = wcm_auto_connect(my_wcm_handle, 1);                         |
|                                                                       |
| os_sem_wait(&connect_lock);                                           |
|                                                                       |
| os_sleep_us(1000000, OS_TIMEOUT_WAKEUP);                              |
|                                                                       |
| if (wcm_cnt == WCM_SUCCESS) {                                         |
|                                                                       |
| auot_sucss = 1; }                                                     |
+=======================================================================+
+-----------------------------------------------------------------------+

Wi-Fi Connection Callback Function
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The app_wcm_notify_cb() function enables the callbacks of link and IP
address.

+-----------------------------------------------------------------------+
| switch(msg->msg_type) {                                               |
|                                                                       |
| case(WCM_NOTIFY_MSG_LINK_UP):                                         |
|                                                                       |
| break;                                                                |
|                                                                       |
| case(WCM_NOTIFY_MSG_LINK_DOWN):                                       |
|                                                                       |
| os_sem_post(&app_wcm_lock);                                           |
|                                                                       |
| break;                                                                |
|                                                                       |
| case(WCM_NOTIFY_MSG_ADDRESS):                                         |
|                                                                       |
| break;                                                                |
|                                                                       |
| case WCM_NOTIFY_MSG_CONNECTED:                                        |
|                                                                       |
| wcm_connect_success = 1;                                              |
|                                                                       |
| os_sem_post(&app_wcm_lock);                                           |
|                                                                       |
| break;                                                                |
|                                                                       |
| }                                                                     |
|                                                                       |
| os_msg_release(msg);                                                  |
+=======================================================================+
+-----------------------------------------------------------------------+

Server Socket Function 
~~~~~~~~~~~~~~~~~~~~~~~

On successfully connecting to the Wi-Fi, the device creates a UDP server
in Talaria TWO with server port number 8000. The server will initially
be in sleep mode. Here, we register a call- back function to wake up
Talaria TWO from sleep mode.

+-----------------------------------------------------------------------+
| static bool add_server_socket(struct hiosock \*hsock, struct          |
| hiosock_uri                                                           |
|                                                                       |
| \*hs_uri)                                                             |
|                                                                       |
| {                                                                     |
|                                                                       |
| os_printf("add_server_socket\\n"); bool status = false;               |
|                                                                       |
| hsock->conn = netconn_new_with_callback(NETCONN_UDP, sock_event_cb);  |
| os_printf("conn created\\n");                                         |
|                                                                       |
| if(hsock->conn != NULL)                                               |
|                                                                       |
| {                                                                     |
|                                                                       |
| if (hs_uri->tos != -1) {                                              |
|                                                                       |
| conn->pcb.tcp->tos = hs_uri->tos;                                     |
|                                                                       |
| }                                                                     |
|                                                                       |
| if (hsock->type == SOCK_STREAM) {                                     |
| netconn_set_nonblocking(hsock->conn, 1);                              |
|                                                                       |
| }                                                                     |
|                                                                       |
| IP_SET_TYPE_VAL(hs_uri->rem_addr, IPADDR_TYPE_ANY);                   |
|                                                                       |
| if (netconn_bind(hsock->conn, &hs_uri->rem_addr, hs_uri->port) ==     |
| ERR_OK) {                                                             |
|                                                                       |
| if (hsock->type == SOCK_STREAM) {                                     |
|                                                                       |
| if (netconn_listen(hsock->conn) == ERR_OK) { status = true;           |
|                                                                       |
| //rsp->status = 0;                                                    |
|                                                                       |
| //rsp->socket = hsock->fd; hsock->state = HIOSOCK_LISTEN;             |
|                                                                       |
| list_add_tail(&hsock_tbl, &hsock->list);                              |
|                                                                       |
| }                                                                     |
|                                                                       |
| } else {                                                              |
|                                                                       |
| status = true;                                                        |
|                                                                       |
| //rsp->status = 0;                                                    |
|                                                                       |
| //rsp->socket = hsock->fd; hsock->state = HIOSOCK_RD_WRT;             |
|                                                                       |
| netconn_set_nonblocking(hsock->conn, 1); list_add_tail(&hsock_tbl,    |
| &hsock->list);                                                        |
|                                                                       |
| }                                                                     |
|                                                                       |
| }                                                                     |
|                                                                       |
| if (status == false) {                                                |
|                                                                       |
| //rsp->status = ERR_VAL; netconn_delete(hsock->conn);                 |
|                                                                       |
| os_printf("server at %s failed\\n", ipaddr_ntoa(&hs_uri-              |
|                                                                       |
| >rem_addr));                                                          |
|                                                                       |
| } else {                                                              |
|                                                                       |
| os_printf("%s server at %s port %d\\n",                               |
|                                                                       |
| (hsock->type == SOCK_STREAM)? "tcp": "udp",                           |
| ipaddr_ntoa(&hs_uri->rem_addr), hs_uri->port);                        |
|                                                                       |
| } } }                                                                 |
+=======================================================================+
+-----------------------------------------------------------------------+

Socket Wake-up Function 
~~~~~~~~~~~~~~~~~~~~~~~~

The thread will be in sleep mode. If any message is sent to the UDP
server from any client, Talaria TWO will wake up for 500ms and go back
to sleep mode.

+-----------------------------------------------------------------------+
| static void\* sock_wake_thread(void\* arg)                            |
|                                                                       |
| {                                                                     |
|                                                                       |
| os_printf("sock wake thread\\n"); while(1)                            |
|                                                                       |
| {                                                                     |
|                                                                       |
| os_msleep(1000);                                                      |
|                                                                       |
| }                                                                     |
|                                                                       |
| return NULL;                                                          |
|                                                                       |
| }                                                                     |
+=======================================================================+
+-----------------------------------------------------------------------+

The os_avail_heap() function reveals the amount of space available on
the heap.

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
| if (event == NETCONN_EVT_RCVPLUS/\* \|\| event ==                     |
| NETCONN_EVT_SENDPLUS*/){                                              |
|                                                                       |
| //int evt = SOCK_EVT_RECVPLUS;                                        |
|                                                                       |
| os_printf("NETCONN_EVT_RCVPLUS\\n");                                  |
|                                                                       |
| os_printf("Waking up\\n");                                            |
|                                                                       |
| os_suspend_disable();                                                 |
|                                                                       |
| os_sleep_us(500000, OS_TIMEOUT_WAKEUP);                               |
|                                                                       |
| os_printf("sleeping\\n");                                             |
|                                                                       |
| os_suspend_enable();                                                  |
|                                                                       |
| }                                                                     |
|                                                                       |
| }                                                                     |
+=======================================================================+
+-----------------------------------------------------------------------+

Running the Application 
~~~~~~~~~~~~~~~~~~~~~~~~

Program sock_wake.elf (sdk_x.y\\examples\\socket_wakeup\\bin) using the
Download tool:

1. Launch the Download tool provided with InnoPhase Talaria TWO SDK.

2. In the GUI window:

   a. Boot Target: Select the appropriate EVK from the drop-down

   b. ELF Input: Load the sock_wake.elf by clicking on Select ELF File.

   c. AP Options: Provide the SSID and Passphrase under AP Options to
      connect to an Access Point.

   d. Programming: Prog RAM or Prog Flash as per requirement.

For more details on using the Download tool, refer to the document:
UG_Download_Tool.pdf (path: *sdk_x.y/pc_tools/Download_Tool/doc*).

**Note**: x and y refer to the SDK release version. For example:
sdk_2.5/doc.

Launch the Hercules tool for Windows and provide the port number along
with the IP address and send the data.

|Graphical user interface, application Description automatically
generated|

Figure : Hercules Tool - Data transfer

Expected Output
~~~~~~~~~~~~~~~

sock_wake.elf is created when compiling the code which provides the
following console output when programmed to Talaria TWO.

+-----------------------------------------------------------------------+
| UART:SNWWWWWAEBuild $Id: git-ba65998b7 $                              |
|                                                                       |
| np_conf_path=/data/nprofile.json ssid=InnoPhase passphrase=43083191   |
|                                                                       |
| $App:git-73e7f910                                                     |
|                                                                       |
| SDK Ver: sdk_2.5                                                      |
|                                                                       |
| Wake From Sock App                                                    |
|                                                                       |
| addr e0:69:3a:00:13:90                                                |
|                                                                       |
| [2.077,676] CONNECT:00:5f:67:cd:c5:a6 Channel:11 rssi:-45 dBm         |
|                                                                       |
| wcm_notify_cb to App Layer - WCM_NOTIFY_MSG_LINK_UP                   |
|                                                                       |
| wcm_notify_cb to App Layer - WCM_NOTIFY_MSG_ADDRESS                   |
|                                                                       |
| [2.808,043] MYIP 192.168.0.102                                        |
|                                                                       |
| [2.808,207] IPv6 [fe80::e269:3aff:fe00:1390]-link                     |
|                                                                       |
| ip:192.168.0.102                                                      |
|                                                                       |
| URI: udp://192.168.0.102:8000                                         |
|                                                                       |
| hiosock_alloc                                                         |
|                                                                       |
| add_server_socket                                                     |
|                                                                       |
| udp server at 192.168.0.102 port 8000                                 |
|                                                                       |
| conn created                                                          |
|                                                                       |
| sock wake thread                                                      |
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
   :width: 5.90551in
   :height: 5.13578in
