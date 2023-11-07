Unassociated Mode
------------------------------

This application note describes the Wi-Fi Unassociated mode transmission
procedure. The WCM APIs used in the accompanying sample code describes
scan parameters which can be set, power management configuration and
transmission of unassociated frames to the AP.

Topology
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Figure 1: Topology

Wi-Fi Unassociated Mode Functionalities
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Wi-Fi Unassociated mode contains functions for transmitting data
over the probe request frames without associating with an AP.

Following functionalities are achieved through these APIs:

1. Creating and destroying Wi-Fi interface

2. Initializing the default scan parameters

3. Disabling beacon reception

4. Setting power saving options

5. Wi-Fi probe transmission

Accompanying sample code provides more details on achieving some of the
listed functionalities.

Wi-Fi Unassociated Mode APIs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

wifi_if_create()
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Creates a Wi-Fi interface with the specified operation mode.

+-----------------------------------------------------------------------+
| struct wifi_net \*                                                    |
|                                                                       |
| wifi_if_create(enum wifi_opmode mode, const uint8_t \*hwaddr)         |
+=======================================================================+
+-----------------------------------------------------------------------+

1. mode: Interface operation mode as specified by wifi_opmode.

+-----------------------------------------------------------------------+
| enum wifi_opmode                                                      |
|                                                                       |
| {                                                                     |
|                                                                       |
| WIFI_MODE_STA,                                                        |
|                                                                       |
| WIFI_MODE_P2P,                                                        |
|                                                                       |
| WIFI_MODE_HOSTAP,                                                     |
|                                                                       |
| WIFI_MODE_MONITOR,                                                    |
|                                                                       |
| WIFI_MODE_SCAN                                                        |
|                                                                       |
| }                                                                     |
+=======================================================================+
+-----------------------------------------------------------------------+

2. hwaddr: Specifies the hardware MAC address to be used for this
   interface. This parameter is NULL (or points to an invalid station
   MAC address) and a random address will be generated for the
   interface.

Returns pointer to the newly created interface in the form of wifi_net.

wifi_if_destroy()
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Destroys a Wi-Fi interface.

+-----------------------------------------------------------------------+
| void                                                                  |
|                                                                       |
| wifi_if_destroy(struct wifi_net \*net)                                |
+=======================================================================+
+-----------------------------------------------------------------------+

1. net: Pointer to a struct wifi_net created by wifi_if_create() API.

Returns void.

wifi_init_scan_default()
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Initializes the scan parameters with default values.

+-----------------------------------------------------------------------+
| void wifi_init_scan_default(struct wifi_scan_param \*param)           |
+=======================================================================+
+-----------------------------------------------------------------------+

1. param: pointer to the Wi-Fi scan param structure.

Returns void.

wifi_ssid_from_bytes()
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Initializes SSID from a byte string.

+-----------------------------------------------------------------------+
| int wifi_ssid_from_bytes(struct wifi_ssid \*ssid, const void          |
| \*ssid_bytes, size_t ssid_length)                                     |
+=======================================================================+
+-----------------------------------------------------------------------+

This function initializes a SSID structure from a byte string. SSID is a
sequence of bytes, not always representable as a zero terminated string.
This function will always generate a zero-terminated result but treating
it as such will cause problems with SSID's having embedded zero bytes
(although this is uncommon). If the input byte sequence is too long
(more than IEEE80211_NWID_LEN bytes), this function will truncate the
value, and return a negative result.

1. ssid: ssid structure to initialize.

2. ssid_bytes: pointer to SSID data.

3. ssid_length: length of ssid_bytes.

Returns zero on success -EINVAL ssid_length exceeds IEEE80211_NWID_LEN.

wifi_set_pm()
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Configures Wi-Fi power-save parameters.

+-----------------------------------------------------------------------+
| int wifi_pm_flags                                                     |
|                                                                       |
| wifi_set_pm(struct wifi_net \*net, uint32_t listen_interval, uint32_t |
| traffic_tmo, uint32_t pm_flags)                                       |
+=======================================================================+
+-----------------------------------------------------------------------+

Initiate a network scan procedure on the specified WCM interface.

1. struct wifi_net \*net: Pointer to wifi_net. This struct is
   representing a Wi-Fi network (or interface).

2. listen_interval: Beacon listen interval.

3. traffic_tmo: Traffic timeout in milliseconds. The traffic timeout
   parameter specifies the amount of time (in ms) for which the device
   should stay active.

4. pm_flags: Using this parameter, following flags can be enabled:

   -  WIFI_PM_PS_POLL

