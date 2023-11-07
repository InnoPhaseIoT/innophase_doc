Utils
---------

Utils API provide a variety of frequently used general purpose
functionalities for the Talaria TWO platform.

Features and Limitations
~~~~~~~~~~~~~~~~~~~~~~~~~

This component provides the following features:

1. File system initialization and file access.

2. System utility function like software reset.

3. Wi-Fi connection profile initialization.

Header file/s
~~~~~~~~~~~~~~~~~~~~~~~~~

1. components/utils/inc/fs_defines.h

2. components/utils/inc/fs_utils.h

3. components/utils/inc/utils.h

4. components/utils/inc/wifi_utils.h

5. components/utils/inc/net_utils.h

API Reference
~~~~~~~~~~~~~~~~~~~~~~~~~

utils_mount_rootfs
~~~~~~~~~~~~~~~~~~~~~~~~~

Overview
~~~~~~~~

This API mounts the root FS. Root FS is used by the user application to
store application specific files like certificates, partition file (if
SSBL is used), FOTA configuration file and others.

This is in-fact a wrapper function for os_mount() API.

Definition
~~~~~~~~~~

.. table:: Table : utils_is_file_present – parameters

   +-----------------------------------------------------------------------+
   | int                                                                   |
   |                                                                       |
   | utils_mount_rootfs (void)                                             |
   +=======================================================================+
   +-----------------------------------------------------------------------+

Parameters
~~~~~~~~~~

None

Return
~~~~~~

Success: 0

Error: -1

utils_is_file_present
~~~~~~~~~~~~~~~~~~~~~~~~~

.. _overview-1:

Overview
~~~~~~~~

Used to check if a file is present in at a specified path or not in root
FS.

.. _definition-1:

Definition 
~~~~~~~~~~~

.. table:: Table : utils_file_size_get - parameters

   +-----------------------------------------------------------------------+
   | int                                                                   |
   |                                                                       |
   | utils_is_file_present (char \*path)                                   |
   +=======================================================================+
   +-----------------------------------------------------------------------+

.. _parameters-1:

Parameters
~~~~~~~~~~

.. table:: Table : utils_file_get - parameters

   +---------------+------------------------------------------------------+
   | **Parameter** | **Description**                                      |
   +===============+======================================================+
   | *path*        | Path of the file                                     |
   +---------------+------------------------------------------------------+

.. _return-1:

Return
~~~~~~

If the file is present – 1

If the file is not present - 0

utils_file_size_get
~~~~~~~~~~~~~~~~~~~~~~~~~

.. _overview-2:

Overview
~~~~~~~~

Used to get the size of the file at a specified path in root FS.

.. _definition-2:

Definition 
~~~~~~~~~~~

.. table:: Table : utils_file_store – parameters

   +-----------------------------------------------------------------------+
   | int                                                                   |
   |                                                                       |
   | utils_file_size_get (char \*path)                                     |
   +=======================================================================+
   +-----------------------------------------------------------------------+

.. _parameters-2:

Parameters
~~~~~~~~~~

.. table:: Table : show_heap – parameters

   +--------------+-------------------------------------------------------+
   | *            | **Description**                                       |
   | *Parameter** |                                                       |
   +==============+=======================================================+
   | *path*       | Path of the file                                      |
   +--------------+-------------------------------------------------------+

.. _return-2:

Return
~~~~~~

File size: >= 0

Error: < 0

utils_file_get
~~~~~~~~~~~~~~~~~~~~~~~~~

.. _overview-3:

Overview
~~~~~~~~

Used to get the content of a file into a buffer.

**Note**: If the buffer return is not freed, it will result in a memory
leak.

.. _definition-3:

Definition 
~~~~~~~~~~~

.. table:: Table : network_profile_new_from_ssid_pw – parameters

   +-----------------------------------------------------------------------+
   | char \*                                                               |
   |                                                                       |
   | utils_file_get (char \*path, int \*len)                               |
   +=======================================================================+
   +-----------------------------------------------------------------------+

.. _parameters-3:

Parameters
~~~~~~~~~~

