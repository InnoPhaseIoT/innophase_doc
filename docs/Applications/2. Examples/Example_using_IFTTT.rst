.. _ex ifttt:

IFTTT - Overview
----------------

This document provides basic information about IFTTT. It discusses using
Talaria TWO with IFTTT with the help of an example application. The
information includes setting up Talaria TWO to connect to IFTTT, a
stepwise procedure to set up IFTTT account and the required
infrastructure in IFTTT.

IFTTT Using IFTTT
~~~~~~~~~~~~~~~~~

IFTTT is a web service that provides easiest way to connect thousands of
apps and devices, including Google Drive, Amazon Alexa, Fitbit, Twitter,
Dropbox, Ring. Using IFTTT, two apps called *services* are connected
using an *applet* defined in IFTTT webservice.

Accessing IFTTT
~~~~~~~~~~~~~~~~~~~~~~

IFTTT web service can be access using the following link:
https://ifttt.com/.

Creating an Account in IFTTT
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Having an account in IFTTT web service is a prerequisite to exploring
more and getting hands-on with the example application. This is free and
simple to create. Open the link in section 3.1 and click on Get Started.
Follow the steps as stated on the website.

IFTTT Concepts 
~~~~~~~~~~~~~~~~~~~~~~

There are four important concepts in IFTTT:

1. Service: Services are already available/defined interfaces such as
   Twitter, Facebook, Google Assistant and so on.

..

   **Note**: These are IFTTT services defined in the IFTTT platform.
   They internally connect with actual web services/applications that
   are available outside IFTTT. Details on creating services is outside
   the scope of this document.

2. Applet: Applet is an entity defined in IFTTT that connects two
   services.

3. Trigger: Once two IFTTT services are connected using an applet, one
   of the application acts as the trigger. This IFTTT service that acts
   as trigger, receives a request from outside and triggers a specific
   action in the other service connected in the same applet.

4. Action: When the IFTTT service acting as the trigger triggers the
   other service in the same applet, an action is taken by the other
   service.

Applet 
~~~~~~~~~~~~~~~~~~~~~~

Applet on the IFTTT platform define the following:

1. The services to be connected

2. The service that is going to act as a trigger

3. The service that is going to take action

Creating an Applet for Talaria TWO
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This section discusses steps to create an applet for Talaria TWO to
interact with IFTTT. For this, already available IFTTT services like
Webhooks and Email can be chosen. The idea is to send data/request to
Webhooks service from Talaria TWO. This should trigger an email being
sent to the email address configured in the Email IFTTT service.

**Note**: It is required to have an account before executing the next
set of steps.

1. Open maker.ifttt.com and sign in.

2. Click Create in the top right. Select If This.

3. In the search field, enter Webhooks and select that service. Select
   Receive a web request.

4. In the Event Name field, enter suitable name like <trigger_from_t2>.
   Click the Create trigger button.

5. Now, click on Then That. Select the Email service.

6. Choose the Send me an email action. If this is your first time
   setting up an email action, click Connect, and proceed with the
   configuration as instructed on IFTTT.

7. Both the trigger and action have now been configured. Click Continue.

8. Click Finish to create the applet.

With this, an applet is defined.

Now, it is required to get the Webhook endpoint URL. Execute the
following steps to acquire the same:

1. Click on your profile picture in the top right, then click My
   services.

2. Choose webhooks and click on Documentation in the upper right.

3. This gives the endpoint, like the following:
   https://maker.ifttt.com/trigger/trigger_from_t2/with/key/c9ebSVVNGeSB1yi6NrVeyl

Code Walkthrough Using IFTTT
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Application Flow Using IFTTT
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

IFTTT is a web service that provides an easy way to connect thousands of
apps and devices, including Google Drive, Amazon Alexa, Fitbit, Twitter,
Dropbox, Ring. Using IFTTT, two apps named services are connected using
an applet defined in IFTTT webservice.

Following are the steps:

1. Connect to Wi-Fi network.

2. Connect to HTTP server.

3. Get the latest config file from remote server.

4. HTTP get method.

5. HTTP post method.

Sample Code Walkthrough Using IFTTT
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A user-defined data struct is created to store the data of IFTTT:

