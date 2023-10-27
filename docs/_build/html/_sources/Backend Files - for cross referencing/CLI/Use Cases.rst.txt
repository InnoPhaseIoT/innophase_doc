Use Cases 
==========

Linux Platform
--------------

Reset Device
~~~~~~~~~~~~

1. **Normal Device Reset**

Reset the device.

**Command syntax**:

+-----------------------------------------------------------------------+
| ./script/boot.py [device] **--reset=evk42**                           |
+=======================================================================+
+-----------------------------------------------------------------------+

|A screenshot of a computer Description automatically generated with
medium confidence|

Figure 16: Normal device reset - terminal output

**Console output**:

+-----------------------------------------------------------------------+
| $ miniterm /dev/ttyUSB3 2457600                                       |
+=======================================================================+
+-----------------------------------------------------------------------+

|Text Description automatically generated|

Figure 17: Normal device reset - console output

In this example, the app HelloWorld is stored in device flash. Hence a
flash-boot from reset will display the Hello World.

1. **Device Reset with Inhibiting-flash-boot (Boot loader mode)**

..

   Reset the device with the inhibiting-flash-boot feature.

   If the device has app code stored in flash from which the device will
   boot, this special reset command is required which will allow
   flashing of a new app code.

   **Command syntax**:

+-----------------------------------------------------------------------+
| ./script/boot.py [device] **--reset=evk42_bl**                        |
+=======================================================================+
+-----------------------------------------------------------------------+

..

   |image1|

Figure 18: inhibiting-flash-boot - terminal output

   This reset will trigger Talaria TWO to abort from device port link
   (expected).

   |image2|

Figure 19: Abort from device port link

   Launch miniterm to resume the device port connection.

   |image3|

Figure 20: Resume device port connection

2. **Reset with Inhibiting-flash-boot with booting Gordon**

..

   Reset the device with inhibiting-flash-boot and boot the gordon app.

   This combination of commands is for the host to obtain access to the
   storage on Talaria TWO and operate read/write data.

   Command syntax:

+-----------------------------------------------------------------------+
| ./script/boot.py [device] **--reset=evk42_bl**                        |
| apps/gordon/bin/gordon.elf                                            |
+=======================================================================+
+-----------------------------------------------------------------------+

..

   |image4|

Figure 21: Inhibiting-flash-boot with booting Gordon - terminal output

Program App in Memory
~~~~~~~~~~~~~~~~~~~~~

Program app in Talaria TWO memory.

**Command syntax**:

+-----------------------------------------------------------------------+
| ./script/boot.py [device] **--reset=evk42** <path>/app.elf [boot_args |
| list]                                                                 |
+=======================================================================+
+-----------------------------------------------------------------------+

|image5|

Figure 22: Programming app in Talaria TWO memory - terminal output

**Console output:**

|image6|

Figure 23: Programming app in Talaria TWO memory - console output

Erase Image or Program New Image in Flash
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Erase Image in Flash

The following command erases the app code in flash:

a. Reset device with inhibiting-flash-boot and load gordon.elf (if not
   done already)

b. Flash empty.img

**Command syntax**:

+-----------------------------------------------------------------------+
| ./script/flash.py [device] **write 0x1000 <path>/empty.img**          |
+=======================================================================+
+-----------------------------------------------------------------------+

|image7|

Figure 24: Flash empty.img

Button reset to confirm the erase operation is a success.

|image8|

Figure 25: Erase operation success

2. Program New Image in Flash

**Command syntax**:

+-----------------------------------------------------------------------+
| ./script/boot.py [device] **--reset=evk42_bl** **--flash=all**        |
| <path>/app.elf [boot_args_list]                                       |
+=======================================================================+
+-----------------------------------------------------------------------+

|image9|

Figure 26: Program new image to flash

Button reset to confirm the flash operation a success.

|image10|

Figure 27: Flash operation success

Storage Data & File: Read/Write
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. **Read Partition Table from Device (to_json)**

Reading file from device involves storage access. Hence, running of
Gordon on the device is necessary.

a. Reset device with inhibiting-flash-boot and load gordon.elf (if not
   done already)

b. Run the flash.py with the command: to_json

**Command syntax**:

+-----------------------------------------------------------------------+
| ./script/flash.py [device] **to_json**                                |
| <user_specify_path>/<user_spefcify_name>.json                         |
+=======================================================================+
+-----------------------------------------------------------------------+

|image11|

Figure 28: Inhibiting-flash-boot and load gordon.elf

Display of the board_356.json file

|Text, timeline Description automatically generated|

Figure 29: Display of the board_356.json file

2. **Write Partition Table in Device (from_json)**

Writing file to device involves storage access. Hence, running of Gordon
on the device is necessary.

a. Reset device with inhibiting-flash-boot and load gordon.elf (if not
   done already)

b. Run the flash.py with the command: from_json

**Command syntax**:

