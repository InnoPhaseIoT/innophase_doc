Introduction 
=============

Talaria TWO EVK has a 2MB SPI Flash for storing user data. This
application note describes using the APIs to show case the filesystem
read, write and remove functionalities on the Talaria TWO EVK.

Sample Code Walkthrough
=======================

Using_filesystem
----------------

The using_filesystem application illustrates performing the following
basic filesystem operations. To mount the file system,
utils_mount_rootfs() is called.

+-----------------------------------------------------------------------+
| /\* Mount FS \*/                                                      |
|                                                                       |
| os_printf("Mounting file system\\n");                                 |
|                                                                       |
| ret_code = utils_mount_rootfs();                                      |
|                                                                       |
| if(ret_code != 0){                                                    |
|                                                                       |
| os_printf("Failed to mount file system\\n");                          |
|                                                                       |
| return 0;                                                             |
|                                                                       |
| }                                                                     |
|                                                                       |
| else                                                                  |
|                                                                       |
| {                                                                     |
|                                                                       |
| os_printf("File system mounted\\n");                                  |
|                                                                       |
| }                                                                     |
+=======================================================================+
+-----------------------------------------------------------------------+

Read and Write
--------------

To read and write, the application uses the C library APIs - fputs() and
fgets().

In this example, a new file named /data/sample_text.txt is written in
the DATA partition of the filesystem.

+-----------------------------------------------------------------------+
| /\* Write file \*/                                                    |
|                                                                       |
| sample_file = fopen(configfile, "w");                                 |
|                                                                       |
| fputs("This is testing for file system...\\n", sample_file);          |
|                                                                       |
| fclose(sample_file);                                                  |
|                                                                       |
| os_printf("Write Done.\\n\\n");                                       |
|                                                                       |
| /\* Read file \*/                                                     |
|                                                                       |
| sample_file = fopen(configfile, "r");                                 |
|                                                                       |
| fgets(str, 50, sample_file);                                          |
|                                                                       |
| os_printf("file data = %s \\n", str);                                 |
|                                                                       |
| fclose(sample_file);                                                  |
|                                                                       |
| os_printf("Read Done.\\n\\n");                                        |
+=======================================================================+
+-----------------------------------------------------------------------+

 Fetching the File into a Buffer
--------------------------------

The utils_file_get() API is used to get the content of a file into a
buffer.

+-----------------------------------------------------------------------+
| char \*file_buf = utils_file_get(configfile, &size);                  |
|                                                                       |
| os_printf("File Data = %s \\n", file_buf);                            |
+=======================================================================+
+-----------------------------------------------------------------------+

Flashing & Running the Application
==================================

In Talaria TWO module, there are two ways of writing into the file
system:

1. Manually for factory setup

2. Programmatically

Generate & Flash a Filesystem Manually for Factory Setup
--------------------------------------------------------

To create a file system manually and write the file image using the
scripts available in SDK, execute the following steps:

a. Generate an image file using the mklittlefs tool. Go to
   *sdk_x.y\\tools\\mklittlefs* folder and execute the following
   command:

..

   **Note**: x and y in sdk_x.y refers to the SDK release version. For
   example: *sdk_2.4\\tools\\*.

   **Note**: The flash.img will contain the file(s) present in the data
   folder of current directory where this binary (mklittlefs) is
   executed.

+-----------------------------------------------------------------------+
| ./mklittlefs -s 0x40000 -c ../../examples/using_filesystem/data       |
| ../../examples/using_filesystem/flash.img                             |
+=======================================================================+
+-----------------------------------------------------------------------+

b. From the SDK folder, execute the remaining commands:

..

   Ensure to have a partition table containing allocation for DATA as a
   prerequisite. To manually flash an image file to a specific location,
   execute the following steps:

i. Load gordon.elf onto the Talaria TWO module.