..

   Send ps poll if a beacon was missed.

-  WIFI_PM_DYN_LISTEN_INT

..

   Dynamic listen interval. Listen to each beacon if there has been
   traffic recently.

-  WIFI_PM_STA_RX_NAP

..

   Turn off receiver for uninteresting frames for station.

-  WIFI_PM_STA_ONLY_BROADCAST

..

   Do not receive multicast frames that are not broadcast.

-  WIFI_PM_TX_PS

..

   Send outgoing frames without leaving Wi-Fi power save.

-  WIFI_PM_MCAST_DONT_CARE

..

   Ignore the multicast flag in beacons. Incoming broadcast ARPs or
   other important broadcast/multicast traffic may be missed.

wifi_scan()
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Initiates a network scan procedure to send the unassociated frame (probe
request) on the specified Wi-Fi connection interface.

+-----------------------------------------------------------------------+
| int                                                                   |
|                                                                       |
| wifi_scan(struct wifi_net \*net, const struct wifi_scan_param         |
| \*param)                                                              |
+=======================================================================+
+-----------------------------------------------------------------------+

Initiate a network scan procedure.

1. struct wifi_net \*net: Pointer to wifi_net. This struct is
   representing a Wi-Fi network (or interface).

2. const struct wifi_scan_param \*param: Pointer to wifi_scan_param
   which contains multiple parameters that tunes the behavior of the
   scan operation.

..

   Returns zero on success, error value otherwise.

Details about struct wifi_scan_param and working of this API are
available in section 7.1.

States and Events of Unassociated Mode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Unassociated Tx Procedure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When the application thread calls the API wifi_scan(),the message to the
Wi-Fi stack is sent to start the scan (send probe request) with
programmed scan parameters.

struct wifi_scan_param contains multiple parameters that are used to
fine tune the behaviour of the scan operation.

+-----------------------------------------------------------------------+
| /\*\* Parametes for WiFi scan operaion \*/                            |
|                                                                       |
| struct wifi_scan_param {                                              |
|                                                                       |
| /\*\* List of channels to scan \*/                                    |
|                                                                       |
| uint8_t channel_mask[8];                                              |
|                                                                       |
| /\*\* Destination address and BSSID for probe requests \*/            |
|                                                                       |
| uint8_t bssid[IEEE80211_ADDR_LEN];                                    |
|                                                                       |
| /\*\* Rate to use for sending probe requests \*/                      |
|                                                                       |
| rate_t txrate;                                                        |
|                                                                       |
| /\*\* Scan for specific SSID (set to empty string for ANY). \*/       |
|                                                                       |
| struct wifi_ssid ssid;                                                |
|                                                                       |
| /\*\* The amount of time (in microseconds) to stay on the channel     |
| after                                                                 |
|                                                                       |
| transmitting the probe request and listening for responses \*/        |
|                                                                       |
| uint32_t dwelltime;                                                   |
|                                                                       |
| /\*\* Idle time between each channel (giving other parties access to  |
| the                                                                   |
|                                                                       |
| media) \*/                                                            |
|                                                                       |
| uint32_t waittime;                                                    |
|                                                                       |
| /\*\* Length of optional extra information elements included in the   |
| probe                                                                 |
|                                                                       |
| request frames \*/                                                    |
|                                                                       |
| size_t ie_len;                                                        |
|                                                                       |
| /\*\* Buffer with information elements that will be inserted in each  |
| probe                                                                 |
|                                                                       |
| request frame. \*/                                                    |
|                                                                       |
| uint8_t ie_list[0];                                                   |
|                                                                       |
| };                                                                    |
+=======================================================================+
+-----------------------------------------------------------------------+

wifi_init_scan_default()initiates wifi_scan_param structure which is
used when scan parameter is passed as NULL which has the following
default values:

1. Sending an unassociated frame for a specific SSID can be performed by
   initializing the SSID field. By default, it is empty and set for
   scanning any SSID.

2. Sending an unassociated frame for any specific channel can be done by
   initializing the channel mask. By default, it is set to 0xff and is
   set for all the channels.

3. By default, dwell-time is set to 25µs, wait time to 0 and no other
   additional information elements are included.

struct wifi_netinfo holds the results and information about scanned
networks. This parameter structure is not valid for the unassociated
mode.

Code Walkthrough
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Unassociated mode Tx Example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Overview
~~~~~~~~

The sample code in the path *example\\unassoc\\src\\main.c* showcases
the unassociated mode transmission.

Sample Code Walkthrough
~~~~~~~~~~~~~~~~~~~~~~~

