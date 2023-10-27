.. _Hardware_Reference/3.INP3000/INP3000_Programmer_Board:

The INP3000 programmer board provides a programming interface for
Talaria TWO modules. It can be used with scripts found in the Talaria
TWO SDK.

INP3000_Programmer_Board
=======================

Prerequisites
-------------
    1. Talaria TWO SDK
    2. PC with Windows 10 or higher
    3. Eclipse build environment setup
    4. libusbK driver for Windows

Generating the Application Image 
++++++++++

This section describes generating an application image (.img) and its
virtual image (.img.vm) using the ELF.

In Windows 
-----------

An application image and its virtual image must be generated over
command line for programming the application over JTAG/SWD. From the SDK
directory, execute the following steps to generate the application
image:

+-----------------------------------------------------------------------+
| python .\\script\\boot.py --output app.img <path to the generated     |
| elf> <boot argument 1> <boot argument 2>                              |
+=======================================================================+
+-----------------------------------------------------------------------+

For Example:

+-----------------------------------------------------------------------+
| python .\\script\\boot.py --output app.img                            |
| .\\examples\\http_client\\bin\\http_client.elf host=httpbin.org       |
| path=/json port=443 secured=1 method=get ca_cert=/data/httpbin_ca.pem |
| ssid=InnoPhase_AE_AP passphrase=innophaseae                           |
+=======================================================================+
+-----------------------------------------------------------------------+

This command generates the app.img and app.img.vm in the current
directory.

|image1|

Figure 4: Generating the application image – Windows

|image2|

Figure 5: Application image and its VM image – Windows

In Linux
--------

To generate the application image in Linux, execute the following
command from the SDK directory

+-----------------------------------------------------------------------+
| sudo python3 ./script/boot.py --output <application image name> <path |
| of the application>                                                   |
+=======================================================================+
+-----------------------------------------------------------------------+

For example:

+-----------------------------------------------------------------------+
| sudo python3 ./script/boot.py --output app.img                        |
| ./examples/http_client/bin/http_client.elf host=httpbin.org           |
| path=/json port=443 secured=1 method=get ca_cert=/data/httpbin_ca.pem |
| ssid=InnoPhase_AE_AP passphrase=innophaseae                           |
+=======================================================================+
+-----------------------------------------------------------------------+

This command generates the app.img and app.img.vm in the current
directory.

|image3|

Figure 6: Generating the application image – Linux

|image4|

Figure 7: Application image and its VM image – Linux

Generating the Data FS Image
-----------

Data image is a user file system which is a .img format. Data FS
contains user defined configurations or application specific
information, such as network configuration file, certificates, user data
and so on. This image should be written over DATA partition which starts
from sector 256. The data partition has a total of 240 sectors to write
user data files.

This section describes generating the data image with certificates.

.. _in-windows-1:

In Windows
----------

This section describes generating the file system image and loading it
onto the Talaria TWO module file system.

In this example, the data FS is generated using certificates. The
certificate is used to authenticate the server for HTTP/MQTT connection.

Copy the required files or certificates to the directory data, and
execute the following instruction which generates an image file which
needs to be flashed to Talaria TWO:

For generating data.img in Windows, execute the following command from
the SDK directory:

+-----------------------------------------------------------------------+
| .\\tools\\mklittlefs\\mklittlefs -s 40000 -c < path to the data       |
| folder which needs to be updated > .\\< path to store the generated   |
| data.img>\\data.img                                                   |
+=======================================================================+
+-----------------------------------------------------------------------+

**Note:** For example, the http_client application needs a certificate
to connect to the server. Copy the files to the data directory and
execute this instruction to create a data.img:

+-----------------------------------------------------------------------+
|    .\\tools\\mklittlefs\\mklittlefs.exe -s 0x40000 -c                 |
|    .\\examples\\http_client\\cert\\data .\\data.img                   |
+=======================================================================+
+-----------------------------------------------------------------------+

This command generates data.img in the current directory.

|image5|

Figure 8: Generating the data image - Windows

|image6|

Figure 9: Generated data image – Windows

.. _in-linux-1:

In Linux
--------

For generating data.img in Linux, execute the following command from the
SDK directory:

+-----------------------------------------------------------------------+
| ./tools/mklittlefs/mklittlefs -s 40000 -c < path to the data folder   |
| which needs to be updated > < path to store the generated data.img>   |
+=======================================================================+
+-----------------------------------------------------------------------+

**Note:** For example, the http_client application needs a certificate
to connect to the server. Copy the files to the data directory and
execute this instruction to create a data.img:

+-----------------------------------------------------------------------+
|    ./tools/mklittlefs/mklittlefs -s 40000 -c                          |
|    ./examples/http_client/cert/data/ ./data.img                       |
+=======================================================================+
+-----------------------------------------------------------------------+

This command generates data.img in the current directory.

|image7|

Figure 10: Generating the data image - Linux

|image8|

Figure 11: Generated data image -Linux

.. toctree::
   :maxdepth: 2

   Programming_Talaria_TWO_over_UART.rst

Programming Talaria TWO over JTAG
+++++++++++

Programming Talaria TWO over SWD
+++++++++++

.. |image1| image:: media/image1.png
   :width: 6.69291in
   :height: 0.68991in
.. |image2| image:: media/image2.png
   :width: 6.69291in
   :height: 4.51229in
.. |image3| image:: media/image3.png
   :width: 6.69291in
   :height: 0.70429in
.. |image4| image:: media/image4.png
   :width: 6.69291in
   :height: 0.64857in
.. |image5| image:: media/image5.png
   :width: 6.69291in
   :height: 0.39898in
.. |image6| image:: media/image6.png
   :width: 5.90551in
   :height: 4.77165in
.. |image7| image:: media/image7.png
   :width: 6.69291in
   :height: 0.22747in
.. |image8| image:: media/image8.png
   :width: 6.69291in
   :height: 0.38683in
