Introduction 
=============

This application note describes the basics of sleep management in
InnoOS™, providing a brief on using os_suspend_enable() and
os_suspend_disable() functions.

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

Calling os_suspend_enable() will suspend the system or enable deep sleep
when the processor is idle. Enabling and disabling suspend mode takes
additional time, which will affect the real-time response of the system.
When an interrupt occurs, the system will wake up even if it is in a
suspended state. However, the latency will be more as compared to when
the system operates in a non-suspended mode.

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

Sleep_enable_disable.c
----------------------

Overview
~~~~~~~~

The sample code is the path:
examples/sleep_enable_disable/src/sleep_enable_disable.c is a simple
application which demonstrates sleep mode.

Sample Code Walkthrough 
~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------------+
| int suspend_count =0;                                                 |
+=======================================================================+
+-----------------------------------------------------------------------+

To connect to a Wi-Fi network, the following APIs from the Wi-Fi
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
| pr_err("could not create network profile %d\\n", rval);\\             |
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
| os_sleep_us(1000000, OS_TIMEOUT_NO_WAKEUP);                           |
|                                                                       |
| if (wcm_cnt == WCM_SUCCESS) {                                         |
|                                                                       |
| auot_sucss = 1; }                                                     |
+=======================================================================+
+-----------------------------------------------------------------------+

