.. _overview:

Overview
========
+----------------------------+-----------------------------------------+
| .. rubric::                | |Graphical user interface Description   |
|    :name: section          | automatically generated with medium     |
|                            | confidence|                             |
+----------------------------+-----------------------------------------+

Talaria TWO™ (INP2045)

Ultra-Low Power Multi-Protocol Wireless Platform SoC

IEEE 802.11 b/g/n, BLE 5.0

User Guide for Talaria TWO MPD Demo Tool - Overview

Release: 11-18-2022

Revision History

+-----+---------+-----------------------------------------------------+
| **  | *       | **Comments**                                        |
| Ver | *Date** |                                                     |
| sio |         |                                                     |
| n** |         |                                                     |
+-----+---------+-----------------------------------------------------+
| 0.  | 07-     | First release.                                      |
| 6.1 | 21-2020 |                                                     |
+-----+---------+-----------------------------------------------------+
| 1.0 | 09-     | Updated for SDK 2.1.1 release & MPD Tool version    |
|     | 23-2020 | v1.1.                                               |
+-----+---------+-----------------------------------------------------+
| 2.0 | 05-     | Updated for SDK 2.2 release & MPD Tool version      |
|     | 13-2021 | v2.2.                                               |
+-----+---------+-----------------------------------------------------+
| 2.1 | 07-     | Added note for PROG RAM functionality.              |
|     | 05-2021 |                                                     |
+-----+---------+-----------------------------------------------------+
| 3.0 | 08-     | Updated for SDK 2.3 release.                        |
|     | 12-2021 |                                                     |
+-----+---------+-----------------------------------------------------+
| 3.1 | 08-     | Updated for SDK 2.3.1 release.                      |
|     | 27-2021 |                                                     |
+-----+---------+-----------------------------------------------------+
| 4.0 | 09-     | Low Power Scan added as part of SDK 2.4 release –   |
|     | 21-2021 | still need to be added.                             |
+-----+---------+-----------------------------------------------------+
| 4.1 | 10-     | Updated with the following:                         |
|     | 13-2021 |                                                     |
|     |         | -  One-Click Installation of libusbk driver         |
|     |         |                                                     |
|     |         | Help option for the Tool                            |
+-----+---------+-----------------------------------------------------+
| 4.2 | 11-     | Updated Appendix with steps to assign a new EVK     |
|     | 16-2021 | serial number to device.                            |
+-----+---------+-----------------------------------------------------+
| 4.3 | 01-     | Updated Demo Tool GUI.                              |
|     | 25-2022 |                                                     |
+-----+---------+-----------------------------------------------------+
| 4.4 | 02-     | Updated MQTT broker.                                |
|     | 01-2022 |                                                     |
+-----+---------+-----------------------------------------------------+
| 4.5 | 02-     | Updated prerequisites with the requirement of       |
|     | 16-2022 | Microsoft Visual C++ Redistributable Software       |
|     |         | Package.                                            |
+-----+---------+-----------------------------------------------------+
| 5.0 | 05-     | Updated with Otti logs for MPD and iPerf3 modes as  |
|     | 16-2022 | applicable.                                         |
+-----+---------+-----------------------------------------------------+
| 5.1 | 06-     | Updated with Wireshark captures for MPD and iPref3  |
|     | 09-2022 | as applicable.                                      |
+-----+---------+-----------------------------------------------------+
| 5.2 | 06-     | Split the MPD demo tool documentation into multiple |
|     | 29-2022 | parts.                                              |
+-----+---------+-----------------------------------------------------+
| 5.3 | 07-     | Updated for SDK 2.5 release.                        |
|     | 07-2022 |                                                     |
+-----+---------+-----------------------------------------------------+
| 5.4 | 08-     | Updated driver installation for Windows OS.         |
|     | 05-2022 |                                                     |
+-----+---------+-----------------------------------------------------+
| 5.5 | 08-     | Updated list of Regulatory Domains.                 |
|     | 23-2022 |                                                     |
+-----+---------+-----------------------------------------------------+
| 6.0 | 09-     | Updated to reflect the appropriate Max_Listen_Time  |
|     | 06-2022 | for Standard Scan.                                  |
+-----+---------+-----------------------------------------------------+
| 6.1 | 10-     | Updated for SDK 2.6 release.                        |
|     | 17-2022 |                                                     |
+-----+---------+-----------------------------------------------------+
| 6.2 | 10-     | Updated to reflect the “View Menu option” of the    |
|     | 27-2022 | console.                                            |
+-----+---------+-----------------------------------------------------+
| 6.3 | 11-     | Updated with Prerequisites to run the application   |
|     | 18-2022 | in Linux.                                           |
+-----+---------+-----------------------------------------------------+

