WCM Multi AP
-------------------------


This application note demonstrates the wcm_multi_ap example which
performs the connection and disconnections with multiple access points
based on the priority of the access point. The priority of the access
point to connect to is set by the application based on the order that
the SSID and passphrase details of the access point are provided through
the boot arguments and also on the Access Point's entry in Talaria TWO’s
scan results.

Wi-Fi Connection with Multi-AP Functionalities
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Overview of wcm_multi_ap
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

wcm_multi_ap takes user entry for APs (SSID and passphrase) the priority
of which is decided depending on the order of the provided AP details,
in the form of boot arguments. It utilizes the functionalities provided
by WCM on the Wi-Fi connection management and provides the following
features:

1. Configuration and management of user-entered, multiple APs.

2. Priority-oriented list for AP connection choice.

Overview of WCM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Wi-Fi connection manager (WCM) contains functions for establishing
and tearing down associations to Wi-Fi access points. It initiates a
four-way handshake for encrypted connections and starts the DHCP client
from LWIP for getting an allocation of the IP address.

Following functionalities are achieved through these APIs:

1. Creating and destroying interfaces.

2. Scanning with different scan parameters and their indication
   structure.

3. Connecting and disconnecting.

4. Adding network to connect asynchronously and removing network.

5. Querying connection information.

Accompanying sample code provides more details on how to achieve some of
the listed functionalities.

 WCM APIs used in wcm_multi_ap
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. wcm_auto_connect() - Starts or stops auto connect.

..

   A network must first be added with reference to wcm_add_network.

2. wcm_delete_network_profile () - Deletes the currently active network
   profile that was previously added.

3. wifi_init_scan_default() - Gets the default parameters for scan
   operation.

..

   The wifi_scan_param will be updated with the default values for the
   scan operation. This function is used to get the default values and
   alter the parameters which need to have values other than the default
   ones. Finally, provide this parameter when calling wcm_scan.

4. wifi_netinfo_get_ssid() - Gets SSID from netinfo.

5. wifi_netinfo_get_chan() - Gets channel from netinfo

6. wcm_free_scanresult() - Frees the memory allocated by wcm_scan

7. osal_free() - Frees allocated memory.

..

   Returns allocated memory to the heap. If the memory has more than one
   reference, the count is simply dropped by one.

8. os_msg_release() - Frees an allocated message.

..

   Frees a message previously allocated using os_msg_alloc().

9. wcm_scan() - Scans for Wi-Fi networks.

..

   Initiates a network scan procedure on the specified Wi-Fi Connection
   Manager interface.

10. Wcm_create() - Creates a Wi-Fi network interface.

..

   Only one wcm_handle instance is supported at the time of writing

11. wcm_add_network_profile() - Adds a network profile to wcm.

Code Walkthrough WCM_MULTI_AP
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Application Flow
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When the app starts, the following sequence of initializations happens
in wcm_multi_ap:

1. User provides the boot arguments consisting of a list of AP entries
   in the form of SSID and the passphrase for each AP. The order of the
   AP as they are entered indicates the priority of the connection.

2. App reads the boot arguments and saves them into the buffer - AP
   manager.

3. App starts a thread with the following functionality:

   a. Create a Wi-Fi network interface.

   b. Pass to the WCM, the list of user-entered SSID’s.

   c. Register the call-back function with the WCM notification.

   d. Start a connection with the most recently used or most recently
      added AP in the list.

4. Enters the loop with the detection for reconnection.

Sample code walkthrough
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. User Data Struct: AP Manager

..

   A user-defined data struct is created to store the data of the multi
   APs:

