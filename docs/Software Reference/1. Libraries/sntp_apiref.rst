.. _sntp apiref:

SNTP APIRef
====

**SNTP API Reference**


This section describes the minimal implementation of SNTPv4 as specified
in RFC 4330. It is simple "SNTP" client for the lwIP raw API.

Features and Limitations
~~~~~~~~~~~~~~~~~~~~~~~~~

Following are the salient features of the SNTP implementation:

1. SNTP is a subset of the Network Time Protocol (NTP), with the latest
   version being SNTP v4.

2. It can synchronize seamlessly to full-blown NTP servers, though it
   was originally developed for small computers and micro-controllers.

3. Requires less memory and processing power than NTP.

4. It is used in applications where precise clock synchronization is not
   critical.

5. Uses the TCP/IP protocol suite, UDP port 123.

Following are the limitations:

1. One of the fundamental disadvantages of SNTP is that it can be
   configured to a function from a solitary time source only.

2. SNTP delivers a significantly lower-quality time sync solution than
   its NTP counterpart, lacking certain algorithms that ensure total
   time accuracy.

3. SNTP applications do not assess the stability or quality of time
   references.

Header file/s
~~~~~~~~~~~~~~~~~~~~~~~~~

*Components/sntp/src/sntp.h*.

Data Structure Definitions 
~~~~~~~~~~~~~~~~~~~~~~~~~

**sntp_msg**


Defines SNTP, which is a protocol for synchronizing clocks across a WAN
or LAN through a specific formatted message.

The SNTP data structure is as follows:

.. table:: Table 1: sntp_msg - Data structure definitions

.. code-block:: shell


    struct sntp_msg {

    PACK_STRUCT_FLD_8(u8_t li_vn_mode);

    PACK_STRUCT_FLD_8(u8_t stratum);

    PACK_STRUCT_FLD_8(u8_t poll);

    PACK_STRUCT_FLD_8(u8_t precision);

    PACK_STRUCT_FIELD(u32_t root_delay);

    PACK_STRUCT_FIELD(u32_t root_dispersion);

    PACK_STRUCT_FIELD(u32_t reference_identifier);

    PACK_STRUCT_FIELD(u32_t reference_timestamp[2]);

    PACK_STRUCT_FIELD(u32_t originate_timestamp[2]);

    PACK_STRUCT_FIELD(u32_t receive_timestamp[2]);

    PACK_STRUCT_FIELD(u32_t transmit_timestamp[2]);

    } PACK_STRUCT_STRUCT;

where,

.. table:: Table 2: sntp_setoperatingmode - parameter descriptions

   +------------------+---------------------------------------------------+
   | **sntp_msg**     | Simple network time message protocol.             |
   +==================+===================================================+
   | **li_vn_mode**   | -  li. Two bits. Leap indicator.                  |
   |                  |                                                   |
   |                  | -  vn. Three bits. Version number of the          |
   |                  |    protocol.                                      |
   |                  |                                                   |
   |                  | -  mode. Three bits. Indicates mode. User will    |
   |                  |    need to use 3 for CLI.                         |
   +------------------+---------------------------------------------------+
   | **stratum**      | Stratum level of the local clock.                 |
   +------------------+---------------------------------------------------+
   | **poll**         | Maximum interval between successive messages.     |
   +------------------+---------------------------------------------------+
   | **precision**    | Precision of the local clock.                     |
   +------------------+---------------------------------------------------+
   | **root_delay**   | Total round trip delay time.                      |
   +------------------+---------------------------------------------------+
   | **r              | Maximum error aloud from primary clock source.    |
   | oot_dispersion** |                                                   |
   +------------------+---------------------------------------------------+
   | **refere         | Reference clock identifier.                       |
   | nce_identifier** |                                                   |
   +------------------+---------------------------------------------------+
   | **refer          | Reference time-stamp seconds.                     |
   | ence_timestamp** |                                                   |
   +------------------+---------------------------------------------------+
   | **origi          | Originate time-stamp seconds.                     |
   | nate_timestamp** |                                                   |
   +------------------+---------------------------------------------------+
   | **rec            | Received time-stamp seconds.                      |
   | eive_timestamp** |                                                   |
   +------------------+---------------------------------------------------+
   | **tran           | Transmit time-stamp seconds.                      |
   | smit_timestamp** |                                                   |
   +------------------+---------------------------------------------------+

**API Reference**


**sntp_init()**

**Overview**

This API initializes the SNTP of the Talaria TWO module. Sends out a
request instantly or after sntp_startup_delay(func).

**Definition**


.. code-block:: shell

    void sntp_init (void)

**Parameters**

None.

**Return**

None.

**sntp_stop()**