Contents
========

`Figures `__ `4 <#figures>`__

`Tables `__ `5 <#tables>`__

`Terms & Definitions `__ `5 <#terms-definitions>`__

`Introduction `__ `6 <#introduction>`__

`Prerequisites `__ `6 <#prerequisites>`__

`Using MPD Tool in Linux `__ `7 <#using-mpd-tool-in-linux>`__

`Microsoft Visual C++ Redistributable Software Package `__
`12 <#microsoft-visual-c-redistributable-software-package>`__

`Installation Instructions for libusbK Driver `__
`13 <#installation-instructions-for-libusbk-driver>`__

`Block Diagram `__ `14 <#block-diagram>`__

`GUI `__ `15 <#gui>`__

`MPD `__ `20 <#mpd>`__

`iPerf3 `__ `21 <#iperf3>`__

`Scan `__ `22 <#scan>`__

`Help `__ `24 <#help>`__

`Appendix `__ `27 <#appendix>`__

`Uninstall Instructions for libusK Driver `__
`27 <#uninstall-instructions-for-libusk-driver>`__

`New Serial Number to Device `__
`30 <#new-serial-number-to-device>`__

`References `__ `33 <#references>`__

`Support `__ `34 <#support>`__

`Disclaimers `__ `35 <#disclaimers>`__

Figures
=======

`Figure 1: Folder Contents `__ `6 <#_Ref59048189>`__

`Figure 2: Signature failed window `__ `7 <#_Ref43368353>`__

`Figure 3: Update device driver for Talaria TWO Evaluation Board `__
`9 <#_Ref110527504>`__

`Figure 4: Talaria TWO Evaluation board under "libusbk USB Devices”
driver `__ `9 <#_Ref110527511>`__

`Figure 5: User Account Control authentication to complete driver
installation `__ `10 <#_Ref106387838>`__

`Figure 6: User Account Control authentication to delete unwanted
libusbk drivers `__ `11 <#_Ref106388164>`__

`Figure 7: Error message for missing Microsoft Visual C++
Redistributable Software Package `__ `12 <#_Ref95925999>`__

`Figure 8: Listing devices in Zadig `__ `13 <#_Ref43128814>`__

`Figure 9: Updating Talaria TWO USB driver to libusbK `__
`13 <#_Toc59047199>`__

`Figure 10: Block Diagram `__ `14 <#_Toc59047203>`__

`Figure 11: Demo Tool GUI `__ `15 <#_Ref44066645>`__

`Figure 12: Console window `__ `17 <#_Ref117785088>`__

`Figure 13: Console – View Menu option `__ `17 <#_Toc117784731>`__

`Figure 14: PROG RAM alert message `__ `18 <#_Ref91516971>`__

`Figure 15: Error communicating with FTDI device `__
`19 <#_Ref110622118>`__

`Figure 16: MPD tab `__ `20 <#_Ref43374837>`__

`Figure 17: Selecting iPerf3 `__ `21 <#_Ref105753894>`__

`Figure 18: Scan tab `__ `22 <#_Toc116904534>`__

`Figure 19: Help Frame `__ `24 <#_Ref105755347>`__

`Figure 20: Default Jumper/Switch setting Window `__
`25 <#_Ref87455047>`__

`Figure 21: Default Jumper/Switch setting Window during Tool
Launch `__ `26 <#_Ref87455011>`__

`Figure 22: Device Manager `__ `27 <#_Ref59136318>`__

`Figure 23: Update Devices `__ `28 <#_Toc116904539>`__

`Figure 24: Select the device driver `__ `29 <#_Toc116904540>`__

`Figure 25: libusbK driver installed `__ `31 <#_Ref87869542>`__

`Figure 26: Serial number updated `__ `31 <#_Toc119663108>`__

`Figure 27: New serial number in flash `__ `32 <#_Toc119663109>`__

Tables
======

`Table 1: Usage of ports in the evaluation board `__
`8 <#_Ref110350619>`__

`Table 2: Default values for Standard Wi-Fi and Low-Power Wi-Fi
Scan `__ `23 <#_Ref88476954>`__

Terms & Definitions
====================

AP Access Point

ARP Address Resolution Protocol

COM Composite Device Driver

ELF Extensible Linking Format

EVK Evaluation Kit

FTDI Future Technology Devices International

