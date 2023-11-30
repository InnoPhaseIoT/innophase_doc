.. websock apiref:

WebSocket API Reference
#######################

This module implements the WebSocket client functionality. WebSocket is
a communication protocol providing full duplex, asynchronous
communication between the connected endpoints. WebSocket is designed to
leverage the currently existing web infrastructure. It is designed to
work over HTTP ports 80 and 443 as well as to support HTTP proxies and
intermediaries. WebSocket is fully compatible with Web (HTTP) servers
and uses HTTP upgrade header to switch from HTTP to WebSocket protocol.
WebSocket is standardized by IETF as RFC6455.

Features and Limitations
~~~~~~~~~~~~~~~~~~~~~~~~~

Following are the list of salient features of this Websocket
implementation:

1. Confirms to RFC6455

2. Both the server IP address and the host name (Domain Name)

3. Supports secured connection using SSL/TLS

Header file/s
======~~~~~~~~~~~~~~~~~~~~~~~~~=======

Components/websocket/inc/websock.h.

Data Structure Definitions 
~~~~~~~~~~~~~~~~~~~~~~~~~

websock_config_t 
~~~~~~~~~~~~~~~~~~~~~~~~~

This data structure is used to pass the parameters while opening a
websocket connection with the remote server using websock_open API.

.. table:: Table 1: websock_config_t - parameters

   +----------------+-----------------------------------------------------+
   | **hostname**   | Host name or the IP address of the server           |
   +================+=====================================================+
   | **port**       | Port                                                |
   +----------------+-----------------------------------------------------+
   | **uri**        | Websocket uri to connect to                         |
   +----------------+-----------------------------------------------------+
   | **secured**    | Secured websocket                                   |
   +----------------+-----------------------------------------------------+
   | **ssl_config** | SSL connection configurations                       |
   +----------------+-----------------------------------------------------+
   | **time_out**   | TCP connection timeout                              |
   +----------------+-----------------------------------------------------+
   | *              | The headers to be set in the WebSocket Handshake    |
   | *hndshk_hdrs** | request. The format is: "key:val". Use this to pass |
   |                | headers that are not set implicitly. Refer          |
   |                | `websock_open() <#websock_open>`__ for the list of  |
   |                | headers set implicitly                              |
   +----------------+-----------------------------------------------------+
   | **num          | Number of headers passed using hndshk_hdrs          |
   | _hndshk_hdrs** |                                                     |
   +----------------+-----------------------------------------------------+

websock_msg_hdr_t
~~~~~~~~~~~~~~~~~~~~~~~~~

This data structure is used to pass information about the data received
from the server.

.. table:: Table 2: websock_msg_hdr_t - parameters

   +----------------+-----------------------------------------------------+
   | **fin**        | End of message                                      |
   +================+=====================================================+
   | **opcode**     | Opcode of the message frame.                        |
   |                |                                                     |
   |                | If < 0, this structure contents are invalid. This   |
   |                | can happen if the header is not fully received in   |
   |                | the current call to websock_recv().                 |
   |                |                                                     |
   |                | This is not an error, keep calling websock_recv(),  |
   |                | unless websock_recv() itself returns < 0            |
   +----------------+-----------------------------------------------------+
   | *              | Total length of the payload of the fragment being   |
   | *payload_len** | received                                            |
   +----------------+-----------------------------------------------------+

API Reference
~~~~~~~~~~~~~~~~~~~~~~~~~

websock_open
~~~~~~~~~~~~~~~~~~~~~~~~~

Overview
~~~~~~~~

This function opens a TCP socket to the server and performs the initial
HTTP-based handshake to upgrade to the websocket protocol. Both secure
(SSL) and non-secure websocket connections are supported.

Headers set implicitly during connection handshake:

1. \|Host\| header field whose value contains /host/ plus optionally ":"
   followed by /port/ (when not using the default port).

2. \|Upgrade\| header field whose value MUST include the "websocket"
   keyword.

3. \|Connection\| header field whose value MUST include the "Upgrade"
   token.

4. \|Sec-websocket-Key\|. The value of this header field MUST be a nonce
   consisting of a randomly selected 16-byte value that has been
   base64-encoded (see section 4 of [RFC4648]). The nonce MUST be
   selected randomly for each connection.

5. \|Sec-websocket-Version\|. The value of this header field MUST be 13.

The \|Host\| \|Upgrade\|, \|Connection\|, \|Sec -Websocket-key\| and
\|Sec-websocket-Version\| headers are implicitly set by the
websock_Open() during the handshake. Any other headers to be used in
connection upgrade request must be set by the caller.

Definition 
~~~~~~~~~~~

.. table:: Table 3: websock_open - parameters

   +-----------------------------------------------------------------------+
   | websock_handle_t                                                      |
   |                                                                       |
   | websock_open(websock_config_t \*ws_cfg)                               |
   +=======================================================================+
   +-----------------------------------------------------------------------+

Parameters
~~~~~~~~~~

