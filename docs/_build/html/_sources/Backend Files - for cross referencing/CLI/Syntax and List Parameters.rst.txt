CLI Command Syntax and List Parameters
======================================

All commands with arguments are entered in a space-separated fashion.

Positional and Optional Arguments

Arguments should be passed on to the app to be loaded into the Talaria
TWO device with the script. There are two different types of arguments:

1. Positional Arguments

Positional arguments must be included in the right order. Their
positions in the sequence should be correct.

2. Optional Arguments

Optional arguments are optional. Defaults will be used when the
arguments are not specified in the command line.

Using boot.py
-------------

1. Command syntax to run boot.py

+-----------------------------------------------------------------------+
| <path_script>/boot.py [device] <path_app_elf>/app.elf [boot_args]     |
+=======================================================================+
+-----------------------------------------------------------------------+

2. where,

   a. <path_script>: Path to the script file. Default: Current folder

   b. [device]: Communication device ID with path.

      i.   If there is only one Talaria TWO device with USB interface
           connected:

      ii.  Examples: COMn(Windows), /dev/ttyUSBn(Linux),
           ftdi://ftdi:xxxxxx(Windows libusbK installed).

      iii. If there are multiple Talaria TWO devices where each of them
           has their own peripheral port connected to the host via the
           USB interface:

      iv.  The device specifier must be expanded with the serial ID of
           the device in the command line. This is accomplished with the
           keyword --SN. Execute the following:

      v.   Command for device ID to the device port as shown above with
           the string is as follows:

+-----------------------------------------------------------------------+
| ./script/boot.py --device /dev/ttyUSB2 --SN 15100010 --reset=evk42    |
| apps/iperf3/bin/iperf3.elf ssid=InnoPhase passphrase=Inno@9070        |
+=======================================================================+
+-----------------------------------------------------------------------+

..

   Refer section `Device Interface on Host
   Machine <#_Device_Interface_on>`__ for information on multiple device
   connection on the host machine (Linux and Windows).

   Default: Windows-none, Linux-/dev/ttyUSB2

3. <path_app_elf>: Path to the app ELF file

4. [boot_args]: Bootargs. Examples: ssid=InnoPhase, passphrase=Inno@9070

Examples:

1. If there is only one Talaria TWO device with USB interface connected:

+-----------------------------------------------------------------------+
| Note: A single line command                                           |
|                                                                       |
| ./script/boot.py --device /dev/ttyUSB2 --reset=evk42                  |
| apps/iperf3/bin/iperf3.elf ssid=InnoPhase passphrase=Inno@9070        |
+=======================================================================+
+-----------------------------------------------------------------------+

2. If there are multiple Talaria TWO devices connected:

+-----------------------------------------------------------------------+
| Note: A single line command                                           |
|                                                                       |
| ./script/boot.py --device /dev/ttyUSB2 --SN 15100010 --reset=evk42    |
| apps/iperf3/bin/iperf3.elf ssid=InnoPhase passphrase=Inno@9070        |
+=======================================================================+
+-----------------------------------------------------------------------+

List Parameters (Manual in Script)

Type boot.py --help to bring up the manual of the boot.py command list:

|Text Description automatically generated|

|A computer screen with white text Description automatically generated|

Figure 13: boot.py - command list

Using flash.py
--------------

1. Command syntax to run flash.py

+-----------------------------------------------------------------------+
| <path_script>/flash.py [device] <pos_arg> [boot_args]                 |
+=======================================================================+
+-----------------------------------------------------------------------+

where:

a. <path_script>: Path to the script file. Default: Current folder

b. [device]: Communication device ID with path.

..

   For example: COMn(Windows), /dev/ttyUSBn(Linux),
   ftdi://ftdi:xxxxxx(Windows libusbK installed).

   Default: Windows-none, Linux-/dev/ttyUSB2

c. <pos_arg>: Positional argument

d. [boot_args]: Bootargs

Example:

+-----------------------------------------------------------------------+
| ./script/flash.py --device /dev/ttyUSB2 to_json ./brd_0183_part.json  |
+=======================================================================+
+-----------------------------------------------------------------------+

2. List Parameters (Manual in Script)

Type flash.py --help to bring up the manual of the flash.py command
list:

|image1|

|A screenshot of a computer program Description automatically generated|

Figure 14: flash.py - command list

Using storage.py
----------------

1. Command syntax to run storage.py

+-----------------------------------------------------------------------+
| <path_script>/storage.py [device] <pos_arg> [boot_args]               |
+=======================================================================+
+-----------------------------------------------------------------------+

where:

a. <path_script>: Path to the script file. Default: Current folder

b. [device]: Communication device ID with path.

..

   For example: COMn, /dev/ttyUSBn, ftdi://ftdi:xxxxxx. Default:
   Windows-none, Linux-/dev/ttyUSB2

c. <pos_arg>: Positional argument

d. [boot_args]: Bootargs

Example:

Connect to the Access Point configured in your **nprofile.json** as

+-----------------------------------------------------------------------+
| ./script/storage.py write nprofile.json /data/ nprofile.json          |
+=======================================================================+
+-----------------------------------------------------------------------+

2. List Parameters (Manual in Script)

Type storage.py --help to bring up the manual of the storage.py command
list:

|image2|

Figure 15: storage.py command script

.. |Text Description automatically generated| image:: media/image1.png
   :width: 5.90551in
   :height: 5.8465in
.. |A computer screen with white text Description automatically generated| image:: media/image2.png
   :width: 5.90694in
   :height: 1.94028in
.. |image1| image:: media/image3.png
   :width: 5.84648in
   :height: 5.83038in
.. |A screenshot of a computer program Description automatically generated| image:: media/image4.png
   :width: 5.86736in
   :height: 2.00694in
.. |image2| image:: media/image5.png
   :width: 5.90551in
   :height: 5.04929in