.. code:: shell

      #define APP_NAME        "IFTTT  Demo Application"
      #define APP_VERSION     "2.0"
      
      OS_APPINFO {.stack_size = 4096};
      
      #define INPUT_PARAMETER_URL         "url"
      #define INPUT_PARAMETER_PORT        "port"
      #define INPUT_PARAMETER_SECURED     "secured"
      #define INPUT_PARAMETER_METHOD      "method"
      #define INPUT_PARAMETER_CA          "ca_cert"
      #define INPUT_PARAMETER_POST_LEN    "post_len"
      #define INPUT_PARAMETER_CLIENT_CERT "client_cert"
      #define INPUT_PARAMETER_CLIENT_KEY  "client_key"
      #define INPUT_PARAMETER_USE_CA_BUNDLE   "use_ca_bundle"
      
      #define NULL_STR  ""
      
      struct param_t {
          const char *ssid;
          const char *passphrase;
          const char *url;
          const char *port;
          const char *secured;
          const char *method;
          const char *ca_cert;
          const char *post_len;
          const char *client_cert;
          const char *client_key;
          const char *use_ca_bundle;
      };
      
      
      struct param_t param;
      char default_port[8];
      char default_secured[8];
      char default_post_len[8];
      
      bool wcm_connected = false;
      static char host[128];
      static char path[128];


Following boot arguments are passed:

1. URL, port, secured, ca_cert, method, post_len, client_cert,
   client_key value and ca_bundle.

2. SD service type and proto, and action.