.. table:: Table : network_profile_new_from_ssid_bssid_pw – parameters

   +--------------+-------------------------------------------------------+
   | *            | **Description**                                       |
   | *Parameter** |                                                       |
   +==============+=======================================================+
   | *path*       | Path of the file                                      |
   +--------------+-------------------------------------------------------+
   | *Len*        | Used to return the length of the file                 |
   +--------------+-------------------------------------------------------+

.. _return-3:

Return
~~~~~~

Success : Pointer to buffer having the content of the file.

Failure : NULL

utils_file_store
~~~~~~~~~~~~~~~~~~~~~~~~~

.. _overview-4:

Overview
~~~~~~~~

Used to store the content of a buffer into a file.

**Note**: There is no way to amend the data with this API. This will
store the data from the beginning of the file, replacing any older data
if present.

.. _definition-4:

Definition 
~~~~~~~~~~~

.. table:: Table : network_profile_new_from_boot_args – parameters

   +-----------------------------------------------------------------------+
   | int                                                                   |
   |                                                                       |
   | utils_file_store (char \*path, char \*buf, int \*len)                 |
   +=======================================================================+
   +-----------------------------------------------------------------------+

.. _parameters-4:

Parameters
~~~~~~~~~~

.. table:: Table : is_valid_ip – parameters

   +--------------+-------------------------------------------------------+
   | *            | **Description**                                       |
   | *Parameter** |                                                       |
   +==============+=======================================================+
   | *path*       | Path of the file                                      |
   +--------------+-------------------------------------------------------+
   | *buf*        | Buffer having data to be store in the specified file  |
   +--------------+-------------------------------------------------------+
   | *Len*        | Lenth/size of data present in the buffer              |
   +--------------+-------------------------------------------------------+

.. _return-4:

Return
~~~~~~

Success : Pointer to buffer having the content of the file.

Failure : NULL

reset_device
~~~~~~~~~~~~~~~~~~~~~~~~~

.. _overview-5:

Overview
~~~~~~~~

Used to soft reset the device.

.. _definition-5:

Definition 
~~~~~~~~~~~

.. table:: Table : wifi_connect_to_network – parameters

   +-----------------------------------------------------------------------+
   | void                                                                  |
   |                                                                       |
   | reset_device (void)                                                   |
   +=======================================================================+
   +-----------------------------------------------------------------------+

show_heap
~~~~~~~~~~~~~~~~~~~~~~~~~

.. _overview-6:

Overview
~~~~~~~~

Used to print the heap available runtime and is used for debugging.

.. _definition-6:

Definition
~~~~~~~~~~

+-----------------------------------------------------------------------+
| void                                                                  |
|                                                                       |
| show_heap (const char \*function, int line_number)                    |
+=======================================================================+
+-----------------------------------------------------------------------+

.. _parameters-5:

Parameters
~~~~~~~~~~

+--------------+-------------------------------------------------------+
| *            | **Description**                                       |
| *Parameter** |                                                       |
+==============+=======================================================+
| *function*   | Name of the function from where this is getting       |
|              | called                                                |
+--------------+-------------------------------------------------------+
| *            | Line number at which this function is getting called  |
| line_number* |                                                       |
+--------------+-------------------------------------------------------+

network_profile_new_from_ssid_pw
~~~~~~~~~~~~~~~~~~~~~~~~~

.. _overview-7:

Overview
~~~~~~~~

Used to allocate new network profile structure from SSID and Passphrase.

.. _definition-7:

Definition 
~~~~~~~~~~~

+-----------------------------------------------------------------------+
| int                                                                   |
|                                                                       |
| network_profile_new_from_ssid_pw(struct network_profile \**np_ret,    |
| char \*ssid, char \*passphrase)                                       |
+=======================================================================+
+-----------------------------------------------------------------------+

.. _parameters-6:

Parameters
~~~~~~~~~~

+----------------+-----------------------------------------------------+
| **Parameter**  | **Description**                                     |
+================+=====================================================+
| *np_ret*       | Newly allocated network_profile structure           |
+----------------+-----------------------------------------------------+
| *ssid*         | SSID of AP                                          |
+----------------+-----------------------------------------------------+
| *passphrase*   | Passphrase of AP                                    |
+----------------+-----------------------------------------------------+

.. _return-5:

Return
~~~~~~

Success: 0

Error: Negative error number

