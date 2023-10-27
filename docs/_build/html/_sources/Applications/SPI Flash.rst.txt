Introduction 
=============

The Talaria TWO module has a 2MB SPI Flash for storing application and
user data. This application note describes using the SPI Flash APIs to
read, write and erase flash on Talaria TWO module.

List of APIs
============

1. spi_mem_device(): SPI memory device.

2. os_flash_get_spi_dev(): Gets SPI device pointer for flash.

3. spi_sector_erase(): Erases sector.

4. spi_mem_write(): Writes on a specific position in flash.

5. spi_mem_read(): Reads from a position in flash.

For more details on APIs, refer:

T2-RM001-V25-Talaria_TWO_SDK_API_Reference_Guide.pdf

(path: *sdk_x.y\\doc\\reference_guides\\api_reference_guide*).

**Note**: x and y refer to the SDK release version. For example:
*sdk_2.4\\doc*.

Using Talaria TWO SPI Flash 
============================

Talaria TWO SPI Flash Memory Layout 
------------------------------------

Figure 1 shows the default SPI Flash memory layout for the Talaria TWO.

|image1|

Figure : Talaria TWO SPI Flash Memory Layout Default Configuration

Figure 2 shows the SPI Flash memory layout for sample application 2
which uses the partition table spiflash_part_table.json.

|image2|

Figure : SPI Flash Memory Layout for SPI Flash Example Applications

**Note**: The block marked as Available in Figure 2 is not assigned as a
partition in the spiflash_part_table.json since raw spi_flash operations
are used for the example applications.

To replace the default partition table, execute the following steps:

1. Load Gordon

+-----------------------------------------------------------------------+
| ./script/boot.py --device /dev/ttyUSB2 --reset=evk42                  |
| ./apps/gordon/bin/gordon.elf                                          |
+=======================================================================+
+-----------------------------------------------------------------------+

..

   |image3|

Figure : Writing gordon.elf – output

2. Write spiflash_part_table.json in Talaria TWO module.

+-----------------------------------------------------------------------+
| ./script/flash.py --device /dev/ttyUSB2 from_json                     |
| ./examples/using_filesystem/spiflash_part_table.json                  |
+=======================================================================+
+-----------------------------------------------------------------------+

..

   |image4|

Figure : Writing spiflash_part_table.json – output

Sample application 1: spiflash_sample1
--------------------------------------

This sample application erases a sector, writes data, and then reads it
back. In the macro, we define 0x100000 as the SPI flash address for this
example.

In this application, the whole sector is erased before performing a
write operation.

+-----------------------------------------------------------------------+
| #define SPI_FLASH_LOC 0x1c0000                                        |
+=======================================================================+
+-----------------------------------------------------------------------+

The struct spi_mem_device is a type of object representing a SPI bus and
the SPI (Flash) memory device.

+-----------------------------------------------------------------------+
| static struct spi_mem_device flash;                                   |
+=======================================================================+
+-----------------------------------------------------------------------+

print_spi_params() prints the SPI flash parameters.

+-----------------------------------------------------------------------+
| os_printf("\\n***SPI Flash Parameters***\\n");                        |
|                                                                       |
| os_printf("id_code: 0x%X\\n", flash.sm_params.mp_idcode);             |
|                                                                       |
| os_printf("page size: %d\\n", flash.sm_params.mp_page_size);          |
|                                                                       |
| os_printf("page count: %d\\n", flash.sm_params.mp_page_count);        |
|                                                                       |
| os_printf("sector size: %d\\n", flash.sm_params.mp_sector_size);      |
|                                                                       |
| os_printf("sector erase time: %d\\n",                                 |
| flash.sm_params.mp_sector_erase_time);                                |
|                                                                       |
| os_printf("bulk erase time: %d\\n\\n",                                |
| flash.sm_params.mp_bulk_erase_time);                                  |
+=======================================================================+
+-----------------------------------------------------------------------+

**Initiate communication between SPI flash and CPU**:

