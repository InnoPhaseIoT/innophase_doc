.. _Development_Environments/Windows/Visual_Studio_Code_Editor/Prerequisites:


Prerequisites 
==============

    * Talaria TWO SDK.
    * PC with Windows 10 or higher.

Prerequisites for Building the Application using VS Code 
=================

Node.js Installation 
---------------------

Node.js is an open-source java script run-time environment.

Download the Windows Installer (.msi) from the Node.js download page and install it with administrative rights: https://nodejs.org/en/.

|Graphical user interface, website Description automatically generated|

Figure 2: Node.js installation

Installation results in a folder similar to: C:\\Program Files\\nodejs
and is added to the system path since it includes the node.exe binary.

NPM Installation 
-----------------

NPM (Node Package Manager) is the package manager for the Node
JavaScript platform. It installs the modules and organizes them so the
node.js can locate the modules. To install NPM, execute the following
steps:

1. Launch the node command prompt.

|Node.js command prompt|

Figure 3: Node command prompt

2. To install latest version of NPM through node.js command line,
   execute the following command:

+-----------------------------------------------------------------------+
| npm install --global npm@latest                                       |
+=======================================================================+
+-----------------------------------------------------------------------+

|Text Description automatically generated|

Figure 4: NPM latest version installation

XPM Installation 
-----------------

XPM is the xPack Project Manager. XPM is mainly intended to manage
projects during development and build configurations to run actions
associated with various build steps.

To install the latest version of XPM through node.js command line,
execute the following command:

+-----------------------------------------------------------------------+
| npm install --global xpm@latest                                       |
+=======================================================================+
+-----------------------------------------------------------------------+

|image1|

Figure 5: XPM installation

Windows-Build-Tools Installation
--------------------------------

To build projects on Windows it is necessary to install make, which is
available from the xPack Windows Build Tools. Running builds on Windows
requires tools that Microsoft does not include in the base distribution
and hence needs to be installed separately.

To install the windows-build-tools through node.js command line ,
execute the following command:

+-----------------------------------------------------------------------+
| xpm install --global @xpack-dev-tools/windows-build-tools@4.3.0-1.1   |
+=======================================================================+
+-----------------------------------------------------------------------+

|image2|

Figure 6: Windows-build-tools installation

Arm Tool Chain Installation
---------------------------

This toolchain contains integrated and validated packages featuring the
compiler, libraries, and other tools necessary for software development.
To build ARM projects, an ARM toolchain xPack GNU Arm Embedded GCC is
required.

To install latest version of the ARM tool chain, execute the following
command:

+-----------------------------------------------------------------------+
| xpm install @xpack-dev-tools/arm-none-eabi-gcc@11.2.1-1.1.1           |
+=======================================================================+
+-----------------------------------------------------------------------+

|image3|

Figure 7: ARM tool chain installation

OpenOCD Installation
--------------------

OpenOCD is used for on-chip debugging. . In a terminal window, execute
the following command to install OpenOCD (For example: version 0.10.0):

+-----------------------------------------------------------------------+
| xpm install --global @xpack-dev-tools/openocd@0.10.0-13.1             |
+=======================================================================+
+-----------------------------------------------------------------------+

|image4|

Figure 8: OpenOCD installation

All xPacks are installed in a central folder similar to the one in the
following location: C:\\Users\\<User name>\\AppData\\Roaming.

Ensure to check the XPM output for the actual location.

.. |A screenshot of a computer Description automatically generated| image:: media/image1.png
   :width: 7.48031in
   :height: 4.02342in
.. |Graphical user interface, website Description automatically generated| image:: media/image2.png
   :width: 7.48031in
   :height: 3.98117in
.. |Node.js command prompt| image:: media/image3.png
   :width: 6.88976in
   :height: 0.8993in
.. |Text Description automatically generated| image:: media/image4.png
   :width: 6.88976in
   :height: 0.88229in
.. |image1| image:: media/image5.png
   :width: 7.48031in
   :height: 0.70106in
.. |image2| image:: media/image6.png
   :width: 7.48031in
   :height: 1.36545in
.. |image3| image:: media/image7.png
   :width: 7.48031in
   :height: 1.10424in
.. |image4| image:: media/image8.png
   :width: 7.48031in
   :height: 1.5886in