GARP Gratuitous Address Resolution Protocol

GUI Graphical User Interface

HTTP Hyper Text Transfer Protocol

HTTPS Hyper Text Transfer Protocol Secure

iPerf Internet Performance Working Group

MPD Multipurpose Demo

MQTT Message Queuing Telemetry Transport

SSID Service Set Identifier

TCP Transmission Control Protocol

UDP User Datagram Protocol

URL Uniform Resource Locator

USB Universal Serial Bus

Introduction
============

This document provides an overview of the Talaria TWO MPD Demo Tool,
which is a GUI tool that enables quick evaluation of power consumption
and throughput performances of Talaria TWO modules. This tool is bundled
with two applications:

-  Multipurpose Demo (MPD) primarily intended to verify power
   consumption under various protocol scenarios (such as TCP, UDP, HTTP
   etc.)

-  iPerf3 application to showcase throughput performance

-  Standard scan and Low power scan, which enables to configure
   different scan feature

**Note**: A detailed description of the different MPD, iPerf3 and Scan
modes are described in Part 2 and Part 3 of the MPD Demo Tool User Guide
respectively.

This GUI is intended for use with the INP3010 and INP3011 Talaria TWO
evaluation boards to enable easy programming and accelerated
evaluations.

Prerequisites
==============

Each release of the Demo Tool is equipped with binaries for Windows and
Linux operating systems, and signed firmware images (ELFs) for MPD and
iPerf3 applications. Though this document specifically describes the use
of the GUI on a Windows platform, the procedure is similar for Linux OS
as well. The content of the release is shown in Figure 1

Application INP_T2_Demo_Windows.exe is for Windows platform while
INP_T2_Demo_Linux is for the Linux OS.

|Graphical user interface, application Description automatically
generated|

Figure 1: Folder_Contents

Using MPD Tool in Linux
-----------------------

There are two ways in which the INP_T2_Demo_Linux can be used in Linux:

1. Run the INP_T2_Demo_Linux tool from terminal with sudo command. For
   example:

+-----------------------------------------------------------------------+
| sudo                                                                  |
| /home/                                                                |
| sdk_2.6/pc_tools/MPDDownload_Tool/bin/INP_T2_DemoT2DownloadTool_Linux |
+-----------------------------------------------------------------------+

2. Double click on INP_T2_Demo_Linux.

..

   Add udev rules and folder access permission to enable double click
   feature. Execute the following steps:

   Step 1: Create Libusb_T2.rules file in */etc/udev/rules.d* directory.

   Step 2: Add the following rules to Libusb_T2.rules file.

   **Libusb_T2.rules:**

+-----------------------------------------------------------------------+
| SUBSYSTEMS==”usb”, ATTRS{idVendor}==”0403”, ATTRS{idProduct}==”6011”, |
| GROUP=”users”, MODE=”0666”                                            |
+-----------------------------------------------------------------------+

..

   In case of Permission Denied error, execute the following step (Step
   3) to extend folder access permission.

   Step 3: Run the following command in the terminal to extend
   permissions to the selected folder and its files.

+-----------------------------------------------------------------------+
| sudo chmod -R a+rwx /Path/to/sdk folder                               |
+-----------------------------------------------------------------------+

The Demo tool verifies the signature of the ELFs prior to downloading it
onto the evaluation board. In case the ELFs are tampered with, an error
message as shown in Figure 2 is printed on the console.

|image1|

Figure 2: Signature failed window

The Talaria TWO evaluation board uses FT4323h, which is a 4-port USB to
UART converter with MPSEE support. By default, these ports enumerate as
COM ports in Windows OS which does not take advantage of the MPSEE
capabilities of the FTDI device. The usage of these ports in the
evaluation board is given in Table 1.

+-------------+--------------------------------------------------------+
| **Port**    | **Usage**                                              |
+-------------+--------------------------------------------------------+
| **A**       | Connected to JTAG pins, this enables JTAG debugging    |
|             | using OpenOCD                                          |
+-------------+--------------------------------------------------------+
| **B**       | Connected to EN_CHIP pin, which enables resetting the  |
|             | module                                                 |
+-------------+--------------------------------------------------------+
| **C**       | Connected to UART pins, this is used for programming   |
|             | the module                                             |
+-------------+--------------------------------------------------------+
| **D**       | Connected to GPIO17 pin which is the default debug log |
|             | console port                                           |
+-------------+--------------------------------------------------------+

Table 1: Usage of ports in the evaluation board

