Introduction 
=============

This application note describes the basics of the Low Power Wi-Fi scan
feature in InnoOS™ with an example illustrating Talaria TWO
implementation, using the provided data structs and API calls in the SDK
release.

System / API Functions
======================

SDK Provided Data Structures and Objects
----------------------------------------

.. table:: Table : SDK Provided Data Structures/Objects

   +-------------------+--------------------------------------------------+
   | **Data            | **Description**                                  |
   | S                 |                                                  |
   | tructure/Object** |                                                  |
   +===================+==================================================+
   | *struct           | Handle to the Wi-Fi connection manager. It is a  |
   | wcm_handle*       | pointer return from the API call wcm_create().   |
   +-------------------+--------------------------------------------------+
   | *struct           | Used to hold the properties of a Wi-Fi network   |
   | wifi_netinfo*     |                                                  |
   +-------------------+--------------------------------------------------+
   | *struct           | Used to hold the parameters for Wi-Fi scan       |
   | wifi_scan_param*  | operation.                                       |
   +-------------------+--------------------------------------------------+
   | *struct           | For the OS queue data                            |
   | os_workqueue*     |                                                  |
   +-------------------+--------------------------------------------------+

**Note**:

1. Wi-Fi data structures are declared in: SDK\\include\\wifi\\scan.h

2. struct os_workqueue is declared in: \\include\\kernel\\workqueue.h

API Functions
-------------

wcm_create()
~~~~~~~~~~~~

Create a Wi-Fi network interface and return a struct wcm_handle pointer

+-----------------------------------------------------------------------+
| static inline struct wcm_handle \*                                    |
|                                                                       |
| wcm_create(const uint8_t \*hwaddr)                                    |
|                                                                       |
| {                                                                     |
|                                                                       |
| ……                                                                    |
|                                                                       |
| }                                                                     |
+=======================================================================+
+-----------------------------------------------------------------------+

wifi_init_scan_default()
~~~~~~~~~~~~~~~~~~~~~~~~

Get the current Wi-Fi scan parameters.

+-----------------------------------------------------------------------+
| void                                                                  |
|                                                                       |
| wifi_init_scan_default(struct wifi_scan_param \*param);               |
+=======================================================================+
+-----------------------------------------------------------------------+

wifi_init_scan_default() is called to get the current Wi-Fi scan
parameters in the param of struct wifi_scan_param.

os_init_workqueue ()
~~~~~~~~~~~~~~~~~~~~

Initialize a work queue with an os_workqueue object.

+-----------------------------------------------------------------------+
| void os_init_workqueue(struct os_workqueue \*wq);                     |
+=======================================================================+
+-----------------------------------------------------------------------+

os_init_delayed_work()
~~~~~~~~~~~~~~~~~~~~~~

Initialize a work queue with an os_workqueue object with the delayed
occurrence for the next callout.

+-----------------------------------------------------------------------+
| int os_queue_delayed_work(struct os_delayed_work \*dw, struct         |
| os_workqueue \*wq, uint32_t expire);                                  |
+=======================================================================+
+-----------------------------------------------------------------------+

os_run_work()
~~~~~~~~~~~~~

Start the queue work with os_workqueue object.

+-----------------------------------------------------------------------+
| void os_run_work(struct os_workqueue \*wq);                           |
+=======================================================================+
+-----------------------------------------------------------------------+

wcm_scan()
~~~~~~~~~~

Perform the Wi-Fi scan with the parameter block. Results are contained
in the buffer pointed with the parameter wifi_netinfo \**result.

+-----------------------------------------------------------------------+
| int wcm_scan(struct wcm_handle \*h, const struct wifi_scan_param      |
| \*param, struct wifi_netinfo \**result, size_t max);                  |
+=======================================================================+
+-----------------------------------------------------------------------+

A Set of Wi-Fi Scan Related Data Retrieval
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A set of Wi-Fi scan related functions for retrieval of data from
wifi_netinfo.