+-----------------------------------------------------------------------+
| ./script/boot.py [device] **--reset=evk42_bl** <path>/gordon.elf      |
|                                                                       |
| ./script/flash.py [device] **from_json**                              |
| <user_specify_path>/<user_spefcify_name>.json                         |
+=======================================================================+
+-----------------------------------------------------------------------+

|image12|

Figure 30: inhibiting-flash-boot and load gordon.elf - terminal output

**Console output**:

|image13|

Figure 31: flash.py - from_json

3. **Show File System Contents**

Display the file system contents.

a. Reset device with inhibiting-flash-boot and load gordon.elf (if not
   done already)

b. Run the storage.py with the command: tree

**Command syntax**:

+-----------------------------------------------------------------------+
| ./script/storage.py **tree**                                          |
+=======================================================================+
+-----------------------------------------------------------------------+

|image14|

Figure 32: Show file system contents

4. **Read File and Store to Location on Host**

Read file from the file system and store it in host.

a. Reset device with inhibiting-flash-boot and load gordon.elf (if not
   done already)

b. Run the storage.py with the command: read

**Command syntax**:

+-----------------------------------------------------------------------+
| ./script/storage.py **read** <path_read>/<file_name_read>             |
| **--output** <path_write>/<file_name_write>                           |
+=======================================================================+
+-----------------------------------------------------------------------+

|Chart, text Description automatically generated|

Figure 33: Inhibiting-flash-boot and load gordon.elf – terminal output

The file is created:

|Shape, rectangle Description automatically generated with medium
confidence|

Figure 34: File creation

5. **Write File to Device**

Write file from host to the device in file system.

a. Reset device with inhibiting-flash-boot and load gordon.elf (if not
   done already)

b. Run the storage.py with the command: write

**Command syntax**:

+-----------------------------------------------------------------------+
| ./script/storage.py **write** <path_read>/<file_name_read>            |
| <path_write>/file_name_write>                                         |
+=======================================================================+
+-----------------------------------------------------------------------+

|image15|

Figure 35: Running storage.py - write

Use ./script/storage.py tree command to check the new file on Talaria
TWO file system:

|image16|

Figure 36: Check new file on Talaria TWO file system

Example: Load certificates

a. $ ./script/storage.py write rootCACert.pem /data/ca.pem

b. $ ./script/storage.py write client_cert.pem /data/client.pem

c. $ ./script/storage.py write client_key.pem /data/client.key

Network Profile
~~~~~~~~~~~~~~~

The Wi-Fi network profile stores the configuration of the Wi-Fi network
with parameters such as SSID, passphrase, BSSID, security type etc.
Network profile can be created from the JSON data.

JSON data can be stored in either:

1. The filesystem: Build a network profile from a file in Talaria TWO
   filesystem given by the path in Talaria TWO filesystem

or

2. A string: JSON string which describes and parses the network profile

Characteristics of creating JSON network profile:

1. All network profiles MUST start with { and end with }.

2. The network profile contents use the form ("key": "value") pairs.

3. All the ("key": "value") pairs MUST be followed by a comma (,) EXCEPT
   the last row.

4. There is NO COMMA at the end of the network profile.

5. Mandatory fields MUST always be present, otherwise, parsing the
   network profile will fail.

6. If a passphrase contains double quotes, for example: "my_secret", a
   backslash MUST preceded the double quotes, i.e., "passphrase":
   "\\"my_secret\\"".

**Note**:

To avoid recomputing the PMK for each connection (WPA/WPA2-PSK), it can
be stored in Talaria TWO’s flash. This can be done by a pmk_path key and
the location of PMK file in Talaria TWO flash. There are two new keys to
make it easier in creating network profiles:

1. security_type key which replaces the old np_type in network profiles
   and can have the following values depending the type of the network:

   a. open

   b. wpa_psk or wpa2_psk

   c. wpa3_psk

   d. wpa23_psk

   e. enterprise

2. auth_type key which can ONLY be used when configuring enterprise
   network profiles and describes the authentication protocol. Values
   for auth_type can be:

   a. eap_psk

   b. eap_tls

   c. eap_peap

Following are some examples of JSON data specifying different network
profiles:

1. **Open security**:

+-----------------------------------------------------------------------+
| {                                                                     |
|                                                                       |
| “security_type”: “open”                                               |
|                                                                       |
| “ssid”: “my_ap_ssid”                                                  |
|                                                                       |
| }                                                                     |
+=======================================================================+
+-----------------------------------------------------------------------+

Profile fields:

a. Mandatory – security_type, ssid

b. Optional – bssid

2. **WPA/WPA2-PSK**:

+-----------------------------------------------------------------------+
| {                                                                     |
|                                                                       |
| "security_type": "wpa23_psk",                                         |
|                                                                       |
| "ssid": "my_wpa2_ap_ssid",                                            |
|                                                                       |
| "passphrase": "my_wpa2_passphrase"                                    |
|                                                                       |
| “pmk_path”: “sys/pmkey_fname.data”                                    |
|                                                                       |
| }                                                                     |
+=======================================================================+
+-----------------------------------------------------------------------+