To utilize these capabilities, on Windows OS, libusbK driver needs to be
installed to communicate and control the Talaria TWO module via the FTDI
device on the evaluation board. The tools/applications provided by
InnoPhase will use this driver.

Talaria TWO Demo Tool comes with an option of One-Click Installation of
libusbk driver. In case the driver is not installed, the tool will ask
for user confirmation to install this driver. If the user selects yes,
various User Account Control authentication screens will appear to
complete the driver installation (as shown in Figure 5).

**Note**:

1. In case of any other unwanted libusbk drivers that are already
   installed, the tool will automatically uninstall the unwanted
   drivers. This action needs User Account Control authentication
   screens shown in Figure 6, in addition to Figure 5. Each unwanted
   drives will require a separate User Account Control authentication
   for uninstallation.

2. Talaria TWO Evaluation Board may get detected under any already
   installed device driver (using libusbk driver). In this case, the
   tool will follow the procedure of One-Click Installation of libusbk
   driver (as shown in Figure 5), and might get completed a with pop-up
   message “Driver Installation Failed”. This will result in any one of
   the following two conditions:

   a. Device found: EVK serial number field in the download tool GUI is
      populated with appropriated EVK serial number. In this case,
      ignore the error message “Driver Installation Failed” and continue
      using the tool. To avoid this from happening repeatedly, update
      the driver for Talaria TWO Evaluation Board to “InnoPhase T2
      Evaluation Board” driver, from device manager (as shown in Figure
      3). Then, ensure the Talaria TWO Evaluation Board is detected
      under “libusbK USB Devices” in device manager (as shown in Figure
      4).

..

   |image2|\ |image3|

Figure 3: Update device driver for Talaria TWO Evaluation Board

b. No device found: Manually install the driver using instructions from
   section: Installation Instructions for libusbK Driver and ensure that
   the Talaria TWO Evaluation Board is detected under “libusbK USB
   Devices” driver (as shown in Figure 4).

..

   |image4|

Figure 4: Talaria TWO Evaluation board under "libusbk USB Devices”
driver

3. Even after successful installation of the driver, there might be
   possibility of the device not being identified for the first time. In
   this case, close the tool and re-open it. The user is notified of the
   same through a pop-up message: “No Device Connected. Please close and
   reopen the Tool.”.

|image5|

Figure 5: User Account Control authentication to complete driver
installation

From Figure 5:

Image 1: Pop-up message for user confirmation, where the user chooses
Yes.

Image 2: On clicking Yes, windows authentication prompt appears on Task
bar.

Image 3: Click on Yes in the next window.

Image 4: Click Yes for the subsequent User Account Control
authentication to complete driver installation.

Image 5: Pop-up message indicating successful driver installation.

Image 6: Pop-up message, in case of user chooses No.

Figure 6: User Account Control authentication to delete unwanted libusbk
drivers

Figure 6: User Account Control authentication to delete unwanted libusbk
drivers

|image6|

From Figure 6:

Image 1: Pop-up message for user confirmation, where the user chooses
Yes.

Image 2: Click Yes for the subsequent User Account Control
authentication to delete unwanted drivers.

Image 3: Pop-up message indicating successful driver installation.

Image 4: Pop-up message, in case of user chooses No.

In case the driver installation using Talaria TWO Demo Tool is not
successful, the user can manually install the driver using instructions
in section: Installation Instructions for libusbK Driver. Uninstall
instructions for this driver is available in section: Uninstall
Instructions for libusK Driver.

Microsoft Visual C++ Redistributable Software Package
-----------------------------------------------------

Microsoft Visual C++ Redistributable software package is a prerequisite
for Windows platform to run the application INP_T2_Demo_Windows.exe
successfully. Incase this software package is not installed on the
Windows platform, application will not launch, leading to a fatal error
message as shown in Figure 7.

In such a scenario, install the Microsoft Visual C++ Redistributable
software package using the link
https://www.microsoft.com/en-in/download/details.aspx?id=48145 and
relaunch the application.

|image7|

Figure 7: Error message for missing Microsoft Visual C++ Redistributable
Software Package

Installation Instructions for libusbK Driver
--------------------------------------------

Download the free software Zadig, available here: -
https://zadig.akeo.ie/\ **.** Connect your Windows PC or Laptop to the
evaluation board using the provided USB cable. Now, open Zadig and click
on Options. Select List All Devices and deselect Ignore Hubs or
Composite Parents as shown in Figure 8.

|image8|

Figure 8: Listing devices in Zadig