+-----------------------------------------------------------------------+
| int wifi_netinfo_get_ssid(const struct wifi_netinfo\* ni, struct      |
| wifi_ssid\* ssid);                                                    |
|                                                                       |
| int wifi_netinfo_get_chan(const struct wifi_netinfo\* ni, uint8_t\*   |
| chan);                                                                |
|                                                                       |
| int wifi_netinfo_get_authmode(const struct wifi_netinfo\* ni,struct   |
| wifi_authmode\* authmode);                                            |
|                                                                       |
| size_t wifi_netinfo_authmode_tostr(uint32_t authmask, char\*          |
| mode_name, size_t size);                                              |
+=======================================================================+
+-----------------------------------------------------------------------+

Code Walkthrough 
=================

lpscan.c
--------

Overview
~~~~~~~~

The sample code is the path: examples/lpscan/src/lpscan.c is a simple
application which demonstrates the low power scan feature.

Sample Code Walkthrough 
~~~~~~~~~~~~~~~~~~~~~~~~

1. User-defined Data Struct for the Scan Work Task:

..

   Declare a data struct scan_workq_task for the scan work task:

+-----------------------------------------------------------------------+
| struct scan_workq_task {                                              |
|                                                                       |
| struct os_delayed_work dwork;                                         |
|                                                                       |
| struct os_workqueue wqueue;                                           |
|                                                                       |
| struct {                                                              |
|                                                                       |
| uint32_t counter;                                                     |
|                                                                       |
| size_t max_nets;                                                      |
|                                                                       |
| int sum_total;                                                        |
|                                                                       |
| struct wcm_handle \*h;                                                |
|                                                                       |
| const struct wifi_scan_param \*param;                                 |
|                                                                       |
| struct wifi_netinfo \**scan_result;                                   |
|                                                                       |
| }conf;                                                                |
|                                                                       |
| };                                                                    |
+=======================================================================+
+-----------------------------------------------------------------------+

2. Static Variables for the Scan Work Task

..

   Define the static variables for the scan feature:

+-----------------------------------------------------------------------+
| #define TIME_BETWEEN_SCAN_ITERS 10                                    |
|                                                                       |
| static bool ap_logging;                                               |
|                                                                       |
| static uint32_t num_iterations, dt_iterations;                        |
+=======================================================================+
+-----------------------------------------------------------------------+

3. Creation of Scan Work Control Object

..

   Use the SDK provided data struct scan_workq_task to create the scan
   work control:

+-----------------------------------------------------------------------+
| struct scan_workq_task \*sworkt;                                      |
|                                                                       |
| if (!sworkt)                                                          |
|                                                                       |
| return -1;                                                            |
+=======================================================================+
+-----------------------------------------------------------------------+

4. Initialization of the Static Variables for the Scan Work Task:

..

   The app initializes the static variables from the boot arguments:

+-----------------------------------------------------------------------+
| ap_logging = os_get_boot_arg_int("ap_logging", 0);                    |
|                                                                       |
| //0 means infinity                                                    |
|                                                                       |
| num_iterations = os_get_boot_arg_int("num_iterations", 0);            |
|                                                                       |
| //time between iterations (in seconds)                                |
|                                                                       |
| dt_iterations = os_get_boot_arg_int("dt_iterations",                  |
| TIME_BETWEEN_SCAN_ITERS);                                             |
|                                                                       |
| assert(dt_iterations >= 5);                                           |
+=======================================================================+
+-----------------------------------------------------------------------+

5. Creation of WCM Object for the Wi-Fi Interface

..

   In the following code, a Wi-Fi handle is created. The NULL parameter
   in the wcm_create() specifies that no user-specified MAC address is
   used, and the MAC address in the flash will be used to create the
   Wi-Fi interface.

+-----------------------------------------------------------------------+
| h = wcm_create(NULL);                                                 |
|                                                                       |
| assert(h != NULL}                                                     |
+=======================================================================+
+-----------------------------------------------------------------------+