Profile fields:

a. Mandatory – security_type, ssid, passphrase

b. Optional – bssid, pmk_path

3. **WPA/WPA2-PSK** specifying one specific AP among several with same
   SSID. BSSID is the APs mac address:

+-----------------------------------------------------------------------+
| {                                                                     |
|                                                                       |
| "security_type": "wpa2_psk",                                          |
|                                                                       |
| "ssid": "my_wpa2_ap_ssid",                                            |
|                                                                       |
| "passphrase": "my_wpa2_passphrase",                                   |
|                                                                       |
| "bssid": "my_ap_bssid"                                                |
|                                                                       |
| “pmk_path”: “/data/pmkey.data”                                        |
|                                                                       |
| }                                                                     |
+=======================================================================+
+-----------------------------------------------------------------------+

Profile fields:

a. Mandatory – security_type, ssid, passphrase

b. Optional – bssid, pmk_path

4. **WPA3-PSK (SAE)** only:

+-----------------------------------------------------------------------+
| {                                                                     |
|                                                                       |
| "security_type": "wpa3_psk",                                          |
|                                                                       |
| "ssid": "my_wpa3_ap_ssid",                                            |
|                                                                       |
| "sae_password": "my_sae_password"                                     |
|                                                                       |
| }                                                                     |
+=======================================================================+
+-----------------------------------------------------------------------+

Profile fields

a. Mandatory: security_type, ssid, sae_password

b. Optional : sae_password_id, bssid

5. **WPA/WPA2-PSK and WPA3-PSK.** If WPA3 is available, it will be given
   a higher priority:

+-----------------------------------------------------------------------+
| {                                                                     |
|                                                                       |
| "security_type": "wpa23_psk",                                         |
|                                                                       |
| "ssid": "my_wpa2_wpa3_ap_ssid",                                       |
|                                                                       |
| "sae_password": "my_sae_password"                                     |
|                                                                       |
| "passphrase": "my_wpa2_passphrase"                                    |
|                                                                       |
| }                                                                     |
+=======================================================================+
+-----------------------------------------------------------------------+

Profile fields

a. Mandatory: security_type, ssid, sae_password, passphrase

b. Optional : bssid

6. **EAP-PSK** Enterprise security:

+-----------------------------------------------------------------------+
| {                                                                     |
|                                                                       |
| "security_type": "enterprise",                                        |
|                                                                       |
| "auth_type": "eap_psk",                                               |
|                                                                       |
| "ssid": "my_eap_psk_ap_ssid",                                         |
|                                                                       |
| "passphrase": "my_eap_psk_passphrase",                                |
|                                                                       |
| "identity": "my_eap_identity"                                         |
|                                                                       |
| }                                                                     |
|                                                                       |
| Profile fields                                                        |
|                                                                       |
| Mandatory: security_type, auth_type, ssid, passphrase, identity       |
|                                                                       |
| Optional : bssid }                                                    |
+=======================================================================+
+-----------------------------------------------------------------------+

**
**

7. **EAP-TLS** Enterprise security.

**Note**: Storing the certificate and key files on flash is not part of
the network profile functionality.

+-----------------------------------------------------------------------+
| {                                                                     |
|                                                                       |
| "security_type": "enterprise",                                        |
|                                                                       |
| "auth_type": "eap_tls",                                               |
|                                                                       |
| "ssid": "my_eap_tls_ap_ssid",                                         |
|                                                                       |
| "identity": "my_eap_tls_identity",                                    |
|                                                                       |
| "ca_path": "/data/ca.pem",                                            |
|                                                                       |
| "cert_path": "/data/client.pem",                                      |
|                                                                       |
| "pkey_path": "/data/client.key",                                      |
|                                                                       |
| "pkey_pwd": "my_key_password"                                         |
|                                                                       |
| }                                                                     |
|                                                                       |
| Profile fields                                                        |
|                                                                       |
| Mandatory: security_type, auth_type, ssid, identity, ca_path,         |
| cert_path, pkey_path                                                  |
|                                                                       |
| Optional : bssid, pkey_pwd, dh_path, server_hostname                  |
+=======================================================================+
+-----------------------------------------------------------------------+

8. **EAP-PEAP/MSCHAPv2** Enterprise security:

+-----------------------------------------------------------------------+
| {                                                                     |
|                                                                       |
| "security_type": "enterprise",                                        |
|                                                                       |
| "auth_type": "eap_peap",                                              |
|                                                                       |
| "ssid": "my_eap_peap-mschapv2_ssid",                                  |
|                                                                       |
| "identity": "my_eap_peap_identity",                                   |
|                                                                       |
| "ca_path": "/data/ca.pem",                                            |
|                                                                       |
| "identity2": "eap-peap",                                              |
|                                                                       |
| "password": "password",                                               |
|                                                                       |
| "phase2auth":"MSCHAPv2"                                               |
|                                                                       |
| }                                                                     |
+=======================================================================+
+-----------------------------------------------------------------------+