To establish communication with Talaria TWO module via the FTDI device
on the InnoPhase Evaluation Board, the Talaria TWO USB driver must be
libusbK. In case the current driver is not libusbK, use the drop-down
menu to select libusbK and click on Replace Driver which will update the
drivers to libusbK.

|Graphical user interface, text, application, Word Description
automatically generated|

Figure 9: Updating Talaria TWO USB driver to libusbK

Block Diagram
=============

|image9|

Figure 10: Block Diagram

GUI
===

On launching the application, the GUI window as shown in Figure 11 will
come into view.

**Note**: In case of windows display setting Scale and layout is more
than 125%, GUI window might go out of screen.

|image10|

Figure 11: Demo Tool GUI

1. **Boot Target**: Connected EVKs appear in the EVK serial number
   drop-down and the appropriate EVK can be selected.

2. **AP Options**: The SSID and Passphrase entered in the respective
   fields will connect the EVK board to the Access Point. Once
   connected, as per requirement MPD/iPerf3/Scan applications can be
   loaded by selecting the appropriate tab

3. **Configure the Application**: Configure the Setup Parameters:

   a. **Turn On deep sleep mode**: When the processor is idle or is
      waiting for an event or data to occur or be received, turning ON
      the Turn On deep sleep mode feature by checking the box adjacent
      to the field will put Talaria TWO in a power saving mode.

   b. **Select Regulatory Domain**: Depending on their region of
      operation, the user can select any one of the following
      appropriate regulatory domains to establish a connection between
      the EVK board and the Access Point:

      i.   FCC

      ii.  ETSI

      iii. TELEC

      iv.  KCC

4. **Program and Reset the Device**:

   a. **Reset**:

..

   Reload the application in Flash memory

b. **CLEAR Flash**:

..

   Erase the application in Flash memory

c. **PROG Ram & Start Test**:

..

   Program the application to RAM memory

d. **PROG Flash & Start Test**:

..

   Program the application to Flash memory

The console window is as shown in Figure 12.

|Graphical user interface, text, application Description automatically
generated|

Figure 12: Console window

|image11|

Figure 13: Console – View Menu option

where,

1. **Clear Console**: Clears the content in the console window.

2. **AutoScroll Disable/Enable**: Turns OFF/ON Autoscroll contents in
   the console window.

**Note**:

1. PROG RAM will clear the application from Flash. The user is alerted
   of the same during PROG RAM through a pop-up message as shown in
   Figure 14. User can select the Do not show again checkbox to stop
   this pop-up message from appearing next time.

..

   |image12|

Figure 14: PROG RAM alert message

2. Keeping this tool idle for a while (around 2 to 3 hours), may lead to
   loss of communication to the EVK device. This is indicated in the
   console as “Error communicating with FTDI device”, as show in Figure
   15. Workaround for this is as follows:

   a. Close the tool

   b. Unplug & re-plug the EVK

   c. Re-open the tool again

..

   |Graphical user interface, text Description automatically generated|

Figure 15: Error communicating with FTDI device

MPD
----

1. Enter the APs SSID and passphrase where, DTIM in the AP is set to 1.

2. To automatically load the signed firmware image for MPD application,
   select the MPD tab as shown in Figure 16.

3. For all the modes, the Keep Alive Wake time is fixed as 2 in the
   application. This time is the time window in milliseconds during
   which Talaria TWO will wait in receive mode before going to sleep.

|image13|

Figure 16: MPD tab

**Note**: Check the Show checkbox to see the passphrase value.

For more information on the different modes in which the MPD application
can be used, refer document: UG_Demo_Tool_Part_2_MPD.pdf
(*sdk_x.y\\pc_tools\\MPD\\doc*).

**Note**: x and y in sdk_x.y refer to the SDK release version.

iPerf3
-------

The iperf.exe application can be downloaded from the following link:
https://iperf.fr/iperf-download.php

1. Enter the SSID and passphrase.

2. To automatically load the signed firmware image for iPerf3
   application, select the iPerf3 tab as shown in Figure 17.

3. It is recommended to click on PROG Flash & Start Test to start
   Talaria TWO as a Server.

|image14|

Figure 17: Selecting iPerf3

**Note**:

1. In case the PROG Ram & Start Test option does not load the
   application, click on PROG Flash & Start Test.

2. Work around for the above limitation is to click Reset before
   clicking on PROG Ram & Start Test again.

3. Work around for error with CLEAR Flash option: Click Reset before
   clicking on CLEAR Flash again.