+-----------------------------------------------------------------------+
| ./script/boot.py --device /dev/ttyUSB2 --reset=evk42_bl               |
| ./apps/gordon/bin/gordon.elf                                          |
+=======================================================================+
+-----------------------------------------------------------------------+

..

   |image1|

Figure 1: Loading gordon.elf

ii. Flash the image file to the desired location on the filesystem.

+-----------------------------------------------------------------------+
| ./script/flash.py --device /dev/ttyUSB2 part_write DATA               |
| ./examples/using_filesystem/flash.img                                 |
+=======================================================================+
+-----------------------------------------------------------------------+

..

   |image2|

Figure 2: Flashing the image

iii. Fetch the file(s) which was flashed.

+-----------------------------------------------------------------------+
| ./script/storage.py ls /data/                                         |
+=======================================================================+
+-----------------------------------------------------------------------+

..

   |image3|

Figure 3: Fetching files from data partition

Writing into the Filesystem Programmatically
--------------------------------------------

Running the Application 
~~~~~~~~~~~~~~~~~~~~~~~~

Program using_filesystem.elf using the Download tool:

1. Launch the Download tool provided with InnoPhase Talaria TWO SDK.

2. In the GUI window:

   a. Boot Target: Select the appropriate EVK from the drop-down.

   b. ELF Input: Load the using_filesystem.elf by clicking on Select ELF
      File.

3. Programming: Prog RAM or Prog Flash as per requirement.

For more details on using the Download tool, refer to the document:
UG_Download_Tool.pdf (path: *sdk_x.y\\pc_tools\\Download_Tool\\doc*).

As mentioned in section 4.2, a new file named \\data\\sample_text.txt is
written in the DATA partition of the filesystem.

Expected Output
~~~~~~~~~~~~~~~

+-----------------------------------------------------------------------+
| Y-BOOT 208ef13 2019-07-22 12:26:54 -0500 790da1-b-7                   |
|                                                                       |
| ROM yoda-h0-rom-16-0-gd5a8e586                                        |
|                                                                       |
| FLASH:PNWWWAEBuild $Id: git-ba65998b7 $                               |
|                                                                       |
| $App:git-d6262fda                                                     |
|                                                                       |
| SDK Ver: sdk_2.5                                                      |
|                                                                       |
| Using File System Demo App                                            |
|                                                                       |
| Mounting file system                                                  |
|                                                                       |
| File system mounted                                                   |
|                                                                       |
| Write Done.                                                           |
|                                                                       |
| File Data = This is testing for file system...                        |
|                                                                       |
| Read Done.                                                            |
|                                                                       |
| File Data = This is testing for file system...                        |
|                                                                       |
| ----------------Program Exit --------------------                     |
+=======================================================================+
+-----------------------------------------------------------------------+

After execution, for evaluation purposes, use the download tool Show
File System Contents option. Click on Show File System Contents. The
pop-up window displays the file written by the application.

|image4|

Figure 4: Download Tool - Show File System Contents

|image5|

Figure 5: Filename and size

The file size is also equal to the read value from the application.

Using the Read Files option available in the Download Tool to retrieve
the files and check the contents.

|image6|

Figure 6: Download Tool - File System: Read files

Contents are extracted into the folder specified in the Download Tool.

|image7|

Figure 7: Extracted files

.. |image1| image:: media/image1.png
   :width: 5.51181in
   :height: 0.47244in
.. |image2| image:: media/image2.png
   :width: 5.11811in
   :height: 0.35667in
.. |image3| image:: media/image3.png
   :width: 5.11811in
   :height: 0.61072in
.. |image4| image:: media/image4.png
   :width: 4.33071in
   :height: 1.48795in
.. |image5| image:: media/image5.png
   :width: 4.33071in
   :height: 0.87719in
.. |image6| image:: media/image6.png
   :width: 5.11811in
   :height: 1.60124in
.. |image7| image:: media/image7.png
   :width: 3.54331in
   :height: 2.16719in