.. _overview-1:

**Overview**

This function stops the Talaria TWO module.

.. _definition-1:

**Definition**

.. code-block:: shell

    void sntp_stop (void)


.. _parameters-1:

**Parameters**

None.

.. _return-1:

**Return**

None.

**sntp_setoperatingmode()**


.. _overview-2:

**Overview**


Sets the operating mode of the Talaria TWO module.

.. _definition-2:

**Definition**

.. code-block:: Shell

    void sntp_setoperatingmode ( u8_t operating_mode)

.. _parameters-2:

**Parameters**

.. table:: Table 6: sntp_retry - parameter description

   +---------------------+------------------------------------------------+
   | **Parameter**       | **Description**                                |
   +=====================+================================================+
   | *u8_toperating_mode*| One of the available operating modes.          |
   +---------------------+------------------------------------------------+

.. _return-2:

**Return**

None.

**sntp_servermode_dhcp()**


.. _overview-3:

**Overview**


This function configures the SNTP with IP address, name of Talaria TWO
Module or DHCP.

.. _definition-3:

**Definition**


.. code-block:: shell

    void sntp_servermode_dhcp(int set_servers_from_dhcp)

.. _parameters-3:

**Parameters**


.. table:: Table 8: sntp_request - parameter description

   +-------------------------+-------------------------------------------------+
   | **Parameters**          | **Description**                                 |
   +=========================+=================================================+
   | *set_servers_from_dhcp* | Enable or disable procuring server addresses    |
   |                         | from DHCP.                                      |
   +-------------------------+-------------------------------------------------+

.. _return-3:

**Return**


None.

**sntp_setservername**


.. _overview-4:

**Overview**


This function initializes one of the NTP servers via the IP address of
the Talaria TWO module.

.. _definition-4:

**Definition**

.. code-block:: shell

    void sntp_setservername(u8_t idx, char \*server)


.. _parameters-4:

**Parameters**

+---------------+--------------------------------------------------------+
| **Parameter** | **Description**                                        |
+===============+========================================================+
| *idx*         | Index of the NTP server. Its value must be less than   |
|               | SNTP_MAX_SERVERS.                                      |
+---------------+--------------------------------------------------------+
| *server*      | DNS name of the NTP server to set, to be resolved at   |
|               | contact time                                           |
+---------------+--------------------------------------------------------+

.. _return-4:

**Return**


None.

**sntp_getservername**


.. _overview-5:

**Overview**


This function obtains one of the currently configured NTP servers by IP
address.

.. _definition-5:

**Definition**


..  code-block:: shell

    char * sntp_getservername(u8_t idx)


.. _parameters-5:

**Parameters**


+---------------+---------------------------------------------------------+
| **Parameter** | **Description**                                         |
+===============+=========================================================+
| *idx*         | Index of the NTP server.                                |
+---------------+---------------------------------------------------------+

.. _return-5:

**Return**


Success: IP address of the indexed NTP server.

Error: NULL. NTP server has not been configured by name (or at all).

**sntp_retry**


.. _overview-6:

**Overview**


This function sends a new request with increased retry timeout.

.. _definition-6:

**Definition**


.. code-block:: shell

    static void sntp_retry(void\* arg)


.. _parameters-6:

**Parameters**


+---------------+--------------------------------------------------------+
| **Parameter** | **Description**                                        |
+===============+========================================================+
| *arg*         | Unused (only necessary to conform to sys_timeout).     |
+---------------+--------------------------------------------------------+

.. _return-6:

**Return**


None.

**sntp_try_next_server**


.. _overview-7:

**Overview**


This function tries the next server or retries the current server with
increased retry timeout.

.. _definition-7:

**Definition**


.. code-block:: shell

    static void sntp_try_next_server(void\* arg)


.. _parameters-7:

**Parameters**


+---------------+-------------------------------------------------------+
| **Parameter** | **Description**                                       |
+===============+=======================================================+
| *arg*         | Unused (only necessary to conform to sys_timeout).    |
+---------------+-------------------------------------------------------+

.. _return-7:

**Return**


None.

**sntp_request**


.. _overview-8:

**Overview**


This function sends out an SNTP request to the server.

.. _definition-8:

**Definition**


.. code-block:: shell

    static void sntp_request(void \*arg)


.. _parameters-8:

**Parameters**


+---------------+-------------------------------------------------------+
| **Parameter** | **Description**                                       |
+===============+=======================================================+
| *arg*         | Unused (only necessary to conform to sys_timeout).    |
+---------------+-------------------------------------------------------+

.. _return-8:

**Return**


None.

**Example Application**


For the example codes, refer: *component\\sntp_src.c* application.
