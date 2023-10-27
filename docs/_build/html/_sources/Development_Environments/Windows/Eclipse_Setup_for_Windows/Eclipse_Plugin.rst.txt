.. _Development_Environments/Windows/Eclipse_Setup_for_Windows/Eclipse_Plugin:

Eclipse Plugin: InnoPhase IoT Software Development Tool for Application Development
===================================================================================

InnoPhase IoT Software Development Tool is an Eclipse plugin which
simplifies the application development for InnoPhase IoT product using
Eclipse IDE.

**Note**:

1. Currently, the plugin supports only one connected device. In case
more than one device is connected, the plugin might not function as
expected.

2. Steps for manually developing the application are available in
section: *Application Development - Manual Procedure*.

InnoPhase IoT Software Development Tool Installation
----------------------------------------------------

Install plugin InnoPhase IoT Software Development Tool onto Eclipse
using following steps:

1. Help -> Install New Software

..

   |image1|

Figure 9: Plugin installation – Install new software

2. Add -> Location to https://www.innophaseiot.com/eclipse-plugins ->Add

|A screenshot of a computer Description automatically generated|

Figure 10: Plugin installation – Add Repository Location

3. Select the check box: InnoPhase IoT -> Next

|image2|

Figure 11: Plugin installation – Choose available software to install

4. Once done, Eclipse begins to calculate the requirements and
   dependencies.

|image3|

Figure 12: Plugin installation – Calculating requirements and
dependencies

5. Select radial button “\ *Keep my installation the same and modify the
   items being installed to be compatible*\ ” -> Next

|image4|

Figure 13: Plugin installation – Install remediation page

6. Press Next to continue.

|image5|

Figure 14: Plugin installation – Install Details

7. Accept terms -> Finish

|image6|

Figure 15: Plugin installation – Review licenses

8. Select the check box Unsigned & Always trust all content and Click on
   Trust Selected -> Yes, I Accept the Risk

|image7|

|A screenshot of a computer error message Description automatically
generated|

Figure 16: Plugin installation – Trust unsigned content

9. Software begins to install, which is indicated in the status bar.

|A screen shot of a computer Description automatically generated|\ c

Figure 17: Plugin installation – Installing software status

10. Once software installation is complete, a pop-up message for
    restarting appears. Click on Restart Now.

|A screenshot of a software update Description automatically generated|

Figure 18: Plugin installation – Restart Now after installation

11. On successful installation, Eclipse IDE will have a tab for
    InnoPhase IoT on restarting.

|image8|

Figure 19: Plugin installation – InnoPhase IoT menu

Download and Configure Support Files for Plugin
-----------------------------------------------

InnoPhase IoT Software Development Tool plugin requires supporting
files, which need to be configured before use. Follow the subsequent
steps to configure the supporting files:

1. InnoPhase IoT -> Download and Configure Support Files

..

   |image9|

Figure 20: Download and configure support files menu

2. Browse and choose a directory to download and configure support files
   for *InnoPhase IoT Software Development Tool* plugin.

|image10|

Figure 21: Download and configure support files - Input window

**Note**: If the plugin support files are already available, then check
the box: Use an existing InnoPhase IoT support directory file system and
choose the existing folder.

3. Click Finish. Support files will be downloaded and saved in the
   selected folder. A pop-up message will confirm once the download is
   completed.

|A screenshot of a message Description automatically generated|

Figure 22: Download and Configure Support Files – Status message

Import Talaria TWO Example Project
----------------------------------

1. Import an existing example as a make file project in eclipse:

   a. Download and unzip Talaria SDK provided

   b. Open Eclipse

   c. Click on File -> Import

..

   |Graphical user interface, application Description automatically
   generated|

Figure 23: Import an existing example in Eclipse

2. Under C/C++, Click Existing code as Makefile Project and then click
   Next.

..

   |Graphical user interface, text, application, email Description
   automatically generated|

Figure 24: Import existing code as makefile project

3. Enter the project name, select any of the applications or examples
   available in SDK package, select the Toolchain as ARM cross GCC and
   click Finish.

4. Project is imported with the source code and existing make file.

..

   |image11|

Figure 25: Project imported

Run Configuration Set-up 
-------------------------

InnoPhase IoT Software Development Tool provides *the Run Configuration
set-up to Build and Flash the Application to connected Talaria TWO EVB*.
Steps for setting up the run configuration is as follows:

1. Right click on Project and select Run As ->Run Configurations.

..

   |image12|

Figure 26: Eclipse Run As – Select Run Configuration

2. Right click on InnoPhase IoT Application Run configuration and select
   New Configuration.

..

   |image13|

Figure 27: InnoPhase IoT Software Development Tool – New Run
Configuration

3. Plugin will create a new configuration, automatically fill the
   required default values. Other values are required to be filled by
   the user as per the required the application.

..

   |image14|

Figure 28: InnoPhase IoT Software Development Tool – Run configuration
input window

4. User inputs are required for only the Main tab. Input parameters for
   this tab are as follows:

   a. **Name:** Name of the run configuration. Automatically filled with
      default name. Can be changed as per requirement.

   b. **Project:** By default, the active project name will be selected.
      Use the Browser button to change the project.

   c. **C/C++ Application:** Depending on the project selected, default
      application file is selected as
      *project_path/out/project_name.elf*.

..

   For example: If the project name is helloworld and the project path
   is ../helloworld, then the default value will be
   ../helloworld/out/helloworld.elf.

   In case the correct file is not selected, use the Browse button to
   select the correct file.

d. **Working Directory:** Selected by default.

e. **Talaria TWO Filesystem:** Is empty by default. Select the folder
   which contains files/folders to be added to the Talaria TWO
   filesystem.

..

   **Note**: Only files/folders inside the selected folder will be added
   to the Talaria TWO filesystem. Selected folder will not be added.

f. **Wi-Fi Network Name:** Is empty by default. Add the name of the
      Wi-Fi API to which Talaria TWO needs to connect.

g. **Wi-Fi Network Password:** Is empty by default. Add the password of
      the Wi-Fi API provided in the Wi-Fi network name.

h. **Boot Arguments:** Is empty by default. Add the boot argument
      required by the C/C++ application selected.

5. Click Apply once the inputs are filled.

6. Click Run to build and flash the application to Talaria TWO EVB
   device.

   a. In case the device is not connected to the system, only the
      application is built. Application build output can be seen on the
      console window CDT Build Console.

..

   |image15|

Figure 29: Console Window – CDT build console

   **Note**: Use Display Selected Console to select the required console
   window.

b. In case the device is connected to the system, the application flash
   and device console output can be seen on the console window InnoPhase
   IoT T2 Device Monitor.

..

   |image16|

Figure 30: InnoPhase IoT T2 Device Monitor Console Window – Run
configuration

   **Note**: Currently, the plugin can flash to only one connected
   device. In case more than one device is connected, the plugin may not
   function as expected.

   **
   **

Debug Configuration Set-up
--------------------------

InnoPhase IoT Software Development Tool provides debug configuration
set-up to build, flash application to the connected Talaria TWO EVB and
debug the application.

Steps to set-up the debug configuration settings are as follows:

1. Right click on Project and select Debug As ->Debug Configurations.

..

   |image17|

Figure 31: Eclipse Debug As – Select debug configuration

2. Right click on InnoPhase IoT Application Debug configuration and
   select New Configuration.

..

   |image18|

Figure 32: InnoPhase IoT Software Development Tool – New debug
configuration

3. Plugin will create a new configuration and automatically fill-in the
   required default values for debugging. As required, the user can fill
   in the other values.

..

   |image19|

Figure 33: InnoPhase IoT Software Development Tool – Debug configuration
input window

   The plugin will automatically fill in the inputs for the Debugger
   tab. For more details on providing the inputs manually, refer *Debug
   Configuration Setting up in Eclipse*.

   User inputs are required for the Main tab. Input parameters are as
   follows:

a. **Name:** Name of the debug configuration. Filled with default name,
      the user can change the name as required.

b. **Project:** By default, the active project name is selected. Use the
      Browser button to change the project.

c. **C/C++ Application:** Dependent on the project selected. Default
      application file is selected as
      *project_path/out/project_name.elf*.

..

   For example: If the project name is helloworld and the project path
   is *..\\helloworld*, then the default value is
   *../helloworld/out/helloworld.elf*.

   In case the correct file is not selected, use the Browse button to
   select the correct file.

d. **Wi-Fi Network Name:** Is empty by default. Add the name of the
      Wi-Fi AP to which Talaria TWO needs to be connected to.

e. **Wi-Fi Network Password:** Is empty by default. Add the password of
      the Wi-Fi AP provided in the Wi-Fi network name.