The os_flash_get_spi_dev() is used for fetching a pointer to SPI Flash
device. This pointer to spi_mem_device is used for further operations on
the SPI Flash as explained further.

+-----------------------------------------------------------------------+
| spi_mem = os_flash_get_spi_dev();                                     |
+=======================================================================+
+-----------------------------------------------------------------------+

**Erase a sector**:

Erase a sector of the SPI Flash using spi_sector_erase() to ensure there
is no previous data and prepare it for writing. It erases the target
location first.

+-----------------------------------------------------------------------+
| os_printf("Erasing sector at 0x%02X\\n\\n", SPI_FLASH_LOC);           |
|                                                                       |
| spi_sector_erase(spi_mem, SPI_FLASH_LOC);                             |
+=======================================================================+
+-----------------------------------------------------------------------+

**Write data**:

Use spi_mem_write()to write the data to SPI flash.

+-----------------------------------------------------------------------+
| os_printf("Writing: 0x");                                             |
|                                                                       |
| for(int i = 0; i < sizeof data; i++)                                  |
|                                                                       |
| {                                                                     |
|                                                                       |
| os_printf("%02X", data[i]);                                           |
|                                                                       |
| }                                                                     |
|                                                                       |
| os_printf("\\tat 0x%02X\\n\\n", SPI_FLASH_LOC);                       |
|                                                                       |
| spi_mem_write(spi_mem, SPI_FLASH_LOC, data, sizeof data);             |
+=======================================================================+
+-----------------------------------------------------------------------+

**Read data**:

Use spi_mem_read()to read the data back from SPI flash.

+-----------------------------------------------------------------------+
| uint8_t buf[sizeof data];                                             |
|                                                                       |
| spi_mem_read(&flash, SPI_FLASH_LOC, buf, sizeof data);                |
|                                                                       |
| os_printf("Read: 0x");                                                |
|                                                                       |
| for(int i = 0; i < sizeof buf; i++)                                   |
|                                                                       |
| {                                                                     |
|                                                                       |
| os_printf("%02X", buf[i]);                                            |
|                                                                       |
| }                                                                     |
|                                                                       |
| os_printf("\\tat 0x%02X\\n\\n", SPI_FLASH_LOC);                       |
+=======================================================================+
+-----------------------------------------------------------------------+

Running the Application 
~~~~~~~~~~~~~~~~~~~~~~~~

Program spiflash_sample1.elf using the Download tool:

1. Launch the Download tool provided with InnoPhase Talaria TWO SDK.

2. In the GUI window:

   a. Boot Target: Select the appropriate EVK from the drop-down.

   b. ELF Input: Load the spiflash_sample1.elf by clicking on Select ELF
      File.

   c. Programming: Prog RAM or Prog Flash as per requirement.

For more details on using the Download tool, refer to the document:
UG_Download_Tool.pdf (path: *sdk_x.y\\pc_tools\\Download_Tool\\doc*).

Expected Output
~~~~~~~~~~~~~~~

+-----------------------------------------------------------------------+
| UART:NWWWWAEBuild $Id: git-f92bee540 $                                |
|                                                                       |
| $App:git-7bdfd62                                                      |
|                                                                       |
| SDK Ver: sdk_2.4                                                      |
|                                                                       |
| Spi Flash Demo App 1                                                  |
|                                                                       |
| \***SPI Flash Parameters**\*                                          |
|                                                                       |
| id_code: 0xC86515                                                     |
|                                                                       |
| page size: 256                                                        |
|                                                                       |
| page count: 8192                                                      |
|                                                                       |
| sector size: 4096                                                     |
|                                                                       |
| sectore erase time: 128000                                            |
|                                                                       |
| bulk erase time: 768000                                               |
|                                                                       |
| Erasing sector at 0x1C0000                                            |
|                                                                       |
| Writing: 0xDEADBEEF at 0x1C0000                                       |
|                                                                       |
| Read: 0xDEADBEEF at 0x1C0000                                          |
+=======================================================================+
+-----------------------------------------------------------------------+