.. code:: shell

      static int
      parse_boot_args(void)
      {
      
      const char *np_path;
      
      int ret = 0;
      sprintf(default_port, "%d", 80);
      sprintf(default_secured, "%d", 0);
      sprintf(default_post_len, "%d", 32);
      
      param.url = os_get_boot_arg_str(INPUT_PARAMETER_URL);
      param.port = os_get_boot_arg_str(INPUT_PARAMETER_PORT);
      param.secured = os_get_boot_arg_str(INPUT_PARAMETER_SECURED);
      param.ca_cert = os_get_boot_arg_str(INPUT_PARAMETER_CA);
      param.method = os_get_boot_arg_str(INPUT_PARAMETER_METHOD);
      param.post_len = os_get_boot_arg_str(INPUT_PARAMETER_POST_LEN);
      param.client_cert = os_get_boot_arg_str(INPUT_PARAMETER_CLIENT_CERT);
      param.client_key = os_get_boot_arg_str(INPUT_PARAMETER_CLIENT_KEY);
      param.use_ca_bundle = os_get_boot_arg_str(INPUT_PARAMETER_USE_CA_BUNDLE);


To connect to a Wi-Fi network, wcm_create()API from the Wi-Fi Connection
Manager is used. Initially, the Wi-Fi network interface is created using
wcm_create().

.. code:: shell

      wcm_handle = wcm_create(NULL);       


..

   wifi_connect_to_network()API, from components library, connects to
   the Wi-Fi network using the AP credentials provided.

.. code:: shell

      wifi_connect_to_network(&wcm_handle, WCM_CONN_WAIT_INFINITE, &wcm_connected);
      if(wcm_connected != true) {
          os_printf("\n[APP]Error: Failed to connect to WiFi N/w");
          goto exit;
      }


Here, the data structure http_client_config_t cfg is used to pass the
parameter while opening a HTTP connection with remote server using
http_client_open such as URL, port, secured, ssl_cfg, time_out.

.. code:: shell

      /* Connect to HTTP server*/
      http_client_config_t cfg = {0};
      http_client_handle_t http_handle;
      
      memset(&cfg, 0, sizeof(http_client_config_t));
      path[0]= '\0';
      if(param.url){
      os_printf("\n[APP]URL = %s", param.url);
      rval = http_client_url_to_host(param.url, host, sizeof(host), path,
      sizeof(path), &cfg.port);
      if(rval < 0){
      os_printf("\n[APP]URL is not proper");
      os_printf("\n\texample URLs:");
      os_printf("\n\t\thttps://maker.ifttt.com/trigger/krg_door_open/with/key/c9ebSVVNGeSB1yi6NrVeyl");
      }
      cfg.hostname = host;
      }
      
      if(param.port){/*If specified explicietly, overide the port specified in URL*/
      cfg.port = atoi(param.port);
      }
      cfg.secured = atoi(param.secured);
      if(cfg.secured) {
      if(cfg.secured == 1){
      cfg.ssl_cfg.auth_mode = SSL_WRAP_VERIFY_NONE;
      }else{
      cfg.ssl_cfg.auth_mode = SSL_WRAP_VERIFY_REQUIRED;
      if(!atoi(param.use_ca_bundle)){
      cfg.ssl_cfg.ca_cert.buf = utils_file_get(param.ca_cert,
      &cfg.ssl_cfg.ca_cert.len);
      if(NULL == cfg.ssl_cfg.ca_cert.buf){
      os_printf("Error: No CA certificate found. Required");
      goto exit;
      }
      }
      }
      if(param.client_cert && strlen(param.client_cert)){
      cfg.ssl_cfg.client_cert.buf = utils_file_get(param.client_cert,
      &cfg.ssl_cfg.client_cert.len);
      if(NULL == cfg.ssl_cfg.client_cert.buf){
      os_printf("Error: Could not open client certificate\n");
      goto exit;
      }
      }
      if(param.client_key && strlen(param.client_key)){
      cfg.ssl_cfg.client_key.buf = utils_file_get(param.client_key,
      &cfg.ssl_cfg.client_key.len);
      if(NULL == cfg.ssl_cfg.client_key.buf){
      os_printf("Error: Could not open client key\n");
      goto exit;
      }
      }
      cfg.secured = 1;
      }



Data structure http_client_resp_info_t is used to pass information about
the data received from the server when HTTP GET is executed using
http_client_get API.

.. code:: shell

      static void
      app_http_cb(void * ctx, http_client_resp_info_t *resp)
      {
      static int total_bytes_rcvd = 0;
      static int hdrs_printed = 0;
      int i;
      if(NULL == resp) {
      return;
      }
      if(!hdrs_printed) {
      os_printf("\n\n[APP]Response:\n%d ----------------------\n", resp->resp_len);
      os_printf("\n%d", resp->status_code);
      i = 0;
      while(resp->resp_hdrs[i]) {
      vTaskDelay(10);
      os_printf("\n%s", resp->resp_hdrs[i]);
      i++;
      }
      os_printf("\n[APP]Body:\n");
      hdrs_printed = 1;
      }
      total_bytes_rcvd += resp->resp_len;
      for(i = 0; i < resp->resp_len; i++) {
      os_printf("%c", resp->resp_body[i]);
      }
      return;
      }



API http_client_open connects to the remote HTTP server. The
configuration needed for the connection is passed using
http_client_config_t.

.. code:: shell

      http_handle = http_client_open(&cfg);
      if(NULL == http_handle) {
      os_printf("\n[APP]Error: HTTP connection failed");
      goto exit;
      }
      os_printf("\n[APP]Succes: HTTP connection done");
      /* Get the latest config file from remote server*/
      http_client_set_req_hdr(http_handle, "Host", cfg.hostname);


This function is used for performing HTTP GET. The HTTP response is
provided through the call back. The call back is called multiple times
until the whole response is received.

.. code:: shell

      if(!strcmp(param.method, "get")) {
      /*HTTP get */
      rval = http_client_get(http_handle, (char *)path, app_http_cb,
      NULL, 300);
      
      http_client_close(http_handle);
      http_handle = NULL;
      
      if(rval < 0) {
      os_printf("\n[APP]Failure : http_client_get(), rval = %d", rval);
      goto exit;
      }else{
      os_printf("\n[APP]Success");
      }
      }


This function is used to perform HTTP POST. Using this data can be sent
to the HTTP server. The response is provided using the call back.
Setting content length header is a must using http_client_set_req_hdr
before calling this API.

.. code:: shell

      if(!strcmp(param.method, "post")) {
      /*HTTP post */
      char *post_data;
      int post_data_len = 0; /*atoi(param.post_len);*/
      int send_len;
      char conetnt_len_hdr_val[16];
      
      post_data = pvPortMalloc(1024);
      if(NULL == post_data) {
      os_printf("\n[APP]Error: malloc failre for post_data");
      goto exit;
      }
      
      sprintf(conetnt_len_hdr_val, "%d", post_data_len);
      http_client_set_req_hdr(http_handle, "Content-length", conetnt_len_hdr_val);
      
      while(post_data_len) {
      send_len = post_data_len > 1024 ? 1024 : post_data_len;
      rval = http_client_post(http_handle, (char *)path,
      post_data, send_len,
      app_http_cb, NULL, 300);
      if(rval < 0) {
      os_printf("\n[APP]Failure : http_client_post(), rval = %d", rval);
      goto exit;
      }
      post_data_len -= send_len;
      }
      http_client_close(http_handle);
      
      if(rval >= 0){
      os_printf("\n[APP]Success");
      }else
      goto exit;
      
      }
      os_printf("\n\n[APP]------ Program Exit-------------\n\n");
      return 0;
      exit:
      os_printf("\n\n[APP]!!!!!! Error Exit !!!!!!!!!!!!!\n\n");
      return 0;
      }



Running the Application Using IFTTT
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Programming Talaria TWO board with ELF Using IFTTT
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Program ifttt.elf *(freertos_sdk_x.y\\examples\\ifttt\\bin)* using the
Download tool:

1. Launch the Download tool provided with InnoPhase Talaria TWO SDK.

2. In the GUI window:

   a. Boot Target: Select the appropriate EVK from the drop-down.

   b. ELF Input: Load the ifttt.elf by clicking on Select ELF File.

   c. Boot arguments: Pass the following boot arguments:

.. code:: shell

      url=https://maker.ifttt.com/trigger/trigger_from_t2/with/key/c9ebSVVNGeSB1yi6NrVeyl,port=443,secured=1,method=get


..

   where,

i.   url: Webhooks end point URL

ii.  port: 443