6. Creation of Local Data for Wi-Fi Scan Results

..

   Use the SDK provided data struct wifi_netinfo as the data object for
   the scan results. This is the scan result data container that will be
   populated by the scan_workq_task.

+-----------------------------------------------------------------------+
| struct wifi_netinfo \**scan_result;                                   |
|                                                                       |
| scan_result = os_alloc(max_nets \* sizeof(void \*));                  |
|                                                                       |
| assert(scan_result != NULL);                                          |
+=======================================================================+
+-----------------------------------------------------------------------+

7. Set-up of Wi-Fi Scan Parameter Block

..

   Use the SDK provided data struct wifi_scan_param to retrieve the
   default values for the Wi-Fi scan task from SDK in the param, get the
   user-entry values from the bootargs, convert the values for format,
   and populate the param with the new values for the scan task.

+-----------------------------------------------------------------------+
| struct wifi_scan_param param;                                         |
|                                                                       |
| wifi_init_scan_default(&param);                                       |
|                                                                       |
| uint32_t channel_mask = os_get_boot_arg_int("wifi.scan_channel_mask", |
| 0xffffffff);                                                          |
|                                                                       |
| memset(param.channel_mask, 0, sizeof(param.channel_mask));            |
|                                                                       |
| memcpy(&param.channel_mask, &channel_mask, sizeof(channel_mask));     |
|                                                                       |
| tmp = os_get_boot_arg_str("addr");                                    |
|                                                                       |
| if (tmp)                                                              |
|                                                                       |
| parse_macaddr(tmp, param.bssid);                                      |
|                                                                       |
| param.txrate = os_get_boot_arg_int("rate", RATE_6);                   |
|                                                                       |
| tmp = os_get_boot_arg_str("scan_ssid");                               |
|                                                                       |
| if (tmp)                                                              |
|                                                                       |
| wifi_ssid_from_bytes(&param.ssid, tmp, strlen(tmp));                  |
|                                                                       |
| max_listen_time = os_get_boot_arg_int("wifi.scan_max_listen_time",    |
| param.max_listen_time/SYSTIME_MS(1));                                 |
|                                                                       |
| min_listen_time = os_get_boot_arg_int("wifi.scan_min_listen_time",    |
| param.min_listen_time/SYSTIME_MS(1));                                 |
|                                                                       |
| wait_time = os_get_boot_arg_int("wifi.scan_wait_time",                |
| param.wait_time/SYSTIME_MS(1));                                       |
|                                                                       |
| probe_tx_timeout= os_get_boot_arg_int("wifi.scan_probe_tx_timeout",   |
| param.probe_tx_timeout/SYSTIME_MS(1));                                |
|                                                                       |
| param.min_listen_time = SYSTIME_MS(min_listen_time);                  |
|                                                                       |
| param.max_listen_time = SYSTIME_MS(max_listen_time);                  |
|                                                                       |
| param.wait_time = SYSTIME_MS(wait_time);                              |
|                                                                       |
| param.probe_tx_timeout= SYSTIME_MS(probe_tx_timeout);                 |
|                                                                       |
| param.num_probes = os_get_boot_arg_int("wifi.scan_num_probes",        |
| param.num_probes);                                                    |
|                                                                       |
| param.idleslots = os_get_boot_arg_int("wifi.scan_idleslots",          |
| param.idleslots);                                                     |
|                                                                       |
| param.max_responses = os_get_boot_arg_int("wifi.scan_max_responses",  |
| param.max_responses);                                                 |
+=======================================================================+
+-----------------------------------------------------------------------+

8. Setup for the Suspend Mode Enable

+-----------------------------------------------------------------------+
| /\* Enable device suspend (deep sleep) via boot argument \*/          |
|                                                                       |
| if (os_get_boot_arg_int("suspend", 1) != 0)                           |
|                                                                       |
| os_suspend_enable();                                                  |
+=======================================================================+
+-----------------------------------------------------------------------+

