Introduction 
=============

The secure_files example application demonstrates reading and writing
encrypted files from/to the filesystem. To use secure_files, the
secureboot mode should be enabled.

For more details on secureboot mode, refer
Application_for_using_SSBL.pdf (*sdk_x.y_alpha\\apps\\ssbl\\doc*).

**Note**: x and y in sdk_x.y refer to the SDK package release version.

Description of Operation 
=========================

1. Reconstruct secureboot secret and get the firmware cipher key from
   flash

2. Mount the filesystem

3. Write the encrypted message to a file using firmware cipher key

4. Read the encrypted message as plain text (should be garbled)

5. Read and decrypt encrypted message (this should show the original
   message contents)

Building and Flashing Process
=============================

Building Components
-------------------

1. Build secure SSBL (refer section: 7.2.1 in Application
   for_using_SSBL.pdf (*sdk_x.y_alpha\\apps\\ssbl\\doc)*

2. Build the secure_files example:

+-----------------------------------------------------------------------+
| cd <sdk>/examples/secure_files                                        |
|                                                                       |
| make clean                                                            |
|                                                                       |
| make KEY=../../apps/ssbl/enroll.json                                  |
+=======================================================================+
+-----------------------------------------------------------------------+

Flashing Components
-------------------

1. Enroll keys & flash SSBL components in secureboot mode (refer steps 1
   to 4 of section: 7.2.2 in Application for_using_SSBL.pdf
   (*sdk_x.y_alpha\\apps\\ssbl\\doc)*

2. Build the secure filesystem (data_secure.img):

+-----------------------------------------------------------------------+
| cd <sdk>                                                              |
|                                                                       |
| python ./script/build_rootfs_generic.py --folder_path                 |
| examples/secure_files/ --secure True --keyfile                        |
| ./apps/ssbl/enroll.json                                               |
+=======================================================================+
+-----------------------------------------------------------------------+

3. Create Signed and encrypted ELF (secure_files.elf.enc)

+-----------------------------------------------------------------------+
| cd <sdk>/examples/secure_files                                        |
|                                                                       |
| make clean                                                            |
|                                                                       |
| make KEY=<sdk>/apps/ssbl/enroll.json                                  |
+=======================================================================+
+-----------------------------------------------------------------------+

4. Flash application at 0x20000

+-----------------------------------------------------------------------+
| cd <sdk>/examples/secure_files$                                       |
|                                                                       |
| ../../script/flash.py write 0x20000 out/secure_files.elf.enc          |
+=======================================================================+
+-----------------------------------------------------------------------+

5. Flash the filesystem

+-----------------------------------------------------------------------+
| cd <sdk>/examples/secure_files$                                       |
|                                                                       |
| ../../script/flash.py write 0x180000 root_secure.img                  |
+=======================================================================+
+-----------------------------------------------------------------------+

Expected Output
---------------

|image1|

Figure : Expected output

.. |image1| image:: media/image1.png
   :width: 6.69291in
   :height: 4.83438in
