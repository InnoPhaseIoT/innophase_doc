Introduction
============

This application note provides details on using the following Radio and
Module parameters on the Talaria TWO module.

1. RF antenna gain: The RF antenna gain is the default power at which an
   antenna can transmit or receive.

2. Regulatory domain: The domain regulatory body which regulates the
   usage of radio frequencies in a particular geographical region.

3. TX power: Tx power is a measure of transmitted signal strength.

Radio and Module Parameters 
============================

Regulatory Domain
-----------------

A regulatory domain can be described as a set of rules and policies
providing the end user with configurations of country code, calibration
channel, and output power settings for a wireless device set up in a
specific area.

The following boot argument allows the user to change the Regulatory
domain:

**Boot Argument:**

.. table:: Table : Antenna gain look-up table

   +-----------------------------------------------------------------------+
   | reg_domain=< reg domain needs to be changed>                          |
   +=======================================================================+
   +-----------------------------------------------------------------------+

The following are the Regulatory domains supported in Talaria TWO with
this application:

1. ETSI

2. FCC

3. KCC

4. SRRC

5. TELEC

RF Antenna Gain
---------------

Antenna gain is the ability of the antenna to radiate in any direction
compared to an isotropic antenna.

The following boot argument allows the user to set antenna gain in dBi:

**Boot Argument:**

+-----------------------------------------------------------------------+
| rf.antenna_gain                                                       |
+=======================================================================+
+-----------------------------------------------------------------------+

The antenna gain value is used in calculation of output power to comply
with regulatory domain settings.

**Note:** User can configure the antenna gain for INP1011, INP1012 and
INP1015 modules.

The following antenna gain look-up table provides reference gain
information for the E.I.R.P. power measurements.

+---------------------------------+------------------------------------+
| **Module Type**                 | **Antenna Gain (dBi)**             |
+=================================+====================================+
| INP1010                         | 1                                  |
+---------------------------------+------------------------------------+
| INP1011                         | 2.15                               |
+---------------------------------+------------------------------------+
| INP1012                         | 2.15                               |
+---------------------------------+------------------------------------+
| INP1013                         | 1                                  |
+---------------------------------+------------------------------------+
| INP1014                         | 1                                  |
+---------------------------------+------------------------------------+
| INP1015                         | 2.15                               |
+---------------------------------+------------------------------------+

Tx Power
--------

The Tx power setting specifies the strength of the signal which the
station produces during transmission. Lowering the Tx power allows the
user to reduce interferences when more Wi-Fi devices are in the
vicinity.

The following boot argument allows the user to set maximum Tx power in
dBm:

**Boot Argument:**

+-----------------------------------------------------------------------+
| tx_power=<MAX TX power in dBm>                                        |
+=======================================================================+
+-----------------------------------------------------------------------+

Device Information
------------------

The device information available in the boot sector of the Talaria TWO
module contains the module type which is stored in the flash memory in
the factory.

APIs used in the Application
============================

Radio and Module Parameter APIs
-------------------------------

1. wcm_set_channel_spec()

..

   Sets channels and Tx power according to channel specification.

2. wcm_get_txpower()

..

   Gets the Tx power value configured using wcm_set_txpower for the
   Wi-Fi interface.

3. wcm_set_txpower()

..

   Sets maximum Tx power for the Wi-Fi interface.

4. os_devinfo_module_type()

..

   Gets module type for the Talaria TWO module.

Source Code Walkthrough
=======================

.. _source-code-walkthrough-1:

Source Code Walkthrough
-----------------------

create_wcm_hndl() function creates the WCM handle and applies the
provided domain.

+-----------------------------------------------------------------------+
| hndl = wcm_create(NULL);                                              |
|                                                                       |
| if(hndl == NULL) {                                                    |
|                                                                       |
| os_printf(“wcm create failed.\\n”);                                   |
|                                                                       |
| return NULL;                                                          |
|                                                                       |
| }                                                                     |
|                                                                       |
| if(domain != 0) {                                                     |
|                                                                       |
| /\* reg domain info given \*/                                         |
|                                                                       |
| os_printf(“Applying reg domain: %s\\n”, domain);                      |
|                                                                       |
| if(wcm_set_channel_spec(hndl, domain) != 0) {                         |
|                                                                       |
| os_printf(“Applying reg domain failed.!\\n”);                         |
|                                                                       |
| return NULL;                                                          |
|                                                                       |
| }                                                                     |
|                                                                       |
| }                                                                     |
+=======================================================================+
+-----------------------------------------------------------------------+

get_devicemodule_type() function reads the device information from the
boot sector of the Talaria TWO module.

+-----------------------------------------------------------------------+
| os_printf(“\\r \\n Reading module type\\n”);                          |
|                                                                       |
| os_devinfo_module_type(&type);                                        |
|                                                                       |
| os_printf(“\\r \\n Module type = INP%u \\n”, type);                   |
+=======================================================================+
+-----------------------------------------------------------------------+

wcmif_txpowerset() API sets the maximum Tx power for the Wi-Fi
interface.

+-----------------------------------------------------------------------+
| wcmif_txpowerset(txpower);                                            |
|                                                                       |
| os_printf(“txpower=%s\\n”, txpower);                                  |
+=======================================================================+
+-----------------------------------------------------------------------+

