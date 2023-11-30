.. _mdns apiref:

mDNS API Reference
##################

mDNS is a protocol that provides DNS like facility to advertise and
discover services in a local area network. The mDNS based service
discovery is defined by two RFCs, 6762 and 6763.

Features and Limitations
~~~~~~~~~~~~~~~~~~~~~~~~~

Following is the list of features provided by this component:

1. Support for IPV4

2. Register hostname

3. Register services

4. Responding to Multi-Question queries

5. Known-Answer Suppression

6. Respond to ADDR, SRV and ANY type of queries

7. One-Shot Multicast DNS queries

Following is the list of some limitations,

1. IPV6 is not supported

2. Probing and conflict detection is not supported

3. Continues multicast querying

Header file/s
~~~~~~~~~~~~~~~~~~~~~~~~~

Components/mdns/inc/mdns.h.

Data Structure Definitions 
~~~~~~~~~~~~~~~~~~~~~~~~~

mdns_srvc_info_t 
~~~~~~~~~~~~~~~~~~~~~~~~~

This data structure is used to pass information about the discovered
service. Information is passed through the callback function provided
while calling the mdns_service_discover API.

.. table:: Table 1: mdns_srvc_info_t - parameters

   +----------------+--------------------------------------------------------------------------+
   | **instance**   | Service Instance name. max limit 63 bytes. Example:                      |
   +================+==========================================================================+
   | **srvc_type**  | Service protocol. Example: “\_tcp”                                       |
   +----------------+--------------------------------------------------------------------------+
   | **protocol**   | Service protocol. Example: “\_tcp”                                       |
   +----------------+--------------------------------------------------------------------------+
   | **domain**     | Domain. In almost all the cases its “local”. This is the default value   |
   +----------------+--------------------------------------------------------------------------+
   | **txtInfo**    | Txt record information data                                              |
   +----------------+--------------------------------------------------------------------------+
   | **port**       | Port on which service is available                                       |
   +----------------+--------------------------------------------------------------------------+
   | **ipaddr**     | IP address of the interface on which service is available                |
   +----------------+--------------------------------------------------------------------------+

mdns_hnreg_param_t 
-------------------

This data structure is used to pass parameters while registering the
Host Name. Following are some of the important parameters:

.. table:: Table 2: mdns_hnreg_param_t - parameters

   +--------------+---------------------------------------------------------+
   | **hostname** | Host name of the device. Keep this unique in the N/w.   |
   |              | Best done by using mac address as part of the host name |
   +==============+=========================================================+
   | **domain**   | Always pass MDNS_LOCAL_DOMAIN                           |
   +--------------+---------------------------------------------------------+
   | **ipaddr**   | IP address of the host interface in little endian       |
   |              | format                                                  |
   +--------------+---------------------------------------------------------+
   | **ttl**      | Time to live. Default value is 120 sec                  |
   +--------------+---------------------------------------------------------+

mdns_srvreg_param_t 
~~~~~~~~~~~~~~~~~~~~~~~~~
This data structure is used to pass the parameters while registering a
service. Following are some of the important parameters:

.. table:: Table 3: mdns_srvreg_param_t – parameters

   +----------------------+--------------------------------------------------------------------+
   | **srvc_name**        | Service name. Example: “prov”                                      |
   +======================+====================================================================+
   | **srvc_sub_type**    | Name of the subtype excluding "\_sub". "\_sub" is added implicitly |
   +----------------------+--------------------------------------------------------------------+
   | **srvc_type**        | Type of service. Example: "\_http"                                 |
   +----------------------+--------------------------------------------------------------------+
   | **srvc_proto**       | Protocol type. "\_tcp" or "\_udp"                                  |
   +----------------------+--------------------------------------------------------------------+
   | **domain**           | Always pass MDNS_LOCAL_DOMAIN                                      |
   +----------------------+--------------------------------------------------------------------+
   | **txt_data**         | Pointer to key/value pairs conveying additional information about  |
   |                      | the named service                                                  |
   +----------------------+--------------------------------------------------------------------+
   | **port**             | Port number for the given service protocol type                    |
   +----------------------+--------------------------------------------------------------------+
   | **ttl**              | Time to live. Default 120 sec                                      |
   +----------------------+--------------------------------------------------------------------+

mdns_srvcdisc_param_t
~~~~~~~~~~~~~~~~~~~~~~~~~

This data structure is used for passing the parameters while discovering
for service of specific type.

