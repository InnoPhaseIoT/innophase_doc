sslwrap
---------

Talaria TWO uses mbed TLS library for the implementation of SSL/TLS.
This component provides wrapper functions for the commonly used
functionalities like connect, read, write and read with timeout. This is
an effort to hide the complicacy of using discrete mbed TLS APIs to
perform commonly used functionality like establishing connection.

**Note**: mbed TLS APIs are available for using directly without the
need of using this module.

Header file/s
~~~~~~~~~~~~~~~~~~~~~~~~~

Components/ssl_wrap/inc/ssl_wrap.h

Data Structure Definitions 
~~~~~~~~~~~~~~~~~~~~~~~~~

ssl_auth_mode_t
~~~~~~~~~~~~~~~~~~~~~~~~~

This enum defines the various authentication modes.

.. table:: Table : ssl_auth_mode_t - authentication modes

   +-----------------------+----------------------------------------------+
   | **S                   | Peer certificate is not checked (default on  |
   | SL_WRAP_VERIFY_NONE** | server. insecure on client)                  |
   +=======================+==============================================+
   | **SSL_W               | Peer certificate is checked; however the     |
   | RAP_VERIFY_OPTIONAL** | handshake continues even if verification     |
   |                       | fails. mbedtls_ssl_get_verify_result() can   |
   |                       | be called after the handshake is complete    |
   +-----------------------+----------------------------------------------+
   | **SSL_W               | Peer **must** present a valid certificate;   |
   | RAP_VERIFY_REQUIRED** | handshake is aborted if verification fails   |
   |                       | (default on client)                          |
   +-----------------------+----------------------------------------------+

ssl_wrap_cert_t
~~~~~~~~~~~~~~~~

This data structure is used to provide information about the certificate
like CA cert, Client cert and Client Key.

.. table:: Table : ssl_wrap_cert_t – parameters

   +-----------------+----------------------------------------------------+
   | **path**        | Not used currently. Path of the certificate in     |
   |                 | file system                                        |
   +=================+====================================================+
   | **buf**         | Pointer to buffer having the certificate           |
   +-----------------+----------------------------------------------------+
   | **len**         | Length of the certificate/key present in the buf   |
   +-----------------+----------------------------------------------------+

ssl_wrap_cfg_t 
~~~~~~~~~~~~~~~~~~~~~~~~~

This data structure is used to pass the parameters while opening an SSL
connection with the remote server using ssl_wrap_connect API.

.. table:: Table : ssl_wrap_cfg_t - parameters

   +-----------------+----------------------------------------------------+
   | **ca_cert**     | CA certificate information. This is a pointer to   |
   |                 | properly initialized ssl_wrap_cert_t               |
   +=================+====================================================+
   | **client_cert** | Client certificate information. This is a pointer  |
   |                 | to properly initialized ssl_wrap_cert_t            |
   +-----------------+----------------------------------------------------+
   | **client_key**  | Client key information. This is a pointer to       |
   |                 | properly initialized ssl_wrap_cert_t               |
   +-----------------+----------------------------------------------------+
   | **auth_mode**   | Authentication mode as defined in ssl_auth_mode_t  |
   +-----------------+----------------------------------------------------+
   | *               | Value will be >= MBEDTLS_SSL_MAX_FRAG_LEN_512 and  |
   | *max_frag_len** | <= MBEDTLS_SSL_MAX_FRAG_LEN_4096                   |
   +-----------------+----------------------------------------------------+

http_client_resp_info_t
~~~~~~~~~~~~~~~~~~~~~~~

This data structure is used to pass information about the data received
from the server when HTTP GET is done using the http_client_get API.

.. table:: Table : http_client_resp_info_t - parameters

   +-------------+--------------------------------------------------------+
   | **st        | HTTP response status code                              |
   | atus_code** |                                                        |
   +=============+========================================================+
   | **          | Response headers. Array of strings                     |
   | resp_hdrs** |                                                        |
   +-------------+--------------------------------------------------------+
   | **          | Response body len                                      |
   | resp_body** |                                                        |
   +-------------+--------------------------------------------------------+
   | *           | Resp len, currently available in the resp_body         |
   | *resp_len** |                                                        |
   +-------------+--------------------------------------------------------+
   | **resp_     | Total length of the response body. If 0, no total      |
   | total_len** | length available before hand as the body may be sent   |
   |             | using chunked or multipart encoding                    |
   +-------------+--------------------------------------------------------+
   | **          | More data will be followed. The callback will be       |
   | more_data** | called again                                           |
   +-------------+--------------------------------------------------------+

API Reference
~~~~~~~~~~~~~~~~~~~~~~~~~

ssl_wrap_connect
~~~~~~~~~~~~~~~~~~~~~~~~~

Overview
~~~~~~~~

This API is used to securely connect to remote server using SSL/TLS.

Definition 
~~~~~~~~~~~

.. table:: Table : ssl_wrap_connect – parameters

   +-----------------------------------------------------------------------+
   | ssl_wrap_handle_t                                                     |
   |                                                                       |
   | ssl_wrap_connect(char \*host_name, int port, ssl_wrap_cfg_t \*cfg)    |
   +=======================================================================+
   +-----------------------------------------------------------------------+

Parameters
~~~~~~~~~~