+-----------------------------------------------------------------------+
| #define AP_CNT 5                                                      |
|                                                                       |
| #define MAX_RETRY 3                                                   |
|                                                                       |
| #define MRU_RETRY 3                                                   |
|                                                                       |
| #define MAX_NETS 16                                                   |
|                                                                       |
| #define AP_DISCONNECTED 0                                             |
|                                                                       |
| #define AP_CONNECTED 1                                                |
|                                                                       |
| #define AP_CONNECTING 2                                               |
|                                                                       |
| struct ap_param                                                       |
|                                                                       |
| {                                                                     |
|                                                                       |
| char ssid[32];                                                        |
|                                                                       |
| uint8_t bssid[6];                                                     |
|                                                                       |
| char passphrase[64];                                                  |
|                                                                       |
| };                                                                    |
|                                                                       |
| struct ap_manager                                                     |
|                                                                       |
| {                                                                     |
|                                                                       |
| struct ap_param ap_param[AP_CNT];                                     |
|                                                                       |
| int priority[AP_CNT];                                                 |
|                                                                       |
| int mru; //index of MRU AP                                            |
|                                                                       |
| int rescan_interval;                                                  |
|                                                                       |
| int cnt;                                                              |
|                                                                       |
| int index;                                                            |
|                                                                       |
| int mru_retries;                                                      |
|                                                                       |
| int connect_retries;                                                  |
|                                                                       |
| } ap_manager;                                                         |
+=======================================================================+
+-----------------------------------------------------------------------+

2. How the AP List is Created and Maintained

..

   When the AP manager is populated with a list of SSID from the boot
   arguments, the AP manager starts to use the AP’s order as the initial
   priority order (in ascending order) of selection for Wi-Fi connection
   with the AP of the highest number (number 0) as the starting
   connection.

a. AP Addition and Initialization of the List

..

   The priority variable is initialized with the order of the AP in the
   function wcma_add_network().

