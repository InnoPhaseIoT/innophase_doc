.. _Development_Environments/Windows/Eclipse_Setup_for_Windows/Application_Development-Manual_Procedure:


Application Development - Manual Procedure 
===========================================

This section describes the manual procedure for developing the
application for InnoPhase IoT product using Eclipse IDE.

Import Talaria TWO Example Project 
-----------------------------------

Procedure to import an example project remains the same as *Import
Talaria TWO Example Project* for Eclipse plugin.

Configuring the Eclipse Project
-------------------------------

1. Click on your project, right click and select Properties.

..

   |Graphical user interface, application Description automatically
   generated|

Figure 42: Select Properties

2. Select Settings under C/C++ build and click on Toolchains. Add the
   tool chain path and build tools path through global, workspace and
   project links. Click Apply and Close.

..

   |Properties for test|

Figure 43: Settings Window

3. Click on ARM Toolchains Path option available under MCU.

4. Click on xPack. and a window opens as shown in the picture below.

5. Select the version of the toolchain and click ‘OK’.

6. Click ‘Apply’.

..

   |A screenshot of a computer Description automatically generated|

Figure 44: Adding ARM Tool Chain Path

7.  Click on Build Tools Path option available under MCU.

8.  Click on xPack and a window opens as shown in the picture below.

9.  Select the version of the buildtools and click OK.

10. Click Apply.

..

   |image1|

Figure 45: Adding Buildtools Path

11. Click on OpenOCD Path, provide the OpenOCD as the executable.

12. Click on xPack, select the version of OpenOCD and click OK.

13. Click on ‘Apply’ and then ‘Apply and Close’.

..

   |image2|

Figure 46: Adding OpenOCD Path

14. Includes directory of the project is added.

..

   |Graphical user interface, text, application Description
   automatically generated|

Figure 47: Includes directory of the project

Building Application in Eclipse
-------------------------------

1. To build a project, click Project -> Build Project.

..

   |image3|

Figure 48: Building the Application

2. On successfully building the application, an out directory containing
   the .elf file is created inside the application.

..

   |image4|

Figure 49: Build console

Debug Configuration Set-up in Eclipse
-------------------------------------

1. To start debugging the application, select the project and right
   click on it. Choose Debug As -> Debug Configuration.

..

   |image5|

Figure 50: Debug configuration settings

2. Double click on GDB OpenOCD Debugging and the debug configuration of
   the project is seen. Select the configuration and then point to the
   generated ELF of the application present in the out directory.

..

   |Graphical user interface, text, application, email Description
   automatically generated|

Figure 51: GDB OpenOCD Debugging settings

3. Under Debugger Settings, select the executable path as an OpenOCD
   installed path by clicking on Browse.

..

   |Debug Configurations|

Figure 52: Debugger settings – OpenOCD installed path

   In Config options, enter the path of configuration files available in
   conf directory of the SDK. These two files contain the configuration
   settings of Talaria TWO EVB. Configuration path should be as follows:

+-----------------------------------------------------------------------+
| -s C:/<PATH TO SDK>/sdk_x.y/conf -f ftdi.cfg -f t2.cfg                |
+=======================================================================+
+-----------------------------------------------------------------------+

..

   **Note:** For SWD debugging, use the following configuration in
   Config options:

+-----------------------------------------------------------------------+
| -s C:/<PATH TO SDK>/sdk_x.y/conf -f ftdi_swd.cfg -f t2_swd.cfg        |
+=======================================================================+
+-----------------------------------------------------------------------+

..

   |image6|

Figure 53: Debugger config window for SWD Configuration

4. In GDB client setup, Select the actual executable arm-none-eabi-gdb
   as shown in Figure 54. Add the following commands in commands tab:

+-----------------------------------------------------------------------+
| set mem inaccessible-by-default off                                   |
|                                                                       |
| set substitute-path /tmp/build-2_gctshx/ "C:/data/"                   |
|                                                                       |
| mem 0 0x40000 ro                                                      |
|                                                                       |
| mem 0x40000 0xc0000 rw                                                |
|                                                                       |
| mem 0x100000 0x200000 ro                                              |
|                                                                       |
| mem 0xfc0000 0x1000000 rw                                             |
|                                                                       |
| mem 0x2000000 0x2100000 rw                                            |
+=======================================================================+
+-----------------------------------------------------------------------+