This example code initializes the scan parameters as default. It also
gets the boot arguments and stores it in scan parameters.

+-----------------------------------------------------------------------+
| // Allocate memory for a @ref wifi_scan_param specifying the length   |
|                                                                       |
| of the ie_list                                                        |
|                                                                       |
| struct wifi_scan_param \*param = os_alloc(sizeof (struct              |
|                                                                       |
| wifi_scan_param) + ie_len);                                           |
|                                                                       |
| // Initiate the default scan param values                             |
|                                                                       |
| wifi_init_scan_default(param);                                        |
|                                                                       |
| // Update the ie_list                                                 |
|                                                                       |
| if(ie_len > 0) {                                                      |
|                                                                       |
| param->ie_len = ie_len;                                               |
|                                                                       |
| memcpy(param->ie_list, ie_list_output, ie_len);                       |
|                                                                       |
| }                                                                     |
|                                                                       |
| // Number of probes to send can be specified by the boot arg          |
|                                                                       |
| num_probes, 0 for infinity                                            |
|                                                                       |
| uint32_t num_probes = os_get_boot_arg_int("num_probes", 0);           |
|                                                                       |
| interval = os_get_boot_arg_int("interval_ms", 1000);                  |
|                                                                       |
| // Specify a target bssid, defaults to ANY                            |
|                                                                       |
| const char \*tmp;                                                     |
|                                                                       |
| tmp = os_get_boot_arg_str("addr");                                    |
|                                                                       |
| if (tmp)                                                              |
|                                                                       |
| parse_macaddr(tmp, param->bssid);                                     |
|                                                                       |
| // Specify the rate to send probes, generally 11b->11g (RATE_1 to     |
|                                                                       |
| RATE_6)                                                               |
|                                                                       |
| param->txrate = os_get_boot_arg_int("rate", RATE_6);                  |
|                                                                       |
| // Specify a target SSID, defaults to ANY                             |
|                                                                       |
| tmp = os_get_boot_arg_str("scan_ssid");                               |
|                                                                       |
| if (tmp)                                                              |
|                                                                       |
| wifi_ssid_from_bytes(&param->ssid, tmp, strlen(tmp));                 |
|                                                                       |
| // Enable device suspend (deep sleep) via boot argument               |
|                                                                       |
| bool suspend = os_get_boot_arg_int("suspend", 0);                     |
|                                                                       |
| if (suspend == 1) {                                                   |
|                                                                       |
| os_printf("deep sleep enabled.\\n");                                  |
|                                                                       |
| os_suspend_enable();                                                  |
|                                                                       |
| } else {                                                              |
|                                                                       |
| os_printf("deep sleep disabled.\\n");                                 |
|                                                                       |
| }                                                                     |
+=======================================================================+
+-----------------------------------------------------------------------+

The following code creates the Wi-Fi interface in scan mode. It also
sets the power management feature and sends unassociated frames in a
while loop.

+-----------------------------------------------------------------------+
| struct wifi_net \*net = wifi_if_create(WIFI_MODE_SCAN, NULL);         |
|                                                                       |
| // Set the shortest traffic_tmo and hope to go to suspend early       |
|                                                                       |
| wifi_set_pm(net, 0, 1, 0);                                            |
|                                                                       |
| uint32_t num_probe_sent = 0;                                          |
|                                                                       |
| callout_init(&probe_callout, send_unassoc_probe);                     |
|                                                                       |
| os_sem_init(&send_probe_sem, 0);                                      |
|                                                                       |
| for(;;) {                                                             |
|                                                                       |
| os_printf("[%u] Sending probe\\n", num_probe_sent);                   |
|                                                                       |
| int result = wifi_probe_send(net, param);                             |
|                                                                       |
| if(result == 0)                                                       |
|                                                                       |
| num_probe_sent++;                                                     |
|                                                                       |
| else                                                                  |
|                                                                       |
| os_printf("[%u] Failed to send probe due to error %d\\n",             |
|                                                                       |
| num_probe_sent, -result);                                             |
|                                                                       |
| start_timeout();                                                      |
|                                                                       |
| os_sem_wait(&send_probe_sem);                                         |
|                                                                       |
| if((num_probes != 0) &&                                               |
|                                                                       |
| (num_probes == num_probe_sent)) {                                     |
|                                                                       |
| os_printf("Probe sending complete.\\n");                              |
|                                                                       |
| break;                                                                |
|                                                                       |
| } }                                                                   |
|                                                                       |
| os_printf("Sent %d out of %d probes.\\n", num_probe_sent,             |
|                                                                       |
| num_probes);                                                          |
|                                                                       |
| wifi_if_destroy(net);                                                 |
|                                                                       |
| os_free(param);                                                       |
|                                                                       |
| while(1) {                                                            |
|                                                                       |
| os_sem_wait(&send_probe_sem);                                         |
|                                                                       |
| } }                                                                   |
+=======================================================================+
+-----------------------------------------------------------------------+