.. table:: Table 4: mdns_srvcdisc_param_t - parameters

   +-------------------+--------------------------------------------------------------------+
   | **srvc_sub_type** | Name of the subtype excluding "\_sub". "\_sub" is added implicitly |
   +===================+====================================================================+
   | **srvc_type**     | Type of service. Example: "\_http"                                 |
   +-------------------+--------------------------------------------------------------------+
   | **srvc_proto**    | Protocol type. "\_tcp" or "\_udp"                                  |
   +-------------------+--------------------------------------------------------------------+
   | **domain**        | Always pass MDNS_LOCAL_DOMAIN                                      |
   +-------------------+--------------------------------------------------------------------+
   | **cb**            | mDNS service discovery callback function                           |
   +-------------------+--------------------------------------------------------------------+
   | **cbctx**         | Callback context to be passed to cb                                |
   +-------------------+--------------------------------------------------------------------+

API Reference
~~~~~~~~~~~~~~~~~~~~~~~~~

mdns_init
~~~~~~~~~~~~~~~~~~~~~~~~~

Overview
~~~~~~~~

This function is used for initializing the mDNS component. This returns
pointer to mDNS handle. This needs to be passed to all other APIs. This
shall be a onetime initialization.

Apart from other initializations, this call creates a thread and a
message queue for handling mDNS activities like packet parsing and
timeouts.

Definition 
~~~~~~~~~~~

.. code:: c

    mdns_ctx_t \*
    mdns_init(mdns_init_params_t \*param)


Parameters
~~~~~~~~~~

+----------------+--------------------------------------------------------+
| **Parameters** | **Description**                                        |
+================+========================================================+
| *param*        | Pointer to data structure of type mdns_init_params_t   |
+----------------+--------------------------------------------------------+

Return
~~~~~~

Success: Pointer to mDNS handle

Error: NULL

mdns_hostname_reg
~~~~~~~~~~~~~~~~~~~~~~~~~

.. _overview-1:

Overview
~~~~~~~~

This function is used for registering the host name of the
interface(node).

.. _definition-1:

Definition 
~~~~~~~~~~~

.. code:: c

    int mdns_hostname_reg(mdns_ctx_t \*mc, mdns_hnreg_param_t \*param);

.. _parameters-1:

Parameters
~~~~~~~~~~

+----------------+--------------------------------------------------------+
| **Parameters** | **Description**                                        |
+================+========================================================+
| *mc*           | Pointer returned by mdns_init()                        |
+----------------+--------------------------------------------------------+
| *param*        | Pointer to structure of type mdns_hnreg_param_t        |
+----------------+--------------------------------------------------------+

.. _return-1:

Return
~~~~~~

Success: 0

Error: -1

mdns_service_register
~~~~~~~~~~~~~~~~~~~~~~~~~

.. _overview-2:

Overview
~~~~~~~~

This function is used for registering the service. Once registered,
response for any matching query will be given internally.

.. _definition-2:

Definition
~~~~~~~~~~


.. code:: c

    int mdns_service_register(mdns_ctx_t \*mc, mdns_srvreg_param_t \*param)

.. _parameters-2:

Parameters
~~~~~~~~~~

+----------------+--------------------------------------------------------+
| **Parameters** | **Description**                                        |
+================+========================================================+
| *mc*           | Pointer returned by mdns_init()                        |
+----------------+--------------------------------------------------------+
| *param*        | Pointer to structure of type mdns_srvreg_param_t       |
+----------------+--------------------------------------------------------+

.. _return-2:

Return
~~~~~~

Success: 0

Error: -1

mdns_service_discover
~~~~~~~~~~~~~~~~~~~~~~~~~

.. _overview-3:

Overview
~~~~~~~~

This function is used for discovering services of given type. When
service is discovered, callback function specified in service discovery
parameter structure will be called to notify the application.

Callback function is called separately for each service it discovers. If
more than one services are detected, callback function will be called as
many times as the total number of service detected.

.. _definition-3:

Definition
~~~~~~~~~~

.. code:: c

    int mdns_service_discover(mdns_ctx_t \*mc, mdns_srvcdisc_param_t \*param)

.. _parameters-3:

Parameters
~~~~~~~~~~

+-----------------+-------------------------------------------------------+
| **Parameters**  | **Description**                                       |
+=================+=======================================================+
| *mc*            | Pointer returned by mdns_init()                       |
+-----------------+-------------------------------------------------------+
| *param*         | Pointer to structure of type mdns_srvcdisc_param_t    |
+-----------------+-------------------------------------------------------+

.. _return-3:

Return
~~~~~~

Success: 0

Error: -1

Application Example
~~~~~~~~~~~~~~~~~~~~~~~~~

For the example code, refer: *examples/mdns application*.
