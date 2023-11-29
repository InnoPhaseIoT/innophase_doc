Http client
------------

HTTP is a stateless application-level protocol used for data transfer.
This section provides information about the HTTP Client APIs and data
structures that can be used by user applications to connect to HTTP
server and transfer data.

Features and Limitations
~~~~~~~~~~~~~~~~~~~~~~~~~

Following is the list of salient features of this HTTP/S implementation:

1. HTTP 1.1 version. Both HTTP and HTTPS

2. Both the server IP address and the host name (Domain Name)

3. HTTP GET and POST methods

4. Setting of headers by the application. Only the Host header is
   implicitly set

5. Supports receiving the response with Transfer encoding Chunked

6. Supports chain of CA certificates or the bundle of CA certificates
   (as configured in browser)

Following are the limitations:

1. CA certificate must be in the PEM format

2. HTTP redirection is not supported

Header file/s
~~~~~~~~~~~~~~~~~~~~~~~~~

Components/http/inc/http_client.h.

Data Structure Definitions 
~~~~~~~~~~~~~~~~~~~~~~~~~

http_client_config_t 
~~~~~~~~~~~~~~~~~~~~~~~~~

This data structure is used to pass the parameters while opening a HTTP
connection with the remote server using http_client_open API.

.. table:: Table : http_client_config_t - parameters

   +----------------------------+-----------------------------------------------------+
   | **hostname**               | Host name or the IP address of the server. Example, |
   |                            | “google.com” or “192.168.1.1”                       |
   +============================+=====================================================+
   | **port**                   | Server port                                         |
   +----------------------------+-----------------------------------------------------+
   | **secured**                | - 0 – HTTP                                          |
   |                            | - 1 - HTTPS without server verification             |
   |                            | - 2 – HTTPS with server certificate validation      |
   +----------------------------+-----------------------------------------------------+
   | **ssl_wrap_cfg_tssl_cfg**  | SSL configuration for secured connection            |
   +----------------------------+-----------------------------------------------------+
   | **time_out**               | Connect timeout in seconds                          |
   +----------------------------+-----------------------------------------------------+

http_client_resp_info_t
~~~~~~~~~~~~~~~~~~~~~~~~~

This data structure is used to pass information about the data received
from the server when HTTP GET is done using the http_client_get API.

.. table:: Table : http_client_resp_info_t - parameters

   +-------------------+-----------------------------------------------------+
   | **status_code**   | HTTP response status code                           |
   +===================+=====================================================+
   | **resp_hdrs**     | Response headers. Array of strings                  |
   +-------------------+-----------------------------------------------------+
   | **resp_body**     | Response body len                                   |
   +-------------------+-----------------------------------------------------+
   | **resp_len**      | Resp len, currently available in the resp_body      |
   +-------------------+-----------------------------------------------------+
   | **resp_total_len**| Total length of the response body. If 0, no total   |
   |                   | length available beforehand as the body maybe sent  |
   |                   | using chunked or multipart encoding                 |
   +-------------------+-----------------------------------------------------+
   | **more_data**     | More data will be followed. The callback will be    |
   |                   | called again                                        |
   +-------------------+-----------------------------------------------------+

API Reference
~~~~~~~~~~~~~~~~~~~~~~~~~

http_client_open
~~~~~~~~~~~~~~~~~~~~~~~~~

Overview
~~~~~~~~

This API connects to the remote HTTP server. The configuration needed
for the connection is passed using http_client_config_t.

Definition
~~~~~~~~~~

.. code:: c

    http_client_handle_t
    http_client_open(http_client_config_t \*cfg)


Parameters
~~~~~~~~~~

.. table:: Table : http_client_get - parameters

   +--------------------+----------------------------------------------------------+
   | **Parameter**      | **Description**                                          |
   +====================+==========================================================+
   | *cfg*              | Pointer to the data structure http_client_config_t       |
   +--------------------+----------------------------------------------------------+

Return
~~~~~~

Success: Pointer to HTTP client connection handle

Error: NULL

http_client_get
~~~~~~~~~~~~~~~~~~~~~~~~~

.. _overview-1:

Overview 
~~~~~~~~~