wcm_get_txpower() API gets the maximum Tx power for the Wi-Fi interface.

+-----------------------------------------------------------------------+
| tx_pow = wcm_get_txpower(hndl);                                       |
|                                                                       |
| os_printf(“\\r\\n Tx power in dBm = %d\\n”, (int)tx_pow);             |
+=======================================================================+
+-----------------------------------------------------------------------+

..

   wifi_connect_to_network() creates a Wi-Fi network interface to
   connect to a network.

   conn_status checks if the Wi-Fi is in a connected or disconnected
   state. Returns 0 on success or a negative error code in case of an
   error.

+-----------------------------------------------------------------------+
| rval = wifi_connect_to_network(&hndl, WCM_CONN_WAIT_INFINITE,         |
| &wcm_connected);                                                      |
|                                                                       |
| if(rval < 0) {                                                        |
|                                                                       |
| os_printf("\\r\\nError: Unable to connect to network\\n");            |
|                                                                       |
| return 0;                                                             |
|                                                                       |
| }                                                                     |
|                                                                       |
| if(wcm_connected != true) {                                           |
|                                                                       |
| os_printf("\\r\\nCouldn't Connect to network");                       |
|                                                                       |
| wcm_disconnect(hndl);                                                 |
|                                                                       |
| return -1;                                                            |
|                                                                       |
| }                                                                     |
+=======================================================================+
+-----------------------------------------------------------------------+

Building the Application
========================

To build the sample application, execute the following commands from the
SDK directory:

+-----------------------------------------------------------------------+
| cd examples/                                                          |
|                                                                       |
| make clean \| make                                                    |
+=======================================================================+
+-----------------------------------------------------------------------+

The make command should generate rf_param.elf in the out directory.

Running the Application
=======================

Programming Talaria TWO using the Download Tool
-----------------------------------------------

Program rf_param.elf (sdk_x.y\\examples\\radio_module_params\\bin) using
the Download tool:

1. Launch the Download tool provided with InnoPhase Talaria TWO SDK.

2. In the GUI window:

   a. Boot Target: Select the appropriate EVK from the drop-down.

   b. ELF Input: Load the rf_param.elf by clicking on Select ELF File.

   c. Boot Arguments: Pass the following boot arguments to set the REG
      domain and TX power.

+-----------------------------------------------------------------------+
| reg_domain=<Reg domain>,tx_power=<MAX TX power in dBm>                |
+=======================================================================+
+-----------------------------------------------------------------------+

d. Programming: Click on PROG Flash.

For more details on using the Download tool, refer to the document:
UG_Download_Tool.pdf (path: *sdk_x.y\\pc_tools\\Download_Tool\\doc*).

**Note**: x and y refer to the SDK release version. For example:
sdk_2.4\\doc.

Expected Output
---------------

On flashing the application using the Download Tool, the console output
is as follows:

+-----------------------------------------------------------------------+
| Y-BOOT 208ef13 2019-07-22 12:26:54 -0500 790da1-b-7                   |
|                                                                       |
| ROM yoda-h0-rom-16-0-gd5a8e586                                        |
|                                                                       |
| FLASH:PNWWWWWAEBuild $Id: git-ba65998b7 $                             |
|                                                                       |
| reg_domain=SRRC tx_power=11 np_conf_path=/data/nprofile.json          |
| ssid=inno_test passphrase=12345678                                    |
|                                                                       |
| $App:git-04aeaa1e                                                     |
|                                                                       |
| SDK Ver: sdk_2.5                                                      |
|                                                                       |
| Radio and Module Parameters Demo App                                  |
|                                                                       |
| reg_domain = SRRC                                                     |
|                                                                       |
| addr e0:69:3a:00:0a:66                                                |
|                                                                       |
| Applying reg domain                                                   |
|                                                                       |
| Reg Domain Applied                                                    |
|                                                                       |
| Maximum TX power set = 11                                             |
|                                                                       |
| Maximum TX power get = 11                                             |
|                                                                       |
| Connecting to added network : inno_test                               |
|                                                                       |
| [1.734,850] CONNECT:04:d1:3a:b2:48:63 Channel:1 rssi:-42 dBm          |
|                                                                       |
| wcm_notify_cb to App Layer - WCM_NOTIFY_MSG_ADDRESS                   |
|                                                                       |
| wcm_notify_cb to App Layer - WCM_NOTIFY_MSG_LINK_UP                   |
|                                                                       |
| [1.772,045] MYIP 192.168.43.164                                       |
|                                                                       |
| [1.772,208] IPv6 [fe80::e269:3aff:fe00:a66]-link                      |
|                                                                       |
| wcm_notify_cb to App Layer - WCM_NOTIFY_MSG_CONNECTED                 |
|                                                                       |
| Connected to added network : inno_test                                |
|                                                                       |
| Reading module type                                                   |
|                                                                       |
| Module type = INP1011                                                 |
|                                                                       |
| Connected to < inno_test > network                                    |
+=======================================================================+
+-----------------------------------------------------------------------+

**Output console**:

|image1|

Figure : Console output

.. |image1| image:: media/image1.png
   :width: 6.69291in
   :height: 5.44579in
