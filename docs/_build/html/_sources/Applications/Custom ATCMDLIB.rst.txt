Introduction
============

ATCMDS application provides the Wi-Fi capability to any device having a
serial (SPI/UART) interface. Host CPU uses serial commands to interface
and configure the Wi-Fi module. All AT or custom commands are parsed and
converted to the corresponding WLAN/Network calls. This mode returns the
responses in the same ASCII format as success or failure with additional
response data.

ATCMDLIB enables the user to add custom commands apart from standard
commands.

ATCMDLIB Application
====================

This section describes the application along with code snippets. The
application uses ATCMDLIB APIs to achieve the functionality.

Include ATCMDLIB header file
----------------------------

+-----------------------------------------------------------------------+
| #include “atcmd_lib.h”                                                |
+=======================================================================+
+-----------------------------------------------------------------------+

ATCMDLIB initialization
-----------------------

+-----------------------------------------------------------------------+
| if(ATCMDLIB\_ SUCCESS == atcmd_init()){                               |
|                                                                       |
| os_printf("ATCMDLIB: Ready\\n");                                      |
|                                                                       |
| }                                                                     |
|                                                                       |
| else {                                                                |
|                                                                       |
| os_printf("ATCMDLIB: Failed\\n");                                     |
|                                                                       |
| }                                                                     |
+=======================================================================+
+-----------------------------------------------------------------------+

Adding sample command function
------------------------------

+-----------------------------------------------------------------------+
| int testcmd_func(int argc , char \*argv[])                            |
|                                                                       |
| {                                                                     |
|                                                                       |
| int i;                                                                |
|                                                                       |
| os_printf("\\r\\nHello");                                             |
|                                                                       |
| for(i = 0 ; i <argc;i++){                                             |
|                                                                       |
| os_printf("\\r\\nargv[%d]=%s",i,argv[i]);                             |
|                                                                       |
| }                                                                     |
|                                                                       |
| return ATCMDLIB_SUCCESS;                                              |
|                                                                       |
| }                                                                     |
+=======================================================================+
+-----------------------------------------------------------------------+

ATCMDLIB add new command 
-------------------------

+-----------------------------------------------------------------------+
| if(ATCMDLIB_ERROR == atcmd_add("testcmd",&testcmd_func))              |
|                                                                       |
| os_printf("Failed to add command\\n");                                |
+=======================================================================+
+-----------------------------------------------------------------------+

ATCMDLIB delete command
-----------------------

+-----------------------------------------------------------------------+
| if(ATCMDLIB_ERROR == atcmd_delete("testcmd))                          |
|                                                                       |
| os_printf("Failed to delete command\\n");                             |
+=======================================================================+
+-----------------------------------------------------------------------+

ATCMDLIB command status 
------------------------

+-----------------------------------------------------------------------+
| /\*use this enum to send command status*/                             |
|                                                                       |
| typedef enum ATCMDLIB_STATUS                                          |
|                                                                       |
| {                                                                     |
|                                                                       |
| ATCMDLIB_SUCCESS =0,                                                  |
|                                                                       |
| ATCMDLIB_ERROR = 1,                                                   |
|                                                                       |
| ATCMDLIB_EINVAL = 2                                                   |
|                                                                       |
| };                                                                    |
+=======================================================================+
+-----------------------------------------------------------------------+

Running the Application 
========================

Program at_custom_cmd.elf(sdk_x.y\\examples\\at_custom_cmd\\bin) using
the Download tool:

1. Launch the Download tool provided with InnoPhase Talaria TWO SDK.

2. In the GUI window:

   a. Boot Target: Select the appropriate EVK from the drop-down

   b. ELF Input: Load the at_custom_cmd.elf by clicking on Select ELF
      File.

   c. Programming: Prog RAM or Prog Flash as per requirement.

For more details on using the Download tool, refer to the document:
UG_Download_Tool.pdf (path: *sdk_x.y/pc_tools/Download_Tool/doc*).

**Note**: x and y refer to the SDK release version. For example:
sdk_2.4/doc.

Expected Output
===============

The previously mentioned code will add an example command testcmd. The
expected output for this command will be console pint Hello followed by
arguments present in command. The code also sends OK on UART as command
status, upon successful execution of the command testcmd.

**Note**: The following console output is from SDK 2.3 release and is
applicable to the current release as well.

+-----------------------------------------------------------------------+
| Y-BOOT 208ef13 2019-07-22 12:26:54 -0500 790da1-b-7                   |
|                                                                       |
| ROM yoda-h0-rom-16-0-gd5a8e586                                        |
|                                                                       |
| FLASH:PNWWWWWWAEBuild $Id: git-f92bee540 $                            |
|                                                                       |
| $App:git-a4227ff                                                      |
|                                                                       |
| SDK Ver: sdk_2.3                                                      |
|                                                                       |
| At Custom Command Demo App                                            |
|                                                                       |
| addr e0:69:3a:00:2c:3c                                                |
|                                                                       |
| domain:1-11@20ATCMDLIB: Ready                                         |
|                                                                       |
| cmd:<null>                                                            |
|                                                                       |
| Added cmd [argc=0:name=testcmd]                                       |
|                                                                       |
| starting thread-sock                                                  |
|                                                                       |
| Zero arguments                                                        |
|                                                                       |
| cmd:at:2                                                              |
|                                                                       |
| Ready                                                                 |
|                                                                       |
| resp-len:9                                                            |
|                                                                       |
| Zero arguments                                                        |
|                                                                       |
| cmd:minicom2.7.90:13                                                  |
|                                                                       |
| resp-len:28                                                           |
|                                                                       |
| Zero arguments                                                        |
|                                                                       |
| cmd:testcmd:7                                                         |
|                                                                       |
| No arguments                                                          |
|                                                                       |
| Hello                                                                 |
|                                                                       |
| resp-len:9                                                            |
|                                                                       |
| Zero arguments                                                        |
|                                                                       |
| cmd:minicom2.7.90:13                                                  |
|                                                                       |
| resp-len:28                                                           |
+=======================================================================+
+-----------------------------------------------------------------------+

Use any serial commands terminal to issue serial interface commands,
like testcmd in this example, to Talaria TWO EVB.

Open minicom on a Ubuntu terminal using the command minicom -s with
115,200 baudrate, 8 bits, no flow control, and no parity once the
at_custom_cmd.elf is loaded on to the Talaria TWO EVB.

|image1|\ |image2|

Figure : Minicom output

.. |image1| image:: media/image1.png
   :width: 1.10236in
   :height: 0.16142in
.. |image2| image:: media/image2.png
   :width: 5.90551in
   :height: 4.04048in
