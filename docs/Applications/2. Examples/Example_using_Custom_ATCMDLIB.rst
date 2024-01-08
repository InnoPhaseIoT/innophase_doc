.. _ex custom atcmdlib:

Custom ATCMDLIB
------------------------

ATCMDS application provides the Wi-Fi capability to any device having
UART interface. Host CPU uses serial commands to interface and configure
the Wi-Fi module. All AT or custom commands are parsed and converted to
the corresponding WLAN/Network calls. This mode returns the responses in
the same ASCII format as success or failure with additional response
data.

ATCMDLIB enables customers to use all standard commands in the library
(libstcmd.a). Custom commands can also be added and linked to the
ATCMDLIB.

ATCMDLIB Application
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This section describes the application along with code snippets. The
application uses ATCMDLIB APIs to achieve functionality.

Include ATCMDLIB Header File
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: shell

      #include “atcmd_lib.h”  


Initialization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: shell

      if(ATCMDLIB_ SUCCESS == atcmd_init()){
          os_printf("ATCMDLIB: Ready\n");
      }
      else {
          os_printf("ATCMDLIB: Failed\n");
      }




Add Sample Command Function
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: shell

      int testcmd_func(int argc , char *argv[])
      {
          int i;
          os_printf("\r\nHello");
          for(i = 0 ; i <argc;i++){
              os_printf("\r\nargv[%d]=%s",i,argv[i]);
          }
          return ATCMDLIB_SUCCESS;
      }



Add New Command 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: shell

      if(ATCMDLIB_ERROR == atcmd_add("testcmd",&testcmd_func))
       os_printf("Failed to add command\n");



Command Status 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: shell

      /*use this enum to send command status*/
      typedef enum ATCMDLIB_STATUS
      {
      	ATCMDLIB_SUCCESS  =0,
      	ATCMDLIB_ERROR  =  1,
      	ATCMDLIB_EINVAL =  2
      };



Running the Application 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Program at_custom_cmd.elf
*(freertos_sdk_x.y\\examples\\at_custom_cmd\\bin)* using the Download
Tool:

1. Launch the Download tool provided with InnoPhase Talaria TWO SDK.

2. In the GUI window:

   a. Boot Target: Select the appropriate EVK from the drop-down

   b. ELF Input: Load the at_custom_cmd.elf by clicking on Select ELF
      File.

   c. Programming: Prog RAM or Prog Flash as per requirement.


Expected Output
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The previously mentioned code will add an example command testcmd. The
expected output for this command will be console pint Hello followed by
arguments present in command. The code also sends OK on UART as command
status, upon successful execution of the command testcmd.

.. code:: shell

      Y-BOOT 208ef13 2019-07-22 12:26:54 -0500 790da1-b-7
      ROM yoda-h0-rom-16-0-gd5a8e586
      FLASH:PWWWWWAE
      Build $Id: git-b8e2cc1 $
      Flash detected. flash.hw.uuid: 39483937-3207-00a8-0068-ffffffffffff
      $App:git-c5c0b68
      SDK Ver: FREERTOS_SDK_1.0
      At Custom Command Demo App
      addr e0:69:3a:00:2c:5e
      
      domain:1-11@20before: magic1=0x0, val=0x0, magic2=0x0
      Crash detection logic initialized
      after: magic1=0x11223344, val=0x0, magic2=0x55667788
      ATCMDLIB: Ready
      cmd:<null>
      Added cmd [argc=0:name=testcmd]
       starting thread-sock
      CMD:atHexdump of uartbuf before processing, len=3
      61 74 00                                          |  at.
      Zero arguments
      cmd:at:2
      Ready
      resp-len:9
      CMD:testcmdHexdump of uartbuf before processing, len=8
      74 65 73 74 63 6D 64 00                           |  testcmd.
      Zero arguments
      cmd:testcmd:7
      No arguments
      Hello
      resp-len:9



Use any serial commands terminal to issue serial interface commands,
like testcmd in this example, to Talaria TWO EVB.

Open minicom on a Ubuntu terminal using the command minicom -s with
115,200 baudrate, 8 bits, no flow control, and no parity once the
at_custom_cmd.elf is loaded on to the Talaria TWO EVB.

|image1|

Figure 1: Minicom output

.. |image1| image:: media/image1.png
   :width: 7.08661in
   :height: 2.56528in