network_profile_new_from_ssid_bssid_pw
~~~~~~~~~~~~~~~~~~~~~~~~~

.. _overview-8:

Overview
~~~~~~~~

Used to allocate new network profile structure from SSID, BSSID and
passphrase.

.. _definition-8:

Definition 
~~~~~~~~~~~

+-----------------------------------------------------------------------+
| int                                                                   |
|                                                                       |
| network_profile_new_from_ssid_bssid_pw(struct network_profile         |
| \**np_ret, char \*ssid, uint8_t \*bssid, char \*passphrase)           |
+=======================================================================+
+-----------------------------------------------------------------------+

.. _parameters-7:

Parameters
~~~~~~~~~~

+-----------------+----------------------------------------------------+
| **Parameter**   | **Description**                                    |
+=================+====================================================+
| *np_ret*        | Newly allocated network_profile structure          |
+-----------------+----------------------------------------------------+
| *ssid*          | SSID of AP                                         |
+-----------------+----------------------------------------------------+
| *bssid*         | BSSID of AP                                        |
+-----------------+----------------------------------------------------+
| *passphrase*    | Passphrase of AP                                   |
+-----------------+----------------------------------------------------+

.. _return-6:

Return
~~~~~~

Success: 0

Error: Negative error number

network_profile_new_from_boot_args
~~~~~~~~~~~~~~~~~~~~~~~~~

.. _overview-9:

Overview
~~~~~~~~

Used to allocate new network profile structure from bootargs.

.. _definition-9:

Definition 
~~~~~~~~~~~

+-----------------------------------------------------------------------+
| int                                                                   |
|                                                                       |
| network_profile_new_from_boot_args(struct network_profile \**np_ret)  |
+=======================================================================+
+-----------------------------------------------------------------------+

.. _parameters-8:

Parameters
~~~~~~~~~~

+-----------------+----------------------------------------------------+
| **Parameter**   | **Description**                                    |
+=================+====================================================+
| *np_ret*        | Newly allocated network_profile structure          |
+-----------------+----------------------------------------------------+

.. _return-7:

Return
~~~~~~

Success: 0

Error: Negative error number

is_valid_ip
~~~~~~~~~~~~~~~~~~~~~~~~~

.. _overview-10:

Overview
~~~~~~~~

Used to verify whether the argument passed is a valid IP address or not.

.. _definition-10:

Definition 
~~~~~~~~~~~

+-----------------------------------------------------------------------+
| int                                                                   |
|                                                                       |
| is_valid_ip(char \*ip_str_in);                                        |
+=======================================================================+
+-----------------------------------------------------------------------+

.. _parameters-9:

Parameters
~~~~~~~~~~

+----------------+-----------------------------------------------------+
| **Parameter**  | **Description**                                     |
+================+=====================================================+
| *ip_str_in*    | String form of IP address, which is to be validated |
+----------------+-----------------------------------------------------+

.. _return-8:

Return
~~~~~~

Success: 0

Error: 1

wifi_connect_to_network
~~~~~~~~~~~~~~~~~~~~~~~~~

.. _overview-11:

Overview
~~~~~~~~

Used to connect to a network.

.. _definition-11:

Definition 
~~~~~~~~~~~

+-----------------------------------------------------------------------+
| int wifi_connect_to_network (struct wcm_handle \**p_wcm, int          |
| timeout_secs, bool \*conn_status);                                    |
+=======================================================================+
+-----------------------------------------------------------------------+

.. _parameters-10:

Parameters
~~~~~~~~~~

+-----------------+----------------------------------------------------+
| **Parameter**   | **Description**                                    |
+=================+====================================================+
| *p_wcm*         | Double pointer to @ref wcm_handle                  |
+-----------------+----------------------------------------------------+
| *timeout_secs*  | Timeout to wait for wifi connection.               |
|                 | -1 = infite, 0 = no wait, >0 = wait_secs           |
+-----------------+----------------------------------------------------+
| *conn_status*   | Status of connection: Connected or Disconnected    |
+-----------------+----------------------------------------------------+

.. _return-9:

Return 
~~~~~~~

Success: 0

Error: Negative Error Code

Application Example
~~~~~~~~~~~~~~~~~~~~~~~~~

For the example code, refer: *components/utils*.