Sample application 2: spiflash_sample2
--------------------------------------

One property of SPI Flash is that, when a bit is set to 0, it cannot be
set to 1 without an erase operation. Also, another property of most SPI
Flash controllers is where an erase operation is done in sectors.

In the Sample Application 1, we avoid this by simply erasing whole
sector before performing a write. In many cases however, we can only
erase the sector without losing data. In the sample application, we make
sure that we preserve the data in the addresses where we did not write.

The sample application below runs three tests:

1. Write data and Read at the same location. Data read will be the same
   as written

2. Write different data2 at the same location without erasing. Data read
   will not match because the location already had existing data

3. Write data3 at a second location. Write data at the original
   location, while verifying contents first. Read data from both
   locations. Data read from both locations should match what was
   written

For this application in the macro, we define 0x100000 as the SPI flash
address.

+-----------------------------------------------------------------------+
| #define SPI_FLASH_LOC 0x1c0000                                        |
|                                                                       |
| #define DATA_OFFSET 0x80                                              |
+=======================================================================+
+-----------------------------------------------------------------------+

struct spi_mem_device is a type of object representing SPI (Flash)
memory device.

os_flash_get_spi_dev() is the get SPI device pointer for flash
(spi-mem).

+-----------------------------------------------------------------------+
| spi_mem = os_flash_get_spi_dev();                                     |
+=======================================================================+
+-----------------------------------------------------------------------+

print_spi_params() prints the SPI flash parameters.

+-----------------------------------------------------------------------+
| print_spi_params();                                                   |
+=======================================================================+
+-----------------------------------------------------------------------+

spi_sector_erase() erases a sector of the SPI flash to ensure there is
no previous data and prepare it for writing. It erases the target
location first.

+-----------------------------------------------------------------------+
| spi_sector_erase(&flash, SPI_FLASH_LOC);                              |
+=======================================================================+
+-----------------------------------------------------------------------+

print_array_hex() prints the array as a hex decimal values.

+-----------------------------------------------------------------------+
| print_array_hex(data, sizeof data);                                   |
+=======================================================================+
+-----------------------------------------------------------------------+

**Case 1**:

spi_mem_write() writes in a specific position in flash. The function
returns M2M_SUCCESS for successful operations and a negative value
otherwise.

+-----------------------------------------------------------------------+
| spi_mem_write(&flash, SPI_FLASH_LOC, data, sizeof data);              |
+=======================================================================+
+-----------------------------------------------------------------------+

spi_mem_read()function reads the data from the mentioned location in
flash memory through serial peripheral interface and print_array_hex()
prints the array as a hex decimal value.

+-----------------------------------------------------------------------+
| uint8_t buf[sizeof data];                                             |
|                                                                       |
| spi_mem_read(&flash, SPI_FLASH_LOC, buf, sizeof data);                |
|                                                                       |
| os_printf("Read: 0x");                                                |
|                                                                       |
| print_array_hex(buf, sizeof buf);                                     |
|                                                                       |
| os_printf("\\tat 0x%02X\\n\\n", SPI_FLASH_LOC);                       |
+=======================================================================+
+-----------------------------------------------------------------------+

**Case 2**:

In test case 2, spi_mem_write() function writes the data in a specific
position in the same location in flash, but with different content.

+-----------------------------------------------------------------------+
| spi_mem_write(&flash, SPI_FLASH_LOC, data2, sizeof data2);            |
+=======================================================================+
+-----------------------------------------------------------------------+

spi_mem_read()function reads the data from mentioned location in flash
memory through serial peripheral interface. The value read will be
different from expected.

print_array_hex() prints the array as hex decimal values.

+-----------------------------------------------------------------------+
| spi_mem_read(&flash, SPI_FLASH_LOC, buf, sizeof data2);               |
|                                                                       |
| os_printf("Read: 0x");                                                |
|                                                                       |
| print_array_hex(buf, sizeof buf);                                     |
|                                                                       |
| os_printf("\\tat 0x%02X\\n\\n", SPI_FLASH_LOC);                       |
+=======================================================================+
+-----------------------------------------------------------------------+