Profile fields

a. Mandatory: security_type, auth_type, ssid, identity, ca_path,
   identity2, password, phase2auth

b. Optional : bssid, server_hostname.

..

   **Note**: For "phase2auth", the key MUST always be "phase2auth":
   while the VALUE can be, For example: "MSCHAPv2", "mschapv2" or
   "MsChAPv2" or any other similar lower/upper case letter combination.

   **
   **

**Prerequisites:**

To upload network profile into Talaria TWO file system, running of
Gordon on the device is necessary.

1. Reset device with inhibiting-flash-boot and load gordon.elf (if not
   done already)

2. Write network profile JSON to Talaria TWO

**Command syntax:**

+-----------------------------------------------------------------------+
| python ./script/storage.py [device] write                             |
| <user_specify_path>/<user_spefcify_name>.json                         |
| /data/<user_specify_name>.json                                        |
+=======================================================================+
+-----------------------------------------------------------------------+

**Note**: It is a single line command.

**Steps:**

1. Create a Network Profile File(JSON file).

Create a file and name anywhere in your PC and name it **nprofile.json**
or **<file_name>.json**, and copy the following contents (we assume we
are connecting to a WPA2-PSK network):

+-----------------------------------------------------------------------+
| {                                                                     |
|                                                                       |
| "security_type":"wpa23_psk",                                          |
|                                                                       |
| "ssid": "My-AP-Name",                                                 |
|                                                                       |
| "passphrase": "0CD7AC607B"                                            |
|                                                                       |
| }                                                                     |
|                                                                       |
| nprofile.json file:                                                   |
+=======================================================================+
+-----------------------------------------------------------------------+

2. To upload our network profile into Talaria file system, start
   **gordon.elf** and reset in bootloader mode.

+-----------------------------------------------------------------------+
| pythton ./script/boot.py --reset=evk42_bl apps/gordon/bin/gordon.elf  |
+=======================================================================+
+-----------------------------------------------------------------------+

|image17|

Figure 37: Starting gordon.elf

3. Use **storage.py** to write the network config file
   (**nprofile.json**) into Talaria TWO file system in the partition
   /data.

+-----------------------------------------------------------------------+
| python ./script/storage.py write nprofile.json /data/nprofile.json    |
+=======================================================================+
+-----------------------------------------------------------------------+

Command Log:

|image18|

Figure 38: Writing network config file

Console Log:

|image19|

Figure 39: Writing network config file – console output

4. Program(RAM/FLASH) app to connect to the Access Point configured in
   **nprofile.json** as:

   a. Program RAM:

+-----------------------------------------------------------------------+
| python ./script/boot.py --reset=evk42                                 |
| examples/using_wifi/bin/wifi_connect.elf                              |
| np_conf_path=/data/nprofile.json                                      |
+=======================================================================+
+-----------------------------------------------------------------------+

..

   Command Log:

   |image20|

Figure 40: Program RAM to connect to AP

   Console Log:

   |A screenshot of a computer Description automatically generated|

Figure 41: Program RAM - Console output

b. Program FLASH:

+-----------------------------------------------------------------------+
| python ./script/boot.py --reset=evk42 –flash=all                      |
| examples/using_wifi/bin/wifi_connect.elf                              |
| np_conf_path=/data/nprofile.json                                      |
+=======================================================================+
+-----------------------------------------------------------------------+

..

   Command Log:

   |A black background with white text Description automatically
   generated with medium confidence|

Figure 42: Program Flash to connect to AP

   Console Log:

   |A screenshot of a computer program Description automatically
   generated|

Figure 43: Program Flash - Console output

Windows Platform – libusbK Installed
------------------------------------

.. _reset-device-1:

Reset Device
~~~~~~~~~~~~

1. **Device Reset**

Reset the device.

**Command syntax**:

+-----------------------------------------------------------------------+
| python script\\boot.py [device] **--reset=evk42**                     |
+=======================================================================+
+-----------------------------------------------------------------------+

|image21|

Figure 44: Device reset

**Console output**:

|image22|

Figure 45: Device reset - console output

2. **Device Reset with Inhibiting-flash-boot**

Reset the device with the inhibiting-flash-boot feature.

If the device has app code stored in flash from which the device will
boot, this special reset command is required which will allow to flash a
new app code.

**Command syntax**:

+-----------------------------------------------------------------------+
| python script\\boot.py [device] **--reset=evk42_bl**                  |
+=======================================================================+
+-----------------------------------------------------------------------+

|image23|

Figure 46: Device Reset with Inhibiting-flash-boot

**Console output**:

|Table Description automatically generated with medium confidence|

Figure 47: Device Reset with Inhibiting-flash-boot - console output

The device has been put into the programming mode
(inhibiting-flash-boot).

3. **Reset with Inhibiting-flash-boot and booting Gordon**

Reset the device with inhibiting-flash-boot and boot Gordon app.

