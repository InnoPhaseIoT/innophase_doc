.. _st api mqtt:

MQTT APIs
~~~~~~~~~

hapi_mqtt_nw_init
^^^^^^^^^^^^^^^^^

Used to initialize the MQTT network. This is the first API to be called
to use MQTT protocol.

.. code:: shell

    struct hapi_mqtt* hapi_mqtt_nw_init(struct hapi *hapi, char* serverName, uint16_t port, char* certName, uint16_t *sockId, uint32_t *status)


Arguments:

1. hapi: HAPI instance pointer.

2. serverName: The MQTT server (Broker) name.

3. port: The MQTT port number.

4. certName: The certificate name in case of MQTT with TLS.

Return: Return: True(1) on Success. False(0) on Error.

hapi_mqtt_set_ind_cb
^^^^^^^^^^^^^^^^^^^^

Used to set the MQTT notification callback.

.. code:: shell

    void hapi_mqtt_set_ind_cb(struct hapi_mqtt *hapi_mqtt, hapi_mqtt_ind_cb cb, void *context)



Arguments:

1. hapi_mqtt: MQTT instance pointer.

2. cb: The callback function.

3. context: The context pointer pass along with the callback.

Return: Return: True(1) on Success. False(0) on Error.

hapi_mqtt_nw_connect
^^^^^^^^^^^^^^^^^^^^

Used to connect to the MQTT network.

.. code:: shell

    bool hapi_mqtt_nw_connect(struct hapi *hapi, struct hapi_mqtt *hapi_mqtt, char* mqtt_server_name, uint16_t mqtt_port)


Arguments:

1. hapi: HAPI instance pointer.

2. hapi_mqtt: The MQTT instance pointer.

3. mqtt_server_name: The server’s name or IP address of the MQTT broker.

4. mqtt_port: The MQTT port number to connect.

Return: True(1) on Success. False(0) on Error.

hapi_mqtt_client_init
^^^^^^^^^^^^^^^^^^^^^

Used to initialize the MQTT client.

.. code:: shell

    bool hapi_mqtt_client_init(struct hapi *hapi, struct hapi_mqtt *hapi_mqtt, uint16_t timeout_ms)


Arguments:

1. hapi: HAPI instance pointer.

2. hapi_mqtt: The MQTT instance pointer

3. timeout_ms: The connection timeout in milli-seconds.

Return: True(1) on Success. False(0) on Error.

hapi_mqtt_connect
^^^^^^^^^^^^^^^^^

Used to connect the MQTT broker with the username and password provided.

.. code:: shell

    bool hapi_mqtt_connect(struct hapi *hapi, struct hapi_mqtt *hapi_mqtt, uint32_t mqtt_version, char* clientId, char* userName, char* password)


Arguments:

1. hapi: HAPI instance pointer.

2. hapi_mqtt: The MQTT instance pointer.

3. mqtt_version: The current supported MQTT version.

4. clientId: The ID of the client, trying to get connected to.

5. userName: The username for the MQTT connection.

6. password: The password for the MQTT connection.

Return: True(1) on Success. False(0) on Error.

hapi_mqtt_publish
^^^^^^^^^^^^^^^^^

Used to publish data to the broker in the existing MQTT connection.

.. code:: shell

    bool hapi_mqtt_publish(struct hapi *hapi, struct hapi_mqtt *hapi_mqtt, char* topic_to_publish, char* topic)


Arguments:

1. hapi: HAPI instance pointer.

2. hapi_mqtt: The MQTT instance pointer.

3. topic_to_publish: Topic of the MQTT to publish.

4. topic: The data to publish.

Return: True(1) on Success. False(0) on Error.

hapi_mqtt_subscribe
^^^^^^^^^^^^^^^^^^^

Used to subscribe to a particular topic.

.. code:: shell

    bool hapi_mqtt_subscribe(struct hapi *hapi, struct hapi_mqtt *hapi_mqtt, char* topic_to_sub, uint16_t qos)


Arguments:

1. hapi: HAPI instance pointer.

2. hapi_mqtt: The MQTT instance pointer.

3. topic_to_sub: Topic of the MQTT to subscribe.

4. qos: The qos of the MQTT connection.

Return: True(1) on Success. False(0) on Error.

hapi_mqtt_unsubscribe
^^^^^^^^^^^^^^^^^^^^^

Used to unsubscribe from a particular topic that has already been
subscribed for.

.. code:: shell

    bool hapi_mqtt_unsubscribe(struct hapi *hapi, struct hapi_mqtt *hapi_mqtt, char* topic)


Arguments:

1. hapi: HAPI instance pointer.

2. hapi_mqtt: The MQTT instance pointer.

3. topic: Topic of the MQTT to un-subscribe.

Return: True(1) on Success. False(0) on Error.

hapi_mqtt_disconnect
^^^^^^^^^^^^^^^^^^^^

Used to disconnect the MQTT.

.. code:: shell

    bool hapi_mqtt_disconnect(struct hapi *hapi, struct hapi_mqtt *hapi_mqtt)


Arguments:

1. hapi: HAPI instance pointer.

2. Hapi_mqtt: The MQTT instance pointer

Return: True(1) on Success. False(0) on Error.

hapi_mqtt_nw_disconnect
^^^^^^^^^^^^^^^^^^^^^^^

Used to disconnect from the network.

.. code:: shell

    bool hapi_mqtt_nw_disconnect(struct hapi *hapi, struct hapi_mqtt *hapi_mqtt)


Arguments:

1. hapi: HAPI instance pointer.

2. hapi_mqtt: The MQTT instance pointer

Return: True(1) on Success. False(0) on Error.

hapi_mqtt_cert_store
^^^^^^^^^^^^^^^^^^^^

Used to store the SSL/TLS certificate for MQTT.

.. code:: shell

    bool hapi_mqtt_cert_store (struct hapi *hapi, char* certName, uint32_t certLen, const unsigned char* certData)


Arguments:

1. hapi: HAPI instance pointer.

2. certName: Certificate name

3. certLen: Length of the certificate

4. certData: the certificate stream.

Return: True(1) on Success. False(0) on Error.

hapi_mqtt_cert_delete
^^^^^^^^^^^^^^^^^^^^^

Used to delete the SSL/TLS certificate for MQTT.

.. code:: shell

    bool hapi_mqtt_cert_delete(struct hapi *hapi, char* certName)


Arguments:

1. hapi: HAPI instance pointer.

2. certName: Certificate name

Return: True(1) on Success. False(0) on Error.

hapi_mqtt_client_connect
^^^^^^^^^^^^^^^^^^^^^^^^

Used to connect to the MQTT client.

.. code:: shell

    struct hapi_mqtt *hapi_mqtt_client_connect(struct hapi *hapi, struct mqtt_client_config *config)


Arguments:

1. hapi: HAPI instance pointer.

2. mqtt_client_config: MQTT client configuration.

Return:

1. hapi_mqtt : Returns MQTT identifier.

hapi_mqtt_client_disconnect
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Used to disconnect the MQTT client.

.. code:: shell

    bool hapi_mqtt_client_disconnect(struct hapi *hapi, struct hapi_mqtt *hapi_mqtt)


Arguments:

1. hapi: HAPI instance pointer.

2. mqtt_client_config: MQTT client configuration.

Return: True(1) on Success. False(0) on Error.
