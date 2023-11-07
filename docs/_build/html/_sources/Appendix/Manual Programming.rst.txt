Manual Programming
-------------------

Python Scripts
~~~~~~~~~~~~~~

1. boot.py – used for programming Talaria TWO and generate .img file
   from application .elf files

2. flash.py – used to flash Talaria TWO. To run the flash.py script the
   Gordon application or factory_loader application must first be loaded
   using boot.py

Write Image or FS
^^^^^^^^^^^^^^^^^

Generate application .img file using boot.py.

+-----------------------------------------------------------------------+
| ./script/boot.py –output=<app.img> <application.elf>                  |
+=======================================================================+
+-----------------------------------------------------------------------+

Use flash.py to flash image.

+-----------------------------------------------------------------------+
| ./script/flash.py write <addr> <img file>                             |
+=======================================================================+
+-----------------------------------------------------------------------+

Read
^^^^

Use flash.py to read contents of flash.

+-----------------------------------------------------------------------+
| ./script/flash.py read –output <filename> <addr> <size>               |
+=======================================================================+
+-----------------------------------------------------------------------+

Verify
^^^^^^

Use flash.py to verify contents of flash.

+-----------------------------------------------------------------------+
| ./script/flash.py verify <addr> <filename>                            |
+=======================================================================+
+-----------------------------------------------------------------------+

Enroll
^^^^^^

1. Generate keys in json format. A sample keys.json is provided.

2. Use flash.py to enroll keys.

+-----------------------------------------------------------------------+
| ./script/flash.py enroll –keyfile <key.json>                          |
+=======================================================================+
+-----------------------------------------------------------------------+

Programming & Reading Partition Table
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Create/modify partition table (default partition table is provided)

2. Program partition table using flash.py

+-----------------------------------------------------------------------+
| ./script/flash.py from_json <default.json>                            |
+=======================================================================+
+-----------------------------------------------------------------------+

3. Read partition table

+-----------------------------------------------------------------------+
| ./script/flash.py to_json <json_file>                                 |
+=======================================================================+
+-----------------------------------------------------------------------+

Re-flashing the Factory Loader
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Inhibit boot (short gpio17 to GND, press reset, unshort gpio17 and
   GND)

2. Load Gordon application

+-----------------------------------------------------------------------+
| ./script/boot.py apps/gordon.elf                                      |
+=======================================================================+
+-----------------------------------------------------------------------+

3. Flash factory loader

+-----------------------------------------------------------------------+
| ./script/flash.py write 0x1000 factory_loader.img                     |
+=======================================================================+
+-----------------------------------------------------------------------+

Building a Filesystem
~~~~~~~~~~~~~~~~~~~~~

To build a filesystem for the user/root file system., the mklittlefs
tool.

+-----------------------------------------------------------------------+
| ./mklittlefs –s 0x70000 –c ./UFS                                      |
+=======================================================================+
+-----------------------------------------------------------------------+

Partition Table Partition
~~~~~~~~~~~~~~~~~~~~~~~~~

The default partition table reflects the flash layout as shown in Figure
9 using SSBL.

+-----------------------------------------------------------------------+
| {                                                                     |
|                                                                       |
| "partitions": [                                                       |
|                                                                       |
| {                                                                     |
|                                                                       |
| "index": 0,                                                           |
|                                                                       |
| "ptype": 30,                                                          |
|                                                                       |
| "sect_start": 1,                                                      |
|                                                                       |
| "sect_count": 31,                                                     |
|                                                                       |
| "\_last": 31,                                                         |
|                                                                       |
| "\_ptype": "BOOT"                                                     |
|                                                                       |
| },                                                                    |
|                                                                       |
| {                                                                     |
|                                                                       |
| "index": 1,                                                           |
|                                                                       |
| "ptype": 30,                                                          |
|                                                                       |
| "sect_start": 32,                                                     |
|                                                                       |
| "sect_count": 352,                                                    |
|                                                                       |
| "\_last": 383,                                                        |
|                                                                       |
| "\_ptype": "BOOT"                                                     |
|                                                                       |
| },                                                                    |
|                                                                       |
| {                                                                     |
|                                                                       |
| "index": 2,                                                           |
|                                                                       |
| "ptype": 15,                                                          |
|                                                                       |
| "sect_start": 384,                                                    |
|                                                                       |
| "sect_count": 112,                                                    |
|                                                                       |
| "\_last": 495,                                                        |
|                                                                       |
| "\_ptype": "DATA"                                                     |
|                                                                       |
| },                                                                    |
|                                                                       |
| {                                                                     |
|                                                                       |
| "index": 3,                                                           |
|                                                                       |
| "ptype": 14,                                                          |
|                                                                       |
| "sect_start": 496,                                                    |
|                                                                       |
| "sect_count": 16,                                                     |
|                                                                       |
| "\_last": 511,                                                        |
|                                                                       |
| "\_ptype": "SYSFS"                                                    |
|                                                                       |
| }                                                                     |
|                                                                       |
| ],                                                                    |
|                                                                       |
| "\_identify": {                                                       |
|                                                                       |
| "idcode": 13133077,                                                   |
|                                                                       |
| "num_pages": 8192,                                                    |
|                                                                       |
| "page_size": 256,                                                     |
|                                                                       |
| "sector_size": 4096                                                   |
|                                                                       |
| }                                                                     |
|                                                                       |
| }                                                                     |
+=======================================================================+
+-----------------------------------------------------------------------+
