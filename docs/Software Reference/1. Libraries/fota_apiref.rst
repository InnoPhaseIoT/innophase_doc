FirmWare Over The Air
-----------------------

Firmware-Over-the-Air (FOTA) allows for wireless delivery of firmware
updates and/or configurations to embedded devices.

This section describes the FOTA process for the Talaria TWO EVB using
the Talaria TWO SDK with details on how to implement or trigger FOTA in
a customer provided application.

This implementation of FOTA provides the following facilities:

1. Check for the availability of new upgrades

2. Securely download the image into flash

3. Check the validity of the downloaded image

4. Set the new image as the boot image

In conjunction with SSBL, it enables booting the latest image
downloaded. The firmware is downloaded into the application image
partition in Flash.

Refer FOTA application for various configuration files and modules on
which FOTA is dependent, its design and functional flow.

Features and Limitations
~~~~~~~~~~~~~~~~~~~~~~~~~

Following are the FOTA application features:

1. FOTA over HTTP/HTTPS.

2. Image download from Cloud or any HTTP/web server.

3. Two copy solution. Backup copy of the correct firmware always exists.

4. Image integrity check using sha256 hash.

5. Error handling and recovery

   a. If any error occurs during downloading the image or updating the
      configuration files (part.json/boot.json/fota_config.json), the
      device will remain in the current image.

   b. If a reboot occurs (due to issues like power failure) during image
      download or configuration files upgrade, the device will boot with
      the current image.

6. JSON based configuration

Limitations: Upgrading the Certificates is not supported as of now.

Header file/s
~~~~~~~~~~~~~~~~~~~~~~~~~
Components/fota/inc/fota.h.

API Reference
~~~~~~~~~~~~~~~~~~~~~~~~~

fota_init
~~~~~~~~~~~~~~~~~~~~~~~~~

Overview
~~~~~~~~~~~~~~~~~~~~~~~~~

This API initializes the FOTA module.

Definition 
~~~~~~~~~~~

.. table:: Table : fota_perform - parameters

   +-----------------------------------------------------------------------+
   | fota_handle_t \*                                                      |
   |                                                                       |
   | fota_init(void)                                                       |
   +=======================================================================+
   +-----------------------------------------------------------------------+

Return
~~~~~~

Success: Pointer to FOTA handle.

Error: NULL.

fota_perform
------------

.. _overview-1:

Overview
~~~~~~~~

Performs the FOTA update. This API checks for the update. If an update
is available, it downloads the firmware specified in the fota.config
file.

.. _definition-1:

Definition
~~~~~~~~~~

.. table:: Table : fota_commit - parameters

   +-----------------------------------------------------------------------+
   | int                                                                   |
   |                                                                       |
   | fota_perform(fota_handle_t \*f_handle, int check_for_update, int      |
   | flags)                                                                |
   +=======================================================================+
   +-----------------------------------------------------------------------+

Parameters
~~~~~~~~~~

.. table:: Table : fota_deinit - parameters

   +---------------+------------------------------------------------------+
   | **Parameter** | **Description**                                      |
   +===============+======================================================+
   | *handle*      | Handle returned by fota_init()                       |
   +---------------+------------------------------------------------------+
   | *chec         | This can be FOTA_NO_CHECK_FOR_UPDATE /               |
   | k_for_update* | FOTA_CHECK_FOR_UPDATE /                              |
   |               | FOTA_FETCH_CFG_NO_CHECK_FOR_UPDATE                   |
   |               |                                                      |
   |               | 1. FOTA_NO_CHECK_FOR_UPDATE - No check done. FOTA is |
   |               |    done using the currently available fota.config    |
   |               |    file in the data fs.                              |
   |               |                                                      |
   |               | 2. FOTA_CHECK_FOR_UPDATE - Check if an update is     |
   |               |    available before executing FOTA. foat.config file |
   |               |    will be fetched from cloud and the package        |
   |               |    version of the latest file is compared against    |
   |               |    the fota.config file present in data fs. FOTA is  |
   |               |    done only if the latest version is greater than   |
   |               |    the one preset on the device.                     |
   |               |                                                      |
   |               | 3. FOTA_FETCH_CFG_NO_CHECK_FOR_UPDATE - foat.config  |
   |               |    file will be fetched from the cloud. No check is  |
   |               |    done using package version. Newly downloaded      |
   |               |    fota.config file will be used for FOTA. This      |
   |               |    option can be used only if availability of newer  |
   |               |    package is confirmed using some other mechanism   |
   |               |    (like, MQTT for example) and FOTA needs to be     |
   |               |    done as per the latest fota.config in the cloud.  |
   +---------------+------------------------------------------------------+
   | *Flags*       | Not currently used. Always set to 0.                 |
   +---------------+------------------------------------------------------+

.. _return-1:

Return
~~~~~~

Success: 0

Error: <0 (Refer fota_error_t)

fota_commit
~~~~~~~~~~~~~~~~~~~~~~~~~
.. _overview-2:

Overview
~~~~~~~~

After the FOTA update is done, call this function to set the newly
updated firmware as the default. This needs to be called after
fota_perform() is a success.

.. _definition-2:

Definition
~~~~~~~~~~

+-----------------------------------------------------------------------+
| int                                                                   |
|                                                                       |
| fota_commit(fota_handle_t \*f_handle, int do_reset)                   |
+=======================================================================+
+-----------------------------------------------------------------------+

.. _parameters-1:

Parameters
~~~~~~~~~~

+-----------+----------------------------------------------------------+
| **Pa      | **Description**                                          |
| rameter** |                                                          |
+===========+==========================================================+
| *         | Pointer to the FOTA handle that was returned by          |
| f_handle* | fota_init()                                              |
+-----------+----------------------------------------------------------+
| *         | If set to 1, perform reset                               |
| do_reset* |                                                          |
+-----------+----------------------------------------------------------+

.. _return-2:

Return
~~~~~~

Success: 0

Error: -1

fota_deinit
~~~~~~~~~~~~~~~~~~~~~~~~~

.. _overview-3:

Overview
~~~~~~~~

This API will release all the resources allocated during fota_init() and
other FOTA API calls.

.. _definition-3:

Definition
~~~~~~~~~~

+-----------------------------------------------------------------------+
| void fota_deinit(fota_handle_t \* f_handle)                           |
+=======================================================================+
+-----------------------------------------------------------------------+

.. _parameters-2:

Parameters
~~~~~~~~~~

+-----------+----------------------------------------------------------+
| **Pa      | **Description**                                          |
| rameter** |                                                          |
+===========+==========================================================+
| *         | Pointer to FOTA handle that was returned by fota_init()  |
| f_handle* |                                                          |
+-----------+----------------------------------------------------------+

.. _return-3:

Return
~~~~~~

None.

Application Example
~~~~~~~~~~~~~~~~~~~~~~~~~

For the example code, refer: *apps/fota application*.