For more information on the different modes in which the iPerf3
application can be used, refer document:
UG_Demo_Tool_Part_3_iPerf3_and_Scan.pdf (*sdk_x.y\\pc_tools\\MPD\\doc*).

Scan
----

The Scan tab allows the user to actively scan for nearby Access Points.

|image15|

Figure 18: Scan tab

**Choose the Scheme**: User can choose Standard Wi-Fi Scan or Low-Power
Wi-Fi Smart Scan for scanning.

1. **Standard Wi-Fi Scan**: In this scan mode, Talaria TWO scans each
   channel with the configured scan time (default being 40ms).

2. **Low Power Wi-Fi Smart Scan**: In this scan mode, Talaria TWO
   reduces the overall current consumption by enabling dynamic dwelling
   and napping features.

Default values of parameters for Standard Wi-Fi and Low-Power Wi-Fi scan
are shown in Table 2. Depending on the user’s choice of the scanning
scheme, respective default values will be set to corresponding
parameters.

+----------------------+---------------+---------------+---------------+
| **Default Value**    |               |               |               |
+----------------------+---------------+---------------+---------------+
| **Parameters**       | **Standard    | **Low-Power   | **Remark**    |
|                      | Wi-Fi scan**  | Wi-Fi Scan**  |               |
+----------------------+---------------+---------------+---------------+
| **No_of_Probes**     | 2             | 1             | Configurable  |
+----------------------+---------------+---------------+---------------+
| **Ide_Slots**        | 3             | 3             | Configurable  |
+----------------------+---------------+---------------+---------------+
| **Select the         | 11b_1Mbps     | 11b_6Mbps     | Configurable  |
| Required Probe       |               |               |               |
| Rate**               |               |               |               |
+----------------------+---------------+---------------+---------------+
| **NAP Enable**       | No            | Yes           | Hard coded    |
+----------------------+---------------+---------------+---------------+

Table 2: Default values for Standard Wi-Fi and Low-Power Wi-Fi Scan

The following scan parameters can be configured from the tool:

1. SSID (optional): Providing the SSID helps enable scan for a specific
   AP.

2. BSSID (optional): Providing the BSSID helps enable scan for a
   specific AP.

3. No_of_probes: Maximum number of probes to send in an active scan.

4. Idle slots: Maximum number of idle slots to decide whether the user
   should keep listening or not.

5. Min_Listen_Time(ms): Minimum amount of time (in milliseconds) to
   listen for probe responses on the channel after transmitting the
   probe request.

6. Max_Listen_Time(ms): Maximum amount of time (in milliseconds,
   including listen and probe requests) to stay on the channel.

7. Wait_Time(ms): Idle time between each channel (giving other parties
   access to the media).

8. Scan Interval (ms): Time duration in milliseconds in which Talaria
   TWO scans the vicinity for networks.

9. Probe_rate: The rate as defined by rate_t used to transmit the probe
   request. If this field is set to 0xffff, no probes will be sent and
   the scan will only be passive.

For more information on the Standard Wi-Fi and Low Power Wi-Fi scan,
refer document: UG_Demo_Tool_Part_3_iPerf3_and_Scan.pdf
(*sdk_x.y\\pc_tools\\MPD\\doc*).

Help
----

Help provides information about default Jumper/Switch settings. Clicking
on Default Jumper Setting as shown in Figure 19 will pop-up new window
with default Jumper/Switch settings information as shown in Figure 20.

|image16|

Figure 19: Help Frame

|A picture containing schematic Description automatically generated|

Figure 20: Default Jumper/Switch setting Window

**Note**: Default Jumper/Switch setting window will appear every time
when tool is launched, as shown in Figure 21. To turn this feature OFF
permanently, check the Do not show again option and close the window.

|A picture containing graphical user interface Description automatically
generated|

Figure 21: Default Jumper/Switch setting Window during Tool Launch

Appendix
========

Uninstall Instructions for libusK Driver
----------------------------------------

To uninstall libusbK and retrieve COM ports, follow the following steps:

1. Go to Device Manager. Expand the libusbK USB Devices and right click
   on the InnoPhase T2 Evaluation Board (Composite Parent). Click on
   Update Driver as shown in Figure 22.

Figure 22: Device Manager

|A screenshot of a social media post Description automatically
generated|

2. On the new window, click on Let me pick from a list of available
   drivers on my computer option and click on Next.

|image17|

Figure 23: Update Devices

3. Select USB Composite Device and install the same for reinstalling COM
   posts.

|image18|

Figure 24: Select the device driver

New Serial Number to Device
---------------------------

