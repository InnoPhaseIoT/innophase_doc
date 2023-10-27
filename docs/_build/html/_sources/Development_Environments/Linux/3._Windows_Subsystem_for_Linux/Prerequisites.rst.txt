.. _Development_Environments/Linux/Windows_Subsystem_for_Linux/Prerequisites:


Windows Subsystem for Linux
---------------------------

Windows Subsystem for Linux is a compatibility layer for running Linux
binary executables natively on Windows OS.

1. Control Panel -> Programs -> Programs and Features -> Click Turn
   Windows feature on and off

..

   |image1|

Figure 1: Programs and features

2. Tick for Virtual Machine Platform and Windows Subsystem for Linux ->
   OK

..

   |image2|

Figure 2: Turn Windows features ON or OFF

3. Restart the system at this stage by clicking on Restart now.

|image3|

Figure 3: Restart the system

Installing Linux
----------------

Install the latest version of Linux:

1. Menu tab -> Microsoft store -> In Search option type Ubuntu. Which
   will show the results for Ubuntu, Click on Get to download the latest
   version of Ubuntu.

..

   |image4|

Figure 4: Open Microsoft store to install Ubuntu

2. Once the download is complete, open Ubuntu from the Menu tab and
   provide the following when prompted:

   a. Enter new UNIX username

   b. New password

   c. Retype new password

..

   |image5|

Figure 5: Username and password

3. This will open a terminal window in the directory in which commands
   can be typed.

..

   |Text Description automatically generated with low
   confidence|\ |image6|

Figure 6: Terminal window

Installing Necessary Packages
-----------------------------

In the terminal window, execute the following commands entering the
password which was set in Figure 6 when prompted.

+-----------------------------------------------------------------------+
| sudo apt update                                                       |
+=======================================================================+
+-----------------------------------------------------------------------+

+-----------------------------------------------------------------------+
| sudo apt upgrade                                                      |
+=======================================================================+
+-----------------------------------------------------------------------+

+-----------------------------------------------------------------------+
| sudo apt-get update                                                   |
+=======================================================================+
+-----------------------------------------------------------------------+

+-----------------------------------------------------------------------+
| lsb_release -a                                                        |
+=======================================================================+
+-----------------------------------------------------------------------+

Console output:

|image7|

Figure 7: Installing necessary packages

Accessing WSL Files from Windows
--------------------------------

An important thing to note about WSL is that it hosts its own file
system. The files you access within the WSL terminal are separate from
your regular Windows file system. You can integrate your WSL files into
the Windows File Explorer by changing to a particular directory in the
WSL terminal and using the command:

+-----------------------------------------------------------------------+
| explorer.exe                                                          |
+=======================================================================+
+-----------------------------------------------------------------------+

Install arm-none-eabi Toolchain
-------------------------------

Install the GCC compiler packages.

+-----------------------------------------------------------------------+
| sudo apt install gcc-arm-none-eabi                                    |
+=======================================================================+
+-----------------------------------------------------------------------+

+-----------------------------------------------------------------------+
| arm-none-eabi-gcc --version                                           |
+=======================================================================+
+-----------------------------------------------------------------------+

Console output:

|image8|

Figure 8: GCC compiler packages

Install Python3 and packages
----------------------------

In any terminal window, execute the following commands to install
Python3 and other Python packages that will be needed. Enter the
password as prompted which was set in Figure 6.

+-----------------------------------------------------------------------+
| sudo apt install python3 -y                                           |
+=======================================================================+
+-----------------------------------------------------------------------+

+-----------------------------------------------------------------------+
| sudo apt install python3-pip -y                                       |
+=======================================================================+
+-----------------------------------------------------------------------+

+-----------------------------------------------------------------------+
| python3 --version                                                     |
+=======================================================================+
+-----------------------------------------------------------------------+

Console output:

|image9|

Figure 9: Installing Python3 & packages

Setting Execute Permissions for SDK Scripts
-------------------------------------------

Compile the InnoPhase SDK

1. Open a terminal in the directory, for example: *sdk_x.y/apps*

2. Execute the make command. Use the ELFs generated in the application’s
   out folder.

+-----------------------------------------------------------------------+
| make                                                                  |
+=======================================================================+
+-----------------------------------------------------------------------+

**Note**: User can also compile the required application, for example:
*sdk_x.y/apps/helloworld/*.

3. By default, in the SDK package, the ELFs can be used from the
   application’s bin folder.

**Note**: x and y refer to the SDK release version. For example:
sdk_2.5/doc.

|image10|

Figure 10: Compiling the InnoPhase SDK

Programming Talaria TWO using Download Tool
-------------------------------------------

Program the helloworld.elf (*sdk_x.y\\apps\\helloworld\\bin*) onto
Talaria TWO using the Download Tool:

1. Launch the Download tool provided with InnoPhase Talaria TWO SDK.

2. In the GUI window:

   a. Programming: Click on Clear Flash and ensure the output is as
      follows:

+-----------------------------------------------------------------------+
| UART:NWWWWWAEBuild $Id: git-b664be2af $                               |
|                                                                       |
| app=gordon                                                            |
|                                                                       |
| flash: Gordon ready!                                                  |
|                                                                       |
| Y-BOOT 208ef13 2019-07-22 12:26:54 -0500 790da1-b-7                   |
|                                                                       |
| ROM yoda-h0-rom-16-0-gd5a8e586                                        |
|                                                                       |
| FLASH:P                                                               |
+=======================================================================+
+-----------------------------------------------------------------------+

b. Boot Target: Select the appropriate EVK from the drop-down

c. ELF Input: Load the helloworld.elf by clicking on Select ELF File.

d. Programming: Prog RAM or Prog Flash as per requirement.

Console output:

+-----------------------------------------------------------------------+
| UART:NWWWWWAEBuild $Id: git-b664be2af $                               |
|                                                                       |
| app=gordon                                                            |
|                                                                       |
| flash: Gordon ready!                                                  |
|                                                                       |
| Y-BOOT 208ef13 2019-07-22 12:26:54 -0500 790da1-b-7                   |
|                                                                       |
| ROM yoda-h0-rom-16-0-gd5a8e586                                        |
|                                                                       |
| FLASH:PNWWWAEBuild $Id: git-b664be2af $                               |
|                                                                       |
| Hello World                                                           |
+=======================================================================+
+-----------------------------------------------------------------------+

.. |image1| image:: ../media/image1.png
   :width: 4.72441in
   :height: 4.46017in
.. |image2| image:: ../media/image2.png
   :width: 4.72441in
   :height: 4.20901in
.. |image3| image:: ../media/image3.png
   :width: 4.72441in
   :height: 3.91847in
.. |image4| image:: ../media/image4.png
   :width: 4.72441in
   :height: 3.22075in
.. |image5| image:: ../media/image5.png
   :width: 5.90551in
   :height: 3.4203in
.. |Text Description automatically generated with low confidence| image:: ../media/image6.png
   :width: 1.00082in
.. |image6| image:: ../media/image7.png
   :width: 5.90551in
   :height: 4.19781in
.. |image7| image:: ../media/image8.png
   :width: 4.72441in
   :height: 1.32292in
.. |image8| image:: ../media/image9.png
   :width: 5.90551in
   :height: 0.64947in
.. |image9| image:: ../media/image10.png
   :width: 4.72441in
   :height: 0.37327in
.. |image10| image:: ../media/image11.png
   :width: 5.51181in
   :height: 2.89434in