iii. secured: 1 - Connecting to server without server verification

iv.  method: GET

d. Programming: Prog RAM or Prog Flash as per requirement.

Expected Output in IFTTT
~~~~~~~~~~~~~~~~~~~~~~~~~

When the application is run with a proper endpoint URL, an email is
received from IFTTT to the email address provided in the Email service
at the time of creating the applet.

.. code-block:: console

      Y-BOOT 208ef13 2019-07-22 12:26:54 -0500 790da1-b-7
      ROM yoda-h0-rom-16-0-gd5a8e586
      FLASH:PWWWWWWAE
      Build $Id: git-b61e4e6 $
      Flash detected. flash.hw.uuid: 39483937-3207-00a8-0068-ffffffffffff
      Bootargs: ssid=T2_test passphrase=1234567890 url=https://maker.ifttt.com/trigger/trigger_from_t2/with/key/c9ebSVVNGeSB1yi6NrVeyl port=443 secured=1 method=get
      $App:git-c8b579b
      SDK Ver: FREERTOS_SDK_1.0
      IFTTT Demo App
      
      Application Information:
      ------------------------
      Name       : IFTTT  Demo Application
      Version    : 2.0
      Build Date : Aug 23 2023
      Build Time : 07:01:34
      Heap Available: 310 KB (318456 Bytes)
      
      [APP]Bootparams :
      --------------------
      url=https://maker.ifttt.com/trigger/trigger_from_t2/with/key/c9ebSVVNGeSB1yi6NrVeyl
      path= 443
      secured= 1
      method= get
      ca_cert=<null>
      post_len=<null>
      use_ca_bundle = <null>
      [APP]Bootparams end here....
      
      [APP]Bootparams check done....ret = 0
      addr e0:69:3a:00:2c:5e
      network profile created for ssid: T2_test
      
      Connecting to added network : T2_test
      [2.743,596] DISCONNECTED
      wcm_notify_cb to App Layer - WCM_NOTIFY_MSG_DISCONNECT_DONE
      [2.828,346] CONNECT:22:69:2a:bb:6b:1c Channel:9 rssi:-54 dBm
      wcm_notify_cb to App Layer - WCM_NOTIFY_MSG_LINK_UP
      wcm_notify_cb to App Layer - WCM_NOTIFY_MSG_ADDRESS
      [4.553,648] MYIP 192.168.239.13
      [4.553,813] IPv6 [fe80::e269:3aff:fe00:2c5e]-link
      wcm_notify_cb to App Layer - WCM_NOTIFY_MSG_CONNECTED
      
      Connected to added network : T2_test
      
      [APP]Success: Connected to <null> N/w
      [APP]URL = https://maker.ifttt.com/trigger/trigger_from_t2/with/key/c9ebSVVNGeSB1yi6NrVeyl
        . [SSL_WRAP]Checking input configurations...
        . [SSL_WRAP]Seeding the random number generator...
        . [SSL_WRAP]Connecting to tcp maker.ifttt.com:443...
        . [SSL_WRAP]Setting up the SSL/TLS structure...
        . [SSL_WRAP]setting configurations..
              >auth mode = 0 (0- skip, 1- optional, 2- required
              >max fragment len = 0
              >Handshake timeout = 30 Sec
        . [SSL_WRAP]Performing the SSL/TLS handshake...
        . [SSL_WRAP] Handshake done. ok
        . [SSL_WRAP]Verifying peer X.509 certificate.
      
      [APP]Succes: HTTP connection done
      
      [APP]Response:
      55 ----------------------
      
      200
      Content-Type: text/html; charset=utf-8
      Content-Length: 55
      Connection: keep-alive
      Date: Wed, 23 Aug 2023 11:02:50 GMT
      ETag: W/"37-4jb44xEDYSdzHhse3E8QAYlkiaM"
      X-Clacks-Overhead: GNU Terry Pratchett
      X-Powered-By: Sad Unicorns
      X-Robots-Tag: none
      X-Top-Secrettt: VG9vIGVhc3k/IElmIHlvdSBjYW4gcmVhZCB0aGlzLCBFbWFpbCB1cyBhdCBqb2JzK3NlY3JldEBpZnR0dC5jb20uIFdlIHdhbnQgTWFrZXJzLg==
      X-Cache: Miss from cloudfront
      Via: 1.1 7d1975e97f05a3fc47c8f5eea10222bc.cloudfront.net (CloudFront)
      X-Amz-Cf-Pop: BOM78-P5
      X-Amz-Cf-Id: IjCwjm55RchOY7BzAM_Yvm5S8s9ysi4wB77DiKXlK7ckzS7BtmZU6A==
      [APP]Body:
      Congratulations! You've fired the trigger_from_t2 event
      [APP]Success
      
      [APP]------ Program Exit-------------