9. Setup of the Scan Work Control Block

..

   Populate the Scan work control block sworkt with the parameter block
   and the scan result object:

+-----------------------------------------------------------------------+
| //set up confs                                                        |
|                                                                       |
| sworkt->conf.counter = 0;                                             |
|                                                                       |
| sworkt->conf.max_nets = max_nets;                                     |
|                                                                       |
| sworkt->conf.h = h;                                                   |
|                                                                       |
| sworkt->conf.param = &param;                                          |
|                                                                       |
| sworkt->conf.scan_result = scan_result;                               |
+=======================================================================+
+-----------------------------------------------------------------------+

10. Initialization of Work Queue and Start of Work

..

   Set up and start the work queue for the scan work:

+-----------------------------------------------------------------------+
| //initialize                                                          |
|                                                                       |
| os_init_workqueue(&sworkt->wqueue);                                   |
|                                                                       |
| os_init_delayed_work(&sworkt->dwork, scan_work_clbk);                 |
|                                                                       |
| os_queue_delayed_work(&sworkt->dwork, &sworkt->wqueue,                |
| os_systime()+SYSTIME_MS(10));                                         |
|                                                                       |
| os_run_work(&sworkt->wqueue);                                         |
+=======================================================================+
+-----------------------------------------------------------------------+

11. Definition of Scan Callback Function scan_work_clbk()

..

   The callback function scan_work_clbk() is called every timeout of the
   interval that is specified with dt_iterations.

+-----------------------------------------------------------------------+
| static void                                                           |
|                                                                       |
| scan_work_clbk(struct os_work \*w)                                    |
|                                                                       |
| {                                                                     |
|                                                                       |
| struct scan_workq_task \*twork = container_of(w, struct               |
| scan_workq_task, dwork.work);                                         |
|                                                                       |
| int num_ap_found;                                                     |
|                                                                       |
| uint32_t next_tmo = os_systime() + SYSTIME_SEC(dt_iterations);        |
|                                                                       |
| twork->conf.counter++;                                                |
|                                                                       |
| num_ap_found = wcm_scan(twork->conf.h,                                |
|                                                                       |
| twork->conf.param,                                                    |
|                                                                       |
| twork->conf.scan_result,                                              |
|                                                                       |
| twork->conf.max_nets);                                                |
|                                                                       |
| pr_always("Round:%u Found %d nets:\\n",                               |
|                                                                       |
| twork->conf.counter, num_ap_found);                                   |
|                                                                       |
| /\*                                                                   |
|                                                                       |
| More code …                                                           |
|                                                                       |
| \*/                                                                   |
|                                                                       |
| //reschedule                                                          |
|                                                                       |
| os_queue_delayed_work(&twork->dwork, &twork->wqueue, next_tmo);       |
|                                                                       |
| }                                                                     |
+=======================================================================+
+-----------------------------------------------------------------------+

..

   The callback function is registered with the system by the statement:

+-----------------------------------------------------------------------+
| //initialize                                                          |
|                                                                       |
| ……;                                                                   |
|                                                                       |
| os_init_delayed_work(&sworkt->dwork, scan_work_clbk);                 |
|                                                                       |
| ……;                                                                   |
+=======================================================================+
+-----------------------------------------------------------------------+

12. Display of the Scan Results

..

   Under the set of the ap_logging flag, the data list from the scan
   work is populated with API calls.

