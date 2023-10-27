.. _Development_Environments/Windows/Visual_Studio_Code_Editor/Add_Paths_to_the_Environment_Variable:


Add Paths to the Environment Variable
=====================================

After completing the installation, add the environment variables using
the following path: Control Panel -> System and Security -> System ->
Advanced System Settings -> Environment Variables -> System Variable ->
Path -> Edit -> New.

|Graphical user interface, application Description automatically
generated|

Figure 13: Adding environment variables

Add the tool chain and build tools path to the environment variable
under System Variables. xPacks installs tools under Appdata/Roming/
directory in Windows.

Steps to add the Environment Variable:

1. Click on New.

2. A new column opens up where the environment path can be added.

3. Add the Path of the built tools bin directory.

[For example:
C:\\Users\\innop\\AppData\\Roaming\\xPacks\\@xpack-dev-tools\\windows-build-tools\\4.2.1-2.1\\.content\\bin]

4. After adding the build tools path, click on New.

5. Add the path of the ARM tool chain bin directory.

[For example:
C:\\Users\\innop\\AppData\\Roaming\\xPacks\\@xpack-dev-tools\\arm-none-eabi-gcc\\10.3.1-2.2.1\\.content\\bin]

6. Click OK.

.. |Graphical user interface, application Description automatically generated| image:: media/image1.png
   :width: 5.90551in
   :height: 2.69191in
