Introduction
============

This application note describes the Wi-Fi Connection Manager APIs
available in the SDK, call-back events, notifications and the data
structures associated with them. The accompanying sample codes help
achieve some of these functionalities using WCM APIs.

Topology
========

|Diagram Description automatically generated|

Figure 1: Wi-Fi Connection Manager – Topology

Wi-Fi Connection Manager Functionalities
========================================

The Wi-Fi connection manager (WCM) contains functions for establishing
and tearing down associations to Wi-Fi access points. It initiates a
four-way handshake for encrypted connections and starts the DHCP client
from LWIP for getting allocation of the IP address.

Following functionalities are achieved through these APIs:

1. Creating and destroying interfaces

2. Scanning with different scan parameters and their indication
   structure

3. Connecting and disconnecting

4. Adding network to connect and removing network

5. Querying connection information

Accompanying sample code provides more details on how to achieve some of
the listed functionalities.

List of APIs
============

1. os_sem_post() - Unlocks the semaphore. Increments the value of a
   semaphore and wakes the first thread waiting for this semaphore.

2. os_msg_release()- Frees an allocated message. Frees a message which
   was previously allocated using os_msg_alloc().

3. os_get_boot_arg_str() - Returns the value of a boot argument as a
   null-terminated string.

4. os_sem_init()- Initializes a semaphore. This API must be called
   before calling any other semaphore related APIs. It is possible to
   statically initialize a semaphore with the OS_SEM_INITALIZER macro.

5. wcm_create()- Creates a Wi-Fi network interface. Only one wcm_handle
   instance is supported at the time of writing.

6. wifi_connect_to_network()- Adds a Wi-Fi network .

7. os_sem_wait()- Locks a semaphore. If the value of the semaphore is
   greater than 0, it decrements the counter. If the value is 0, it puts
   the current thread to sleep until the value becomes positive. This
   function cannot be used in interrupt context.

8. os_msg_release()- Frees an allocated message. Free a message
   previously allocated using os_msg_alloc().

9. os_create_thread()- Creates a new thread.

..

   This creates a new thread with priority specified in flags (via
   OS_CRTHREAD_PRIO macro). The thread is placed in the run queue, but
   there is no immediate reschedule. The thread continues to run until
   the entry point returns, at a point where the return value (a
   pointer) can be obtained with os_join_thread().

   If the return value is of no consequence, OS_CRTHREAD_DETACHED can be
   passed in flags. This causes the OS to reap the thread. Returns
   pointer to struct os_thread if successful, NULL otherwise.

10. os_join_thread()- Waits for a thread to terminate and destroy the
    thread.

..

   Calling this function will suspend execution of the calling thread
   until the target thread exits. The memory used to hold the threads
   stack and control block are freed.

11. os_suspend_enable()- Enables system suspend when idle.

..

   Calling os_suspend_enable() will enable the suspend (deep sleep) for
   the system. If enabled, the system will go into suspended mode when
   there is nothing to do for the processor. Entering and leaving
   suspend mode takes some extra time, so enabling this will affect the
   real-time response of the system. When in suspended state, the system
   will still wakeup if an interrupt occurs, but the latency will be
   much larger compared to running with suspend mode disabled.

12. os_get_boot_arg_int()- Returns the value of a boot argument as an
    integer

13. wifi_init_scan_default()- Gets the default parameters for the scan
    operation. The wifi_scan_param will be updated with the default
    values for the scan operation. This function is used to get the
    default values and alter the parameters whose values are different
    from the default. Finally, provide these parameters while calling
    the wcm_scan() API.

14. wcm_scan()- Scans for Wi-Fi networks. Returns the number of networks
    found during the scan operation. In case the scan could not be
    performed, an error code (negative value) is returned. Initiate a
    network scan procedure on the specified Wi-Fi Connection Manager
    interface.

15. wifi_netinfo_get_ssid()-Gets the SSID information from netinfo.

16. wifi_netinfo_get_chan()-Gets the channel information from netinfo.

17. wcm_free_scanresult() - Frees the memory allocated by wcm_scan().

18. wcm_set_hostname() - Sets host name for DHCP client.

19. wcm_get_hostname() - Gets host name of DHCP client.

States and Events of Wi-Fi Connection Manager
=============================================

The architecture of the WCM, its calls and events with LWIP and Wi-Fi
stacks are described in detail through the API flow.

WCM states are explained and notifications passed to application
programmer are described.

Initialization
--------------

When the API wcm_create() is called, the following sequence of
initializations happen on the WCM:

1. LWIP stack is initiated.

2. Wi-Fi interface and resources are created with the passed hwaddr.

3. Wi-Fi interface is created in WIFI_MODE_SCAN mode and a scan client
   is attached with scan_notify() and scan_done() call-backs to get scan
   results.

4. LWIP TCP/IP stack is started with the Wi-Fi interface in
   WIFI_MODE_STA mode.

5. wcm_notify_handler() is registered with the Wi-Fi stack for listening
   to the following link status notifications:

+-----------------------------------------------------------------------+
| #define WIFI_NOTIFY_MSG_LEAVE 100 /\* AP disconnected us \*/          |
|                                                                       |
| #define WIFI_NOTIFY_MSG_LOST 101 /\* Lost tracking of AP \*/          |
|                                                                       |
| #define WIFI_NOTIFY_MSG_RESTARTED 102 /\* Associated AP restarted \*/ |
+=======================================================================+
+-----------------------------------------------------------------------+

6. wcm_netif_callback() is registered with LWIP stack for listening IP
   address change events.