.. table:: Table : ssl_wrap_read - parameters

   +--------------+-------------------------------------------------------+
   | *            | **Description**                                       |
   | *Parameter** |                                                       |
   +==============+=======================================================+
   | *hostname*   | DNS name or the IP address of the remote server       |
   +--------------+-------------------------------------------------------+
   | *port*       | Port number to connect to                             |
   +--------------+-------------------------------------------------------+
   | *cfg*        | SSL configuration parameters required to make the SSL |
   |              | connection                                            |
   +--------------+-------------------------------------------------------+

Return
~~~~~~

Success: Pointer to SSL wrap connection handle.

Error: NULL

ssl_wrap_read
~~~~~~~~~~~~~~~~~~~~~~~~~

.. _overview-1:

Overview
~~~~~~~~

This function is used to read data received over the SSL connection
established using the ssl_wrap_connect API. This API blocks indefinitely
for the data.

.. _definition-1:

Definition
~~~~~~~~~~

.. table:: Table : ssl_wrap_write - parameters

   +-----------------------------------------------------------------------+
   | int                                                                   |
   |                                                                       |
   | ssl_wrap_read(ssl_wrap_handle_t handle, unsigned char \*buf, int len) |
   +=======================================================================+
   +-----------------------------------------------------------------------+

.. _parameters-1:

Parameters
~~~~~~~~~~

.. table:: Table : ssl_wrap_read_timeout - parameters

   +--------------+-------------------------------------------------------+
   | *            | **Description**                                       |
   | *Parameter** |                                                       |
   +==============+=======================================================+
   | *handle*     | Handle returned by ssl_wrap_connect                   |
   +--------------+-------------------------------------------------------+
   | *buf*        | Buffer to read data in to                             |
   +--------------+-------------------------------------------------------+
   | *len*        | Max length of the buffer                              |
   +--------------+-------------------------------------------------------+

.. _return-1:

Return
~~~~~~

Success: >0. Number of bytes read.

Error: -1

ssl_wrap_write
~~~~~~~~~~~~~~~~~~~~~~~~~

.. _overview-2:

Overview
~~~~~~~~

This function is used to send data over the SSL connection established
using the ssl_wrap_connect API.

.. _definition-2:

Definition 
~~~~~~~~~~~

+-----------------------------------------------------------------------+
| int                                                                   |
|                                                                       |
| ssl_wrap_write (ssl_wrap_handle_t handle, unsigned char \*buf, int    |
| len)                                                                  |
+=======================================================================+
+-----------------------------------------------------------------------+

.. _parameters-2:

Parameters
~~~~~~~~~~

+----------------+-----------------------------------------------------+
| **Parameters** | **Description**                                     |
+================+=====================================================+
| *handle*       | Handle returned by ssl_wrap_connect                 |
+----------------+-----------------------------------------------------+
| *buf*          | Buffer having data to be sent                       |
+----------------+-----------------------------------------------------+
| *len*          | Length of data to be sent                           |
+----------------+-----------------------------------------------------+

.. _return-2:

Return
~~~~~~

Success: >=0. Number of bytes sent.

Error: -1

ssl_wrap_read_timeout
~~~~~~~~~~~~~~~~~~~~~~~~~

.. _overview-3:

Overview
~~~~~~~~

This function is used to tread data received over the SSL connection
established using the ssl_wrap_connect API. This is similar to
ssl_wrap_read, the difference being, this API will return after a
specified timeout.

.. _definition-3:

Definition 
~~~~~~~~~~~

+-----------------------------------------------------------------------+
| int                                                                   |
|                                                                       |
| ssl_wrap_read_timeout(ssl_wrap_handle_t handle, unsigned char\* buf,  |
| int len,                                                              |
|                                                                       |
| int timeout_ms)                                                       |
+=======================================================================+
+-----------------------------------------------------------------------+

.. _parameters-3:

Parameters
~~~~~~~~~~

+------------+---------------------------------------------------------+
| **P        | **Description**                                         |
| arameter** |                                                         |
+============+=========================================================+
| *handle*   | Handle returned by ssl_wrap_connect                     |
+------------+---------------------------------------------------------+
| *buf*      | Buffer to read data into                                |
+------------+---------------------------------------------------------+
| *len*      | Max length of the buffer                                |
+------------+---------------------------------------------------------+
| *timeout*  | Timeout in seconds after which API will return with an  |
|            | error if no data is received from the server            |
+------------+---------------------------------------------------------+

.. _return-3:

Return
~~~~~~

Success: >0. Number of bytes read.

Error: -1

ssl_wrap_disconnect
~~~~~~~~~~~~~~~~~~~~~~~~~

.. _overview-4:

Overview
~~~~~~~~

This function is used to disconnect the SSL connection established using
the ssl_wrap_connect API.

.. _definition-4:

Definition 
~~~~~~~~~~~

+-----------------------------------------------------------------------+
| void                                                                  |
|                                                                       |
| ssl_wrap_disconnect(ssl_wrap_handle_t handle)                         |
+=======================================================================+
+-----------------------------------------------------------------------+

.. _parameters-4:

Parameters
~~~~~~~~~~

+---------------+------------------------------------------------------+
| **Parameter** | **Description**                                      |
+===============+======================================================+
| *handle*      | Handle returned by ssl_wrap_connect                  |
+---------------+------------------------------------------------------+

.. _return-4:

Return
~~~~~~

None.

Application Example
~~~~~~~~~~~~~~~~~~~~~~~~~

For the example code, refer: *components/http_client*, *components/mqtt*
and other similar directories.