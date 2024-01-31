.. _st api aws:

AWS APIs 
~~~~~~~~~

hapi_aws_connect 
^^^^^^^^^^^^^^^^^

Connects the AWS socket.

+-----------------------------------------------------------------------+
| bool hapi_aws_connect(struct hapi \*hapi)                             |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi: HAPI instance pointer.

Return: AWS connection status. True=Success, False=Failure.

hapi_aws_disconnect 
^^^^^^^^^^^^^^^^^^^^

Disconnects the AWS socket.

+-----------------------------------------------------------------------+
| bool hapi_aws_disconnect(struct hapi \*hapi)                          |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi: HAPI instance pointer.

Return: AWS disconnection status. True=Success, False=Failure.

hapi_aws_send_data 
^^^^^^^^^^^^^^^^^^^

Sends AWS data.

+-----------------------------------------------------------------------+
| bool hapi_aws_send_data(struct hapi \*hapi, char \*data, uint32_t     |
| datalen, uint8_t always_connected, uint8_t aws_data_type)             |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi: HAPI instance pointer.

2. data: AWS data to be sent.

3. datalen: Number of bytes to be sent.

4. always_connected: If Talaria TWO is to be ON always, set this
   parameter to 1 or else 0.

5. aws_data_type: Type of data to be sent.

Return: Status of sending AWS data. True=Success, False=Failure.

hapi_aws_set_config 
^^^^^^^^^^^^^^^^^^^^

Sets AWS configuration.

+-----------------------------------------------------------------------+
| bool hapi_aws_set_config(struct hapi \*hapi, const char               |
| \*aws_host_url, const char \*aws_thing_name, const uint16_t aws_port, |
| const uint32_t sleep_interval, const char \*root_ca_path, const char  |
| \*device_cert_path, const char \*device_pkey_path, const char         |
|                                                                       |
| \*client_id)                                                          |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi: HAPI instance pointer.

2. aws_host_url: AWS host string or AWS URL.

3. aws_thing_name: AWS thing name.

4. aws_port: AWS port number (should be 8883).

5. sleep_interval: AWS update interval.

6. root_ca_path: Pointer to the CA certificate path.

7. device_cert_path: Pointer to the client certificate path.

8. device_pkey_path: Pointer to the private key file path.

9. client_id: AWS client name/ID.

Return: Status of setting AWS configuration. True=Success,
False=Failure.

hapi_aws_set_ind_cb 
^^^^^^^^^^^^^^^^^^^^

Sets AWS callback function.

+-----------------------------------------------------------------------+
| void hapi_aws_set_ind_cb(hapi_aws_ind_cb cb)                          |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi_aws_ind_cb: AWS callback handle.

Return: NULL.

Heartbeat APIs 
~~~~~~~~~~~~~~~

hapi\_ beat_send
^^^^^^^^^^^^^^^^

Sends heartbeat signal from host to Talaria TWO.

+-----------------------------------------------------------------------+
| bool heart_beat_send(struct hapi \*hapi)                              |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi: HAPI instance pointer.

Return: Heartbeat send status. True=Success, False=Failure.