This combination of commands is for the host to obtain access to the
storage on Talaria TWO and operate read/write data.

**Command syntax:**

+-----------------------------------------------------------------------+
| python script\\boot.py [device] **--reset=evk42_bl**                  |
| apps\\gordon\\bin\\gordon.elf                                         |
+=======================================================================+
+-----------------------------------------------------------------------+

|image24|

Figure 48: Reset with Inhibiting-flash-boot with booting Gordon

**Console output:**

|A picture containing graphical user interface Description automatically
generated|

Figure 49: Reset with Inhibiting-flash-boot with booting Gordon -
console output

.. _program-app-in-memory-1:

Program App in Memory
~~~~~~~~~~~~~~~~~~~~~

Program app in Talaria TWO memory, assuming Talaria TWO has no code
stored in flash to boot from.

**Command syntax**:

+-----------------------------------------------------------------------+
| python script\\boot.py [device] **--reset=evk42** <path>\\app.elf     |
| [boot_args_list]                                                      |
+=======================================================================+
+-----------------------------------------------------------------------+

|image25|

Figure 50: Program app in Talaria TWO memory

**Console output**:

|image26|

Figure 51: Program app in Talaria TWO memory - console output

.. _erase-image-or-program-new-image-in-flash-1:

Erase Image or Program New Image in Flash
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Erase Image in Flash**

The following command erases the app code in flash:

a. Reset device with inhibiting-flash-boot and load gordon.elf (if not
   done so)

b. Flash empty.img

**Command syntax**:

+-----------------------------------------------------------------------+
| python script\\flash.py [device] **write 0x1000 <path>\\empty.img**   |
+=======================================================================+
+-----------------------------------------------------------------------+

|image27|

Figure 52: Erase image in flash

**Console output**:

|image28|

Figure 53: Erase image in flash - console output

**Program New Image in Flash**

**Command syntax**:

+-----------------------------------------------------------------------+
| python script\\boot.py [device] **--reset=evk42_bl** **--flash=all**  |
| <path>\\app.elf [boot_args_list]                                      |
+=======================================================================+
+-----------------------------------------------------------------------+

|image29|

Figure 54: Program new image in flash

**Console output**:

|Text Description automatically generated with medium confidence|

Figure 55: Program new image in flash - console output

.. _storage-data-file-readwrite-1:

Storage Data & File: Read/Write
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. **Read Partition Table from Device (to_json)**

Reading file from device involves storage access. Hence, the running of
Gordon on the device is necessary.

a. Reset device with inhibiting-flash-boot and load gordon.elf (if not
   done already)

b. Run the flash.py with the command: to_json

**Command syntax:**

+-----------------------------------------------------------------------+
| python script\\flash.py [device] **to_json**                          |
| <user_specify_path>\\<user_spefcify_name>.json                        |
+=======================================================================+
+-----------------------------------------------------------------------+

|image30|

Figure 56: Read Partition Table from device

Display of the board_0183.json file

|Text, timeline Description automatically generated|

Figure 57: Display of the board_0183.json file

2. **Write Partition Table in Device (from_json)**

Writing file to device involves storage access. Hence, running of Gordon
on the device is necessary.

a. Reset device with inhibiting-flash-boot and load gordon.elf (if not
   done already)

b. Run the flash.py with the command: from_json

**Command syntax:**

+-----------------------------------------------------------------------+
| python script\\flash.py [device] **from_json**                        |
| <user_specify_path>/<user_spefcify_name>.json                         |
+=======================================================================+
+-----------------------------------------------------------------------+

|image31|

Figure 58: Write Partition Table in device

3. **Show File System Contents**

Display the file system contents.

a. Reset device with inhibiting-flash-boot and load gordon.elf (if not
   done already)

b. Run the storage.py with the command: tree

**Command syntax**:

+-----------------------------------------------------------------------+
| python script\\storage.py [device] **tree**                           |
+=======================================================================+
+-----------------------------------------------------------------------+

|image32|

Figure 59: Show file system contents

4. **Read File and Store to Location on Host**

Read file from the file system and store it in host.

a. Reset device with inhibiting-flash-boot and load gordon.elf (if not
   done already)

b. Run the storage.py with the command: read

**Command syntax**:

+-----------------------------------------------------------------------+
| python script\\storage.py [device] **read**                           |
| <path_read>\\<file_name_read> **--output**                            |
| <path_write>/<file_name_write>                                        |
+=======================================================================+
+-----------------------------------------------------------------------+

**Note**: Single line command.

|image33|

Figure 60: Read file and store to location on host

The file is created as per user entry:

|image34|

Figure 61: File creation

5. **Write File to Device**

Write file from host to the device in file system.

a. Reset device with inhibiting-flash-boot and load gordon.elf (if not
   done already)

b. Run the storage.py with the command: write

**Command syntax:**

+-----------------------------------------------------------------------+
| python script\\storage.py [device] **write**                          |
| <path_read>\\<file_name_read> <path_write>\\file_name_write>          |
+=======================================================================+
+-----------------------------------------------------------------------+