7. A dedicated wcm_thread is created which takes care of WCM’s state
   transitions at various stages of Wi-Fi connection procedure based on
   the previously described call-backs from the Wi-Fi stack, scanning
   interface and LWIP stack.

States of WCM
-------------

All the possible states of the WCM are defined as follows:

+-----------------------------------------------------------------------+
| enum c_state {                                                        |
|                                                                       |
| C_INITIAL,                                                            |
|                                                                       |
| C_SCANNING,                                                           |
|                                                                       |
| C_AUTHENTICATING,                                                     |
|                                                                       |
| C_ASSOCIATING,                                                        |
|                                                                       |
| C_WAIT_4WAY,                                                          |
|                                                                       |
| C_WAIT_DHCP,                                                          |
|                                                                       |
| C_CONNECTED,                                                          |
|                                                                       |
| C_FAILED, };                                                          |
+=======================================================================+
+-----------------------------------------------------------------------+

The message pointer \*msg has a message type associated with it.
msg->msg_type can have a value from the enum wcm_notify_msg_type,
containing message types of WCM. This will notify message callbacks as
shown:

+-----------------------------------------------------------------------+
| enum wcm_notify_msg_type {                                            |
|                                                                       |
| /\*\* WiFi link is up \*/                                             |
|                                                                       |
| WCM_NOTIFY_MSG_LINK_UP = 200,                                         |
|                                                                       |
| /\*\* WiFi link is down \*/                                           |
|                                                                       |
| WCM_NOTIFY_MSG_LINK_DOWN = 201,                                       |
|                                                                       |
| /\*\* Address has changed.                                            |
|                                                                       |
| WCM_NOTIFY_MSG_ADDRESS = 202                                          |
|                                                                       |
| };                                                                    |
+=======================================================================+
+-----------------------------------------------------------------------+

If the notification WCM_NOTIFY_MSG_ADDRESS occurs, then the message
received is of the type wcm_address_event. The structure definition for
wcm_address_event is as follows:

+-----------------------------------------------------------------------+
| struct wcm_address_event {                                            |
|                                                                       |
| /\*\* Message header \*/                                              |
|                                                                       |
| struct os_msg iev_hdr;                                                |
|                                                                       |
| /\*\* Typically AF_INET or AF_INET6 \*/                               |
|                                                                       |
| unsigned int iev_af;                                                  |
|                                                                       |
| /\*\* The address of up to 16 bytes (IPv6) \*/                        |
|                                                                       |
| unsigned char iev_address[0];                                         |
|                                                                       |
| };                                                                    |
+=======================================================================+
+-----------------------------------------------------------------------+

Address type and address data can be retrieved by typecasting the
message to struct wcm_address_event.

Source Code Walkthrough
=======================

Wifi_Connect 
-------------

Overview
~~~~~~~~

The sample code in the path *apps\\using_wifi\\src\\wifi_connect.c*
showcases simple connecting to a network with the API
wifi_connect_to_network().

**Note:** Upon disconnection of station (Talaria TWO module) from the AP
due to various reasons such as AP power off, module tries to reconnect
by sending a probe request packet. Each failed connection attempt will
increase the reconnect backoff time exponentially as 1, 2, 4, 8, 16, 32,
60 seconds.

After 60 seconds, module tries to reconnect indefinitely at every 60
seconds. Below sniffer capture shows Talaria TWO’s exponential
reconnection method.

|image1|

Figure 2: Sniffer Capture – Wi-Fi Reconnection

|image2|

Figure 3: Talaria TWO Console Logs – Wi-Fi Reconnection

Sample Code Walkthrough
~~~~~~~~~~~~~~~~~~~~~~~

To connect to a Wi-Fi network, wcm_create()API from the Wi-Fi Connection
Manager is used. Initially, the Wi-Fi network interface is created using
wcm_create().

+-----------------------------------------------------------------------+
| h = wcm_create(NULL);                                                 |
+=======================================================================+
+-----------------------------------------------------------------------+

wcm_set_hostname() API is used to set the host name in DHCP client. It
is used for identifying the client device (Talaria TWO) in the
network/AP.

Note: Default host name of Talaria TWO is talaria2.

+-----------------------------------------------------------------------+
| if(host_name != NULL)                                                 |
|                                                                       |
| wcm_set_hostname(wcm_handle, host_name);                              |
|                                                                       |
| host_name = wcm_get_hostname(wcm_handle);                             |
|                                                                       |
| os_printf("host name %s\\n", host_name);                              |
+=======================================================================+
+-----------------------------------------------------------------------+

wifi_connect_to_network()API, from components library, connects to the
Wi-Fi network using the AP credentials provided.

+-----------------------------------------------------------------------+
| rval = wifi_connect_to_network(&h, WCM_CONN_WAIT_INFINITE,            |
| &wcm_connect_success);                                                |
|                                                                       |
| if(rval < 0) {                                                        |
|                                                                       |
| os_printf("\\nError: Unable to connect to network\\n");               |
|                                                                       |
| return 0;                                                             |
|                                                                       |
| }                                                                     |
+=======================================================================+
+-----------------------------------------------------------------------+

Running the Application
~~~~~~~~~~~~~~~~~~~~~~~

Program wifi_connect.elf(*sdk_x.y\\examples\\using_wifi\\bin*)using the
Download tool(*sdk_x.y\\pc_tools\\Download_Tool*)provided with InnoPhase
Talaria TWO SDK.

1. Launch the Download tool.