+-----------------------------------------------------------------------+
| int wcma_add_network(struct wcm_handle \*handle, const char           |
| ssid[32],const char bssid[17], const char passphrase[64], struct      |
| ap_manager \*manager)                                                 |
|                                                                       |
| .                                                                     |
|                                                                       |
| .                                                                     |
|                                                                       |
| for(int i = 0; i < AP_CNT; i++)                                       |
|                                                                       |
| {                                                                     |
|                                                                       |
| if(manager->ap_param[i].ssid[0] == 0)                                 |
|                                                                       |
| {                                                                     |
|                                                                       |
| os_printf("adding %s to list\\n", ssid);                              |
|                                                                       |
| memcpy(manager->ap_param[i].ssid, ssid, ssid_len);                    |
|                                                                       |
| if(bssid != NULL)                                                     |
|                                                                       |
| {                                                                     |
|                                                                       |
| os_printf("BSSID: %s\\n", bssid);                                     |
|                                                                       |
| parse_macaddr(bssid, manager->ap_param[i].bssid);                     |
|                                                                       |
| }                                                                     |
|                                                                       |
| else                                                                  |
|                                                                       |
| {                                                                     |
|                                                                       |
| memset(manager->ap_param[i].bssid, 0, 6);                             |
|                                                                       |
| }                                                                     |
+=======================================================================+
+-----------------------------------------------------------------------+

3. Update of the Priority Numbers of APs

The priority order of the AP determines which AP from the AP list will
be chosen for the next connection to be made. This list is managed
automatically by the app.

The order of APs can be changed from time to time. For instance, based
on the change of status of the connection with the current AP, if the
connection gets dropped , the AP manager will attempt to connect to the
AP that is next on the priority list. The priority list of APs in the AP
manager will be updated accordingly in the manager based on the index
variable value.

+-----------------------------------------------------------------------+
| /\* perform scan \*/                                                  |
|                                                                       |
| wcma_scan_retry(handle, 3, manager);                                  |
|                                                                       |
| /\* get AP with highest priority \*/                                  |
|                                                                       |
| int highest_priority = manager->cnt+1;                                |
|                                                                       |
| manager->index = -1;                                                  |
|                                                                       |
| for(int i = 0; i < manager->cnt; i++)                                 |
|                                                                       |
| {                                                                     |
|                                                                       |
| if((manager->priority[i] >=0) && (manager->priority[i] <              |
| highest_priority))                                                    |
|                                                                       |
| {                                                                     |
|                                                                       |
| highest_priority = manager->priority[i];                              |
|                                                                       |
| manager->index = i;                                                   |
|                                                                       |
| }                                                                     |
|                                                                       |
| }                                                                     |
+=======================================================================+
+-----------------------------------------------------------------------+

4. Last Used Entry (LRU)

..

   AP manager uses the ap_mamager,mru variable as the index of LRU AP.

+-----------------------------------------------------------------------+
| static void my_wcm_notify_cb(void \*ctx, struct os_msg \*msg)         |
|                                                                       |
| {                                                                     |
|                                                                       |
| switch(msg->msg_type)                                                 |
|                                                                       |
| .                                                                     |
|                                                                       |
| .                                                                     |
|                                                                       |
| {                                                                     |
|                                                                       |
| case(WCM_NOTIFY_MSG_ADDRESS):                                         |
|                                                                       |
| os_printf("wcm_notify_cb to App Layer - WCM_NOTIFY_MSG_ADDRESS\\n");  |
|                                                                       |
| // set most recently used AP and updated priority in list             |
|                                                                       |
| ap_manager.mru = ap_manager.index;                                    |
|                                                                       |
| ap_manager.priority[ap_manager.index] = 0;                            |
|                                                                       |
| ap_manager.connect_retries = 0;                                       |
|                                                                       |
| ap_manager.mru_retries = MRU_RETRY;                                   |
|                                                                       |
| connection_status = AP_CONNECTED;                                     |
|                                                                       |
| last_connect_time = os_systime();                                     |
|                                                                       |
| break;                                                                |
+=======================================================================+
+-----------------------------------------------------------------------+

It is set when the call-back from WCM is received indicating that the
connection to the AP has been made. It is used to set the AP entry as
the AP to connect to.

5. Selection of AP to Connect to

..

   The selection for an AP to connect to is decided based on the index
   and mru variable values in the AP manager:

a. ap_manager: index contains the index to the AP that the next
   connection will be made to.

b. ap_manager: mru contains the index to the entry of used last time, or
   the retry attempts.

+-----------------------------------------------------------------------+
| void wcma_auto_connect(struct wcm_handle \*handle, struct ap_manager  |
| \*manager)                                                            |
|                                                                       |
| {                                                                     |
|                                                                       |
| reconnect_next_ap = false;                                            |
|                                                                       |
| last_disconnect_time = 0xFFFFFFFF;                                    |
|                                                                       |
| if(manager->cnt > 0)                                                  |
|                                                                       |
| {                                                                     |
|                                                                       |
| if((manager->mru >= 0) && manager->mru_retries >= 0)                  |
|                                                                       |
| {                                                                     |
|                                                                       |
| os_printf("connecting to most recently used AP, SSID: %s PASS:        |
| %s\\n", manager->ap_param[manager->mru].ssid,                         |
| manager->ap_param[manager->mru].passphrase);                          |
|                                                                       |
| if(manager->ap_param[manager->mru].passphrase[0] == 0)                |
|                                                                       |
| {                                                                     |
|                                                                       |
| rval = network_profile_new_from_ssid_bssid_pw(&profile,               |
| manager->ap_param[manager->mru].ssid, NULL, NULL);                    |
+=======================================================================+
+-----------------------------------------------------------------------+

..

   wcm_add_network_profile()API is used to add the network.

+-----------------------------------------------------------------------+
| if (rval < 0) {                                                       |
|                                                                       |
| pr_err("could not create network profile %d\\n", rval);               |
|                                                                       |
| return 0;                                                             |
|                                                                       |
| }                                                                     |
|                                                                       |
| add_ntwk = wcm_add_network_profile(handle, profile);                  |
|                                                                       |
| }                                                                     |
|                                                                       |
| else if(manager->ap_param[manager->mru].bssid[0] != 0)                |
|                                                                       |
| {                                                                     |
|                                                                       |
| rval =                                                                |
| network_profile_                                                      |
| new_from_ssid_bssid_pw(&profile,manager->ap_param[manager->mru].ssid, |
| (uint8_t \*)manager->ap_param[manager->mru].bssid,                    |
| manager->ap_param[manager->mru].passphrase);                          |
+=======================================================================+
+-----------------------------------------------------------------------+

Running the Application
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Program wcma.elf *(freertos_sdk_x.y\\examples\\wcm_multi_ap\\bin)* using
the Download tool:

1. Launch the Download tool provided with InnoPhase Talaria TWO FreeRTOS
   SDK.

2. In the GUI window:

   a. Boot Target: Select the appropriate EVK from the drop-down

   b. ELF Input: Load the wcma.elf by clicking on Select ELF File.

   c. Boot arguments: Pass the following boot arguments:

+-----------------------------------------------------------------------+
| hssid1=Asus_Qos_2G,passphrase1=99999999,ssid2=                        |
| manasvi,passphrase2=manasvi123,hssid3=TP-Link_2G,passphrase3=12345678 |
+=======================================================================+
+-----------------------------------------------------------------------+

d. Programming: Prog RAM or Prog Flash as per requirement.

Expected Output
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

wcma.elf is created when compiling this code and gives the following
console output when programmed to Talaria TWO.

Initially, the Talaria TWO app connects with the AP mentioned in
“ssid1”. If the AP with “ssid1” goes down, then the Talaria TWO app
retries to reconnect with the same, after which it connects with the
next in the list “ssid2”.

If AP is in hidden network, SSID should be mentioned as “hssid1” and
passphrase as “hpassphrase1”.

+-----------------------------------------------------------------------+
| UART:SNWWWWAE                                                         |
|                                                                       |
| 4 DWT comparators, range 0x8000                                       |
|                                                                       |
| Build $Id: git-8bc43d639 $                                            |
|                                                                       |
| hio.baudrate=921600                                                   |
|                                                                       |
| flash: Gordon ready!                                                  |
|                                                                       |
| Y-BOOT 208ef13 2019-07-22 12:26:54 -0500 790da1-b-7                   |
|                                                                       |
| ROM yoda-h0-rom-16-0-gd5a8e586                                        |
|                                                                       |
| FLASH:PNWWWWWWAE                                                      |
|                                                                       |
| Build $Id: git-50a5d91 $                                              |
|                                                                       |
| Flash detected. flash.hw.uuid: 39483937-3207-003a-006e-ffffffffffff   |
|                                                                       |
| Bootargs:                                                             |
| hssid1=Asus_Qos_2G,passphrase1=99999999,ssid2=                        |
| manasvi,passphrase2=manasvi123,hssid3=TP-Link_2G,passphrase3=12345678 |
|                                                                       |
| $App:git-3b62b4a                                                      |
|                                                                       |
| SDK Ver: FREERTOS_SDK_1.0                                             |
|                                                                       |
| Wifi Multi AP Demo App                                                |
|                                                                       |
| adding dp to list                                                     |
|                                                                       |
| adding tplinkc6_iop to list                                           |
|                                                                       |
| adding TP-Link_2G(\*) to list                                         |
|                                                                       |
| passphrase is NULL!!!                                                 |
|                                                                       |
| AP 0, SSID: dp Passphrase: deepu.123                                  |
|                                                                       |
| AP 1, SSID: tplinkc6_iop Passphrase: InnoQA2023$                      |
|                                                                       |
| AP 2, SSID: TP-Link_2G Passphrase:                                    |
|                                                                       |
| addr e0:69:3a:00:01:01                                                |
|                                                                       |
| Found 7 nets:Found 3 nets:                                            |
|                                                                       |
| 3c:84:6a:f4:4e:b0 on channel 5 @ -31 'manasvi'                        |
|                                                                       |
| b4:43:26:4b:4c:d4 on channel 10 @ -64 'Ananth Krishna'                |
|                                                                       |
| 5c:f9:fd:6b:e9:09 on channel 5 @ -79 'manasvi'                        |
|                                                                       |
| Found 2 nets:                                                         |
|                                                                       |
| 3c:84:6a:f4:4e:b0 on channel 5 @ -30 'manasvi'                        |
|                                                                       |
| b4:43:26:4b:4c:d4 on channel 10 @ -61 'Ananth Krishna'                |
|                                                                       |
| Found 3 nets:                                                         |
|                                                                       |
| 3c:84:6a:f4:4e:b0 on channel 5 @ -32 'manasvi'                        |
|                                                                       |
| b4:43:26:4b:4c:d4 on channel 10 @ -62 'Ananth Krishna'                |
|                                                                       |
| a0:ab:1b:27:99:4c on channel 9 @ -67 'Vinoth_room2.4g'                |
|                                                                       |
| Hidden network: Asus_Qos_2G                                           |
|                                                                       |
| Hidden network: TP-Link_2G                                            |
|                                                                       |
| Found 4 nets:                                                         |
|                                                                       |
| 3c:84:6a:f4:4e:b0 on channel 5 @ -30 'manasvi'                        |
|                                                                       |
| b4:43:26:4b:4c:d4 on channel 10 @ -63 'Ananth Krishna'                |
+=======================================================================+
+-----------------------------------------------------------------------+