There might be certain instances when the EVK serial number is absent or
appears to be corrupted on a Talaria TWO (T2) device.

The following are the setups needed to create a new serial number
created and write it to the Talaria TWO flash using the tool. This
process of creating a new serial number and writing it is executed
automatically.

1. Ensure the device is connected to the PC

If the connection from Talaria TWO device is not found, unplug and
re-plug the cable, to ensure the device is recognized by the host
machine.

2. Run the Zadig Tool to Install the libusbK driver (Windows PC only)

The libusbK driver installation is for Windows machine only.

The interface provided by libusbK driver is supported natively on Linux
machine, hence, no additional installation is required on Linux.

On launching Zadig, the devices that are listed on it might have a
slightly different name tag with respect to the Talaria TWO device. This
is dependent on the how the user-installed drivers were used the
previous time. For example:

-  The driver has been uninstalled, or

-  The port has been updated to a COM port or

-  The way in which the device list has been updated by the machine’s
   Device Manager is different.

   a. If the InnoPhase T2 Evaluation Board is shown on the list, either
      InnoPhase T2 Evaluation Board (Composite Parent), or InnoPhase T2
      Evaluation Board, go ahead to install the driver per standard
      procedure.

   b. If the InnoPhase T2 Evaluation Board is not shown on the list, a
      device by the name Quad RS232-HS should be on the list of instead.

Ensure to check the following:

c. There should be only one Talaria TWO device that is connected, to
   which the new serial number will be written to.

d. If there are any other known devices that are probably using the
   libusbK driver, disconnect them, unplug/re-plug the Talaria TWO
   device and re-launch Zadig to ensure Quad RS232-HS is the device from
   the Talaria TWO connection.

Select the Quad RS232-HS (Composite Parent) device and select the driver
libusbK and click on Replace Driver.

After the installation, the Talaria TWO device with the libusbK driver
should be shown as evident in Figure 25:

   |image19|

Figure 25: libusbK driver installed

3. Launch the Tool (Detecting absence of Serial Number and creating a
   new one in device).

On launching, the tool checks if the serial number is present on the
device. If it is not found, the tool will automatically generate one and
write it to the device as the new serial number.

   |image20|

Figure 26: Serial number updated

Format of the serial number:

+-----------------------------------------------------------------------+
| <year_stamp>-<integer>                                                |
+-----------------------------------------------------------------------+

where,

-  <year_stamp>: current year (for example: 2021)

-  <integer>: formed from the sum of last 3 octets (in decimal) of the
   mac address found in the device.

Before relaunching the tool, unplug and re-plug the device to have the
connection of the device refreshed by the host machine.

4. Re-Launch of the Tool (Serial Number Detected)

Now the device has a new serial number in its flash.

   |image21|

Figure 27: New serial number in flash

References
==========

1. UG_Download_Tool.pdf

(*sdk_x.y\\pc_tools\\Download_Tool\\doc\\UG_Download_Tool.pdf*).

2. UG_Demo_Tool_Part_2_MPD.pdf

(*sdk_x.y\\pc_tools\\pc_tools\\MPD\\doc\\*
UG_Demo_Tool_Part_2_MPD\ *.pdf*).

3. UG_Demo_Tool_Part_3_iPerf3_and_Scan.pdf

(*sdk_x.y\\pc_tools\\pc_tools\\MPD\\doc\\* UG_Demo_Tool_Part_3\_
iPerf3_and_Scan\ *.pdf*).

Support
=======

1. Sales Support: Contact an InnoPhase sales representative via email –
   sales@innophaseiot.com

2. Technical Support:

   a. Visit: https://innophaseiot.com/contact/

   b. Also Visit: https://innophaseiot.com/talaria-two-modules/

   c. Contact: support@innophaseiot.com

InnoPhase is working diligently to provide customers outstanding support
to all customers.

Disclaimers
===========

Limited warranty and liability — Information in this document is
believed to be accurate and reliable. However, InnoPhase IoT
Incorporated does not give any representations or warranties, expressed
or implied, as to the accuracy or completeness of such information and
assumes no liability associated with the use of such information.
InnoPhase IoT Incorporated takes no responsibility for the content in
this document if provided by an information source outside of InnoPhase
IoT Incorporated.

InnoPhase IoT Incorporated disclaims liability for any indirect,
incidental, punitive, special or consequential damages associated with
the use of this document, applications and any products associated with
information in this document, whether or not such damages are based on
tort (including negligence), warranty, including warranty of
merchantability, warranty of fitness for a particular purpose, breach of
contract or any other legal theory. Further, InnoPhase IoT Incorporated
accepts no liability and makes no warranty, express or implied, for any
assistance given with respect to any applications described herein or
customer product design, or the application or use by any customer’s
third-party customer(s).