+-----------------------------------------------------------------------+
| if (ap_logging) {                                                     |
|                                                                       |
| for (int i = 0; i < num_ap_found; i++) {                              |
|                                                                       |
| uint8_t chan;                                                         |
|                                                                       |
| char mode_name[64];                                                   |
|                                                                       |
| struct wifi_ssid ssid;                                                |
|                                                                       |
| struct wifi_authmode authmode;                                        |
|                                                                       |
| wifi_netinfo_get_ssid(twork->conf.scan_result[i], &ssid);             |
|                                                                       |
| wifi_netinfo_get_chan(twork->conf.scan_result[i], &chan);             |
|                                                                       |
| wifi_netinfo_get_authmode(twork->conf.scan_result[i], &authmode);     |
|                                                                       |
| wifi_netinfo_authmode_tostr(authmode.authmask, mode_name, 64);        |
|                                                                       |
| pr_always("%6pM on channel %2d @ %3d '%s' '%s'\\n",                   |
|                                                                       |
| twork->conf.scan_result[i]->ni_bssid,                                 |
|                                                                       |
| chan,                                                                 |
|                                                                       |
| twork->conf.scan_result[i]->ni_rssi,                                  |
|                                                                       |
| ssid.ws_ssid,                                                         |
|                                                                       |
| mode_name );                                                          |
|                                                                       |
| }                                                                     |
|                                                                       |
| }                                                                     |
|                                                                       |
| wcm_free_scanresult(twork->conf.scan_result, num_ap_found);           |
+=======================================================================+
+-----------------------------------------------------------------------+

Running the Application 
~~~~~~~~~~~~~~~~~~~~~~~~

Program lpscan.elf (sdk_x.y\\examples\\lp_scan\\bin) using the Download
tool:

1. Launch the Download tool provided with InnoPhase Talaria TWO SDK.

2. In the GUI window:

   a. Boot Target: Select the appropriate EVK from the drop-down

   b. ELF Input: Load the lpscan.elf by clicking on Select ELF File.

   c. Boot arguments: Pass the following boot arguments:

+-----------------------------------------------------------------------+
| wifi.scan_min_listen_time=8, wifi.scan_max_listen_time=24,            |
| wifi.scan_num_probes=1, wifi.scan_idleslots=3, wifi.nap_scan=1,       |
| dt_iterations=10, ap_logging=1, suspend=1                             |
+=======================================================================+
+-----------------------------------------------------------------------+

d. Programming: Prog RAM or Prog Flash as per requirement.

For more details on using the Download tool, refer to the document:
UG_Download_Tool.pdf (path: *sdk_x.y/pc_tools/Download_Tool/doc*).

**Note**: x and y refer to the SDK release version. For example:
sdk_2.4/doc.

Expected Output
~~~~~~~~~~~~~~~

lpscan.elf is created when compiling the code which provides the
following console output when programmed to Talaria TWO:

**Note**: The following console output is from SDK 2.3 release and is
applicable to the current release as well.