f. **Boot Arguments:** Is empty by default. Add the boot argument
      required by the C/C++ application selected.

4. Click the Apply button once the inputs are filled.

5. Click Debug to build, flash the application onto Talaria TWO EVB and
   start debugging.

   a. In case the device is not connected to the system, only
      application will get build. Application build output can be seen
      in Console window “CDT Build Console”, refer Figure 29.

   b. In case the device is connected to the system:

      i.  The application flash and device console output can be seen in
          the console window InnoPhase IoT T2 Device Monitor, refer
          Figure 30.

      ii. Once the application is flashed successfully onto Talaria TWO
          EVB, Eclipse may prompt to switch to Debug Perspective. Press
          Switch to continue debugging.

..

   |image20|

   Figure 34: InnoPhase IoT Software Development Tool – Debug
   perspective switch

c. Eclipse will begin to debug and the same is displayed in Debug
   Perspective as shown in Figure 35.

..

   |image21|

Figure 35: InnoPhase IoT Software Development Tool – Debug start

1. Debug the application with Eclipse’s general debugging procedure
      (refer point 4 to 7 of section *Debugging in Eclipse*).

2. While debugging the application, the application’s prints will be
      visible on the console window InnoPhase IoT T2 Device Monitor as
      shown in Figure 30.

.. |image1| image:: ../media/image1.png
   :width: 3.93701in
   :height: 4.81331in
.. |A screenshot of a computer Description automatically generated| image:: ../media/image2.png
   :width: 6.88976in
   :height: 5.45572in
.. |image2| image:: ../media/image3.png
   :width: 6.88976in
   :height: 5.44521in
.. |image3| image:: ../media/image4.png
   :width: 6.88976in
   :height: 5.4504in
.. |image4| image:: ../media/image5.png
   :width: 6.88976in
   :height: 5.45116in
.. |image5| image:: ../media/image6.png
   :width: 6.88976in
   :height: 4.16328in
.. |image6| image:: ../media/image7.png
   :width: 6.88976in
   :height: 3.3733in
.. |image7| image:: ../media/image8.png
   :width: 6.88976in
   :height: 4.25634in
.. |A screenshot of a computer error message Description automatically generated| image:: ../media/image9.png
   :width: 6.88976in
   :height: 2.97571in
.. |A screen shot of a computer Description automatically generated| image:: ../media/image10.png
   :width: 6.88976in
   :height: 0.74912in
.. |A screenshot of a software update Description automatically generated| image:: ../media/image11.png
   :width: 6.88976in
   :height: 1.95793in
.. |image8| image:: ../media/image12.png
   :width: 6.88976in
   :height: 1.49444in
.. |image9| image:: ../media/image13.png
   :width: 4.72441in
   :height: 1.53398in
.. |image10| image:: ../media/image14.png
   :width: 6.88976in
   :height: 2.89731in
.. |A screenshot of a message Description automatically generated| image:: ../media/image15.png
   :width: 6.88976in
   :height: 2.00514in
.. |Graphical user interface, application Description automatically generated| image:: ../media/image16.png
   :width: 3.93701in
   :height: 4.04292in
.. |Graphical user interface, text, application, email Description automatically generated| image:: ../media/image17.tmp
   :width: 4.72441in
   :height: 4.29633in
.. |image11| image:: ../media/image18.png
   :width: 4.37917in
   :height: 5.16181in
.. |image12| image:: ../media/image19.png
   :width: 6.49606in
   :height: 7.28281in
.. |image13| image:: ../media/image20.png
   :width: 6.49606in
   :height: 3.99296in
.. |image14| image:: ../media/image21.png
   :width: 6.49606in
   :height: 4.24553in
.. |image15| image:: ../media/image22.png
   :width: 5.90551in
   :height: 1.14204in
.. |image16| image:: ../media/image23.png
   :width: 5.90551in
   :height: 1.48737in
.. |image17| image:: ../media/image24.png
   :width: 5.90551in
   :height: 6.74598in
.. |image18| image:: ../media/image25.png
   :width: 6.49606in
   :height: 4.51372in
.. |image19| image:: ../media/image26.png
   :width: 6.49606in
   :height: 3.59747in
.. |image20| image:: ../media/image27.png
   :width: 5.51181in
   :height: 2.64963in
.. |image21| image:: ../media/image28.png
   :width: 5.90551in
   :height: 2.49125in
