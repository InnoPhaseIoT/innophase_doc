JSON file format reference
----------------------------

1.  BOOT_TYPE

    a. SECUREBOOT - Determine if secureboot is used

2.  PROVIS_INFO

    a. AP_SSID - SSID of AP

    b. AP_PASSPHRASE – Passphrase for AP

3.  HTTP

    a. IMAGES[] – List of binary images to be flashed from HTTP

       i.   URL – URL of server

       ii.  PORT – port of server

       iii. IMG_FILE – image file name

       iv.  IMG_ADDR – address in flash to flash image

    b. FILES[] – List of files to be downloaded from server and written
       to filesystem

       i.   URL – URL of server

       ii.  PORT – port of server

       iii. FILE - filename

       iv.  MOUNT_POINT – mount point of filesystem to write file to

4.  ENROLL

    a. KEY_FILE - JSON keyfile used for enrollment

5.  PARTITION

    a. PART_FILE - JSON file describing partition table

6.  BOOT_IMAGE

    a. IMG_FILE - Default boot image flashed at 0x1000

7.  IMAGES

    a. APP_IMAGES []- List images to and files to be flashed

       i.  ELF_FILE – filename of ELF file

       ii. ADDR – address in flash to flash image to

8.  PARTITION

    a. PART_FILE – Partition table json file

9.  USER_FS

    a. MOUNT_ADDR – Mount address for UFS

    b. UFS_FILES - List of files to be combined into a filesystem image
       then flashed

10. FILES[] – List of files to be written to mounted filesystem

    a. FILE - Filename

    b. MOUNT_POINT – Mount point of filesystem to write file to

11. SYSFS

    a. SYSFS_FILES[] – List of files to add to sysfs

12. VERIFY

    a. Enable extra verification step

13. ENCRYPT

    a. FILES[] – List of files in filesystem to be encrypted