Running the Example
~~~~~~~~~~~~~~~~~~~

Program unassoc.elf *(freertos_sdk_x.y\\examples\\unassoc\\bin)* using
the Download tool:

1. Launch the Download tool provided with InnoPhase Talaria TWO SDK.

2. In the GUI window:

   a. Boot Target: Select the appropriate EVK from the drop-down.

   b. ELF Input: Load the unassoc.elf by clicking on Select ELF File.

   c. Boot Arguments: Pass the following boot arguments:

+-----------------------------------------------------------------------+
| scan_ssid=InnoPhase_AE_AP,ie_list=0x11:0x02:0x3                       |
| 3:0x44:0x12:0x04:0x77:0x88:0x99:0xaa:0x13:0x07:0xa0:0xa1:0xa2:0xa3:0x |
| a4:0xa5:0xa6,rate=0,num_probes=3,suspend=1,interval_ms=1500,verbose=1 |
+=======================================================================+
+-----------------------------------------------------------------------+

..

   **Note**: For one, two and three custom ies, refer the README file in
   the following location: *freertos_sdk_x.y\\examples\\unassoc\\doc*.

d. Programming: Click on Prog Flash.

Expected Output
~~~~~~~~~~~~~~~

unassoc.elf provides the following console output in different scenarios
when programmed to Talaria TWO.

+-----------------------------------------------------------------------+
| Y-BOOT 208ef13 2019-07-22 12:26:54 -0500 790da1-b-7                   |
|                                                                       |
| ROM yoda-h0-rom-16-0-gd5a8e586                                        |
|                                                                       |
| FLASH:PNWWWWWWAE                                                      |
|                                                                       |
| Build $Id: git-df9b9ef $                                              |
|                                                                       |
| Flash detected. flash.hw.uuid: 39483937-3207-00b0-0064-ffffffffffff   |
|                                                                       |
| Bootargs: scan_ssid=Lucy                                              |
| ie_list=0x11:0x02:0x33:0x44:0x12:                                     |
| 0x04:0x77:0x88:0x99:0xaa:0x13:0x07:0xa0:0xa1:0xa2:0xa3:0xa4:0xa5:0xa6 |
| rate=0 num_probes=3 suspend=1 interval_ms=1500 verbose=1              |
|                                                                       |
| $App:git-6600fea                                                      |
|                                                                       |
| SDK Ver: FREERTOS_SDK_1.0                                             |
|                                                                       |
| Un-Assoc Tx Example                                                   |
|                                                                       |
| ie_len=94                                                             |
|                                                                       |
| ie_len=19                                                             |
|                                                                       |
| Hexdump of IES, len=19                                                |
|                                                                       |
| 11 02 33 44 12 04 77 88 99 AA 13 07 A0 A1 A2 A3 \| ..3D..w.........   |
|                                                                       |
| A4 A5 A6 \| ...                                                       |
|                                                                       |
| Hexdump of ie tag:11, len=2                                           |
|                                                                       |
| 33 44 \| 3D                                                           |
|                                                                       |
| Hexdump of ie tag:12, len=4                                           |
|                                                                       |
| 77 88 99 AA \| w...                                                   |
|                                                                       |
| Hexdump of ie tag:13, len=7                                           |
|                                                                       |
| A0 A1 A2 A3 A4 A5 A6 \| .......                                       |
|                                                                       |
| deep sleep enabled.                                                   |
|                                                                       |
| [1] Sending probe.                                                    |
|                                                                       |
| [1] Probe completed.                                                  |
|                                                                       |
| [2] Sending probe.                                                    |
|                                                                       |
| [2] Probe completed.                                                  |
|                                                                       |
| [3] Sending probe.                                                    |
|                                                                       |
| [3] Probe completed.                                                  |
|                                                                       |
| Done sending probes!                                                  |
|                                                                       |
| Done                                                                  |
+=======================================================================+
+-----------------------------------------------------------------------+

Wireshark output in Figure 2 shows the 3 probe requests sent to
configured SSID for interval of 1500ms.

|image1|

Figure : Probe requests sent to configured SSID – Wireshark output

.. |image1| image:: media/image1.png
   :width: 6.29921in
   :height: 1.34808in