1. In the GUI window:

   a. Boot Target: Select the appropriate EVK from the drop-down.

   a. ELF Input: Load the wifi_connect.elf by clicking on Select ELF
      File.

   a. AP Options: Pass the appropriate SSID and passphrase to connect to
      an Access Point.

   a. Boot Arguments: Add the host name as a boot argument.

+-----------------------------------------------------------------------+
| host_name=<host_name>                                                 |
+=======================================================================+
+-----------------------------------------------------------------------+

..

   Note: Default host name is talaria2.

a. Programming: Prog RAM or Prog Flash as per requirement.

For more details on using the Download tool, refer to the document:
UG_Download_Tool.pdf (path: *sdk_x.y\\pc_tools\\Download_Tool\\doc*).

**Note**: x and y refer to the SDK release version. For example:
sdk_2.4\\doc.

Expected Output
~~~~~~~~~~~~~~~

wifi_connect.elf execution displays the following output on the console
for different scenarios:

+-----------------------------------------------------------------------+
| Y-BOOT 208ef13 2019-07-22 12:26:54 -0500 790da1-b-7                   |
|                                                                       |
| ROM yoda-h0-rom-16-0-gd5a8e586                                        |
|                                                                       |
| FLASH:PNWWWWWAEBuild $Id: git-d198c0771 $                             |
|                                                                       |
| np_conf_path=/data/nprofile.json ssid=InnoPhase passphrase=Inno@1234  |
|                                                                       |
| $App:git-200f5dc1                                                     |
|                                                                       |
| SDK Ver: sdk_2.6.2                                                    |
|                                                                       |
| Wifi Connect Demo App                                                 |
|                                                                       |
| addr e0:69:3a:00:2d:fc                                                |
|                                                                       |
| host name talaria2                                                    |
|                                                                       |
| Connecting to added network : InnoPhase                               |
|                                                                       |
| [0.987,027] CONNECT:98:da:c4:73:b7:76 Channel:10 rssi:-45 dBm         |
|                                                                       |
| wcm_notify_cb to App Layer - WCM_NOTIFY_MSG_LINK_UP                   |
|                                                                       |
| wcm_notify_cb to App Layer - WCM_NOTIFY_MSG_ADDRESS                   |
|                                                                       |
| [1.261,104] MYIP 192.168.1.222                                        |
|                                                                       |
| [1.261,268] IPv6 [fe80::e269:3aff:fe00:2dfc]-link                     |
|                                                                       |
| wcm_notify_cb to App Layer - WCM_NOTIFY_MSG_CONNECTED                 |
|                                                                       |
| Connected to added network : InnoPhase                                |
|                                                                       |
| ------------ Program Exit -------------------                         |
+=======================================================================+
+-----------------------------------------------------------------------+

Wifi_Connect_Disconnect
-----------------------

.. _overview-1:

Overview
~~~~~~~~

Sample code in the path:

*apps\\using_wifi\\src\\wifi_connect_disconnect.c* showcases connecting
to and disconnecting from a network asynchronously with the API
wcm_auto_connect() and wcm_add_network_profile().

.. _sample-code-walkthrough-1:

Sample Code Walkthrough
~~~~~~~~~~~~~~~~~~~~~~~

This example code initializes two semaphores and creates two threads.

+-----------------------------------------------------------------------+
| /\* initializes the semaphores \*/                                    |
|                                                                       |
| os_sem_init( &my_sem1, 0 );                                           |
|                                                                       |
| os_sem_init( &my_sem2, 0 );                                           |
|                                                                       |
| /\* creates a thread \*/                                              |
|                                                                       |
| thread1 = os_create_thread("thread1", my_app_thread_func1,            |
|                                                                       |
| (void\*)my_arg1, MY_APP_THREAD_PRIO, MY_APP_THREAD_STACK_SIZE);       |
|                                                                       |
| /\* creates a thread \*/                                              |
|                                                                       |
| thread2 = os_create_thread("thread2", my_app_thread_func2,            |
|                                                                       |
| (void\*)my_arg2, MY_APP_THREAD_PRIO, MY_APP_THREAD_STACK_SIZE);       |
+=======================================================================+
+-----------------------------------------------------------------------+

thread2 on running enters a loop where it first waits for a semaphore
from thread1.

thread1 on running attempts wcm_add_network_profile()and
wcm_auto_connect()with param bool enable as 1 to connect, and waits for
10 seconds and finally enters a loop where it:

1. calls wcm_auto_connect()with param bool enable as 0 to asynchronously
   disconnect, without removing the network

2. waits for 10 seconds and unblocks thread2 by posting a semaphore

3. Finally waits on a semaphore posted from thread2, before looping back
   again to asynchronously disconnect attempt using wcm_auto_connect().

