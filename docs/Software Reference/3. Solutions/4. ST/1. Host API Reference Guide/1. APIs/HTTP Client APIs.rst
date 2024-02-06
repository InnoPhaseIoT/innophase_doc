.. _st api http client:

HTTP Client APIs
~~~~~~~~~~~~~~~~

hapi_http_client_setup
^^^^^^^^^^^^^^^^^^^^^^

Used to setup the HTTP client service.

.. code:: shell

    void hapi_http_client_setup(struct hapi *hapi_p, hapi_http_client_resp_cb cb, void *cb_ctx)


Arguments:

1. hapi_p: HAPI instance pointer.

2. cb: The http callback function pointer.

3. cb_ctx: The callback context.

Return: None.

hapi_http_client_start
^^^^^^^^^^^^^^^^^^^^^^

Used to start the HTTP client connection.

.. code:: shell

    bool hapi_http_client_start(struct hapi *hapi_p, char* serverName, uint32_t port, char* certName, uint32_t* clientID)


Arguments:

1. hapi_p: HAPI instance pointer.

2. serverName: The server domain name or IP address.

3. port: The port number of the http server.

4. certName: The SSL certificate name.

5. clientID: Pointer to integer used for returning client ID.

Return: Return: True(1) on Success. False(0) on Error.

hapi_http_client_send_req
^^^^^^^^^^^^^^^^^^^^^^^^^

Used to send HTTP request to the server. The HTTP server connection
should exist for this API to work.

.. code:: shell

    bool hapi_http_client_send_req(struct hapi *hapi_p, uint32_t clientID, uint32_t method, char* req_uri, uint32_t dataLen, char* dataToSend)


Arguments:

1. hapi_p: HAPI instance pointer

2. clientID: The valid client id created with the HTTP connection.

3. method: The GET(1) and POST(0) methods.

4. Req_uri: The URI to request.

5. dataLen: The length of the data to request.

6. dataToSend: Pointer to the data.

Return: Return: True(1) on Success. False(0) on Error.

hapi_http_client_hdr_set
^^^^^^^^^^^^^^^^^^^^^^^^

Used to set HTTP request header.

.. code:: shell

    bool hapi_http_client_hdr_set(struct hapi *hapi_p, uint32_t headerID, char* headerVal)


Arguments:

1. hapi_p: HAPI instance pointer.

2. headerID: The header id as per the httphdrtype definition.

The httphdrtype is defined as:

.. code:: shell

    typedef enum {
        STW_HTTP_HDR_INVAL,       /* special value for invalid header */
        STW_HTTP_HDR_ALLOW,
        STW_HTTP_HDR_AUTHORIZATION,
        STW_HTTP_HDR_CONNECTION,
        STW_HTTP_HDR_CONTENT_ENCODING,
        STW_HTTP_HDR_CONTENT_LENGTH,
        STW_HTTP_HDR_CONTENT_RANGE,
        STW_HTTP_HDR_CONTENT_TYPE,
        STW_HTTP_HDR_COOKIE,
        STW_HTTP_HDR_COOKIE2,
        STW_HTTP_HDR_DATE,
        STW_HTTP_HDR_EXPIRES,
        STW_HTTP_HDR_FROM,
        STW_HTTP_HDR_HOST,
        STW_HTTP_HDR_IF_MODIFIED_SINCE,
        STW_HTTP_HDR_LAST_MODIFIED,
        STW_HTTP_HDR_LOCATION,
        STW_HTTP_HDR_PRAGMA,
        STW_HTTP_HDR_RANGE,
        STW_HTTP_HDR_REFERER,
        STW_HTTP_HDR_SERVER,
        STW_HTTP_HDR_SET_COOKIE,
        STW_HTTP_HDR_TRANSFER_ENCODING,
        STW_HTTP_HDR_USER_AGENT,
        STW_HTTP_HDR_WWW_AUTHENTICATE,
        STW_HTTP_HDR_COUNT,
        STW_HTTP_HDR_CUSTOM       /* Value indicating the start of custom headers */
    } httphdrtype;


3. headerVal: The header value to set.

Return: True(1) on Success. False(0) on Error.

hapi_http_client_hdr_delete
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Used to delete HTTP request header.

.. code:: shell

    bool hapi_http_client_hdr_delete(struct hapi *hapi_p, uint32_t headerID)

Arguments:

1. hapi_p: HAPI instance pointer

2. headerID: The header ID as per the httphdrtype definition.

Return: Return: True(1) on Success. False(0) on Error.

hapi_http_cert_store
^^^^^^^^^^^^^^^^^^^^

Used to store SSL/TLS certificate for HTTPS connection.

.. code:: shell

    bool hapi_http_cert_store(struct hapi *hapi_p, char* certName, uint32_t certLen, char* certData)


Arguments:

1. hapi_p: HAPI instance pointer.

2. certName: The certificate name.

3. certData: The certificate content data pointer.

Return: Return: True(1) on Success. False(0) on Error.

hapi_http_cert_delete
^^^^^^^^^^^^^^^^^^^^^

Used to delete SSL/TLS certificate for HTTPS.

.. code:: shell

    bool hapi_http_cert_delete(struct hapi *hapi_p, char *certName) 


Arguments:

1. hapi_p: HAPI instance pointer.

2. certName: The certificate name to delete.

Return: Return: True(1) on Success. False(0) on Error.

hapi_http_close
^^^^^^^^^^^^^^^

Used to close the HTTP connection opened.

.. code:: shell

    bool hapi_http_close(struct hapi *hapi_p, uint32_t clientId) 


Arguments:

1. hapi_p: HAPI instance pointer.

2. clientID: The valid client id created with the http connection.

Return: Return: True(1) on Success. False(0) on Error.