Notwithstanding any damages that a customer might incur for any reason
whatsoever, InnoPhase IoT Incorporated’ aggregate and cumulative
liability for the products described herein shall be limited in
accordance with the Terms and Conditions of identified in the commercial
sale documentation for such InnoPhase IoT Incorporated products.

Right to make changes — InnoPhase IoT Incorporated reserves the right to
make changes to information published in this document, including,
without limitation, changes to any specifications and product
descriptions, at any time and without notice. This document supersedes
and replaces all information supplied prior to the publication hereof.

Suitability for use — InnoPhase IoT Incorporated products are not
designed, authorized or warranted to be suitable for use in life
support, life-critical or safety-critical systems or equipment, nor in
applications where failure or malfunction of an InnoPhase IoT
Incorporated product can reasonably be expected to result in personal
injury, death or severe property or environmental damage. InnoPhase IoT
Incorporated and its suppliers accept no liability for inclusion and/or
use of InnoPhase IoT Incorporated products in such equipment or
applications and such inclusion and/or use is at the customer’s own
risk.

All trademarks, trade names and registered trademarks mentioned in this
document are property of their respective owners and are hereby
acknowledged.

.. |Graphical user interface Description automatically generated with medium confidence| image:: media/image1.jpeg
   :width: 3.97014in
   :height: 1.5in
.. |Graphical user interface, application Description automatically generated| image:: media/image2.png
   :width: 5.90486in
   :height: 1.48333in
.. |image1| image:: media/image3.png
   :width: 1.96806in
   :height: 1.50625in
.. |image2| image:: media/image4.png
   :width: 1.98403in
   :height: 0.2in
.. |image3| image:: media/image5.png
   :width: 3.93701in
   :height: 2.08404in
.. |image4| image:: media/image6.png
   :width: 4.72441in
   :height: 0.55425in
.. |image5| image:: media/image7.png
   :width: 5.90486in
   :height: 5.41528in
.. |image6| image:: media/image8.png
   :width: 5.90486in
   :height: 3.93889in
.. |image7| image:: media/image9.png
   :width: 4.72441in
   :height: 1.80695in
.. |image8| image:: media/image10.png
   :width: 4.72431in
   :height: 2.08611in
.. |Graphical user interface, text, application, Word Description automatically generated| image:: media/image11.png
   :width: 4.92083in
   :height: 2.15556in
.. |image9| image:: media/image12.png
   :width: 7.08661in
   :height: 2.8009in
.. |image10| image:: media/image13.png
   :width: 5.90486in
   :height: 5.42847in
.. |Graphical user interface, text, application Description automatically generated| image:: media/image14.png
   :width: 5.90486in
   :height: 1.325in
.. |image11| image:: media/image15.png
   :width: 5.90486in
   :height: 1.82222in
.. |image12| image:: media/image16.png
   :width: 5.90486in
   :height: 5.2in
.. |Graphical user interface, text Description automatically generated| image:: media/image17.png
   :width: 5.90486in
   :height: 1.25in
.. |image13| image:: media/image18.png
   :width: 5.90486in
   :height: 1.83056in
.. |image14| image:: media/image19.png
   :width: 5.90486in
   :height: 2.50556in
.. |image15| image:: media/image20.png
   :width: 5.90486in
   :height: 4.70139in
.. |image16| image:: media/image21.png
   :width: 5.90486in
   :height: 5.23472in
.. |A picture containing schematic Description automatically generated| image:: media/image22.png
   :width: 4.72431in
   :height: 7.27986in
.. |A picture containing graphical user interface Description automatically generated| image:: media/image23.png
   :width: 4.72431in
   :height: 7.33542in
.. |A screenshot of a social media post Description automatically generated| image:: media/image24.png
   :width: 5.90486in
   :height: 4.31944in
.. |image17| image:: media/image25.png
   :width: 5.90486in
   :height: 4.37153in
.. |image18| image:: media/image26.png
   :width: 5.90486in
   :height: 4.36458in
.. |image19| image:: media/image27.png
   :width: 3.93701in
   :height: 1.19338in
.. |image20| image:: media/image28.png
   :width: 5.90486in
   :height: 2.50972in
.. |image21| image:: media/image29.png
   :width: 5.90551in
   :height: 2.0865in