**Case 3**:

In test case 3, spi_mem_safe_write() function writes data at a different
location in flash.

Post which, it writes at the same location as case 1 and 2 again.
spi_mem_read() reads the flash memory and prints it in the console.

+-----------------------------------------------------------------------+
| os_printf("Writing: 0x");                                             |
|                                                                       |
| print_array_hex(data3, sizeof data3);                                 |
|                                                                       |
| os_printf("\\tat 0x%02X\\n", SPI_FLASH_LOC+DATA_OFFSET);              |
|                                                                       |
| spi_flash_safe_write(spi_mem, SPI_FLASH_LOC+DATA_OFFSET, data3,       |
| sizeof data3);                                                        |
+=======================================================================+
+-----------------------------------------------------------------------+

spi_mem_read()reads data from the location which is
SPI_FLASH_LOC+DATA_OFFSET and prints it in console.

+-----------------------------------------------------------------------+
| spi_mem_read(spi_mem, SPI_FLASH_LOC+DATA_OFFSET, buf, sizeof buf);    |
|                                                                       |
| os_printf("Read: 0x");                                                |
|                                                                       |
| print_array_hex(buf, sizeof buf);                                     |
|                                                                       |
| os_printf("\\tat 0x%02X\\n\\n", SPI_FLASH_LOC+DATA_OFFSET);           |
+=======================================================================+
+-----------------------------------------------------------------------+

print_spi_params() function prints all the parameters of the flash onto
the console.

+-----------------------------------------------------------------------+
| os_printf("\\n***SPI Flash Parameters***\\n");                        |
|                                                                       |
| os_printf("id_code: 0x%X\\n", flash.sm_params.mp_idcode);             |
|                                                                       |
| os_printf("page size: %d\\n", flash.sm_params.mp_page_size);          |
|                                                                       |
| os_printf("page count: %d\\n", flash.sm_params.mp_page_count);        |
|                                                                       |
| os_printf("sector size: %d\\n", flash.sm_params.mp_sector_size);      |
|                                                                       |
| os_printf("sectore erase time: %d\\n",                                |
| flash.sm_params.mp_sector_erase_time);                                |
|                                                                       |
| os_printf("bulk erase time: %d\\n\\n",                                |
| flash.sm_params.mp_bulk_erase_time);                                  |
+=======================================================================+
+-----------------------------------------------------------------------+

Here, we implement a function called spi_flash_safe_write(). To ensure
we can write in SPI Flash properly, we execute the following steps:

1. Read the contents of target address and make sure all bits are still
   set to 1

2. If all contents are still 1, do a normal write operation. Write
   operation is complete at this point

3. If not, read the entire contents of the sector where target address
   belongs to a buffer

4. Insert the contents of the data to be written into the buffer

5. Erase the sector where the address belongs to

6. Write the buffer into the sector where the address belongs to.

spi_flash_safe_write() reads data at target location and verifies the
data it is all Fs. big_buff is a memory buffer which has memory
allocated to it by the os_alloc() function. This function allocates a
block of memory at least size bytes in length. The largest possible
allocated memory block is 57336 bytes, but this depends on the
availability of free blocks. Memory is freed by calling os_free()
previously. This reads the sector and modifies the data.

+-----------------------------------------------------------------------+
| uint8_t \*big_buff;                                                   |
|                                                                       |
| big_buff = os_alloc(dev->sm_params.mp_sector_size);                   |
+=======================================================================+
+-----------------------------------------------------------------------+

This allocates enough data to read a whole sector.

