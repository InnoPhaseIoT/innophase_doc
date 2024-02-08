.. _ex http client:

HTTP Client
--------------

This document provides details on using the HTTP client APIs provided by
the HTTP module under components. This application demonstrates using
these APIs to connect to HTTP servers in secured (HTTPS) and non-secured
way.

The document also discusses the GET and POST of HTTP methods and ways of
executing it.

Features and Limitations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The HTTP/S implementation supports:

1. HTTP 1.1 version. Both HTTP and HTTPS

2. HTTP client connection to the server specified by the IP address or
   Host name)

3. HTTP GET and POST methods

4. Setting of headers by the application. Only the Host header is
   implicitly set

5. Supports receiving the response with Transfer encoding Chunked.

Following are the limitations:

1. CA certificate must be in the PEM format.

2. HTTP redirection is not supported

HTTP/S APIs 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

HTTP/S Open
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is performed using the following API:

.. code:: shell

    http_client_handle_t
    http_client_open(http_client_config_t *cfg)


This API connects to the remote HTTP server. The configuration needed
for the connection is passed using the following data structure:

.. code:: shell

      typedef struct {
          char *hostname;/**<Host name or the IP address of the server*/
          int port;/**<Server port*/
          int secured; /** 0 – HTTP (non secure), 
                           1 - HTTPS without server verification
                           2 – HTTPS with server certificate validation*/
          ssl_wrap_cfg_t ssl_cfg;/**<SSL configuration*/
          int time_out;/**<Connect timeout in seconds*/
      } http_client_config_t;


HTTP/S Get
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once the connection is established using http_client_open(), GET is
performed using the following API:

.. code:: shell

      int
      http_client_get(http_client_handle_t handle, char *uri,
                      http_client_resp_cb cb, void *cb_ctx,
                      int time_out)


The HTTP response is provided through the call back. The call back is
called multiple times until the response. Following is the call back
definition and the data structure passed to call back:

.. code:: shell

      typedef struct {
          int status_code;/**< HTTP response status code*/
          char **resp_hdrs;/*< Response headers. Array of strings*/
          char *resp_body; /**< Response body len*/
          int resp_len; /**< Resp len, currently availabe in the resp_body*/
          unsigned int resp_total_len;/**< Total length of the response body. If 0,
                                  No total length available before hand as the body
                                  may be sent using chunked or multipart encoding*/
          int more_data;
      } http_client_resp_info_t;
      
      /*This is the call back called when the response is received*/
      typedef void http_client_resp_cb(void *ctx, http_client_resp_info_t *resp);


HTTP/S Post
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once the connection is performed using http_client_open(), data can be
posted to HTTP server using the following API:

.. code:: shell

      int
      http_client_post(http_client_handle_t handle, char *uri,
                       char *buff, int buff_len,
                       http_client_resp_cb cb, void *cb_ctx,
                       int time_out);


The response is provided using the call back. Setting content length
header is a must before using this API.

Setting the header
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

User application can set the header using the following API:

.. code:: shell

      int
      http_client_set_req_hdr(http_client_handle_t handle, const char *hdrname, const char *hdrval);


Closing the connection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The connection can be closed using the following API:

.. code:: shell

      int
      http_client_close(http_client_handle_t handle);


Running the Application 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Programming Talaria TWO board with certificates 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For HTTPS secure applications, CA certificates need to be provided. For
Testing with httpbin.org, the certificate - httpbin_ca.pem which is
present in the location: examples/http_client/cert can be used. This
file can be written into the Talaria TWO File System using the Download
Tool as mentioned in the subsequent sections. The default path for
httpbin_ca.pem in the File System should be:
/data/certs/https_client/app.

Show File System Contents
~~~~~~~~~~~~~~~~~~~~~~~~~

Click on Show File System Contents to see the current available files in
the file system.

Write Files
~~~~~~~~~~~

Before writing the file(s) into Talaria TWO, user must create a folder
with the name data and place the certificate either directly into the
data or they can create multiple subfolders (for example: data/ or
data/certs/https_client/app ) and place the certificates inside the
sub-directory. The certificate shall be present in the data fs with the
same name as in the boot arguments.