.. table:: Table 4: websock_close - parameters

   +-------------+--------------------------------------------------------+
   | **          | **Description**                                        |
   | Parameter** |                                                        |
   +=============+========================================================+
   | *cfg*       | Pointer to properly initialized configuration DS of    |
   |             | type websock_config_t                                  |
   +-------------+--------------------------------------------------------+

Return
~~~~~~

Success: Pointer to websocket connection handle

Error: NULL

websock_close
~~~~~~~~~~~~~~~~~~~~~~~~~

.. _overview-1:

Overview
~~~~~~~~

This function is used to close the connection.

.. _definition-1:

Definition 
~~~~~~~~~~~

.. table:: Table 5: websock_send_text - parameters

   +-----------------------------------------------------------------------+
   | void                                                                  |
   |                                                                       |
   | websock_close(websock_handle_t h)                                     |
   +=======================================================================+
   +-----------------------------------------------------------------------+

.. _parameters-1:

Parameters
~~~~~~~~~~

.. table:: Table 6: websock_send_binary - parameters

   +--------------+-------------------------------------------------------+
   | *            | **Description**                                       |
   | *Parameter** |                                                       |
   +==============+=======================================================+
   | *handle*     | Handle returned by websock_open                       |
   +--------------+-------------------------------------------------------+

.. _return-1:

Return
~~~~~~

None.

websock_send_text
~~~~~~~~~~~~~~~~~~~~~~~~~

.. _overview-2:

Overview
~~~~~~~~

This function is used to send “text” data over websocket connection.

.. _definition-2:

Definition 
~~~~~~~~~~~

.. table:: Table 7: websock_recv - parameters

   +-----------------------------------------------------------------------+
   | int                                                                   |
   |                                                                       |
   | websock_send_text(websock_handle_t handle, char \*payload, int len)   |
   +=======================================================================+
   +-----------------------------------------------------------------------+

.. _parameters-2:

Parameters
~~~~~~~~~~

+--------------+-------------------------------------------------------+
| *            | **Description**                                       |
| *Parameter** |                                                       |
+==============+=======================================================+
| *handle*     | Handle returned by websock_open                       |
+--------------+-------------------------------------------------------+
| *payload*    | Message payload                                       |
+--------------+-------------------------------------------------------+
| *len*        | Payload length                                        |
+--------------+-------------------------------------------------------+

.. _return-2:

Return
~~~~~~

Success: 0

Error: -1

websock_send_binary
~~~~~~~~~~~~~~~~~~~~~~~~~

.. _overview-3:

Overview
~~~~~~~~

This function is used to send “binary” data over websocket connection.

.. _definition-3:

Definition 
~~~~~~~~~~~

+-----------------------------------------------------------------------+
| int                                                                   |
|                                                                       |
| websock_send_binary(websock_handle_t handle, char \*payload, int len) |
+=======================================================================+
+-----------------------------------------------------------------------+

.. _parameters-3:

Parameters
~~~~~~~~~~

+---------------+------------------------------------------------------+
| **Parameter** | **Description**                                      |
+===============+======================================================+
| *handle*      | Handle returned by websock_open                      |
+---------------+------------------------------------------------------+
| *payload*     | Message payload                                      |
+---------------+------------------------------------------------------+
| *len*         | Payload length                                       |
+---------------+------------------------------------------------------+

.. _return-3:

Return
~~~~~~

Success: 0

Error: -1

websock_recv
~~~~~~~~~~~~~~~~~~~~~~~~~

.. _overview-4:

Overview
~~~~~~~~

This function receives websocket messages. This internally handles
websocket close and ping messages. This is a blocking call, and blocks
for the data for the specified timeout.

**Note**: This API needs to be kept calling in loop in a separate thread
context.

.. _definition-4:

Definition 
~~~~~~~~~~~

+-----------------------------------------------------------------------+
| int                                                                   |
|                                                                       |
| websock_recv(websock_handle_t handle, websock_msg_hdr_t \*msg_hdr,    |
|                                                                       |
| char \*buf, int \*len, int timeout)                                   |
+=======================================================================+
+-----------------------------------------------------------------------+

.. _parameters-4:

Parameters
~~~~~~~~~~

+-------------+--------------------------------------------------------+
| **          | **Description**                                        |
| Parameter** |                                                        |
+=============+========================================================+
| *handle*    | Handle returned by websock_open                        |
+-------------+--------------------------------------------------------+
| *msg_hdr*   | Pointer to structure of type websock_msg_hdr_t used to |
|             | pass on the websocket message header information to    |
|             | the calling application                                |
+-------------+--------------------------------------------------------+
| *buf*       | Pointer to buffer to copy payload data                 |
+-------------+--------------------------------------------------------+
| *len*       | Max buf length                                         |
+-------------+--------------------------------------------------------+
| *timeout*   | Receive timeout                                        |
+-------------+--------------------------------------------------------+

.. _return-4:

Return
~~~~~~

Success: Received bytes. >=0

Error: -1

Application Example
~~~~~~~~~~~~~~~~~~~~~~~~~

For the example code, refer: *examples/websocket* application.