..

   |image7|

Figure 54: Debugger settings

5. Click on Apply.

Programming Talaria TWO EVB
---------------------------

Flash the ELF onto Talaria TWO using the Download tool. Point to the elf
file and click on PROG Flash to flash the application.

Ensure that the output is as shown in Figure 56. If not, Click on Clear
Flash on the Download Tool and program the elf onto Talaria TWO again.

|image8|

Figure 56: Download Tool Console

Debugging in Eclipse
--------------------

To debug the application the debugger provides control of program
execution by setting breakpoints, suspending executed programs, stepping
through the code and examining the contents of variables.

1. Click on Start-up tab and select the following options:

   a. Initial Reset

   b. Load symbols

   c. Load executable

   d. Debug in RAM

   e. Click on Debug in the start-up tab

..

   |image9|

Figure 57: Debug start-up settings

2. On being prompted to switch to the Debug perspective, click Switch.

..

   |image10|

Figure 58: Confirm Perspective Switch

3. The Debug perspective appears with the application window open.
   Eclipse IDE re-positions into debug perspective.

..

   |image11|

Figure 59: Debug perspective

4. |image12|\ |image13|\ Breakpoints can be set by double-clicking to
   the left of the line number. The blue circle indicates ( ) that the
   breakpoint is set. Similarly, multiple breakpoints can be added. To
   start debugging, click on ( ).

..

   |image14|

Figure 60: Setting breakpoint

5. The execution will stop at the first breakpoint added to the c file.
   As shown in Figure 60, breakpoint is set at line 6.

6. |image15|\ To continue execution, click the Resume button ( ) on the
   toolbar of the Debug view. This will resume execution of the program
   and stop at the next breakpoint.

7. Step into and step over can also be used to continue execution of the
   next line.

8. While debugging the application, the application’s prints will be
   visible on Download Tool’s console window.

..

   |image16|

Figure 61: Step run output in console

.. |Graphical user interface, application Description automatically generated| image:: ../media/image1.png
   :width: 6.49606in
   :height: 3.48102in
.. |Properties for test| image:: ../media/image2.png
   :width: 5.90556in
   :height: 3.77292in
.. |A screenshot of a computer Description automatically generated| image:: ../media/image3.png
   :width: 5.90551in
   :height: 2.53479in
.. |image1| image:: ../media/image4.png
   :width: 6.49606in
   :height: 2.78827in
.. |image2| image:: ../media/image5.png
   :width: 6.49606in
   :height: 2.78827in
.. |Graphical user interface, text, application Description automatically generated| image:: ../media/image6.png
   :width: 3.93681in
   :height: 2.92083in
.. |image3| image:: ../media/image7.png
   :width: 6.29921in
   :height: 3.07599in
.. |image4| image:: ../media/image8.png
   :width: 6.29921in
   :height: 3.37775in
.. |image5| image:: ../media/image9.png
   :width: 6.29921in
   :height: 3.39331in
.. |Graphical user interface, text, application, email Description automatically generated| image:: ../media/image10.png
   :width: 6.29921in
   :height: 3.5096in
.. |Debug Configurations| image:: ../media/image11.png
   :width: 6.69291in
   :height: 3.30845in
.. |image6| image:: ../media/image12.png
   :width: 6.69291in
   :height: 0.96168in
.. |image7| image:: ../media/image13.png
   :width: 6.69291in
   :height: 3.75807in
.. |image8| image:: ../media/image14.png
   :width: 7.47888in
   :height: 2.4875in
.. |image9| image:: ../media/image15.png
   :width: 6.29921in
   :height: 4.63552in
.. |image10| image:: ../media/image16.png
   :width: 4.72441in
   :height: 2.01427in
.. |image11| image:: ../media/image17.png
   :width: 6.29921in
   :height: 3.37775in
.. |image12| image:: ../media/image18.png
   :width: 0.14792in
   :height: 0.2in
.. |image13| image:: ../media/image19.png
   :width: 0.16667in
   :height: 0.12639in
.. |image14| image:: ../media/image20.png
   :width: 6.29921in
   :height: 3.3896in
.. |image15| image:: ../media/image19.png
   :width: 0.16667in
   :height: 0.12639in
.. |image16| image:: ../media/image21.png
   :width: 6.69291in
   :height: 3.73249in