To write files into Talaria TWO File System, use the Download Tool as
shown in Figure 2. After clicking on “Select Path to Write Files”,
select the data directory from the host in which the certificate is
stored and then click on “Write Files” to write the certificate into the
File System.

**Note:** When trying to access a secured web server, keep only the CA
certificate specific to that server in data fs. Do not use bundle of CA
certificates intended for a browser. Use use_ca_bundle=1 if bundled
certificates are used.

Programming Talaria TWO board with ELF
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Program http_client.elf *(freertos_sdk_x.y\\examples\\http_client\\bin)*
using the Download tool:

1. Launch the Download tool provided with InnoPhase Talaria TWO SDK.

2. In the GUI window:

   a. Boot Target: Select the appropriate EVK from the drop-down

   b. ELF Input: Load the http_client.elf by clicking on Select ELF
      File.

   c. AP Options: Provide the SSID and Passphrase under AP Options to
      connect to an Access Point.

   d. Boot arguments: Pass the following boot arguments:

.. code:: shell

      host=httpbin.org,path=/json,port=80,secured=0,method=get,post_len=3000


e. Programming: Prog RAM or Prog Flash as per requirement.

**
**

Using the Application
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The list of boot arguments are as follows:

1. ssid: SSID of the Wi-Fi network to connect to

2. passphrase: Passphrase of the network

3. host: Domain name of the server or the IP address (dotted decimal
   format)

4. path: path of the file

5. port: Server port. 80 in case of non-secured (HTTP), 443 in case of
   secured (HTTPS)

6. secured:

..

   0 - HTTP,

1. HTTPS without server verification

2. HTTPS with server certificate validation

7. method: Get/Post

8. ca_cert: Certificate path in data FS in case of HTTPS

9. post_len: Number of bytes to be sent as part of post data. The post
   data is internally generated

Example boot args for HTTP Get (non-secure)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: shell

      ssid=<ssid>,passphrase=<passphrase>,host=httpbin.org,path=/json,port=80,secured=0,method=get


Console output:

.. code:: shell

      Y-BOOT 208ef13 2019-07-22 12:26:54 -0500 790da1-b-7
      ROM yoda-h0-rom-16-0-gd5a8e586
      FLASH:PWWWWWWAE
      Build $Id: git-e52d93e $
      Flash detected. flash.hw.uuid: 39483937-3207-0080-0055-ffffffffffff
      Bootargs: ssid=innotest_AP passphrase=inno@1234 host=httpbin.org path=/json port=80 secured=0 method=get
      $App:git-8b301e9
      SDK Ver: FREERTOS_SDK_1.0
      Http Client Demo App
      
      
      Application Information:
      ------------------------
      Name       : HTTP  application
      Version    : 2.0
      Build Date : Aug 24 2023
      Build Time : 15:26:32
      Heap Available: 309 KB (316664 Bytes)
      
      [APP]Bootparams :
      --------------------
      url=<null>
      host= httpbin.org
      port=80
      path= /json
      secured= 0
      method= get
      ca_cert=<null>
      post_len=<null>
      test_iterations = <null>
      use_ca_bundle = <null>
      hdr1_name= <null>	hdr1_val= <null>
      hdr2_name= <null>	hdr2_val= <null>
      hdr3_name= <null>	hdr3_val= <null>
      
      post_data= <null>
      post_data_file= <null>
      [APP]Bootparams end here....
      
      [APP]Bootparams check done....ret = 0
      addr e0:69:3a:00:08:38
      network profile created for ssid: innotest_AP
      Connecting to added network : innotest_AP
      [0.743,823] CONNECT:0e:70:6c:d6:3a:62 Channel:6 rssi:-30 dBm
      wcm_notify_cb to App Layer - WCM_NOTIFY_MSG_LINK_UP
      wcm_notify_cb to App Layer - WCM_NOTIFY_MSG_ADDRESS
      [0.801,323] MYIP 192.168.99.195
      [0.801,488] IPv6 [fe80::e269:3aff:fe00:838]-link
      wcm_notify_cb to App Layer - WCM_NOTIFY_MSG_CONNECTED
      Connected to added network : innotest_AP
      ** Test Iterations = 1 **
      [APP]Calling http_client_open(). heap size = 241760
      [APP]Succes: HTTP connection done
      [APP]HTTP Get
      [APP]Response:
      429 ----------------------
      200
      Date: Thu, 24 Aug 2023 13:08:05 GMT
      Content-Type: application/json
      Content-Length: 429
      Connection: keep-alive
      Server: gunicorn/19.9.0
      Access-Control-Allow-Origin: *
      Access-Control-Allow-Credentials: true
      [APP]Body:
      {
        "slideshow": {
          "author": "Yours Truly", 
          "date": "date of publication", 
          "slides": [
            {
              "title": "Wake up to WonderWidgets!", 
              "type": "all"
            }, 
            {
              "items": [
                "Why <em>WonderWidgets</em> are great", 
                "Who <em>buys</em> WonderWidgets"
              ], 
              "title": "Overview", 
              "type": "all"
            }
          ], 
          "title": "Sample Slide Show"
        }
      }
      
      [APP]Success: http_client_get(), rval = 0
      
      [APP]------ Program Exit------------- 



