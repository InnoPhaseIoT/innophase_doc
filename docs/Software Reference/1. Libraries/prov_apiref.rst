.. _prov apiref:

Provisionining APIRef
==============

**Provisionining API Reference**


Provisioning component provides APIs and definitions to facilitate the
provisioning service. Provisioning is done over BLE, and the
configuration data is stored in the file system.

For more details on functionality overview, data exchange formats and
profile definition (with service and characteristics information) refer
provisioning application.

Features and Limitations
~~~~~~~~~~~~~~~~~~~~~~~~~

This implementation of Provisioning provides the following facilities:

1. Crete Provisioning GATT server.

2. Scan and provide the list of APs in the range.

3. Store configuration data.

4. Check Wi-Fi connectivity using the configured SSID and passphrase.

Limitations:

Provisioning is done by storing the whole configuration data at once.
Reading and changing only a specific parameter in the configuration data
is not possible.

Header file/s
~~~~~~~~~~~~~~~~~~~~~~~~~

Components/prov/inc/prov.h.

Data Structure Definitions 
~~~~~~~~~~~~~~~~~~~~~~~~~

prov_start_prams_t
~~~~~~~~~~~~~~~~~~~~~~~~~

This data structure is used during provisioning module initialization.

.. table:: Table 1: prov_start_prams_t – parameters

   +-----------------+----------------------------------------------------+
   | **method**      | Only provisioning over BLE is supported currently  |
   +=================+====================================================+
   | **name**        | Device name. If NULL, PROV_DFLT_NAME is set        |
   +-----------------+----------------------------------------------------+
   | **appearance**  | Appearance. Default is set to 0                    |
   +-----------------+----------------------------------------------------+
   | **manu          | Manufacturer name. If NULL,                        |
   | facturer_name** | PROV_DFLT_MANUFCTR_NAME is set                     |
   +-----------------+----------------------------------------------------+
   | **cb**          | The user callback to be called when provisioning   |
   |                 | is done                                            |
   +-----------------+----------------------------------------------------+
   | **cb_ctx**      | Context pointer to be passed with callback         |
   +-----------------+----------------------------------------------------+

API Reference
~~~~~~~~~~~~~~~~~~~~~~~~~

prov_start
~~~~~~~~~~~~~~~~~~~~~~~~~

Overview
~~~~~~~~

This API initializes and starts the Provisioning service. It initializes
the BLE communication, starts the GATT server and begins advertising the
Provisioning service.

All provisioning-related activities are handled internally. If provided
through config parameter, a user supplied callback will be called when
the new configuration file received and is written into data fs.

Definition
~~~~~~~~~~

.. table:: Table 2: prov_start - parameters

   +-----------------------------------------------------------------------+
   | int                                                                   |
   |                                                                       |
   | prov_start(prov_start_prams_t \*cfg)                                  |
   +=======================================================================+
   +-----------------------------------------------------------------------+

Parameters
~~~~~~~~~~

.. table:: Table 3: prov_conf_param_str_get - parameters

   +------------+---------------------------------------------------------+
   | **P        | **Description**                                         |
   | arameter** |                                                         |
   +============+=========================================================+
   | *cfg*      | Pointer to the data structure of type                   |
   |            | prov_start_prams_t                                      |
   +------------+---------------------------------------------------------+

Return
~~~~~~

Success: 0

Error: -1

prov_conf_param_str_get
~~~~~~~~~~~~~~~~~~~~~~~~~
.. _overview-1:

Overview
~~~~~~~~

This API gets the configuration parameters of type string. For example:
“ssid” or “passphrase”. The value of the key passes is returned.

.. _definition-1:

Definition 
~~~~~~~~~~~

.. table:: Table 4: prov_conf_param_int_get – parameters

   +-----------------------------------------------------------------------+
   | const char \*                                                         |
   |                                                                       |
   | prov_conf_param_str_get(char \*key)                                   |
   +=======================================================================+
   +-----------------------------------------------------------------------+

.. _parameters-1:

Parameters
~~~~~~~~~~

+-------------+--------------------------------------------------------+
| **          | **Description**                                        |
| Parameter** |                                                        |
+=============+========================================================+
| *key*       | Key part of the configuration                          |
+-------------+--------------------------------------------------------+

.. _return-1:

Return
~~~~~~

Success: Pointer to the value of the key passed.

Error: NULL.

prov_conf_param_int_get
~~~~~~~~~~~~~~~~~~~~~~~~~

.. _overview-2:

Overview
~~~~~~~~

This API gets the configuration parameter of type integer. For example:
“port”. The value of the key passes is returned.

.. _definition-2:

Definition
~~~~~~~~~~

+-----------------------------------------------------------------------+
| int                                                                   |
|                                                                       |
| prov_conf_param_int_get(char \*key)                                   |
+=======================================================================+
+-----------------------------------------------------------------------+

.. _parameters-2:

Parameters
~~~~~~~~~~

+------------+---------------------------------------------------------+
| **P        | **Description**                                         |
| arameter** |                                                         |
+============+=========================================================+
| *key*      | Key part of the configuration                           |
+------------+---------------------------------------------------------+

.. _return-2:

Return
~~~~~~

Success: Pointer to the value of the key passed.

No such parameter exists: NULL.

prov_is_provisioned
~~~~~~~~~~~~~~~~~~~~~~~~~

.. _overview-3:

Overview
~~~~~~~~

This API is used to check if the device is provisioned atleast once.

.. _definition-3:

Definition 
~~~~~~~~~~~

+-----------------------------------------------------------------------+
| bool                                                                  |
|                                                                       |
| prov_is_provisioned(void)                                             |
+=======================================================================+
+-----------------------------------------------------------------------+

.. _parameters-3:

Parameters
~~~~~~~~~~

None.

.. _return-3:

Return
~~~~~~

Not Provisioned: 0

Provisioning: 1

Application Example
~~~~~~~~~~~~~~~~~~~~~~~~~

For the example code, refer: *examples/prov application*.