**Note**: A single line command.

|image35|

Figure 62: Write file to device

Use the ./script/storage.py tree command to check the new file on
Talaria TWO file system:

|image36|

Figure 63: Check new file on Talaria TWO file system

Windows Platform – With COM Port
--------------------------------

To retrieve the COM ports on the device, the libusbK drivers need to be
uninstalled.

For more details on updating driver from libusbK to COM port, refer
section: Update Driver from libusbK to COM Port of document
UG_Download_Tool.pdf (*sdk_x.y\\pc_tools\\Download_Tool\\doc*).

**Note**: x and y in sdk_x.y refer to the SDK release version.

.. _reset-device-2:

Reset Device
~~~~~~~~~~~~

All command resets are not supported under this setup.

Depending on the requirement to reset the device manually, execute the
following steps:

1. Reset the device manually:

   a. Press the RESET button on Talaria TWO EVB

2. Inhibiting-flash-boot (to re-enable programming):

   a. Short GPIO17 to GND

   b. Press the RESET button on EVB

   c. Un-short GPIO17 and GND

   d. Load gordon.elf from host, using boot.py

Load Gordon
~~~~~~~~~~~

Load Gordon app to run the flash.py from host, assuming the image in
device flash has been erased or has been placed in the
inhibiting-flash-boot state.

**Command syntax:**

+-----------------------------------------------------------------------+
| python script\\boot.py [device] apps\\gordon\\bin\\gordon.elf         |
+=======================================================================+
+-----------------------------------------------------------------------+

|image37|

Figure 64: Load gordon.elf

Console output shows the inhibiting-flash-boot in effect and Gordon
being ready.

|image38|

Figure 65: inhibiting-flash-boot in effect

Erase Image
~~~~~~~~~~~

The following command erases the app code in flash.

1. Reset device with inhibiting-flash-boot and load gordon.elf (if not
   done so)

2. Flash empty.img

**Command syntax**:

+-----------------------------------------------------------------------+
| python script\\flash.py [device] **write 0x1000 <path>\\empty.img**   |
+=======================================================================+
+-----------------------------------------------------------------------+

|A picture containing timeline Description automatically generated|

Figure 66: Erase image

Button reset to confirm the erase operation is a success.

|image39|

Figure 67: Erase operation – success

.. _storage-data-file-readwrite-2:

Storage Data & File: Read/Write
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. **Read Partition Table from Device (to_json)**

Reading file from device involves storage access. Hence, running of
Gordon on the device is necessary.

a. Reset device with inhibiting-flash-boot and load gordon.elf (if not
   done already)

b. Run the flash.py with the command: to_json

**Command syntax**:

+-----------------------------------------------------------------------+
| python script\\flash.py [device] **to_json**                          |
| <user_specify_path>\\<user_spefcify_name>.json                        |
+=======================================================================+
+-----------------------------------------------------------------------+

|image40|

Figure 68: Read Partition Table from device

Display of the board_0407.json file

|Text, timeline Description automatically generated|

Figure 69: Display of the board_0407.json file

2. **Write Partition Table in Device (from_json)**

Writing file to device involves storage access. Hence, running of Gordon
on the device is necessary.

a. Reset device with inhibiting-flash-boot and load gordon.elf (if not
   done already)

b. Run the flash.py with the command: from_json

**Command syntax**:

+-----------------------------------------------------------------------+
| python script\\flash.py [device] **from_json**                        |
| <user_specify_path>/<user_spefcify_name>.json                         |
+=======================================================================+
+-----------------------------------------------------------------------+

|image41|

Figure 70: Write Partition Table in device

**Console output**:

|image42|

Figure 71: Write Partition Table in device - console output

3. **Show File System Contents**

Display the file system contents.

a. Reset device with inhibiting-flash-boot and load gordon.elf (if not
   done already)

b. Run the storage.py with the command: tree

**Command syntax**:

+-----------------------------------------------------------------------+
| python script\\storage.py [device] **tree**                           |
+=======================================================================+
+-----------------------------------------------------------------------+

|image43|

Figure 72: Show file system contents

4. **Read File and Store to Location on Host**

Read file from the file system and store it in host.

a. Reset device with inhibiting-flash-boot and load gordon.elf (if not
   done already)

b. Run the storage.py with the command: read

**Command syntax:**

+-----------------------------------------------------------------------+
| python script\\storage.py [device] **read**                           |
| <path_read>\\<file_name_read> **--output**                            |
| <path_write>/<file_name_write>                                        |
+=======================================================================+
+-----------------------------------------------------------------------+

**Note**: A single line command.

|image44|

Figure 73: Read file and store to location on host

The file is created per user entry:

|image45|

Figure 74: File creation

3. **Write File to Device**

Write file from the host to the device in file system.

a. Reset device with inhibiting-flash-boot and load gordon.elf (if not
   done already)

