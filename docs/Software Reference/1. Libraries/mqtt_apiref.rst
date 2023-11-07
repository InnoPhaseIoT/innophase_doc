mqtt
-----

MQTT is a messaging protocol based on publish-subscribe pattern. It
works on top of the TCP/IP protocol and is used in IoT.

This implementation of MQTT is from eclipse.org. Platform specific
initializations and functions are provided under *platform/* directory.
The APIs under *platform/* provide MQTT initialization and connect
functionalities for connection over TCP, SSL (TLS) and Websocket.

Features and Limitations
~~~~~~~~~~~~~~~~~~~~~~~~~

Here is the list of salient features of this MQTT implementation:

1. Supports MQTT v3.1

2. MQTT Subscribe and Publish are supported

3. Supports Publish with QOS 2

4. Supports MQTT keepalive

5. Supports Secured MQTT (MQTT over TLS connection)

6. Supports MQTT over Websockets (Both Secured and Non-secured)

Header file/s
~~~~~~~~~~~~~~~~~~~~~~~~~

1. Components/mqtt/include/ MQTTClient.h.

2. Components/mqtt/platform/ mqtt_nw.h.

API Reference
~~~~~~~~~~~~~~~~~~~~~~~~~

MQTTNetworkInit
~~~~~~~~~~~~~~~~~~~~~~~~~

Overview
~~~~~~~~

This API needs to be called if the intended MQTT connection is over TCP.
This initializes the connection handle passed to the API.

Definition 
~~~~~~~~~~~

.. table:: Table : MQTTNetworkInit - parameters

   +-----------------------------------------------------------------------+
   | void MQTTNetworkInit(MQTTNetwork\* handle)                            |
   +=======================================================================+
   +-----------------------------------------------------------------------+

Parameter
~~~~~~~~~

.. table:: Table : MQTTNetworkConnect - parameters

   +------------+---------------------------------------------------------+
   | **P        | **Description**                                         |
   | arameter** |                                                         |
   +============+=========================================================+
   | *handle*   | Pointer to connection handle data structure of type     |
   |            | MQTTNetwork                                             |
   +------------+---------------------------------------------------------+

Return
~~~~~~

None.

MQTTNetworkConnect
~~~~~~~~~~~~~~~~~~~~~~~~~

.. _overview-1:

Overview
~~~~~~~~

This function is used to connect to the broker over TCP. This connection
will be non-secured.

.. _definition-1:

Definition 
~~~~~~~~~~~

.. table:: Table : MQTTNetworkDisconnect - parameters

   +-----------------------------------------------------------------------+
   | int                                                                   |
   |                                                                       |
   | MQTTNetworkConnect(MQTTNetwork\* handle, char\* addr, int port)       |
   +=======================================================================+
   +-----------------------------------------------------------------------+

Parameters
~~~~~~~~~~

.. table:: Table : MQTTNetworkInit_Tls – parameters

   +------------+---------------------------------------------------------+
   | **P        | **Description**                                         |
   | arameter** |                                                         |
   +============+=========================================================+
   | *handle*   | Pointer to connection handle data structure of type     |
   |            | MQTTNetwork that was passed to MQTTNetworkInit()        |
   +------------+---------------------------------------------------------+
   | *addr*     | DNS name of the Broker                                  |
   +------------+---------------------------------------------------------+
   | *port*     | Broker port number                                      |
   +------------+---------------------------------------------------------+

.. _return-1:

Return
~~~~~~

Success: 0

Error: -1

MQTTNetworkDisconnect
~~~~~~~~~~~~~~~~~~~~~~~~~
.. _overview-2:

Overview
~~~~~~~~

This function disconnects the MQTT connection.

.. _definition-2:

Definition 
~~~~~~~~~~~

.. table:: Table : MQTTNetworkConnect_Tls - parameters

   +-----------------------------------------------------------------------+
   | void MQTTNetworkDisconnect(MQTTNetwork \*handle)                      |
   +=======================================================================+
   +-----------------------------------------------------------------------+

.. _parameters-1:

Parameters
~~~~~~~~~~

.. table:: Table : MQTTNetworkDisconnect_Tls - parameters

   +--------------+-------------------------------------------------------+
   | *            | **Description**                                       |
   | *Parameter** |                                                       |
   +==============+=======================================================+
   | *handle*     | Pointer to connection handle data structure of type   |
   |              | MQTTNetwork that was passed to MQTTNetworkInit()      |
   +--------------+-------------------------------------------------------+

.. _return-2:

Return
~~~~~~

None.

MQTTNetworkInit_Tls
~~~~~~~~~~~~~~~~~~~~~

.. _overview-3:

Overview
~~~~~~~~

This API needs to be called if the intended MQTT connection is over
SSL(TLS). This initializes the connection handle passed to the API.

.. _definition-3:

Definition 
~~~~~~~~~~~

.. table:: Table : MQTTNetworkInit_Ws - parameters

   +-----------------------------------------------------------------------+
   | void MQTTNetworkInit_Tls(MQTTNetwork\* handle)                        |
   +=======================================================================+
   +-----------------------------------------------------------------------+

.. _parameters-2:

Parameters
~~~~~~~~~~

.. table:: Table : MQTTNetworkDisconnect_Ws - parameters

   +-------------+--------------------------------------------------------+
   | **          | **Description**                                        |
   | Parameter** |                                                        |
   +=============+========================================================+
   | *handle*    | Pointer to connection handle data structure of type    |
   |             | MQTTNetwork                                            |
   +-------------+--------------------------------------------------------+

.. _return-3:

Return
~~~~~~

None.

MQTTNetworkConnect_Tls
~~~~~~~~~~~~~~~~~~~~~~~~~

.. _overview-4:

Overview
~~~~~~~~

This function is used for connecting to Broker over SSL (TLS). This is a
secured connection.

.. _definition-4:

Definition 
~~~~~~~~~~~

+-----------------------------------------------------------------------+
| int                                                                   |
|                                                                       |
| MQTTNetworkConnect_Tls(MQTTNetwork \*n, char \*host, int port,        |
|                                                                       |
| ssl_wrap_cfg_t \*cfg)                                                 |
+=======================================================================+
+-----------------------------------------------------------------------+

.. _parameters-3:

Parameters
~~~~~~~~~~

+--------------+-------------------------------------------------------+
| *            | **Description**                                       |
| *Parameter** |                                                       |
+==============+=======================================================+
| *handle*     | Pointer to connection handle data structure of type   |
|              | MQTTNetwork that was passed to MQTTNetworkInit_Tls()  |
+--------------+-------------------------------------------------------+
| *host*       | DNS name of the Broker or the IP address              |
+--------------+-------------------------------------------------------+
| *port*       | Broker port number                                    |
+--------------+-------------------------------------------------------+
| *cfg*        | Pointer to data structure of type ssl_wrap_cfg_t.     |
|              | This is used to pass the SSL related configurations   |
+--------------+-------------------------------------------------------+

.. _return-4:

Return
~~~~~~

Success: 0

Error: -1

MQTTNetworkDisconnect_Tls
~~~~~~~~~~~~~~~~~~~~~~~~~

.. _overview-5:

Overview
~~~~~~~~

This function disconnects the MQTT connection done using
MQTTNetworkConnect_Tls.

.. _definition-5:

Definition 
~~~~~~~~~~~

+-----------------------------------------------------------------------+
| void MQTTNetworkDisconnect_Tls(MQTTNetwork \*handle)                  |
+=======================================================================+
+-----------------------------------------------------------------------+

.. _parameters-4:

Parameters
~~~~~~~~~~

+--------------+-------------------------------------------------------+
| *            | **Description**                                       |
| *Parameter** |                                                       |
+==============+=======================================================+
| *handle*     | Pointer to connection handle data structure of type   |
|              | MQTTNetwork that was passed to MQTTNetworkInit_Tls()  |
+--------------+-------------------------------------------------------+

.. _return-5:

Return
~~~~~~

None.

MQTTNetworkInit_Ws
~~~~~~~~~~~~~~~~~~~~~~~~~

.. _overview-6:

Overview
~~~~~~~~

This API needs to be called if the intended MQTT connection is over
Websocket. This initializes the connection handle passed to the API.

.. _definition-6:

Definition 
~~~~~~~~~~~

+-----------------------------------------------------------------------+
| void MQTTNetworkInit_Ws(MQTTNetwork\* handle)                         |
+=======================================================================+
+-----------------------------------------------------------------------+

.. _parameters-5:

Parameters
~~~~~~~~~~

+-------------+--------------------------------------------------------+
| **          | **Description**                                        |
| Parameter** |                                                        |
+=============+========================================================+
| *handle*    | Pointer to connection handle data structure of type    |
|             | MQTTNetwork                                            |
+-------------+--------------------------------------------------------+

.. _return-6:

Return
~~~~~~

None.

MQTTNetworkConnect_Ws
~~~~~~~~~~~~~~~~~~~~~~~~~

.. _overview-7:

Overview
~~~~~~~~

This function is used for connecting to Broker over Websocket. The
connection can be secured or non-secured.

.. _definition-7:

Definition
~~~~~~~~~~

+-----------------------------------------------------------------------+
| int MQTTNetworkConnect_Ws(MQTTNetwork\* n, websock_config_t \*        |
| ws_cfg)                                                               |
+=======================================================================+
+-----------------------------------------------------------------------+

.. _parameters-6:

Parameters
~~~~~~~~~~

+------------+---------------------------------------------------------+
| **P        | **Description**                                         |
| arameter** |                                                         |
+============+=========================================================+
| *handle*   | Pointer to connection handle data structure of type     |
|            | MQTTNetwork that was passed to MQTTNetworkInit_Ws()     |
+------------+---------------------------------------------------------+
| *ws*       | Pointer to data structure of type websock_config_t.     |
|            | This is used to pass the Websocket related              |
|            | configurations                                          |
+------------+---------------------------------------------------------+

.. _return-7:

Return
~~~~~~

Success: 0

Error: -1

MQTTNetworkDisconnect_Ws
~~~~~~~~~~~~~~~~~~~~~~~~~

.. _overview-8:

Overview
~~~~~~~~

This API disconnects the MQTT connection established using
MQTTNetworkConnect_Ws.

.. _definition-8:

Definition
~~~~~~~~~~

+-----------------------------------------------------------------------+
| void MQTTNetworkDisconnect_Tls(MQTTNetwork \*handle)                  |
+=======================================================================+
+-----------------------------------------------------------------------+

.. _parameters-7:

Parameters
~~~~~~~~~~

+-------------+--------------------------------------------------------+
| **          | **Description**                                        |
| Parameter** |                                                        |
+=============+========================================================+
| *handle*    | Pointer to connection handle data structure of type    |
|             | MQTTNetwork that was passed to MQTTNetworkInit_Ws()    |
+-------------+--------------------------------------------------------+

.. _return-8:

Return
~~~~~~

None.

Application Example
~~~~~~~~~~~~~~~~~~~~~~~~~

For the example code, refer: *examples/mqtt application*.
