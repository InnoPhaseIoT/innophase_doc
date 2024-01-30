TLS APIs
~~~~~~~~

hapi_tls_create
^^^^^^^^^^^^^^^

Creates the TLS socket and does the handshake to support the TLS
functionality.

+-----------------------------------------------------------------------+
| struct hapi_tls \* hapi_tls_create(struct hapi \*hapi,const char      |
| \*server, const char \*port, uint16_t maxfraglen, uint16_t cacertlen, |
| uint16_t owncertlen, uint16_t pkeylen)                                |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi: HAPI instance pointer.

2. server: Server URI string.

3. port: Server port.

4. maxfraglen: Max fragmentation size.

5. cacertlen: The CA certificate length.

6. owncertlen: Own certificate length.

7. pkeylen: The key length.

Return: TLS HAPI instance pointer on Success, NULL on Failure.

hapi_tls_set_dataready_cb
^^^^^^^^^^^^^^^^^^^^^^^^^

Registers the callback function when the TLS data is available.

+-----------------------------------------------------------------------+
| void hapi_tls_set_dataready_cb(struct hapi_tls \*hapi_tls,            |
| hapi_tls_dataready_cb dataready_cb, void \*context)                   |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi_tls: HAPI TLS instance pointer.

2. dataready_cb: Call back function.

3. context: The context to pass when the callback getting called.

Return: None.

hapi_tls_upload_cert
^^^^^^^^^^^^^^^^^^^^

Stores the certificate passed.

+-----------------------------------------------------------------------+
| bool hapi_tls_upload_cert(struct hapi_tls \*hapi_tls, enum            |
| hapi_tls_cert_type cert_type, const char \* cert, size_t cert_size)   |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi_tls: HAPI TLS instance pointer.

2. hapi_tls_cert_type cert_type: Type of the certificate to load.

3. cert: The certificate start pointer.

4. cert_size: The size of the certificate in bytes.

Return: Bool, True on Success, False on Failure.

hapi_tls_handshake
^^^^^^^^^^^^^^^^^^

Triggers the TLS handshake operation.

+-----------------------------------------------------------------------+
| bool hapi_tls_handshake(struct hapi_tls \*hapi_tls, enum              |
| hapi_tls_auth_mode auth_mode)                                         |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi_tls: HAPI TLS instance pointer.

2. auth_mode: The authentication mode supported.

Return: Bool, True on Success, False on Failure.

hapi_tls_write
^^^^^^^^^^^^^^

Sends data on the TLS connection.

+-----------------------------------------------------------------------+
| ssize_t hapi_tls_write(struct hapi_tls \*hapi_tls, const void \*      |
| data, size_t size)                                                    |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi_tls: HAPI TLS instance pointer.

2. data: Data to be sent.

3. Size: Size of the data in bytes to be sent.

Return: the number of bytes sent, on Success, 0 on Failure.

hapi_tls_read
^^^^^^^^^^^^^

Reads data from the TLS socket.

+-----------------------------------------------------------------------+
| ssize_t hapi_tls_read(struct hapi_tls \*hapi_tls, void \* buf, size_t |
| size)                                                                 |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi_tls: HAPI TLS instance pointer.

2. buf: Data buffer to which the reception happens.

3. Size: Size of the data in bytes TPO read.

Return: the number of bytes received, on Success, 0 on Failure.

hapi_tls_close
^^^^^^^^^^^^^^

Closes the TLS socket and releases all the resources allocated.

+-----------------------------------------------------------------------+
| bool hapi_tls_close(struct hapi_tls \*hapi_tls)                       |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi_tls: HAPI TLS instance pointer.

Return: True on Success, False on Failure.

hapi_tls_set_notification_cb
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Registers TLS set notification callback.

+-----------------------------------------------------------------------+
| void                                                                  |
|                                                                       |
| hapi_tls_set_notification_cb(struct hapi_tls \*hapi_tls,              |
| hapi_tls_notification_cb notification_cb, void \*context)             |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi_tls: HAPI TLS instance pointer.

2. hapi_tls_notification_cb: TLS data ready callback function.

3. context: Context for callback.

Return: None.