+-----------------------------------------------------------------------+
| static void my_wcm_notify_cb(void \*ctx, struct os_msg \*msg)         |
|                                                                       |
| {                                                                     |
|                                                                       |
| switch(msg->msg_type)                                                 |
|                                                                       |
| {                                                                     |
|                                                                       |
| case(WCM_NOTIFY_MSG_LINK_UP):                                         |
|                                                                       |
| os_printf("wcm_notify_cb to App Layer - WCM_NOTIFY_MSG_LINK_UP\\n");  |
|                                                                       |
| break;                                                                |
|                                                                       |
| case(WCM_NOTIFY_MSG_LINK_DOWN):                                       |
|                                                                       |
| os_printf("wcm_notify_cb to App Layer -                               |
| WCM_NOTIFY_MSG_LINK_DOWN\\n");                                        |
|                                                                       |
| break;                                                                |
|                                                                       |
| case(WCM_NOTIFY_MSG_ADDRESS):                                         |
|                                                                       |
| os_printf("wcm_notify_cb to App Layer - WCM_NOTIFY_MSG_ADDRESS\\n");  |
|                                                                       |
| if (os_sem_waiting(&connect_lock)){                                   |
|                                                                       |
| os_sem_post(&connect_lock);                                           |
|                                                                       |
| }                                                                     |
|                                                                       |
| break;                                                                |
|                                                                       |
| case(WCM_NOTIFY_MSG_DISCONNECT_DONE):                                 |
|                                                                       |
| os_printf("wcm_notify_cb to App Layer -                               |
| WCM_NOTIFY_MSG_DISCONNECT_DONE\\n");                                  |
|                                                                       |
| if (os_sem_waiting(&connect_lock)){                                   |
|                                                                       |
| os_sem_post(&connect_lock);                                           |
|                                                                       |
| }                                                                     |
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

suspend_count is used to count the number of times the sleep
enable/disable functionality is called for in the program. The values
are printed in the console.

**Case 1**:

On successfully connecting to the Wi-Fi network, enable sleep for a
duration of 5 seconds and then disable it:

+-----------------------------------------------------------------------+
| /\**Enable sleep for 5 sec then disable**/                            |
|                                                                       |
| os_printf("\\nCase 1: Enable then disable\\n");                       |
|                                                                       |
| os_printf("os_suspend enable 1x\\n");                                 |
|                                                                       |
| enable_sleep();                                                       |
|                                                                       |
| os_printf("suspend_count: %d\\n", suspend_count);                     |
|                                                                       |
| os_sleep_us(5000000, OS_TIMEOUT_NO_WAKEUP);                           |
|                                                                       |
| os_printf("os_suspend disable 1x\\n");                                |
|                                                                       |
| disable_sleep();                                                      |
|                                                                       |
| os_printf("suspend_count: %d\\n", suspend_count);                     |
|                                                                       |
| os_sleep_us(5000000, OS_TIMEOUT_NO_WAKEUP);                           |
+=======================================================================+
+-----------------------------------------------------------------------+

**Case 2**:

Sleep enable function is called twice to put the device to sleep and
disabled after 5 seconds. Though the sleep mode is disabled,
os_suspend_disable() function is called once the device continues to
stay in sleep mode for the next five seconds. On calling the disable
sleep function again, the system resets to default state and sleep is
disabled.

+-----------------------------------------------------------------------+
| /\*\*                                                                 |
|                                                                       |
| Calls os_suspend_enable twice then os_suspend_disable.                |
|                                                                       |
| T2 will not get out of low-power mode on first os_suspend_disable     |
| call                                                                  |
|                                                                       |
| \**/                                                                  |
|                                                                       |
| os_printf("\\nCase 2: Enable 2x then disable 1x\\n");                 |
|                                                                       |
| os_printf("os_suspend enable 2x\\n");                                 |
|                                                                       |
| enable_sleep();                                                       |
|                                                                       |
| enable_sleep();                                                       |
|                                                                       |
| os_printf("suspend_count: %d\\n", suspend_count);                     |
|                                                                       |
| os_sleep_us(5000000, OS_TIMEOUT_NO_WAKEUP);                           |
|                                                                       |
| /\*low-power mode will not be disabled though we call                 |
|                                                                       |
| os_suspened_disable()*/                                               |
|                                                                       |
| os_printf("os_suspend disable 1x\\n");                                |
|                                                                       |
| disable_sleep();                                                      |
|                                                                       |
| os_printf("suspend_count: %d\\n", suspend_count);                     |
|                                                                       |
| os_sleep_us(5000000, OS_TIMEOUT_NO_WAKEUP);                           |
|                                                                       |
| /\* reset to default state. Sleep will be disabled \*/                |
|                                                                       |
| os_printf("os_suspend disable 1x\\n");                                |
|                                                                       |
| disable_sleep();                                                      |
|                                                                       |
| os_printf("suspend_count: %d\\n", suspend_count);                     |
|                                                                       |
| os_sleep_us(5000000, OS_TIMEOUT_NO_WAKEUP);                           |
+=======================================================================+
+-----------------------------------------------------------------------+

**Case 3**:

Call the os_suspend_disable() first. In this case, the low power mode
will not be enabled as the disable function is called before
os_suspend_enable().

+-----------------------------------------------------------------------+
| /\*\*                                                                 |
|                                                                       |
| Calls os_suspend_disable dirst os_suspend_enable.                     |
|                                                                       |
| low-power mode not be enabled because os_suspend_disable              |
|                                                                       |
| was called before a os_suspend_enable                                 |
|                                                                       |
| \**/                                                                  |
|                                                                       |
| os_printf("\\nCase 3: Disable then enable\\n");                       |
|                                                                       |
| os_printf("os_suspend disable 1x\\n");                                |
|                                                                       |
| disable_sleep();                                                      |
|                                                                       |
| os_printf("suspend_count: %d\\n", suspend_count);                     |
|                                                                       |
| os_sleep_us(5000000, OS_TIMEOUT_NO_WAKEUP);                           |
|                                                                       |
| /\*T2 will not go into low-power mode because we called               |
|                                                                       |
| os_suspend_disable before os_suspend_enable                           |
|                                                                       |
| \*/                                                                   |
|                                                                       |
| os_printf("os_suspend enable 1x\\n");                                 |
|                                                                       |
| enable_sleep();                                                       |
|                                                                       |
| os_printf("suspend_count: %d\\n", suspend_count);                     |
|                                                                       |
| os_sleep_us(5000000, OS_TIMEOUT_NO_WAKEUP);                           |
+=======================================================================+
+-----------------------------------------------------------------------+

Running the Application 
~~~~~~~~~~~~~~~~~~~~~~~~

Program sleep_enable_disable.elf
(sdk_x.y\\examples\\sleep_enable_disable\\bin) using the Download tool:

Launch the Download tool provided with InnoPhase Talaria TWO SDK.

In the GUI window:

1. Boot Target: Select the appropriate EVK from the drop-down

2. ELF Input: Load the sleep_enable_disable.elf by clicking on Select
   ELF File.

3. AP Options: Provide the SSID and Passphrase under AP Options to
   connect to an Access Point.

4. Programming: Prog RAM or Prog Flash as per requirement.

For more details on using the Download tool, refer to the document:
UG_Download_Tool.pdf (path: *sdk_x.y/pc_tools/Download_Tool/doc*).

**Note**: x and y refer to the SDK release version. For example:
sdk_2.4/doc.

Expected Output
~~~~~~~~~~~~~~~

sleep_enable_disable.elf is created when compiling the code which
provides the following console output when programmed to Talaria TWO.

+-----------------------------------------------------------------------+
| UART:SNWWWWWAEBuild $Id: git-ba65998b7 $                              |
|                                                                       |
| np_conf_path=/data/nprofile.json ssid=InnoPhase passphrase=43083191   |
|                                                                       |
| $App:git-73e7f910                                                     |
|                                                                       |
| SDK Ver: sdk_2.5                                                      |
|                                                                       |
| Sleep Enable Disable App                                              |
|                                                                       |
| addr e0:69:3a:00:13:90                                                |
|                                                                       |
| [2.099,560] CONNECT:00:5f:67:cd:c5:a6 Channel:11 rssi:-46 dBm         |
|                                                                       |
| wcm_notify_cb to App Layer - WCM_NOTIFY_MSG_LINK_UP                   |
|                                                                       |
| wcm_notify_cb to App Layer - WCM_NOTIFY_MSG_ADDRESS                   |
|                                                                       |
| [3.009,283] MYIP 192.168.0.104                                        |
|                                                                       |
| [3.009,330] IPv6 [fe80::e269:3aff:fe00:1390]-link                     |
|                                                                       |
| [3.009,394] IPv6 [2406:7400:63:5c3:e269:3aff:fe00:1390]               |
|                                                                       |
| Case 1: Enable then disable                                           |
|                                                                       |
| os_suspend enable 1x                                                  |
|                                                                       |
| suspend_count: 1                                                      |
|                                                                       |
| os_suspend disable 1x                                                 |
|                                                                       |
| suspend_count: 0                                                      |
|                                                                       |
| Case 2: Enable 2x then disable 1x                                     |
|                                                                       |
| os_suspend enable 2x                                                  |
|                                                                       |
| suspend_count: 2                                                      |
|                                                                       |
| os_suspend disable 1x                                                 |
|                                                                       |
| suspend_count: 1                                                      |
|                                                                       |
| os_suspend disable 1x                                                 |
|                                                                       |
| suspend_count: 0                                                      |
|                                                                       |
| Case 3: Disable then enable                                           |
|                                                                       |
| os_suspend disable 1x                                                 |
|                                                                       |
| suspend_count: -1                                                     |
|                                                                       |
| os_suspend enable 1x                                                  |
|                                                                       |
| suspend_count: 0                                                      |
+=======================================================================+
+-----------------------------------------------------------------------+
