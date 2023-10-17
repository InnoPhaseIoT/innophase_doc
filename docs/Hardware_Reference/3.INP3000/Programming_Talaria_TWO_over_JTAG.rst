.. _Hardware_Reference/3.INP3000/Programming_Talaria_TWO_over_JTAG:


Programming Talaria TWO over JTAG
=================================


The INP3000 Programmer Board version 3.0 has the JTAG interface to
program Talaria TWO modules.

Install the appropriate dependencies for programming over JTAG.

In Windows
----------

1. Open command prompt and reset the device in boot loader mode by
   executing the following command from the SDK directory:

+-----------------------------------------------------------------------+
| .\\script\\reset.py evk42_bl                                          |
+=======================================================================+
+-----------------------------------------------------------------------+

|image1|

Figure 36: JTAG - Resetting the device in boot loader mode- console
output (Windows)

2. Open the command prompt and start OpenOCD by executing the following
   command from the SDK directory:

+-----------------------------------------------------------------------+
| openocd -s .\\conf -f ftdi.cfg -f t2.cfg                              |
+=======================================================================+
+-----------------------------------------------------------------------+

The following output is seen on command prompt console:

|image2|

Figure 37: JTAG - Starting OpenOCD – console output

3. Flash the default partition table by executing the following command:

+-----------------------------------------------------------------------+
| .\\pc_tools\\T2_Flasher\\bin\\T2_Flasher_Windows.exe                  |
| --operation=write_ptable .\\<path to the standard_part_table.json     |
| file available in sdk_x.y/tools/partition_files directory>            |
+=======================================================================+
+-----------------------------------------------------------------------+

Following output is observed after flashing the default partition table:

|image3|

Figure 38: JTAG - Flashing the default partition table – console output

4. In the same terminal, execute the following command from the SDK
   directory to flash the data image (data.img).

**Note**: This step is needed only if the application uses any
certificates.

+-----------------------------------------------------------------------+
| .\\pc_tools\\T2_Flasher\\bin\\T2_Flasher_Windows.exe                  |
| --operation=write_part --partition=DATA .\\<path to the generated     |
| data image>\\data.img                                                 |
+=======================================================================+
+-----------------------------------------------------------------------+

The following output is observed after flashing the data image:

|image4|

Figure 39: JTAG - Flashing the data image - console output

5. In a separate command prompt window, execute the following command
   from the SDK directory to flash the application image:

+-----------------------------------------------------------------------+
| .\\pc_tools\\T2_Flasher\\bin\\T2_Flasher_Windows.exe                  |
| --operation=write_part --partition=BOOT .\\<path to the generated     |
| application image>\\app.img                                           |
+=======================================================================+
+-----------------------------------------------------------------------+

The following output is observed after flashing the application image:

|image5|

Figure 40: JTAG - Flashing the application image - console output

6. In the same terminal, flash the VM image of the application by
   executing the following command:

+-----------------------------------------------------------------------+
| .\\pc_tools\\T2_Flasher\\bin\\T2_Flasher_Windows.exe                  |
| --operation=write_part --partition=VIRT .\\<path to the generated     |
| application image.vm>                                                 |
+=======================================================================+
+-----------------------------------------------------------------------+

Following output is observed after flashing the application’s VM image:

|image6|

Figure 41: JTAG - Flashing application's VM image – console output

The application is successfully flashed over JTAG. Now, OpenOCD needs to
be terminated before debugging using Eclipse. Close all the command
prompt windows to terminate OpenOCD.

In Linux
--------

1. Open command prompt and reset the device in boot loader mode by
   executing the following command from the SDK directory:

+-----------------------------------------------------------------------+
| ./script/reset.py evk42_bl                                            |
+=======================================================================+
+-----------------------------------------------------------------------+

|image7|

Figure 42: JTAG - Resetting the device in boot loader mode- console
output (Windows)

2. Open command prompt and start OpenOCD by executing the following
   command from the SDK directory:

+-----------------------------------------------------------------------+
| openocd -s ./conf -f ftdi.cfg -f t2.cfg                               |
+=======================================================================+
+-----------------------------------------------------------------------+

The following output is seen on command prompt console:

|image8|

Figure 43: JTAG - Starting OpenOCD – console output

3. Flash the default partition table by executing the following command:

+-----------------------------------------------------------------------+
| .\\pc_tools\\T2_Flasher\\bin\\T2_Flasher_Linux                        |
| --operation=write_ptable .\\<path to the standard_part_table.json     |
| file available in sdk_x.y/tools/partition_files directory>            |
+=======================================================================+
+-----------------------------------------------------------------------+

Following output is observed after flashing the default partition table:

|image9|

Figure 44: JTAG - Flashing the default partition table – console output

4. In the same terminal, execute the following command from the SDK
   directory to flash the data image (data.img).

**Note**: This step is needed only if the application uses any
certificates.

+-----------------------------------------------------------------------+
| .\\pc_tools\\T2_Flasher\\bin\\T2_Flasher_Linux --operation=write_part |
| --partition=DATA .\\<path to the generated data image>\\data.img      |
+=======================================================================+
+-----------------------------------------------------------------------+

The following output is observed after flashing the data image:

|image10|

Figure 45: JTAG - Flashing the data image - console output

5. In a separate command prompt window, execute the following command
   from the SDK directory to flash the application image:

+-----------------------------------------------------------------------+
| .\\pc_tools\\T2_Flasher\\bin\\T2_Flasher_Linux --operation=write_part |
| --partition=BOOT .\\<path to the generated application                |
| image>\\app.img                                                       |
+=======================================================================+
+-----------------------------------------------------------------------+

The following output is observed after flashing the application image:

|image11|

Figure 46: JTAG - Flashing the application image - console output

6. In the same terminal, flash the VM image of the application by
   executing the following command:

+-----------------------------------------------------------------------+
| .\\pc_tools\\T2_Flasher\\bin\\T2_Flasher_Linux –operation=write_part  |
| –partition=VIRT .\\<path to the generated application                 |
| image.vm>\\app.img.vm                                                 |
+=======================================================================+
+-----------------------------------------------------------------------+

Following output is observed after flashing the application’s VM image:

|image12|

Figure 47: JTAG - Flashing application's VM image – console output

The application is successfully flashed over JTAG. Now, OpenOCD needs to
be terminated before debugging using Eclipse. Close all the command
prompt windows to terminate OpenOCD.

.. |image1| image:: media/image1.png
   :width: 6.69291in
   :height: 0.79597in
.. |image2| image:: media/image2.png
   :width: 6.69291in
   :height: 2.47494in
.. |image3| image:: media/image3.png
   :width: 6.69291in
   :height: 2.4272in
.. |image4| image:: media/image4.png
   :width: 6.69291in
   :height: 3.53706in
.. |image5| image:: media/image5.png
   :width: 6.69291in
   :height: 3.58143in
.. |image6| image:: media/image6.png
   :width: 6.69291in
   :height: 4.52193in
.. |image7| image:: media/image7.png
   :width: 6.69291in
   :height: 0.82298in
.. |image8| image:: media/image8.png
   :width: 6.69291in
   :height: 3.05694in
.. |image9| image:: media/image9.png
   :width: 6.69291in
   :height: 3.17864in
.. |image10| image:: media/image10.png
   :width: 6.69291in
   :height: 4.20087in
.. |image11| image:: media/image11.png
   :width: 6.69291in
   :height: 4.1976in
.. |image12| image:: media/image12.png
   :width: 6.69291in
   :height: 4.19529in