+-----------------------------------------------------------------------+
| UART:NWWWWAEBuild $Patch: git-5e70acd25 $ $Id: git-c74d301bc $        |
|                                                                       |
| app=gordon                                                            |
|                                                                       |
| flash: Gordon ready!                                                  |
|                                                                       |
| Y-BOOT 208ef13 2019-07-22 12:26:54 -0500 790da1-b-7                   |
|                                                                       |
| ROM yoda-h0-rom-16-0-gd5a8e586                                        |
|                                                                       |
| FLASH:PNWWWWWWAEBuild $Id: git-f92bee540 $                            |
|                                                                       |
| wifi.scan_min_listen_time=8 wifi.scan_max_listen_time=24              |
| wifi.scan_num_probes=1 wifi.scan_idleslots=3 wifi.nap_scan=1          |
| dt_iterations=10 ap_logging=1 suspend=1                               |
|                                                                       |
| addr 02:03:04:66:f4:63                                                |
|                                                                       |
| [0.566,075] Round:1 Found 12 nets:                                    |
|                                                                       |
| -------------------------                                             |
|                                                                       |
| [0.566,503] ac:9e:17:45:fc:28 on channel 8 @ -36 'Asus_AC87U'         |
| 'WPA2-PSK+PMF'                                                        |
|                                                                       |
| [0.566,726] 10:c3:7b:52:6b:c8 on channel 11 @ -39 'dtim100'           |
| 'WPA2-PSK+PMF'                                                        |
|                                                                       |
| [0.566,946] f6:c3:2a:92:3a:fa on channel 6 @ -40 '' 'WPA2-PSK'        |
|                                                                       |
| [0.567,083] 00:24:a5:f1:8c:9e on channel 10 @ -45 'IP006'             |
| 'WPA-PSK/WPA2-PSK Mixed Mode'                                         |
|                                                                       |
| [0.567,199] 74:da:88:a9:02:dd on channel 4 @ -46 'TPLinkC3'           |
| 'WPA2-PSK'                                                            |
|                                                                       |
| [0.567,310] ec:41:18:1a:d5:05 on channel 13 @ -46 'IP014' 'WPA2-PSK'  |
|                                                                       |
| [0.567,423] 28:80:88:28:4c:d2 on channel 1 @ -48 'NGR8000_1'          |
| 'WPA2-PSK+PMF'                                                        |
|                                                                       |
| [0.567,533] 8c:fe:74:35:40:a8 on channel 6 @ -54 'RuckusR500'         |
| 'WPA2-PSK'                                                            |
|                                                                       |
| [0.567,670] bc:54:fc:c7:1c:8c on channel 8 @ -57 'IP011'              |
| 'WPA-PSK/WPA2-PSK Mixed Mode'                                         |
|                                                                       |
| [0.567,789] 14:d6:4d:25:67:b2 on channel 2 @ -57 'dlink' 'WPA2-PSK'   |
|                                                                       |
| [0.567,896] d0:ae:ec:99:97:fc on channel 12 @ -57 '360cn' 'WPA2-PSK'  |
|                                                                       |
| [0.568,339] 08:9b:b9:3d:1d:14 on channel 1 @ -65 'ATTsyYY4SQ'         |
| 'WPA2-PSK+PMF'                                                        |
|                                                                       |
| [10.600,973] Round:2 Found 10 nets:                                   |
|                                                                       |
| -------------------------                                             |
|                                                                       |
| [10.601,061] 04:d4:c4:3e:74:88 on channel 6 @ -36 'AsusC3'            |
| 'WPA2-PSK+PMF'                                                        |
|                                                                       |
| [10.601,174] 10:c3:7b:52:6b:c8 on channel 11 @ -38 'dtim100'          |
| 'WPA2-PSK+PMF'                                                        |
|                                                                       |
| [10.601,290] 3c:7c:3f:62:5f:f8 on channel 6 @ -39 'AsusC4'            |
| 'WPA2-PSK+PMF'                                                        |
|                                                                       |
| [10.601,403] e4:c3:2a:92:3a:fa on channel 6 @ -40 'TPLinkC4'          |
| 'WPA2-PSK'                                                            |
|                                                                       |
| [10.601,843] 86:da:88:a9:02:dd on channel 4 @ -43 '' 'WPA2-PSKip'     |
| 'WPA2-PSK+PMF'                                                        |
|                                                                       |
| [10.603,544] d0:ae:ec:99:97:fc on channel 12 @ -58 '360cn' 'WPA2-PSK' |
|                                                                       |
| [10.603,681] bc:54:fc:c7:1c:8c on channel 8 @ -59 'IP011'             |
| 'WPA-PSK/WPA2-PSK Mixed Mode'                                         |
|                                                                       |
| [10.603,795] 84:82:f4:35:f5:58 on channel 13 @ -61 'IP021' 'WPA2-PSK' |
|                                                                       |
| [10.604,019] 08:9b:b9:3d:1d:14 on channel 1 @ -63 'ATTsyYY4SQ'        |
| 'WPA2-PSK+PMF'                                                        |
|                                                                       |
| [10.604,243] 14:1f:ba:7a:30:04 on channel 11 @ -66                    |
| 'NVR-2.4G_2M024D2PAZ00916' 'WPA2-PSK'                                 |
+=======================================================================+
+-----------------------------------------------------------------------+