b. Run the storage.py with the command: write

**Command syntax**:

+-----------------------------------------------------------------------+
| python script\\storage.py [device] **write**                          |
| <path_read>\\<file_name_read> <path_write>\\file_name_write>          |
+=======================================================================+
+-----------------------------------------------------------------------+

**Note**: A single line command.

|image46|

Figure 75: Write file to device

Use the ./script/storage.py tree command to check the new file on
Talaria TWO file system:

|image47|

Figure 76: Check new file on Talaria TWO filesystem

Write New App to Device with Factory Loaded Image
-------------------------------------------------

Assume a Talaria TWO module is preloaded loaded with factory-loaded app
like the helloworld app as shown in Figure 77.

|image48|

Figure 77: Talaria TWO preloaded with factory-loaded app

Sequence of CLI Commands
~~~~~~~~~~~~~~~~~~~~~~~~

1. **Reset with inhibiting-flash-boot and load Gordon**

**Command Syntax:**

+-----------------------------------------------------------------------+
| ./script/boot.py --device /dev/ttyUSB2 --reset=evk42_bl               |
| apps/gordon/bin/gordon.elf                                            |
+=======================================================================+
+-----------------------------------------------------------------------+

**Console Output**:

|image49|

Figure 78: Reset with inhibiting-flash-boot and load gordon

2. **Write the Partition Table**

Write the Partition Table which is a standard configuration,
standard_part_table.json, to Talaria TWO device:

**Command Syntax**:

+-----------------------------------------------------------------------+
| ./script/flash.py --device /dev/ttyUSB2 from_json                     |
| tools/partition_files/standard_part_table.json                        |
+=======================================================================+
+-----------------------------------------------------------------------+

**Note**: A single line command.

**Console Output**:

|image50|

Figure 79: Write partition table - console output

3. **Flash New App to Device**

Write a new application, iperf3 with bootargs, to the device.

**Command Syntax**:

+-----------------------------------------------------------------------+
| ./script/boot.py --device /dev/ttyUSB2 --reset=evk42_bl --flash=all   |
| ./apps/iperf3/bin/iperf3.elf ssid=TP-LINK_Guest_864F                  |
| passphrase=test13579                                                  |
+=======================================================================+
+-----------------------------------------------------------------------+

|image51|

Figure 80: Flash new app to device

Re-launch the console terminal app and reset Talaria TWO device.

**Console output**:

|image52|

Figure 81: Flash new app to device - console output

Figure 81 shows that the new app has been written to Talaria TWO’s flash
and runs as expected.

Flash New App to Device with an Existing App
--------------------------------------------

Write the new app, stw.elf, to flash.

Command Syntax:

+-----------------------------------------------------------------------+
| ./script/boot.py --device /dev/ttyUSB2 --reset=evk42_bl --flash=all   |
| ./apps/stw/bin/stw.elf                                                |
+=======================================================================+
+-----------------------------------------------------------------------+

|image53|

Figure 82: Write new app to flash

Re-launch the console terminal app and reset Talaria TWO device.

**Console Output**:

|image54|

Figure 83: Write new app to flash - console output

Figure 83 shows that the new app, STW, has been written to Talaria TWO’s
flash and runs as expected.

.. |A screenshot of a computer Description automatically generated with medium confidence| image:: media/image1.png
   :width: 5.90551in
   :height: 0.69145in
.. |Text Description automatically generated| image:: media/image2.png
   :width: 5.90551in
   :height: 1.31037in
.. |image1| image:: media/image3.png
   :width: 5.90551in
   :height: 0.8448in
.. |image2| image:: media/image4.png
   :width: 5.90551in
   :height: 1.05263in
.. |image3| image:: media/image5.png
   :width: 5.90551in
   :height: 0.59042in
.. |image4| image:: media/image6.png
   :width: 5.90551in
   :height: 1.02731in
.. |image5| image:: media/image7.png
   :width: 6.29921in
   :height: 1.49511in
.. |image6| image:: media/image8.png
   :width: 6.29921in
   :height: 2.28008in
.. |image7| image:: media/image9.png
   :width: 6.29921in
   :height: 0.43486in
.. |image8| image:: media/image10.png
   :width: 6.29921in
   :height: 1.32202in
.. |image9| image:: media/image11.png
   :width: 6.29921in
   :height: 2.34393in
.. |image10| image:: media/image12.png
   :width: 6.29921in
   :height: 1.40204in
.. |image11| image:: media/image13.png
   :width: 6.29921in
   :height: 1.51567in
.. |Text, timeline Description automatically generated| image:: media/image14.png
   :width: 3.10043in
   :height: 6.51429in
.. |image12| image:: media/image15.png
   :width: 6.29921in
   :height: 1.66855in
.. |image13| image:: media/image16.png
   :width: 6.29921in
   :height: 1.49655in
.. |image14| image:: media/image17.png
   :width: 6.29921in
   :height: 3.91951in
