Overview
========

This application note provides details on the sntpapplication to fetch
time from the NTP server by using the Simple Network Time Protocol
(SNTP) component of the SDK for Talaria TWO modules.

Simple Network Time Protocol (SNTP)
===================================

SNTP is a networking protocol for synchronizing the computer clocks to
some reference over a network. SNTP is a stripped-down version of NTP
that is suited to small networks and computers with limited processing
power.

Relevant APIs
=============

SNTP APIs
---------

sntp_setoperatingmode()
~~~~~~~~~~~~~~~~~~~~~~~

Sets the operating mode.

+-----------------------------------------------------------------------+
| sntp_setoperatingmode(SNTP_OPMODE_POLL);                              |
+=======================================================================+
+-----------------------------------------------------------------------+

SNTP has two operating modes:

1. SNTP_OPMODE_POLL: Poll using unicast. Requires server name to be set.

2. SNTP_OPMODE_LISTENONLY: This mode requires broadcast NTP on the
   network.

..

   The example in this document uses SNTP_OPMODE.

sntp_init()
~~~~~~~~~~~

Initializes the module.

+-----------------------------------------------------------------------+
| sntp_init();                                                          |
+=======================================================================+
+-----------------------------------------------------------------------+

sntp_stop()
~~~~~~~~~~~

Stops the module.

+-----------------------------------------------------------------------+
| sntp_stop();                                                          |
+=======================================================================+
+-----------------------------------------------------------------------+

os_systime64()
~~~~~~~~~~~~~~

Returns the current system time in microseconds.

+-----------------------------------------------------------------------+
| uint64_t now = os_systime64();                                        |
|                                                                       |
| os_printf("\\r\\n time:%lld \\n", now);                               |
+=======================================================================+
+-----------------------------------------------------------------------+

Code Walkthrough
================

Connecting to a Wi-Fi network
-----------------------------

To connect to a Wi-Fi network, wcm_create()API from the Wi-Fi Connection
Manager are used.

Initially, the Wi-Fi network interface is created using wcm_create().

+-----------------------------------------------------------------------+
| h = wcm_create(NULL);                                                 |
+=======================================================================+
+-----------------------------------------------------------------------+

..

   wifi_connect_to_network()API, from components library, connects to
   the Wi-Fi network using the AP credentials provided.

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

Getting time from NTP
---------------------

In the main function, application initiates the Wi-Fi connection. After
the connection is successful, the ntpdate() function is called to fetch
the time.

+-----------------------------------------------------------------------+
| print_ver("Using NTP Application", 1, 1);                             |
|                                                                       |
| os_sem_init(&app_wcm_lock, 0);                                        |
|                                                                       |
| /\*wifi connection*/                                                  |
|                                                                       |
| wcm_handle = wcm_create(NULL);                                        |
|                                                                       |
| /\*Connect to WiFi N/w*/                                              |
|                                                                       |
| app_wcm_connect(wcm_handle);                                          |
|                                                                       |
| if(!wcm_connected)                                                    |
|                                                                       |
| {                                                                     |
|                                                                       |
| os_printf("\\n [APP]Error: Failed to connect to WiFi N/w");           |
|                                                                       |
| return false;                                                         |
|                                                                       |
| }                                                                     |
|                                                                       |
| os_printf("Wifi connected \\n");                                      |
|                                                                       |
| ntpdate();                                                            |
+=======================================================================+
+-----------------------------------------------------------------------+

The SNTP module can be initiated with the operating mode of
SNTP_OPMODE_POLL. This creates the NTP interface and fetches time. The
SNTP will fetch the time data from the default server time.google.com.

The time.google.com automatically picks time servers which are
geographically close to Talaria TWO.