This function is used for performing HTTP GET. The HTTP response is
provided through the call back. The call back is called multiple times
until the whole response is received.

.. _definition-1:

Definition
~~~~~~~~~~
.. code:: c

    int
    http_client_get(http_client_handle_t handle, char \*uri,
    http_client_resp_cb cb, void \*cb_ctx, int time_out)


.. _parameters-1:

Parameters
~~~~~~~~~~

.. table:: Table : http_client_set_req_hdr - parameters

   +------------------+-----------------------------------------------------------------------------------+
   | **Parameter**    | **Description**                                                                   |
   +==================+===================================================================================+
   | *handle*         | Handle returned by http_client_open()                                             |
   +------------------+-----------------------------------------------------------------------------------+
   | *uri*            | HTTP URI to GET                                                                   |
   +------------------+-----------------------------------------------------------------------------------+
   | *cb*             | User application callback to be called when response is received from the server  |
   +------------------+-----------------------------------------------------------------------------------+

.. _return-1:

Return 
~~~~~~~

Success: 0

Error: -1

http_client_post
~~~~~~~~~~~~~~~~~~~~~~~~~

.. _overview-2:

Overview 
~~~~~~~~~

This function is used to perform HTTP POST. Using this data can be sent
to the HTTP server. The response is provided using the call back.
Setting content length header is a must using http_client_set_req_hdr
before calling this API.

.. _definition-2:

Definition 
~~~~~~~~~~~

.. code:: c

    int
    http_client_post(http_client_handle_t handle, char \*uri, char \*buff, int buff_len, http_client_resp_cb cb, void \*cb_ctx int time_out)


.. _parameters-2:

Parameters
~~~~~~~~~~

+--------------------+----------------------------------------------------------+
| **Parameter**      | **Description**                                          |
+====================+==========================================================+
| *handle*           | Handle returned by http_client_open()                    |
+--------------------+----------------------------------------------------------+
| *uri*              | HTTP URI to POST                                         |
+--------------------+----------------------------------------------------------+
| *buff*             | Buffer having data to be sent to server                  |
+--------------------+----------------------------------------------------------+
| *buff_len*         | Length of the data present in the buff. This is the      |
|                    | length of the data to be POSTed                          |
+--------------------+----------------------------------------------------------+
| *cb*               | User application callback to be called when response is  |
|                    | received from the server                                 |
+--------------------+----------------------------------------------------------+

.. _return-2:

Return
~~~~~~

Success: 0

Error: -1

http_client_set_req_hdr
~~~~~~~~~~~~~~~~~~~~~~~~~

.. _overview-3:

Overview
~~~~~~~~

User application can set the header to be sent with GET/POST request
using this API.

.. _definition-3:

Definition 
~~~~~~~~~~~

.. code:: c

    int http_client_set_req_hdr(http_client_handle_t handle, const char \*hdrname, const char \*hdrval)


.. _parameters-3:

Parameters
~~~~~~~~~~

+--------------------+----------------------------------------------------------+
| **Parameters**     | **Description**                                          |
+====================+==========================================================+
| *handle*           | HTTP connection handle                                   |
+--------------------+----------------------------------------------------------+
| *hdrname*          | Name part of the header. For example: “content length”   |
+--------------------+----------------------------------------------------------+
| *hdrval*           | Value part of the header. For example: “1024”            |
+--------------------+----------------------------------------------------------+

.. _return-3:

Return
~~~~~~

Success: 0

Error: -1

http_client_close
~~~~~~~~~~~~~~~~~~~~~~~~~

.. _overview-4:

Overview
~~~~~~~~

This API is used for closing the connection.

.. _definition-4:

Definition 
~~~~~~~~~~~

.. code:: c

    int http_client_close(http_client_handle_t handle)

.. _parameters-4:

Parameters
~~~~~~~~~~

+---------------+----------------------------------------------------------+
| **Parameter** | **Description**                                          |
+===============+==========================================================+
| *handle*      | HTTP connection handle                                   |
+---------------+----------------------------------------------------------+

.. _return-4:

Return
~~~~~~

Success: 0

Error: -1

Application Example
~~~~~~~~~~~~~~~~~~~~~~~~~

For the example code, refer: *examples/http_client application*.
