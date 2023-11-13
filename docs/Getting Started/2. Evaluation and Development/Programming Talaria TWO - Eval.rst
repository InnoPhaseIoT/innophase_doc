Programming Talaria TWO
=======================

Program t2_atcmds.elf (*Open_Web_SDK_x.y/at/bin*) using the Download
tool provided with the EVK package:

1. Launch the Download tool

2. In the GUI window:

   a. Boot Target: Select the appropriate EVK from the drop-down.

   b. ELF Input: Load the t2_atcmds.elf by clicking on Select ELF File.

   c. Boot Arguments: Pass the following boot arguments:

+-----------------------------------------------------------------------+
| baudrate=9600                                                         |
+=======================================================================+
+-----------------------------------------------------------------------+

d. Programming: Prog RAM or Prog Flash as per requirement.

For more details on using the Download tool, refer: Download_Tool.

**Note**: x and y refer to the EVK release version. For example:
*Open_Web_SDK_2.4/doc*.

Console output:

+-----------------------------------------------------------------------+
| Y-BOOT 208ef13 2019-07-22 12:26:54 -0500 790da1-b-7                   |
|                                                                       |
| ROM yoda-h0-rom-16-0-gd5a8e586                                        |
|                                                                       |
| FLASH:PNWWWWWWAEBuild $Id: git-34e3eddb8 $                            |
|                                                                       |
| baudrate=9600                                                         |
|                                                                       |
| Application Information:                                              |
|                                                                       |
| ------------------------                                              |
|                                                                       |
| Name : atcmd                                                          |
|                                                                       |
| Version : 2.0                                                         |
|                                                                       |
| Build Date : Aug 8 2022                                               |
|                                                                       |
| Build Time : 03:58:11                                                 |
|                                                                       |
| Heap Available: 311 KB (318608 Bytes)                                 |
|                                                                       |
| $App:git-b369bc3f                                                     |
|                                                                       |
| SDK Ver: SDK_2.5                                                      |
|                                                                       |
| At Command App                                                        |
|                                                                       |
| addr e0:69:3a:00:13:90                                                |
|                                                                       |
| domain:1-11@20before: magic1=0x0, val=0x0, magic2=0x0                 |
|                                                                       |
| Crash detection logic initialized                                     |
|                                                                       |
| after: magic1=0x11223344, val=0x0, magic2=0x55667788                  |
|                                                                       |
| Serial-to-Wireless: Ready                                             |
|                                                                       |
| starting thread-sock                                                  |
+=======================================================================+
+-----------------------------------------------------------------------+