+-----------------------------------------------------------------------+
| int status;                                                           |
|                                                                       |
| int time_now;                                                         |
|                                                                       |
| int times = 0;                                                        |
|                                                                       |
| ip_addr_t server_ip;                                                  |
|                                                                       |
| time_t tim;                                                           |
|                                                                       |
| sntp_stop();                                                          |
|                                                                       |
| sntp_setoperatingmode(SNTP_OPMODE_POLL);                              |
|                                                                       |
| server_addr = "216.239.35.0";/\*time.google.org*/                     |
|                                                                       |
| status = ipaddr_aton(server_addr, &server_ip);                        |
|                                                                       |
| if(status != 1) {                                                     |
|                                                                       |
| return false;                                                         |
|                                                                       |
| }                                                                     |
|                                                                       |
| sntp_init();                                                          |
|                                                                       |
| sntp_setserver(0, &server_ip);                                        |
|                                                                       |
| os_msleep(2000);                                                      |
|                                                                       |
| uint64_t now = os_systime64();                                        |
|                                                                       |
| os_printf("\\r\\ntime:%lld \\n", now);                                |
|                                                                       |
| do{                                                                   |
|                                                                       |
| time_now = sntp_time();                                               |
|                                                                       |
| os_printf("\\r\\nwaiting for sntp, times=%d:%d\\n", times++,          |
| time_now);                                                            |
|                                                                       |
| if(0 != time_now)                                                     |
|                                                                       |
| {                                                                     |
|                                                                       |
| break;                                                                |
|                                                                       |
| }                                                                     |
|                                                                       |
| os_msleep(2000);                                                      |
|                                                                       |
| }                                                                     |
|                                                                       |
| while(times < 16);                                                    |
|                                                                       |
| if(times >= 16)                                                       |
|                                                                       |
| return 0;                                                             |
|                                                                       |
| tim = time_now;                                                       |
|                                                                       |
| os_printf("\\r\\ndate: %s\\r\\n", ctime(&tim));                       |
|                                                                       |
| sntp_stop();                                                          |
+=======================================================================+
+-----------------------------------------------------------------------+

Running the Application
=======================

Programming Talaria TWO Device using Download Tool
--------------------------------------------------

Program sntp.elf (*sdk_x.y\\examples\\using_sntp\\bin*) using the
Download tool:

1. Launch the Download tool provided with InnoPhase Talaria TWO SDK.

2. In the GUI window:

   a. Boot Target: Select the appropriate EVK from the drop-down

   b. ELF Input: Load the sntp.elf by clicking on Select ELF File.

   c. AP Options: Provide the SSID and Passphrase under AP Options to
      connect to an Access Point.

   d. Programming: Prog RAM or Prog Flash as per requirement.

For more details on using the Download tool, refer to the document:
UG_Download_Tool.pdf (path: *sdk_x.y\\pc_tools\\Download_Tool\\doc*).

**Note**: x and y refer to the SDK release version. For example:
*sdk_2.5\\doc*.

Expected Output
---------------

On flashing the application using the Download Tool, the console output
is as follows:

The application will connect to the AP specified by the SSID and
passphrase. Upon successful connection, the latest time is fetched from
the NTP server.

+-----------------------------------------------------------------------+
| UART:SNWWWWWAEBuild $Id: git-ba65998b7 $                              |
|                                                                       |
| np_conf_path=/data/nprofile.json ssid=InnoPhase passphrase=43083191   |
|                                                                       |
| $App:git-73e7f910                                                     |
|                                                                       |
| SDK Ver: sdk_2.5                                                      |
|                                                                       |
| Using SNTP Application                                                |
|                                                                       |
| addr e0:69:3a:00:13:90                                                |
|                                                                       |
| Connecting to added network : InnoPhase                               |
|                                                                       |
| [2.401,377] CONNECT:00:5f:67:cd:c5:a6 Channel:11 rssi:-48 dBm         |
|                                                                       |
| wcm_notify_cb to App Layer - WCM_NOTIFY_MSG_LINK_UP                   |
|                                                                       |
| wcm_notify_cb to App Layer - WCM_NOTIFY_MSG_ADDRESS                   |
|                                                                       |
| [4.121,170] MYIP 192.168.0.102                                        |
|                                                                       |
| [4.121,219] IPv6 [fe80::e269:3aff:fe00:1390]-link                     |
|                                                                       |
| wcm_notify_cb to App Layer - WCM_NOTIFY_MSG_CONNECTED                 |
|                                                                       |
| Connected to added network : InnoPhase                                |
|                                                                       |
| Wifi connected                                                        |
|                                                                       |
| SNTP: using server: pool.ntp.org                                      |
|                                                                       |
| time:6127449                                                          |
|                                                                       |
| waiting for sntp, times=0:0                                           |
|                                                                       |
| waiting for sntp, times=1:0                                           |
|                                                                       |
| waiting for sntp, times=2:0                                           |
|                                                                       |
| waiting for sntp, times=3:0                                           |
|                                                                       |
| waiting for sntp, times=4:0                                           |
|                                                                       |
| waiting for sntp, times=5:0                                           |
|                                                                       |
| sntp_process: Thu Jul 7 18:04:17 2022                                 |
|                                                                       |
| waiting for sntp, times=6:1657217057                                  |
|                                                                       |
| date: Thu Jul 7 18:04:17 202                                          |
+=======================================================================+
+-----------------------------------------------------------------------+