.. |Chart, text Description automatically generated| image:: media/image18.png
   :width: 6.29921in
   :height: 1.04693in
.. |Shape, rectangle Description automatically generated with medium confidence| image:: media/image19.png
   :width: 3.93701in
   :height: 0.82677in
.. |image15| image:: media/image20.png
   :width: 5.90551in
   :height: 0.46175in
.. |image16| image:: media/image21.png
   :width: 5.90436in
   :height: 2.34861in
.. |image17| image:: media/image22.png
   :width: 5.90551in
   :height: 1.16492in
.. |image18| image:: media/image21.png
   :width: 5.90436in
   :height: 0.4625in
.. |image19| image:: media/image23.png
   :width: 5.90551in
   :height: 0.86422in
.. |image20| image:: media/image24.png
   :width: 5.11811in
   :height: 1.72643in
.. |A screenshot of a computer Description automatically generated| image:: media/image25.png
   :width: 5.51181in
   :height: 4.94003in
.. |A black background with white text Description automatically generated with medium confidence| image:: media/image26.png
   :width: 5.90551in
   :height: 0.89989in
.. |A screenshot of a computer program Description automatically generated| image:: media/image27.png
   :width: 5.51181in
   :height: 4.9459in
.. |image21| image:: media/image28.png
   :width: 6.29921in
   :height: 0.96024in
.. |image22| image:: media/image29.png
   :width: 6.29921in
   :height: 1.10055in
.. |image23| image:: media/image30.png
   :width: 6.29921in
   :height: 1.0881in
.. |Table Description automatically generated with medium confidence| image:: media/image31.png
   :width: 6.29921in
   :height: 0.87801in
.. |image24| image:: media/image32.png
   :width: 6.29921in
   :height: 0.96933in
.. |A picture containing graphical user interface Description automatically generated| image:: media/image33.png
   :width: 6.29921in
   :height: 0.98259in
.. |image25| image:: media/image34.png
   :width: 6.29921in
   :height: 1.6378in
.. |image26| image:: media/image35.png
   :width: 6.29921in
   :height: 2.23423in
.. |image27| image:: media/image36.png
   :width: 6.29921in
   :height: 0.52922in
.. |image28| image:: media/image37.png
   :width: 6.29921in
   :height: 0.92827in
.. |image29| image:: media/image38.png
   :width: 6.29921in
   :height: 1.68091in
.. |Text Description automatically generated with medium confidence| image:: media/image39.png
   :width: 6.29921in
   :height: 1.21173in
.. |image30| image:: media/image40.png
   :width: 6.29921in
   :height: 1.23126in
.. |image31| image:: media/image41.png
   :width: 6.29921in
   :height: 1.38806in
.. |image32| image:: media/image42.png
   :width: 5.90551in
   :height: 3.96993in
.. |image33| image:: media/image43.png
   :width: 6.29921in
   :height: 0.55095in
.. |image34| image:: media/image44.png
   :width: 3.93701in
   :height: 0.50238in
.. |image35| image:: media/image45.png
   :width: 6.29921in
   :height: 0.56564in
.. |image36| image:: media/image21.png
   :width: 6.29818in
   :height: 2.5in
.. |image37| image:: media/image46.png
   :width: 7.48031in
   :height: 1.18536in
.. |image38| image:: media/image47.png
   :width: 7.48031in
   :height: 1.43047in
.. |A picture containing timeline Description automatically generated| image:: media/image48.png
   :width: 7.48031in
   :height: 0.74305in
.. |image39| image:: media/image49.png
   :width: 7.48031in
   :height: 1.14822in
.. |image40| image:: media/image50.png
   :width: 7.00787in
   :height: 1.69683in
.. |image41| image:: media/image51.png
   :width: 6.29921in
   :height: 1.43079in
.. |image42| image:: media/image52.png
   :width: 6.29921in
   :height: 1.79405in
.. |image43| image:: media/image53.png
   :width: 6.29921in
   :height: 4.97065in
.. |image44| image:: media/image54.png
   :width: 6.29921in
   :height: 0.63639in
.. |image45| image:: media/image55.png
   :width: 3.93701in
   :height: 0.47118in
.. |image46| image:: media/image56.png
   :width: 6.29921in
   :height: 0.76846in
.. |image47| image:: media/image57.png
   :width: 6.29921in
   :height: 0.63301in
.. |image48| image:: media/image58.png
   :width: 6.29921in
   :height: 3.89528in
.. |image49| image:: media/image59.png
   :width: 6.29921in
   :height: 1.12996in
.. |image50| image:: media/image60.png
   :width: 6.29921in
   :height: 0.43812in
.. |image51| image:: media/image61.png
   :width: 6.29921in
   :height: 2.04523in
.. |image52| image:: media/image62.png
   :width: 6.29921in
   :height: 2.62131in
.. |image53| image:: media/image63.png
   :width: 6.29921in
   :height: 2.04994in
.. |image54| image:: media/image64.png
   :width: 6.29921in
   :height: 1.32781in