Example boot args for HTTPS Get (without server verification)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: shell

      ssid=<ssid>,passphrase=<passphrase>,host=httpbin.org,path=/json,port=443,secured=1,method=get,ca_cert=/data/httpbin_ca.pem 


Console output:

.. code:: shell

      Y-BOOT 208ef13 2019-07-22 12:26:54 -0500 790da1-b-7
      ROM yoda-h0-rom-16-0-gd5a8e586
      FLASH:PWWWWWWAE
      Build $Id: git-e52d93e $
      Flash detected. flash.hw.uuid: 39483937-3207-0080-0055-ffffffffffff
      Bootargs: ssid=innotest_AP passphrase=inno@1234 host=httpbin.org path=/json port=443 secured=1 method=get ca_cert=/data/httpbin_ca.pem
      $App:git-8b301e9
      SDK Ver: FREERTOS_SDK_1.0
      Http Client Demo App
      
      Application Information:
      ------------------------
      Name       : HTTP  application
      Version    : 2.0
      Build Date : Aug 24 2023
      Build Time : 15:26:32
      Heap Available: 309 KB (316664 Bytes)
      
      [APP]Bootparams :
      --------------------
      url=<null>
      host= httpbin.org
      port=443
      path= /json
      secured= 1
      method= get
      ca_cert=/data/httpbin_ca.pem
      post_len=<null>
      test_iterations = <null>
      use_ca_bundle = <null>
      hdr1_name= <null>	hdr1_val= <null>
      hdr2_name= <null>	hdr2_val= <null>
      hdr3_name= <null>	hdr3_val= <null>
      
      post_data= <null>
      post_data_file= <null>
      [APP]Bootparams end here....
      
      [APP]Bootparams check done....ret = 0
      addr e0:69:3a:00:08:38
      network profile created for ssid: innotest_AP
      
      Connecting to added network : innotest_AP
      [0.735,885] DEAUTHENTICATED: reason 1
      [0.846,413] CONNECT:0e:70:6c:d6:3a:62 Channel:6 rssi:-23 dBm
      wcm_notify_cb to App Layer - WCM_NOTIFY_MSG_LINK_UP
      wcm_notify_cb to App Layer - WCM_NOTIFY_MSG_ADDRESS
      [0.923,206] MYIP 192.168.99.195
      [0.923,369] IPv6 [fe80::e269:3aff:fe00:838]-link
      wcm_notify_cb to App Layer - WCM_NOTIFY_MSG_CONNECTED
      
      Connected to added network : innotest_AP
      
      ** Test Iterations = 1 **
      
      [APP]Calling http_client_open(). heap size = 241768
        . [SSL_WRAP]Checking input configurations...
        . [SSL_WRAP]Seeding the random number generator...
        . [SSL_WRAP]Connecting to tcp httpbin.org:443...
        . [SSL_WRAP]Setting up the SSL/TLS structure...
        . [SSL_WRAP]setting configurations..
              >auth mode = 0 (0- skip, 1- optional, 2- required
              >max fragment len = 0
              >Handshake timeout = 30 Sec
        . [SSL_WRAP]Performing the SSL/TLS handshake...
        . [SSL_WRAP] Handshake done. ok
        . [SSL_WRAP]Verifying peer X.509 certificate.
      [APP]Succes: HTTP connection done
      [APP]HTTP Get
      [APP]Response:
      0 ----------------------
      200
      Date: Thu, 24 Aug 2023 15:18:35 GMT
      Content-Type: application/json
      Content-Length: 429
      Connection: keep-alive
      Server: gunicorn/19.9.0
      Access-Control-Allow-Origin: *
      Access-Control-Allow-Credentials: true
      [APP]Body:
      {
        "slideshow": {
          "author": "Yours Truly", 
          "date": "date of publication", 
          "slides": [
            {
              "title": "Wake up to WonderWidgets!", 
              "type": "all"
            }, 
            {
              "items": [
                "Why <em>WonderWidgets</em> are great", 
                "Who <em>buys</em> WonderWidgets"
              ], 
              "title": "Overview", 
              "type": "all"
            }
          ], 
          "title": "Sample Slide Show"
        }
      }
      
      [APP]Success: http_client_get(), rval = 0
      
      [APP]------ Program Exit-------------



Example boot args for HTTPS Get (with server certificate validation)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: shell

      ssid=<ssid>,passphrase=<passphrase>, host=httpbin.org,path=/json,port=443,secured=2,method=get,ca_cert= /data/certs/https_client/app/httpbin_ca.pem, post_len=3000


Console output:

.. code:: shell

      Y-BOOT 208ef13 2019-07-22 12:26:54 -0500 790da1-b-7
      ROM yoda-h0-rom-16-0-gd5a8e586
      FLASH:PWWWWWWAE
      Build $Id: git-e52d93e $
      Flash detected. flash.hw.uuid: 39483937-3207-0080-0055-ffffffffffff
      Bootargs: ssid=innotest_AP passphrase=inno@1234 host=httpbin.org path=/json port=443 secured=2 method=get ca_cert=/data/httpbin_ca.pem
      $App:git-8b301e9
      SDK Ver: FREERTOS_SDK_1.0
      Http Client Demo App
      
      Application Information:
      ------------------------
      Name       : HTTP  application
      Version    : 2.0
      Build Date : Aug 24 2023
      Build Time : 15:26:32
      Heap Available: 309 KB (316664 Bytes)
      
      [APP]Bootparams :
      --------------------
      url=<null>
      host= httpbin.org
      port=443
      path= /json
      secured= 2
      method= get
      ca_cert=/data/httpbin_ca.pem
      post_len=<null>
      test_iterations = <null>
      use_ca_bundle = <null>
      hdr1_name= <null>	hdr1_val= <null>
      hdr2_name= <null>	hdr2_val= <null>
      hdr3_name= <null>	hdr3_val= <null>
      
      post_data= <null>
      post_data_file= <null>
      [APP]Bootparams end here....
      
      [APP]Bootparams check done....ret = 0
      addr e0:69:3a:00:08:38
      network profile created for ssid: innotest_AP
      
      Connecting to added network : innotest_AP
      [0.746,258] CONNECT:0e:70:6c:d6:3a:62 Channel:6 rssi:-23 dBm
      wcm_notify_cb to App Layer - WCM_NOTIFY_MSG_LINK_UP
      wcm_notify_cb to App Layer - WCM_NOTIFY_MSG_ADDRESS
      [0.811,476] MYIP 192.168.99.195
      [0.811,644] IPv6 [fe80::e269:3aff:fe00:838]-link
      wcm_notify_cb to App Layer - WCM_NOTIFY_MSG_CONNECTED
      Connected to added network : innotest_AP
      ** Test Iterations = 1 **
      [APP]Calling http_client_open(). heap size = 236616
        . [SSL_WRAP]Checking input configurations...
        . [SSL_WRAP]Seeding the random number generator...
        . [SSL_WRAP]Loading the CA root certificate ...Cert Len = 4755
        . [SSL_WRAP]Connecting to tcp httpbin.org:443...
        . [SSL_WRAP]Setting up the SSL/TLS structure...
        . [SSL_WRAP]setting configurations..
              >auth mode = 2 (0- skip, 1- optional, 2- required
              >max fragment len = 0
              >Handshake timeout = 30 Sec
        . [SSL_WRAP]Performing the SSL/TLS handshake...
        . [SSL_WRAP] Handshake done. ok
        . [SSL_WRAP]Verifying peer X.509 certificate.
      
      [APP]Succes: HTTP connection done
      [APP]HTTP Get
      [APP]Response:
      0 ----------------------
      
      200
      Date: Thu, 24 Aug 2023 15:19:53 GMT
      Content-Type: application/json
      Content-Length: 429
      Connection: keep-alive
      Server: gunicorn/19.9.0
      Access-Control-Allow-Origin: *
      Access-Control-Allow-Credentials: true
      [APP]Body:
      {
        "slideshow": {
          "author": "Yours Truly", 
          "date": "date of publication", 
          "slides": [
            {
              "title": "Wake up to WonderWidgets!", 
              "type": "all"
            }, 
            {
              "items": [
                "Why <em>WonderWidgets</em> are great", 
                "Who <em>buys</em> WonderWidgets"
              ], 
              "title": "Overview", 
              "type": "all"
            }
          ], 
          "title": "Sample Slide Show"
        }
      }
      
      [APP]Success: http_client_get(), rval = 0
      
      [APP]------ Program Exit-------------



Example boot args for HTTP Post (non-secure)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: shell

      ssid=<ssid>,passphrase=<passphrase>,host=httpbin.org,path=/anything,port=80,secured=0,method=post, post_len=100


**Note**:

1. If only post_len is provided, internally generated data of specified
   length is posted.

2. Use post_data boot param to send a specific data. This data length is
   limited by the boot param max length.

3. To send a file content as post data, place the file in the data fs
   and provide the file name using post_data_file boot param. Example,
   /data/postdata.txt. postdata.txt mist be part of the data fs

Console output:

.. code:: shell

      Y-BOOT 208ef13 2019-07-22 12:26:54 -0500 790da1-b-7
      ROM yoda-h0-rom-16-0-gd5a8e586
      FLASH:PWWWWWWAE
      Build $Id: git-e52d93e $
      Flash detected. flash.hw.uuid: 39483937-3207-0080-0055-ffffffffffff
      Bootargs: ssid=innotest_AP passphrase=inno@1234 host=httpbin.org path=/anything port=80 secured=0 method=post post_len=128
      $App:git-8b301e9
      SDK Ver: FREERTOS_SDK_1.0
      Http Client Demo App
      
      Application Information:
      ------------------------
      Name       : HTTP  application
      Version    : 2.0
      Build Date : Aug 24 2023
      Build Time : 15:26:32
      Heap Available: 309 KB (316664 Bytes)
      
      [APP]Bootparams :
      --------------------
      url=<null>
      host= httpbin.org
      port=80
      path= /anything
      secured= 0
      method= post
      ca_cert=<null>
      post_len=128
      test_iterations = <null>
      use_ca_bundle = <null>
      hdr1_name= <null>	hdr1_val= <null>
      hdr2_name= <null>	hdr2_val= <null>
      hdr3_name= <null>	hdr3_val= <null>
      
      post_data= <null>
      post_data_file= <null>
      [APP]Bootparams end here....
      
      [APP]Bootparams check done....ret = 0
      addr e0:69:3a:00:08:38
      network profile created for ssid: innotest_AP
      
      Connecting to added network : innotest_AP
      [0.736,982] DEAUTHENTICATED: reason 1
      [0.845,208] CONNECT:0e:70:6c:d6:3a:62 Channel:6 rssi:-41 dBm
      wcm_notify_cb to App Layer - WCM_NOTIFY_MSG_LINK_UP
      wcm_notify_cb to App Layer - WCM_NOTIFY_MSG_ADDRESS
      [0.902,951] MYIP 192.168.99.195
      [0.903,115] IPv6 [fe80::e269:3aff:fe00:838]-link
      wcm_notify_cb to App Layer - WCM_NOTIFY_MSG_CONNECTED
      Connected to added network : innotest_AP
      ** Test Iterations = 1 **
      [APP]Calling http_client_open(). heap size = 241768
      [APP]Succes: HTTP connection done
      [APP]HTTP Post
      [APP]Response:
      446 ----------------------
      200
      Date: Thu, 24 Aug 2023 15:23:59 GMT
      Content-Type: application/json
      Content-Length: 446
      Connection: keep-alive
      Server: gunicorn/19.9.0
      Access-Control-Allow-Origin: *
      Access-Control-Allow-Credentials: true
      [APP]Body:
      {
        "args": {}, 
        "data": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", 
        "files": {}, 
        "form": {}, 
        "headers": {
          "Content-Length": "128", 
          "Host": "httpbin.org", 
          "X-Amzn-Trace-Id": "Root=1-64e775f1-309cfc7a175a59de33be917a"
        }, 
        "json": null, 
        "method": "POST", 
        "origin": "223.186.99.101", 
        "url": "http://httpbin.org/anything"
      }
      
      [APP]Success: http_client_post(), rval = 0
      
      [APP]------ Program Exit-------------



Example boot args for HTTPS Post (without server verification)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: shell

      ssid=<ssid>,passphrase=<passphrase>,host=httpbin.org,path=/anything,port=443,secured=1,method=post,ca_cert=/data/certs/https_client/app/httpbin_ca.pem, post_len=100


Console output:

.. code:: shell

      Y-BOOT 208ef13 2019-07-22 12:26:54 -0500 790da1-b-7
      ROM yoda-h0-rom-16-0-gd5a8e586
      FLASH:PWWWWWWAE
      Build $Id: git-e52d93e $
      Flash detected. flash.hw.uuid: 39483937-3207-0080-0055-ffffffffffff
      Bootargs: ssid=innotest_AP passphrase=inno@1234 host=httpbin.org path=/anything port=80 secured=0 method=post post_len=128
      $App:git-8b301e9
      SDK Ver: FREERTOS_SDK_1.0
      Http Client Demo App
      
      Application Information:
      ------------------------
      Name       : HTTP  application
      Version    : 2.0
      Build Date : Aug 24 2023
      Build Time : 15:26:32
      Heap Available: 309 KB (316664 Bytes)
      
      [APP]Bootparams :
      --------------------
      url=<null>
      host= httpbin.org
      port=80
      path= /anything
      secured= 0
      method= post
      ca_cert=<null>
      post_len=128
      test_iterations = <null>
      use_ca_bundle = <null>
      hdr1_name= <null>	hdr1_val= <null>
      hdr2_name= <null>	hdr2_val= <null>
      hdr3_name= <null>	hdr3_val= <null>
      
      post_data= <null>
      post_data_file= <null>
      [APP]Bootparams end here....
      
      [APP]Bootparams check done....ret = 0
      addr e0:69:3a:00:08:38
      network profile created for ssid: innotest_AP
      
      Connecting to added network : innotest_AP
      [0.736,982] DEAUTHENTICATED: reason 1
      [0.845,208] CONNECT:0e:70:6c:d6:3a:62 Channel:6 rssi:-41 dBm
      wcm_notify_cb to App Layer - WCM_NOTIFY_MSG_LINK_UP
      wcm_notify_cb to App Layer - WCM_NOTIFY_MSG_ADDRESS
      [0.902,951] MYIP 192.168.99.195
      [0.903,115] IPv6 [fe80::e269:3aff:fe00:838]-link
      wcm_notify_cb to App Layer - WCM_NOTIFY_MSG_CONNECTED
      Connected to added network : innotest_AP
      ** Test Iterations = 1 **
      [APP]Calling http_client_open(). heap size = 241768
      [APP]Succes: HTTP connection done
      [APP]HTTP Post
      [APP]Response:
      446 ----------------------
      200
      Date: Thu, 24 Aug 2023 15:23:59 GMT
      Content-Type: application/json
      Content-Length: 446
      Connection: keep-alive
      Server: gunicorn/19.9.0
      Access-Control-Allow-Origin: *
      Access-Control-Allow-Credentials: true
      [APP]Body:
      {
        "args": {}, 
        "data": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", 
        "files": {}, 
        "form": {}, 
        "headers": {
          "Content-Length": "128", 
          "Host": "httpbin.org", 
          "X-Amzn-Trace-Id": "Root=1-64e775f1-309cfc7a175a59de33be917a"
        }, 
        "json": null, 
        "method": "POST", 
        "origin": "223.186.99.101", 
        "url": "http://httpbin.org/anything"
      }
      
      [APP]Success: http_client_post(), rval = 0
      
      [APP]------ Program Exit-------------


Example boot args for HTTPS Post (with server certificate validation)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: shell

      ssid=<ssid>,passphrase=<passphrase>,host=httpbin.org,path=/anything,port=443,secured=2,method=post,ca_cert=/data/certs/https_client/app/httpbin_ca.pem, post_len=100


Console output:

.. code:: shell

      $App:git-8b301e9
      SDK Ver: FREERTOS_SDK_1.0
      Http Client Demo App
      
      Application Information:
      ------------------------
      Name       : HTTP  application
      Version    : 2.0
      Build Date : Aug 24 2023
      Build Time : 15:26:32
      Heap Available: 309 KB (316664 Bytes)
      
      [APP]Bootparams :
      --------------------
      url=<null>
      host= httpbin.org
      port=443
      path= /anything
      secured= 2
      method= post
      ca_cert=/data/httpbin_ca.pem
      post_len=128
      test_iterations = <null>
      use_ca_bundle = <null>
      hdr1_name= <null>	hdr1_val= <null>
      hdr2_name= <null>	hdr2_val= <null>
      hdr3_name= <null>	hdr3_val= <null>
      
      post_data= <null>
      post_data_file= <null>
      [APP]Bootparams end here....
      
      [APP]Bootparams check done....ret = 0
      addr e0:69:3a:00:08:38
      network profile created for ssid: innotest_AP
      
      Connecting to added network : innotest_AP
      [0.738,653] DEAUTHENTICATED: reason 1
      [0.846,537] CONNECT:0e:70:6c:d6:3a:62 Channel:6 rssi:-30 dBm
      wcm_notify_cb to App Layer - WCM_NOTIFY_MSG_LINK_UP
      wcm_notify_cb to App Layer - WCM_NOTIFY_MSG_ADDRESS
      [0.898,345] MYIP 192.168.99.195
      [0.898,510] IPv6 [fe80::e269:3aff:fe00:838]-link
      wcm_notify_cb to App Layer - WCM_NOTIFY_MSG_CONNECTED
      
      Connected to added network : innotest_AP
      ** Test Iterations = 1 **
      [APP]Calling http_client_open(). heap size = 236656
        . [SSL_WRAP]Checking input configurations...
        . [SSL_WRAP]Seeding the random number generator...
        . [SSL_WRAP]Loading the CA root certificate ...Cert Len = 4755
        . [SSL_WRAP]Connecting to tcp httpbin.org:443...
        . [SSL_WRAP]Setting up the SSL/TLS structure...
        . [SSL_WRAP]setting configurations..
              >auth mode = 2 (0- skip, 1- optional, 2- required
              >max fragment len = 0
              >Handshake timeout = 30 Sec
        . [SSL_WRAP]Performing the SSL/TLS handshake...
        . [SSL_WRAP] Handshake done. ok
        . [SSL_WRAP]Verifying peer X.509 certificate.
      
      [APP]Succes: HTTP connection done
      [APP]HTTP Post
      
      [APP]Response:
      0 ----------------------
      200
      Date: Thu, 24 Aug 2023 15:30:08 GMT
      Content-Type: application/json
      Content-Length: 447
      Connection: keep-alive
      Server: gunicorn/19.9.0
      Access-Control-Allow-Origin: *
      Access-Control-Allow-Credentials: true
      [APP]Body:
      {
        "args": {}, 
        "data": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", 
        "files": {}, 
        "form": {}, 
        "headers": {
          "Content-Length": "128", 
          "Host": "httpbin.org", 
          "X-Amzn-Trace-Id": "Root=1-64e7777f-08d8f53955c752f716a6427c"
        }, 
        "json": null, 
        "method": "POST", 
        "origin": "223.186.99.101", 
        "url": "https://httpbin.org/anything"
      }
      
      [APP]Success: http_client_post(), rval = 0
      
      [APP]------ Program Exit-------------