+-----------------------------------------------------------------------+
| memset(big_buff, 0xFF, dev->sm_params.mp_sector_size);                |
|                                                                       |
| uint8_t sector_num = address/dev->sm_params.mp_sector_size;           |
|                                                                       |
| uint16_t offset = address%dev->sm_params.mp_sector_size;              |
|                                                                       |
| uint32_t sector_start = sector_num \* dev->sm_params.mp_sector_size;  |
|                                                                       |
| spi_mem_read(dev, sector_start, big_buff,                             |
| dev->sm_params.mp_sector_size);                                       |
|                                                                       |
| memcpy(big_buff+offset, data, len);                                   |
+=======================================================================+
+-----------------------------------------------------------------------+

spi_sector_erase() function erases the memory sector.

+-----------------------------------------------------------------------+
| spi_sector_erase(dev, sector_start);                                  |
+=======================================================================+
+-----------------------------------------------------------------------+

spi_mem_write() function writes on a specific position in flash and
frees the memory by calling os_free().

+-----------------------------------------------------------------------+
| spi_mem_write(dev, sector_start, big_buff,                            |
| dev->sm_params.mp_sector_size);                                       |
|                                                                       |
| os_free(big_buff);                                                    |
+=======================================================================+
+-----------------------------------------------------------------------+

.. _running-the-application-1:

Running the Application 
~~~~~~~~~~~~~~~~~~~~~~~~

Program spiflash_sample2.elf using the Download tool:

1. Launch the Download tool provided with InnoPhase Talaria TWO SDK.

2. In the GUI window:

   a. Boot Target: Select the appropriate EVK from the drop-down.

   b. ELF Input: Load the spiflash_sample2.elf by clicking on Select ELF
      File.

   c. Programming: Prog RAM or Prog Flash as per requirement.

For more details on using the Download tool, refer to the document:
UG_Download_Tool.pdf (path: *sdk_x.y\\pc_tools\\Download_Tool\\doc*).

.. _expected-output-1:

Expected Output
~~~~~~~~~~~~~~~

+-----------------------------------------------------------------------+
| UART:NWWWWAEBuild $Id: git-f92bee540 $                                |
|                                                                       |
| $App:git-7bdfd62                                                      |
|                                                                       |
| SDK Ver: sdk_2.4                                                      |
|                                                                       |
| Spi Flash Demo App 2                                                  |
|                                                                       |
| \***SPI Flash Parameters**\*                                          |
|                                                                       |
| id_code: 0xC86515                                                     |
|                                                                       |
| page size: 256                                                        |
|                                                                       |
| page count: 8192                                                      |
|                                                                       |
| sector size: 4096                                                     |
|                                                                       |
| sectore erase time: 128000                                            |
|                                                                       |
| bulk erase time: 768000                                               |
|                                                                       |
| Erasing sector at 0x1C0000                                            |
|                                                                       |
| Test 1:                                                               |
|                                                                       |
| Writing: 0xDEADBEEF at 0x1C0000                                       |
|                                                                       |
| Read: 0xDEADBEEF at 0x1C0000                                          |
|                                                                       |
| Test 2:                                                               |
|                                                                       |
| Writing: 0xAAAAAAAA at 0x1C0000                                       |
|                                                                       |
| Read: 0x8AA8AAAA at 0x1C0000                                          |
|                                                                       |
| Test 3:                                                               |
|                                                                       |
| Writing: 0xC0DEC0DE at 0x1C0080                                       |
|                                                                       |
| Writing: 0xDEADBEEF at 0x1C0000                                       |
|                                                                       |
| Read: 0x8AA8AAAA at 0x1C0000                                          |
|                                                                       |
| Read: 0xC0DEC0DE at 0x1C0080                                          |
+=======================================================================+
+-----------------------------------------------------------------------+

.. |image1| image:: media/image1.png
   :width: 6.69291in
   :height: 0.56243in
.. |image2| image:: media/image2.png
   :width: 6.69291in
   :height: 0.56243in
.. |image3| image:: media/image3.png
   :width: 6.29921in
   :height: 0.85122in
.. |image4| image:: media/image4.png
   :width: 6.29921in
   :height: 0.37661in