+-----------------------------------------------------------------------+
| /\*the thread function \*/                                            |
|                                                                       |
| static void\* my_app_thread_func1(void\* arg)                         |
|                                                                       |
| {                                                                     |
|                                                                       |
| os_printf("thread1 prints -- %s\\n", (char\*)arg);                    |
|                                                                       |
| /\*Create a Wi-Fi network interface*/                                 |
|                                                                       |
| my_wcm_handle = wcm_create(NULL);                                     |
|                                                                       |
| wcm_notify_enable(my_wcm_handle, my_wcm_notify_cb, NULL);             |
|                                                                       |
| /\*"/data/nprofile.json"\*/                                           |
|                                                                       |
| const char \*np_conf_path = os_get_boot_arg_str("np_conf_path")?:     |
| NULL;                                                                 |
|                                                                       |
| struct network_profile \*profile;                                     |
|                                                                       |
| int rval;                                                             |
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
| return NULL;                                                          |
|                                                                       |
| }                                                                     |
|                                                                       |
| rval = wcm_add_network_profile(my_wcm_handle, profile);               |
|                                                                       |
| if (rval < 0) {                                                       |
|                                                                       |
| pr_err("could not associate network profile to wcm %d\\n", rval);     |
|                                                                       |
| return NULL;                                                          |
|                                                                       |
| }                                                                     |
|                                                                       |
| os_sleep_us(2000000, OS_TIMEOUT_NO_WAKEUP);                           |
|                                                                       |
| os_printf("thread1 prints -- calling api wcm_auto_connect(1) to       |
| connect to already added network\\n");                                |
|                                                                       |
| wcm_auto_connect(my_wcm_handle, 1);                                   |
|                                                                       |
| os_printf("thread1 prints -- will try a disconnect after 10           |
| seconds... \\n");                                                     |
|                                                                       |
| os_sleep_us(10000000, OS_TIMEOUT_NO_WAKEUP);                          |
|                                                                       |
| while(1){                                                             |
|                                                                       |
| os_printf("thread1 prints -- calling api wcm_auto_connect(0) to just  |
| disconnect without removing network..\\n");                           |
|                                                                       |
| wcm_auto_connect(my_wcm_handle, 0);                                   |
|                                                                       |
| os_sleep_us(10000000, OS_TIMEOUT_NO_WAKEUP);                          |
|                                                                       |
| /\*unlock Thread2 \*/                                                 |
|                                                                       |
| os_sem_post( &my_sem2 );                                              |
|                                                                       |
| /\*block until thread 2 unblocks us \*/                               |
|                                                                       |
| os_sem_wait( &my_sem1 );                                              |
|                                                                       |
| }                                                                     |
|                                                                       |
| return NULL;                                                          |
|                                                                       |
| }                                                                     |
+=======================================================================+
+-----------------------------------------------------------------------+

As noted earlier, thread2 is in a loop, and when unblocked:

1. Calls wcm_auto_connect()with param bool enable as 1 to asynchronously
   connect to previously added network

2. waits for 10 seconds and unblocks thread1 by posting a semaphore

3. enters its loop again where it finally waits on a semaphore posted
   from thread1, before trying to asynchronously connect attempt using
   wcm_auto_connect().

+-----------------------------------------------------------------------+
| /\* the thread function \*/                                           |
|                                                                       |
| static void\* my_app_thread_func2(void\* arg)                         |
|                                                                       |
| {                                                                     |
|                                                                       |
| os_sleep_us(5000000, OS_TIMEOUT_NO_WAKEUP);                           |
|                                                                       |
| os_printf("thread2 prints -- %s\\n", (char\*)arg);                    |
|                                                                       |
| while(1){                                                             |
|                                                                       |
| /\*block until thread 1 unblocks us \*/                               |
|                                                                       |
| os_sem_wait( &my_sem2 );                                              |
|                                                                       |
| os_printf("thread2 prints -- calling api wcm_auto_connect(1) to       |
| connect to already added network\\n");                                |
|                                                                       |
| wcm_auto_connect(my_wcm_handle, 1);                                   |
|                                                                       |
| os_sleep_us(10000000, OS_TIMEOUT_NO_WAKEUP);                          |
|                                                                       |
| /\*unlock Thread1 \*/                                                 |
|                                                                       |
| os_sem_post( &my_sem1 );                                              |
|                                                                       |
| }                                                                     |
|                                                                       |
| return NULL;                                                          |
|                                                                       |
| }                                                                     |
+=======================================================================+
+-----------------------------------------------------------------------+

In this example, the Talaria TWO module connects and disconnects from
the network approximately every 10 seconds without removing the network
name.

Notifications from WCM are registered and gets printed just like the
previous example.

.. _running-the-application-1:

Running the Application
~~~~~~~~~~~~~~~~~~~~~~~

Program wifi_connect_diconnect.elf
(*sdk_x.y\\examples\\using_wifi\\bin*) using the Download tool
(*sdk_x.y\\pc_tools\\Download_Tool*) provided with InnoPhase Talaria TWO
SDK.

Refer steps mentioned in section 8.1.3 for more details.

PMK Caching
~~~~~~~~~~~

When Talaria TWO connects to an Access Point, the PMK generated after
802.1X authentication method will be stored in Talaria TWO’s flash and
this cached PMK will be used for subsequent connections.

This ensures minimal connection latency between the Access Point and
Talaria TWO as it avoids recomputing of PMK for each connection. PMK
cache feature is supported only on WPA2-PSK or Mixed mode.

.. _expected-output-1:

Expected Output
~~~~~~~~~~~~~~~

wifi_connect_disconnect.elf execution displays the following output on
the console for different scenarios:

Case 1
^^^^^^

AP is already ON at connection attempt, connect success, alternate
connect disconnect with autoconnect API, and add network and remove
network, as expected. Background notifications are received.

+-----------------------------------------------------------------------+
| UART:SNWWWWAE                                                         |
|                                                                       |
| Build $Id: git-d198c0771 $                                            |
|                                                                       |
| hio.baudrate=921600                                                   |
|                                                                       |
| flash: Gordon ready!                                                  |
|                                                                       |
| Y-BOOT 208ef13 2019-07-22 12:26:54 -0500 790da1-b-7                   |
|                                                                       |
| ROM yoda-h0-rom-16-0-gd5a8e586                                        |
|                                                                       |
| FLASH:PNWWWWWAEBuild $Id: git-d198c0771 $                             |
|                                                                       |
| np_conf_path=/data/nprofile.json ssid=Asus_CC_2G1 passphrase=12345678 |
|                                                                       |
| SDK Ver: sdk_2.6.2                                                    |
|                                                                       |
| Wifi Async Connect Demo App                                           |
|                                                                       |
| thread1 prints -- application thread1 will attempt                    |
| wcm_add_network_profile() and wcm_auto_connect(1) and then disconnect |
| with wcm_auto_connect(0) 10 seconds after every connection            |
|                                                                       |
| addr e0:69:3a:00:01:05                                                |
|                                                                       |
| thread1 prints -- calling api wcm_auto_connect(1) to connect to       |
| already added network                                                 |
|                                                                       |
| thread1 prints -- will try a disconnect after 10 seconds...           |
|                                                                       |
| [2.730,711] CONNECT:24:4b:fe:5e:fd:d8 Channel:1 rssi:-36 dBm          |
|                                                                       |
| wcm_notify_cb to App Layer - WCM_NOTIFY_MSG_ADDRESS                   |
|                                                                       |
| wcm_notify_cb to App Layer - WCM_NOTIFY_MSG_LINK_UP                   |
|                                                                       |
| [2.769,323] MYIP 192.168.1.4                                          |
|                                                                       |
| [2.769,486] IPv6 [fe80::e269:3aff:fe00:105]-link                      |
|                                                                       |
| thread2 prints -- application thread2 will attempt connect using      |
| wcm_auto_connect(1).                                                  |
|                                                                       |
| thread1 prints -- calling api wcm_auto_connect(0) to just disconnect  |
| without removing network..                                            |
|                                                                       |
| wcm_notify_cb to App Layer - WCM_NOTIFY_MSG_LINK_DOWN                 |
|                                                                       |
| [12.209,898] DISCONNECTED                                             |
|                                                                       |
| thread2 prints -- calling api wcm_auto_connect(1) to connect to       |
| already added network                                                 |
|                                                                       |
| [22.255,835] CONNECT:24:4b:fe:5e:fd:d8 Channel:1 rssi:-37 dBm         |
|                                                                       |
| wcm_notify_cb to App Layer - WCM_NOTIFY_MSG_LINK_UP                   |
|                                                                       |
| wcm_notify_cb to App Layer - WCM_NOTIFY_MSG_ADDRESS                   |
|                                                                       |
| [22.303,722] MYIP 192.168.1.4                                         |
|                                                                       |
| [22.304,002] IPv6 [fe80::e269:3aff:fe00:105]-link                     |
|                                                                       |
| thread1 prints -- calling api wcm_auto_connect(0) to just disconnect  |
| without removing network..                                            |
|                                                                       |
| wcm_notify_cb to App Layer - WCM_NOTIFY_MSG_LINK_DOWN                 |
|                                                                       |
| [32.210,984] DISCONNECTED                                             |
|                                                                       |
| thread2 prints -- calling api wcm_auto_connect(1) to connect to       |
| already added network                                                 |
|                                                                       |
| [42.253,134] CONNECT:24:4b:fe:5e:fd:d8 Channel:1 rssi:-37 dBm         |
|                                                                       |
| wcm_notify_cb to App Layer - WCM_NOTIFY_MSG_LINK_UP                   |
|                                                                       |
| wcm_notify_cb to App Layer - WCM_NOTIFY_MSG_ADDRESS                   |
|                                                                       |
| [42.296,531] MYIP 192.168.1.4                                         |
|                                                                       |
| [42.296,694] IPv6 [fe80::e269:3aff:fe00:105]-link                     |
+=======================================================================+
+-----------------------------------------------------------------------+

Case 2
^^^^^^

AP is already ON at connection attempt, wrong password given, connect
failure, alternate connect disconnect and add network and remove network
as expected, without any thread hanging.

+-----------------------------------------------------------------------+
| UART:SNWWWWAE                                                         |
|                                                                       |
| Build $Id: git-d198c0771 $                                            |
|                                                                       |
| hio.baudrate=921600                                                   |
|                                                                       |
| flash: Gordon ready!                                                  |
|                                                                       |
| [9.230,063] partitions mounted                                        |
|                                                                       |
| UART:SNWWWWAE                                                         |
|                                                                       |
| Build $Id: git-d198c0771 $                                            |
|                                                                       |
| hio.baudrate=921600                                                   |
|                                                                       |
| flash: Gordon ready!                                                  |
|                                                                       |
| Y-BOOT 208ef13 2019-07-22 12:26:54 -0500 790da1-b-7                   |
|                                                                       |
| ROM yoda-h0-rom-16-0-gd5a8e586                                        |
|                                                                       |
| FLASH:PNWWWWWAEBuild $Id: git-d198c0771 $                             |
|                                                                       |
| np_conf_path=/data/nprofile.json ssid=Asus_CC_2G1                     |
| passphrase=123456789                                                  |
|                                                                       |
| SDK Ver: sdk_2.6.2                                                    |
|                                                                       |
| Wifi Async Connect Demo App                                           |
|                                                                       |
| thread1 prints -- application thread1 will attempt                    |
| wcm_add_network_profile() and wcm_auto_connect(1) and then disconnect |
| with wcm_auto_connect(0) 10 seconds after every connection            |
|                                                                       |
| addr e0:69:3a:00:01:05                                                |
|                                                                       |
| thread1 prints -- calling api wcm_auto_connect(1) to connect to       |
| already added network                                                 |
|                                                                       |
| thread1 prints -- will try a disconnect after 10 seconds...           |
|                                                                       |
| [2.741,498] CONNECT:24:4b:fe:5e:fd:d8 Channel:6 rssi:-34 dBm          |
|                                                                       |
| thread2 prints -- application thread2 will attempt connect using      |
| wcm_auto_connect(1).                                                  |
|                                                                       |
| [10.742,444] DISCONNECTED during key negotiation, wrong key?          |
|                                                                       |
| [10.764,455] Trying to connect in 2 seconds                           |
|                                                                       |
| thread1 prints -- calling api wcm_auto_connect(0) to just disconnect  |
| without removing network..                                            |
|                                                                       |
| thread2 prints -- calling api wcm_auto_connect(1) to connect to       |
| already added network                                                 |
|                                                                       |
| [22.378,399] CONNECT:24:4b:fe:5e:fd:d8 Channel:6 rssi:-34 dBm         |
|                                                                       |
| [30.378,648] DISCONNECTED during key negotiation, wrong key?          |
|                                                                       |
| [30.400,425] Trying to connect in 2 seconds                           |
|                                                                       |
| thread1 prints -- calling api wcm_auto_connect(0) to just disconnect  |
| without removing network..                                            |
|                                                                       |
| thread2 prints -- calling api wcm_auto_connect(1) to connect to       |
| already added network                                                 |
|                                                                       |
| [42.375,801] CONNECT:24:4b:fe:5e:fd:d8 Channel:6 rssi:-33 dBm         |
|                                                                       |
| [50.376,281] DISCONNECTED during key negotiation, wrong key?          |
|                                                                       |
| [50.397,366] Trying to connect in 2 seconds                           |
+=======================================================================+
+-----------------------------------------------------------------------+

Case 3
^^^^^^

AP is switched OFF at connection attempt, alternate connect disconnect
and add network and remove network as expected, without any thread
hanging.

   Later, AP is switched ON, connect success, alternate connect
   disconnect and add remove as expected.

+-----------------------------------------------------------------------+
| UART:SNWWWWAE                                                         |
|                                                                       |
| Build $Id: git-d198c0771 $                                            |
|                                                                       |
| hio.baudrate=921600                                                   |
|                                                                       |
| flash: Gordon ready!                                                  |
|                                                                       |
| [9.426,279] partitions mounted                                        |
|                                                                       |
| UART:SNWWWWAE                                                         |
|                                                                       |
| Build $Id: git-d198c0771 $                                            |
|                                                                       |
| hio.baudrate=921600                                                   |
|                                                                       |
| flash: Gordon ready!                                                  |
|                                                                       |
| Y-BOOT 208ef13 2019-07-22 12:26:54 -0500 790da1-b-7                   |
|                                                                       |
| ROM yoda-h0-rom-16-0-gd5a8e586                                        |
|                                                                       |
| FLASH:PNWWWWWAEBuild $Id: git-d198c0771 $                             |
|                                                                       |
| np_conf_path=/data/nprofile.json ssid=Asus_CC_2G1 passphrase=12345678 |
|                                                                       |
| SDK Ver: sdk_2.6.2                                                    |
|                                                                       |
| Wifi Async Connect Demo App                                           |
|                                                                       |
| thread1 prints -- application thread1 will attempt                    |
| wcm_add_network_profile() and wcm_auto_connect(1) and then disconnect |
| with wcm_auto_connect(0) 10 seconds after every connection            |
|                                                                       |
| addr e0:69:3a:00:01:05                                                |
|                                                                       |
| thread1 prints -- calling api wcm_auto_connect(1) to connect to       |
| already added network                                                 |
|                                                                       |
| thread1 prints -- will try a disconnect after 10 seconds...           |
|                                                                       |
| [2.742,962] CONNECT:24:4b:fe:5e:fd:d8 Channel:6 rssi:-34 dBm          |
|                                                                       |
| wcm_notify_cb to App Layer - WCM_NOTIFY_MSG_LINK_UP                   |
|                                                                       |
| wcm_notify_cb to App Layer - WCM_NOTIFY_MSG_ADDRESS                   |
|                                                                       |
| [4.689,892] MYIP 192.168.1.4                                          |
|                                                                       |
| [4.690,055] IPv6 [fe80::e269:3aff:fe00:105]-link                      |
|                                                                       |
| thread2 prints -- application thread2 will attempt connect using      |
| wcm_auto_connect(1).                                                  |
|                                                                       |
| thread1 prints -- calling api wcm_auto_connect(0) to just disconnect  |
| without removing network..                                            |
|                                                                       |
| wcm_notify_cb to App Layer - WCM_NOTIFY_MSG_LINK_DOWN                 |
|                                                                       |
| [12.205,311] DISCONNECTED                                             |
|                                                                       |
| thread2 prints -- calling api wcm_auto_connect(1) to connect to       |
| already added network                                                 |
|                                                                       |
| [22.613,616] Trying to connect in 1 seconds                           |
|                                                                       |
| [23.739,080] Trying to connect in 2 seconds                           |
|                                                                       |
| [25.864,544] Trying to connect in 4 seconds                           |
|                                                                       |
| [29.990,008] Trying to connect in 8 seconds                           |
|                                                                       |
| thread1 prints -- calling api wcm_auto_connect(0) to just disconnect  |
| without removing network..                                            |
|                                                                       |
| thread2 prints -- calling api wcm_auto_connect(1) to connect to       |
| already added network                                                 |
|                                                                       |
| [42.717,590] Trying to connect in 1 seconds                           |
|                                                                       |
| [43.843,054] Trying to connect in 2 seconds                           |
|                                                                       |
| [45.968,518] Trying to connect in 4 seconds                           |
|                                                                       |
| [50.093,983] Trying to connect in 8 seconds                           |
|                                                                       |
| thread1 prints -- calling api wcm_auto_connect(0) to just disconnect  |
| without removing network..                                            |
|                                                                       |
| thread2 prints -- calling api wcm_auto_connect(1) to connect to       |
| already added network                                                 |
|                                                                       |
| [62.389,674] CONNECT:24:4b:fe:5e:fd:d8 Channel:6 rssi:-33 dBm         |
|                                                                       |
| wcm_notify_cb to App Layer - WCM_NOTIFY_MSG_LINK_UP                   |
|                                                                       |
| wcm_notify_cb to App Layer - WCM_NOTIFY_MSG_ADDRESS                   |
|                                                                       |
| [62.503,180] MYIP 192.168.1.4                                         |
|                                                                       |
| [62.503,635] IPv6 [fe80::e269:3aff:fe00:105]-link                     |
|                                                                       |
| thread1 prints -- calling api wcm_auto_connect(0) to just disconnect  |
| without removing network..                                            |
|                                                                       |
| wcm_notify_cb to App Layer - WCM_NOTIFY_MSG_LINK_DOWN                 |
|                                                                       |
| [72.207,219] DISCONNECTED                                             |
+=======================================================================+
+-----------------------------------------------------------------------+

Wi-Fi Scan 
-----------

.. _overview-2:

Overview
~~~~~~~~

The sample code in the path *example\\using_wifi\\src\\wifi_scan.c*
scans for available Wi-Fi networks and prints them out.

Following are the steps:

1. Create a data structure to store the parameters and results of scan.

2. Set the default parameter for scanning using the API
   wifi_init_scan_default()

3. In a loop, let the code scan and print the nearby networks from
   vicinity for every 10 second interval of time.

.. _sample-code-walkthrough-2:

Sample Code Walkthrough
~~~~~~~~~~~~~~~~~~~~~~~

The necessary data structures to store parameters and result of scan are
created as shown:

+-----------------------------------------------------------------------+
| int main(void)                                                        |
|                                                                       |
| {                                                                     |
|                                                                       |
| struct wcm_handle \*h;                                                |
|                                                                       |
| const size_t max_nets = 64;                                           |
|                                                                       |
| struct wifi_netinfo \**scan_result;                                   |
|                                                                       |
| struct wifi_scan_param param;                                         |
|                                                                       |
| …                                                                     |
|                                                                       |
| …                                                                     |
|                                                                       |
| …                                                                     |
|                                                                       |
| scan_result = os_alloc(max_nets \* sizeof(void \*));                  |
|                                                                       |
| assert(scan_result != NULL);                                          |
+=======================================================================+
+-----------------------------------------------------------------------+

wifi_init_scan_default()API is used to set the default parameters for
the scanning, and wcm_scan() is used with explained parameters to start
scanning.

The example code runs in a loop, scans and prints the results using
wifi_netinfo_get_ssid() and wifi_netinfo_get_chan(), frees up the memory
allocated for scan result using wcm_free_scanresult() and waits for 10
seconds before scanning and printing again as shown in the following
code:

+-----------------------------------------------------------------------+
| wifi_init_scan_default(&param);                                       |
|                                                                       |
| // print scan parameters                                              |
|                                                                       |
| print_scan_params(param);                                             |
|                                                                       |
| for (;;) {                                                            |
|                                                                       |
| // perform scan                                                       |
|                                                                       |
| int n = wcm_scan(h, &param, scan_result, max_nets);                   |
|                                                                       |
| // print out results of scan                                          |
|                                                                       |
| os_printf("Found %d nets:\\n", n);                                    |
|                                                                       |
| for (int i = 0; i < n; i++) {                                         |
|                                                                       |
| uint8_t chan;                                                         |
|                                                                       |
| struct wifi_ssid ssid;                                                |
|                                                                       |
| wifi_netinfo_get_ssid(scan_result[i], &ssid);                         |
|                                                                       |
| wifi_netinfo_get_chan(scan_result[i], &chan);                         |
|                                                                       |
| os_printf("%6pM on channel %2d @ %3d '%s'\\n",                        |
|                                                                       |
| scan_result[i]->ni_bssid, chan, scan_result[i]->ni_rssi,              |
| ssid.ws_ssid);                                                        |
|                                                                       |
| }                                                                     |
|                                                                       |
| wcm_free_scanresult(scan_result, n);                                  |
|                                                                       |
| os_sleep_us(10000000, OS_TIMEOUT_NO_WAKEUP);                          |
|                                                                       |
| }                                                                     |
+=======================================================================+
+-----------------------------------------------------------------------+

.. _running-the-application-2:

Running the Application
~~~~~~~~~~~~~~~~~~~~~~~

Program wifi_scan.elf (*sdk_x.y\\examples\\using_wifi\\bin*)using the
Download tool(*sdk_x.y\\pc_tools\\Download_Tool*)provided with InnoPhase
Talaria TWO SDK.

Refer steps mentioned in section 8.1.3 for more details.

.. _expected-output-2:

Expected Output
~~~~~~~~~~~~~~~

wifi_scan.elf execution displays the following output on the console for
different scenarios:

+-----------------------------------------------------------------------+
| UART:SNWWWWWAEBuild $Id: git-ba65998b7 $                              |
|                                                                       |
| np_conf_path=/data/nprofile.json ssid=InnoPhase passphrase=43083191   |
|                                                                       |
| SDK Ver: sdk_2.5                                                      |
|                                                                       |
| Wifi Scan Demo App                                                    |
|                                                                       |
| addr e0:69:3a:00:13:90                                                |
|                                                                       |
| Scan parameters:                                                      |
|                                                                       |
| channel_masks: 255 255 255 255 255 255 255 255                        |
|                                                                       |
| bssid: 0xFFFFFFFFFFFF                                                 |
|                                                                       |
| txrate: 0                                                             |
|                                                                       |
| waittime: 0                                                           |
|                                                                       |
| ie list: 0x                                                           |
|                                                                       |
| Found 6 nets:                                                         |
|                                                                       |
| 6e:8a:ce:99:b1:c8 on channel 6 @ -39 'Inno' 'OPEN'                    |
|                                                                       |
| 00:5f:67:cd:c5:a6 on channel 11 @ -46 'InnoPhase' 'WPA2-PSK'          |
|                                                                       |
| e4:a7:c5:d4:ea:86 on channel 6 @ -74 'Airtel-E5573-EA86' 'WPA2-PSK'   |
|                                                                       |
| 70:4f:57:77:7e:d4 on channel 2 @ -74 'Rahul' 'WPA2-PSK'               |
|                                                                       |
| d8:0f:99:72:13:65 on channel 5 @ -79 'JioFi3_721365'                  |
| 'WPA-PSK/WPA2-PSK Mixed Mode'                                         |
|                                                                       |
| d8:47:32:2e:e1:e0 on channel 11 @ -80 'GPMH' 'WPA2-PSK'               |
|                                                                       |
| Found 7 nets:                                                         |
|                                                                       |
| 6e:8a:ce:99:b1:c8 on channel 6 @ -34 'Inno' 'OPEN'                    |
|                                                                       |
| 00:5f:67:cd:c5:a6 on channel 11 @ -46 'InnoPhase' 'WPA2-PSK'          |
|                                                                       |
| ba:6b:ad:62:6d:8b on channel 11 @ -72 'DESKTOP-9B1DNVC 1786'          |
| 'WPA2-PSK'                                                            |
|                                                                       |
| 34:0a:33:70:f3:a2 on channel 1 @ -76 'Siddusm' 'WPA2-PSK'             |
|                                                                       |
| dc:71:37:56:91:b0 on channel 8 @ -77 'Hathway_Raghuram'               |
| 'WPA-PSK/WPA2-PSK Mixed Mode'                                         |
|                                                                       |
| d8:0f:99:72:13:65 on channel 5 @ -78 'JioFi3_721365'                  |
| 'WPA-PSK/WPA2-PSK Mixed Mode'                                         |
|                                                                       |
| ac:84:c6:88:10:46 on channel 13 @ -85 'Lakshmi pg 3rd floor '         |
| 'WPA2-PSK'                                                            |
|                                                                       |
| Found 6 nets:                                                         |
|                                                                       |
| 6e:8a:ce:99:b1:c8 on channel 6 @ -33 'Inno' 'OPEN'                    |
|                                                                       |
| 00:5f:67:cd:c5:a6 on channel 11 @ -47 'InnoPhase' 'WPA2-PSK'          |
|                                                                       |
| ba:6b:ad:62:6d:8b on channel 11 @ -71 'DESKTOP-9B1DNVC 1786'          |
| 'WPA2-PSK'                                                            |
|                                                                       |
| d8:0f:99:72:13:65 on channel 5 @ -77 'JioFi3_721365'                  |
| 'WPA-PSK/WPA2-PSK Mixed Mode'                                         |
|                                                                       |
| b0:a7:b9:73:8e:51 on channel 4 @ -78 'Lakshmi pg 2nd floor 2g'        |
| 'WPA2-PSK'                                                            |
|                                                                       |
| dc:71:37:56:91:b0 on channel 8 @ -79 'Hathway_Raghuram'               |
| 'WPA-PSK/WPA2-PSK Mixed Mode'                                         |
+=======================================================================+
+-----------------------------------------------------------------------+

Power Optimization with Rx Nap Scan
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In a crowded environment, Rx Nap Scan feature can be enabled to save
power during the scan process. In this mode, the Rx nap function will
turn the Talaria TWO’s receiver OFF (*takes a nap*) for the duration of
the frame when there are uninteresting frames with high signal strength.
The frames of interest are probe responses and beacon frames.

This mode is enabled by default in wifi_scan.elf and can be disabled
using the following boot argument:

+-----------------------------------------------------------------------+
| wifi.nap_scan=0                                                       |
+=======================================================================+
+-----------------------------------------------------------------------+

As shown in Figure 4, Talaria TWO takes naps when there are
uninteresting frames. During the naps, current consumption dips to 8mA
whereas during the scan period, the average Rx current remains at ~33mA.

|image3|

Figure 4: Talaria TWO naps during uninteresting frames

Rx nap scan mode disabled is as shown in Figure 5.

|image4|

Figure 5: Rx nap scan mode disabled

.. |Diagram Description automatically generated| image:: media/image1.png
   :width: 5.11806in
   :height: 1.69861in
.. |image1| image:: media/image2.png
   :width: 5.90556in
   :height: 1.47292in
.. |image2| image:: media/image3.png
   :width: 3.14931in
   :height: 2.88958in
.. |image3| image:: media/image4.png
   :width: 5.90556in
   :height: 2.95069in
.. |image4| image:: media/image5.png
   :width: 5.90556in
   :height: 2.93611in
