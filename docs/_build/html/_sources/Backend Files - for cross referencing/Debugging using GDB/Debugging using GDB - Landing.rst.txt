Debugging using GDB
===================

This section describes the procedure for debugging the applications
using GDB to work with OpenOCD.

Prerequisites 
==============

Install Talaria TWO SDK 
------------------------

1. Download Talaria TWO SDK from the InnoPhase portal:
   https://innophaseiot.com/portal/portal-hub/

2. Unzip the SDK in an appropriate location as per requirement.

Required Software 
------------------

1. PC with Ubuntu 20.04 (or higher).

2. GNU GDB v.10.1 (or higher).

For the above Linux set-up, refer the following user guide:
UG_Environment_Setup_for_Linux.pdf.

Execute the following Linux command in any terminal window to determine
the versions of Ubuntu and GNU GDB:

For Ubuntu version:

+-----------------------------------------------------------------------+
| lsb_release -a                                                        |
+=======================================================================+
+-----------------------------------------------------------------------+

Console output:

|A screenshot of a computer Description automatically generated|

Figure 1: Ubuntu version

For GNU GDB version:

+-----------------------------------------------------------------------+
| gdb --version                                                         |
+=======================================================================+
+-----------------------------------------------------------------------+

**Note:** In case of Ubuntu 20.04, default version of the GDB is 9.2.
Hence, GDB needs to be updated

to version 10.2 by executing the following commands:

+-----------------------------------------------------------------------+
| sudo add-apt-repository ppa:ubuntu-toolchain-r/test                   |
|                                                                       |
| sudo apt-get update                                                   |
|                                                                       |
| sudo apt-get -y --force-yes install gdb                               |
+=======================================================================+
+-----------------------------------------------------------------------+

Console output:

|A computer screen shot of a program Description automatically
generated|

Figure 2: GNU GDB version

Installing necessary packages
-----------------------------

In any terminal window, execute the following commands:

+-----------------------------------------------------------------------+
| sudo apt update                                                       |
|                                                                       |
| sudo apt install build-essential libc6-armel-cross                    |
| libc6-dev-armel-cross binutils-arm-linux-gnueabi libncurses5-dev -y   |
+=======================================================================+
+-----------------------------------------------------------------------+

Installing ARM toolchain
------------------------

From within a directory of your choice, execute the following command in
a terminal window to download the ARM toolchain:

+-----------------------------------------------------------------------+
| sudo apt install gcc-arm-none-eabi                                    |
+=======================================================================+
+-----------------------------------------------------------------------+

Installing Python3 and dependencies 
------------------------------------

In any terminal window, execute the following commands to install
Python3 and other Python packages that will be needed. Enter the
password as prompted.

+-----------------------------------------------------------------------+
| sudo apt install python3 -y                                           |
|                                                                       |
| sudo apt install python3-pip -y                                       |
|                                                                       |
| pip3 install pyelftools pyserial pyusb pyftdi ecdsa pycryptodome      |
+=======================================================================+
+-----------------------------------------------------------------------+

Installing OpenOCD
------------------

In any terminal window, execute the following command to install
OpenOCD. Enter the password as prompted.

+-----------------------------------------------------------------------+
| sudo apt install openocd -y                                           |
+=======================================================================+
+-----------------------------------------------------------------------+

Install gdb-multiarch in any terminal window. Execute the following
command to install gdb-multiarch:

+-----------------------------------------------------------------------+
| sudo apt-get install gdb-multiarch                                    |
+=======================================================================+
+-----------------------------------------------------------------------+

.. |A screenshot of a computer Description automatically generated| image:: media/image1.png
   :width: 5.51181in
   :height: 1.08302in
.. |A computer screen shot of a program Description automatically generated| image:: media/image2.png
   :width: 6.53543in
   :height: 1.05812in
