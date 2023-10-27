Introduction 
=============

This document provides information on using the WebSocket client APIs
provided by the WebSocket module under components. This application
demonstrates using these APIs to connect to WebSocket servers in secured
(Secured WebSocket) and non-secured way.

The document also discusses ways to execute WebSocket GET and POST.

Features and Limitations
========================

The WebSocket implementation supports:

1. Secured and non-secured WebSocket client APIs

2. The server address can be either IP address or the host name (Domain
   Name)

3. APIs to send Text and Binary data

4. APIs for sending Close, Ping and Pong control packets

WebSocket/S APIs 
=================

WebSocket Open:
---------------

This is performed using the following API:

+-----------------------------------------------------------------------+
| websock_handle_t                                                      |
|                                                                       |
| websock_open(websock_config_t \*ws_cfg)                               |
+=======================================================================+
+-----------------------------------------------------------------------+

This API connects to the remote WebSocket server. The configuration
needed for the connection is passed using the following data structure:

+-----------------------------------------------------------------------+
| typedef struct {                                                      |
|                                                                       |
| char \*hostname;/\**<host name or the ip address of the server*/      |
|                                                                       |
| int port;/\**<port*/                                                  |
|                                                                       |
| char \*uri;/\**<Websocket uri/path to connect to*/                    |
|                                                                       |
| int secured; /\*secured websocket*/                                   |
|                                                                       |
| ssl_wrap_cfg_t ssl_config;                                            |
|                                                                       |
| int time_out;/\**<tcp connection timeout*/                            |
|                                                                       |
| /\**<The headers to be set in the WebSocket Handshake request.        |
|                                                                       |
| The format shall be "key:val". Use this to pass headers that are not  |
|                                                                       |
| set implicitly. Refer websock_open() for the list of headers set      |
|                                                                       |
| implicitly*/                                                          |
|                                                                       |
| websoc_hndshk_hdr_t hndshk_hdrs[WEBSOCK_MAX_HNDSHK_HDRS];             |
|                                                                       |
| int num_hndshk_hdrs;/\*\* Number of headers provided through,         |
|                                                                       |
| hndshk_hdrs[WEBSOCK_MAX_HNDSHK_HDRS]*/                                |
|                                                                       |
| } websock_config_t;                                                   |
+=======================================================================+
+-----------------------------------------------------------------------+

**Note**: If a URL is available in the form: ws://<domain
name>:port/<path>, use http_client_url_to_host() API to get the hostname
port and the path from the URL.

The \|Host\| \|Upgrade\|, \|Connection\|, \|Sec -Websocket-key\| and
\|Sec-websocket-Version\| headers are implicitly set by the
websock_Open() during the handshake. If any more headers need to be sent
during handshake, it needs to be passed using
hndshk_hdrs[WEBSOCK_MAX_HNDSHK_HDRS] in websock_config_t .

WebSocket Send
--------------

Once the connection is established using websock_open(), data can be
sent to the server using the following APIs:

+-----------------------------------------------------------------------+
| int                                                                   |
|                                                                       |
| websock_send_text(websock_handle_t handle, char \*payload, int len)   |
+=======================================================================+
+-----------------------------------------------------------------------+

+-----------------------------------------------------------------------+
| int                                                                   |
|                                                                       |
| websock_send_binary(websock_handle_t handle, char \*payload, int len) |
+=======================================================================+
+-----------------------------------------------------------------------+

websock_send_text is used for sending the Text frames (Opcode = 1).
websock_send_binary is used for sending Binary frames (Opcode = 2).

WebSocket Close:
----------------

A connection opened using websock_open() can be closed using the
following API:

+-----------------------------------------------------------------------+
| void                                                                  |
|                                                                       |
| websock_close(websock_handle_t h);                                    |
+=======================================================================+
+-----------------------------------------------------------------------+

PING and PONG
-------------

WebSocket provides Ping and Pong control packets to check and maintain
the connection. These packets can be sent using the following APIs:

+-----------------------------------------------------------------------+
| int                                                                   |
|                                                                       |
| websock_send_ping(websock_handle_t handle, char \*payload, int len);  |
+=======================================================================+
+-----------------------------------------------------------------------+

+-----------------------------------------------------------------------+
| int                                                                   |
|                                                                       |
| websock_send_pong(websock_handle_t handle, char \*payload, int len);  |
+=======================================================================+
+-----------------------------------------------------------------------+

Code Walkthrough
================

Application Flow
----------------

WebSocket is a communication protocol providing full duplex,
asynchronous communication between the connected endpoints.

Following are the steps:

1. Connect to Wi-Fi Network.

2. Connect to WebSocket server.

3. Send message to server.

4. Receive the message.

Sample Code Walkthrough
-----------------------

A user-defined data struct is created to store the data of the
Websocket:

+-----------------------------------------------------------------------+
| #define APP_NAME "WebSocket application"                              |
|                                                                       |
| #define APP_VERSION "2.0"                                             |
|                                                                       |
| OS_APPINFO {.stack_size = 4096};                                      |
|                                                                       |
| #define INPUT_PARAMETER_HOST "host"                                   |
|                                                                       |
| #define INPUT_PARAMETER_URL "url"                                     |
|                                                                       |
| #define INPUT_PARAMETER_PATH "path"                                   |
|                                                                       |
| #define INPUT_PARAMETER_PORT "port"                                   |
|                                                                       |
| #define INPUT_PARAMETER_SECURED "secured"                             |
|                                                                       |
| #define INPUT_PARAMETER_METHOD "method"                               |
|                                                                       |
| #define INPUT_PARAMETER_CA "ca_cert"                                  |
|                                                                       |
| #define INPUT_PARAMETER_POST_LEN "post_len"                           |
|                                                                       |
| #define INPUT_PARAMETER_CLIENT_CERT "client_cert"                     |
|                                                                       |
| #define INPUT_PARAMETER_CLIENT_KEY "client_key"                       |
|                                                                       |
| #define INPUT_PARAMETER_TEST_ITER "test_iterations"                   |
|                                                                       |
| #define INPUT_PARAMETER_USE_CA_BUNDLE "use_ca_bundle"                 |
|                                                                       |
| #define NULL_STR ""                                                   |
|                                                                       |
| struct param_t {                                                      |
|                                                                       |
| const char \*url;                                                     |
|                                                                       |
| const char \*host;                                                    |
|                                                                       |
| const char \*path;                                                    |
|                                                                       |
| const char \*port;                                                    |
|                                                                       |
| const char \*secured;                                                 |
|                                                                       |
| const char \*ca_cert;                                                 |
|                                                                       |
| const char \*client_cert;                                             |
|                                                                       |
| const char \*client_key;                                              |
|                                                                       |
| const char \*test_iterations;                                         |
|                                                                       |
| const char \*use_ca_bundle;                                           |
|                                                                       |
| };                                                                    |
|                                                                       |
| /\*CA certificate bundle*/                                            |
|                                                                       |
| extern uint8_t ca_bundle_start[] asm("\_binary_ca_bundle_start");     |
|                                                                       |
| extern uint8_t ca_bundle_end[] asm("\_binary_ca_bundle_end");         |
|                                                                       |
| struct param_t param;                                                 |
|                                                                       |
| char default_port[8];                                                 |
|                                                                       |
| char default_secured[8];                                              |
|                                                                       |
| struct os_semaphore app_wcm_lock;                                     |
|                                                                       |
| int wcm_connect_success = 0;                                          |
|                                                                       |
| static char host[128];                                                |
|                                                                       |
| static char path[128];                                                |
+=======================================================================+
+-----------------------------------------------------------------------+

Following boot arguments are passed in this application:

1. URL, port, secured, ca_cert, method, post_len, client_cert,
   client_key value and ca_bundle.

2. SD service type and proto, and action.

+-----------------------------------------------------------------------+
| static int                                                            |
|                                                                       |
| parse_boot_args(void)                                                 |
|                                                                       |
| {                                                                     |
|                                                                       |
| const char \*np_path;                                                 |
|                                                                       |
| int ret = 0;                                                          |
|                                                                       |
| sprintf(default_port, "%d", 80);                                      |
|                                                                       |
| sprintf(default_secured, "%d", 0);                                    |
|                                                                       |
| param.url = os_get_boot_arg_str(INPUT_PARAMETER_URL);                 |
|                                                                       |
| param.host = os_get_boot_arg_str(INPUT_PARAMETER_HOST);               |
|                                                                       |
| param.path = os_get_boot_arg_str(INPUT_PARAMETER_PATH);               |
|                                                                       |
| param.port = os_get_boot_arg_str(INPUT_PARAMETER_PORT);               |
|                                                                       |
| param.secured = os_get_boot_arg_str(INPUT_PARAMETER_SECURED);         |
|                                                                       |
| param.ca_cert = os_get_boot_arg_str(INPUT_PARAMETER_CA);              |
|                                                                       |
| param.client_cert = os_get_boot_arg_str(INPUT_PARAMETER_CLIENT_CERT); |
|                                                                       |
| param.client_key = os_get_boot_arg_str(INPUT_PARAMETER_CLIENT_KEY);   |
|                                                                       |
| param.test_iterations =                                               |
| os_get_boot_arg_str(INPUT_PARAMETER_TEST_ITER);                       |
|                                                                       |
| param.use_ca_bundle =                                                 |
| os_get_boot_arg_str(INPUT_PARAMETER_USE_CA_BUNDLE);                   |
+=======================================================================+
+-----------------------------------------------------------------------+

To connect to a Wi-Fi network, wcm_create()API from the Wi-Fi Connection
Manager is used. Initially, the Wi-Fi network interface is created using
wcm_create().

+-----------------------------------------------------------------------+
| h = wcm_create(NULL);                                                 |
+=======================================================================+
+-----------------------------------------------------------------------+

..

   wifi_connect_to_network()API, from components library, connects to
   the Wi-Fi network using the AP credentials provided.

+-----------------------------------------------------------------------+
| rval = wifi_connect_to_network(&h, WCM_CONN_WAIT_INFINITE,            |
| &wcm_connect_success);                                                |
|                                                                       |
| if(rval < 0) {                                                        |
|                                                                       |
| os_printf("\\nError: Unable to connect to network\\n");               |
|                                                                       |
| return 0;                                                             |
|                                                                       |
| }                                                                     |
+=======================================================================+
+-----------------------------------------------------------------------+

Here, the data structure websoc_config_t is used to pass the parameters
while opening a WebSocket connection with the remote server using the
websock_open API such as URL, port, secured, ca_cert, method, post_len,
client_cert, client_key value and ca_bundle.

+-----------------------------------------------------------------------+
| websock_config_t cfg = {0};                                           |
|                                                                       |
| websock_handle_t ws_handle;                                           |
|                                                                       |
| memset(&cfg, 0, sizeof(websock_config_t));                            |
|                                                                       |
| path[0]= '\\0';                                                       |
|                                                                       |
| if(param.url){                                                        |
|                                                                       |
| os_printf("\\n[APP]URL = %s", param.url);                             |
|                                                                       |
| rval = http_client_url_to_host(param.url, host, sizeof(host), path,   |
|                                                                       |
| sizeof(path), &cfg.port);                                             |
|                                                                       |
| if(rval < 0){                                                         |
|                                                                       |
| os_printf("\\n[APP]URL is not proper");                               |
|                                                                       |
| os_printf("\\n\\texample URLs:");                                     |
|                                                                       |
| os_printf("\\n\\t\\twss://echo.websocket.org/");                      |
|                                                                       |
| os_printf("\\n\\t\\tws://192.168.1.155:8000/");                       |
|                                                                       |
| }                                                                     |
|                                                                       |
| cfg.hostname = host;                                                  |
|                                                                       |
| cfg.uri = path;                                                       |
|                                                                       |
| os_printf("\\nuri/path = %s", cfg.uri);                               |
|                                                                       |
| }else{                                                                |
|                                                                       |
| cfg.hostname = (char \*)param.host;                                   |
|                                                                       |
| }                                                                     |
|                                                                       |
| if(param.port){/\*If specified explicietly, overide the port          |
| specified in URL*/                                                    |
|                                                                       |
| cfg.port = atoi(param.port);                                          |
|                                                                       |
| }                                                                     |
|                                                                       |
| cfg.secured = atoi(param.secured);                                    |
|                                                                       |
| if(cfg.secured) {                                                     |
|                                                                       |
| if(cfg.secured == 1){                                                 |
|                                                                       |
| cfg.ssl_config.auth_mode = SSL_WRAP_VERIFY_NONE;                      |
|                                                                       |
| }else{                                                                |
|                                                                       |
| cfg.ssl_config.auth_mode = SSL_WRAP_VERIFY_REQUIRED;                  |
|                                                                       |
| if(!param.use_ca_bundle \|\| !atoi(param.use_ca_bundle)){             |
|                                                                       |
| cfg.ssl_config.ca_cert.buf = utils_file_get(param.ca_cert,            |
|                                                                       |
| &cfg.ssl_config.ca_cert.len);                                         |
|                                                                       |
| if(NULL == cfg.ssl_config.ca_cert.buf){                               |
|                                                                       |
| os_printf("[APP]Error: No CA certificate found. Required");           |
|                                                                       |
| goto exit;                                                            |
|                                                                       |
| }                                                                     |
|                                                                       |
| }else if(atoi(param.use_ca_bundle)){                                  |
|                                                                       |
| /\*If use_ca_bundle is set, initialise CA bundle*/                    |
|                                                                       |
| os_printf("[APP]Initializing the ca bundle");                         |
|                                                                       |
| ssl_wrap_crt_bundle_init((const char \*)ca_bundle_start);             |
|                                                                       |
| }                                                                     |
|                                                                       |
| }                                                                     |
|                                                                       |
| if(param.client_cert && strlen(param.client_cert)){                   |
|                                                                       |
| cfg.ssl_config.client_cert.buf = utils_file_get(param.client_cert,    |
|                                                                       |
| &cfg.ssl_config.client_cert.len);                                     |
|                                                                       |
| if(NULL == cfg.ssl_config.client_cert.buf){                           |
|                                                                       |
| os_printf("Error: Could not open client certificate\\n");             |
|                                                                       |
| goto exit;                                                            |
|                                                                       |
| }                                                                     |
|                                                                       |
| }                                                                     |
|                                                                       |
| if(param.client_key && strlen(param.client_key)){                     |
|                                                                       |
| cfg.ssl_config.client_key.buf = utils_file_get(param.client_key,      |
|                                                                       |
| &cfg.ssl_config.client_key.len);                                      |
|                                                                       |
| if(NULL == cfg.ssl_config.client_key.buf){                            |
|                                                                       |
| os_printf("Error: Could not open client key\\n");                     |
|                                                                       |
| goto exit;                                                            |
|                                                                       |
| }                                                                     |
|                                                                       |
| }                                                                     |
|                                                                       |
| cfg.secured = 1;                                                      |
|                                                                       |
| }                                                                     |
|                                                                       |
| if(NULL != param.test_iterations){                                    |
|                                                                       |
| test_iterations = atoi(param.test_iterations);                        |
|                                                                       |
| if(0 == test_iterations)test_iterations = 1;                          |
|                                                                       |
| }                                                                     |
|                                                                       |
| os_printf("\\n*\* Test Iterations = %d \**\\n", test_iterations);     |
+=======================================================================+
+-----------------------------------------------------------------------+

This function opens a TCP socket to the server and performs the initial
HTTP-based handshake to upgrade to the WebSocket protocol. Both secure
(SSL) and non-secure WebSocket connections are supported.

Function websock_send_text is used to send “text” data over WebSocket
connection.

+-----------------------------------------------------------------------+
| websock_send_text(ws_handle,APP_MESSAGE, strlen(APP_MESSAGE));        |
+=======================================================================+
+-----------------------------------------------------------------------+

The data structure websock_msg_hdr_t is used to pass information about
the data received from the server.

Function websock_recv receives WebSocket messages. This internally
handles WebSocket close and ping messages.

+-----------------------------------------------------------------------+
| /\*Receive message*/                                                  |
|                                                                       |
| char recv_buf[128];                                                   |
|                                                                       |
| websock_msg_hdr_t msg_hdr;                                            |
|                                                                       |
| int recv_len = 128;                                                   |
|                                                                       |
| websock_recv(ws_handle, &msg_hdr,recv_buf,&recv_len,10);              |
|                                                                       |
| recv_buf[recv_len] = 0;                                               |
|                                                                       |
| os_printf("\\n[APP] Received Message = %s", recv_buf);                |
|                                                                       |
| exit:                                                                 |
|                                                                       |
| os_printf("\\n\\n[APP]------ Program Exit-------------\\n\\n");       |
|                                                                       |
| return 0;                                                             |
|                                                                       |
| }                                                                     |
+=======================================================================+
+-----------------------------------------------------------------------+

Running the Application 
========================

WebSocket Server Setup
----------------------

There is no specific server available in public domain for free testing
of the websockets. A local server is required to test the same. One of
the simple local server set-ups can be found at
https://github.com/dpallot/simple-websocket-server.

This is a Python based server with a Readme for setup instructions.

Programming Talaria TWO board with ELF
--------------------------------------

Program websock_client.elf(sdk_x.y\\examples\\websocket\\bin) using the
Download tool:

1. Launch the Download tool provided with InnoPhase Talaria TWO SDK.

2. In the GUI window:

   a. Boot Target: Select the appropriate EVK from the drop-down.

   b. ELF Input: Load the websock_client.elf by clicking on Select ELF
      File.

   c. Boot arguments: Pass the following boot arguments:

+-----------------------------------------------------------------------+
| url=ws://192.168.1.111/,port=8000,secured=0                           |
+=======================================================================+
+-----------------------------------------------------------------------+

..

   where,

i.   url: URL of the server to connect to

     1. *ws://<domain name OR ip address>:<port>/<path>* **or**

     2. *ws://<domain name OR ip address>/<path>*

ii.  port: Server port. Default - 80 in case of non-secured (WebSocket),
     443 in case of secured (Secured WebSocket)

iii. secured:

..

   0 - WebSocket,

   1 - Secured WebSocket without server verification

   2 - Secured WebSocket with server verification

iv. ca_cert: Certificate path in root FS in case of Secured WebSocket

d. Programming: Prog RAM or Prog Flash as per requirement.

For more details on using the Download tool, refer to the document:
UG_Download_Tool.pdf (path: *sdk_x.y/pc_tools/Download_Tool/doc*).

**Note**: x and y refer to the SDK release version. For example:
sdk_2.4/doc.

Expected Output
---------------

+-----------------------------------------------------------------------+
| ---------------PROG Flash: Start Time 05 Apr 2023 12:16:20 PM         |
| ------------                                                          |
|                                                                       |
| UART:SNWWWWAE                                                         |
|                                                                       |
| Build $Id: git-f1a4f00fb $                                            |
|                                                                       |
| hio.baudrate=921600                                                   |
|                                                                       |
| flash: Gordon ready!                                                  |
|                                                                       |
| [9.547,958] partitions mounted                                        |
|                                                                       |
| UART:SNWWWWAE                                                         |
|                                                                       |
| Build $Id: git-f1a4f00fb $                                            |
|                                                                       |
| hio.baudrate=921600                                                   |
|                                                                       |
| flash: Gordon ready!                                                  |
|                                                                       |
| Y-BOOT 208ef13 2019-07-22 12:26:54 -0500 790da1-b-7                   |
|                                                                       |
| ROM yoda-h0-rom-16-0-gd5a8e586                                        |
|                                                                       |
| FLASH:PNWWWWWAEBuild $Id: git-f1a4f00fb $                             |
|                                                                       |
| url=ws://192.168.0.166/ port=8000 secured=0                           |
| np_conf_path=/data/nprofile.json ssid=tplink_conf                     |
| passphrase=InnoQA2023$                                                |
|                                                                       |
| $App:git-6519235e                                                     |
|                                                                       |
| SDK Ver: sdk_2.6.3_alpha                                              |
|                                                                       |
| WebSocket Client Demo App                                             |
|                                                                       |
| Application Information:                                              |
|                                                                       |
| ------------------------                                              |
|                                                                       |
| Name : WebSocket application                                          |
|                                                                       |
| Version : 2.0                                                         |
|                                                                       |
| Build Date : Apr 3 2023                                               |
|                                                                       |
| Build Time : 20:57:22                                                 |
|                                                                       |
| Heap Available: 331 KB (339096 Bytes)                                 |
|                                                                       |
| [APP]Bootparams :                                                     |
|                                                                       |
| --------------------                                                  |
|                                                                       |
| url=ws://192.168.0.166/                                               |
|                                                                       |
| host= <null>                                                          |
|                                                                       |
| port=8000                                                             |
|                                                                       |
| path= <null>                                                          |
|                                                                       |
| secured= 0                                                            |
|                                                                       |
| ca_cert=<null>                                                        |
|                                                                       |
| test_iterations = <null>                                              |
|                                                                       |
| use_ca_bundle = <null>                                                |
|                                                                       |
| [APP]Bootparams end here....                                          |
|                                                                       |
| [APP]Bootparams check done....ret = 0                                 |
|                                                                       |
| addr e0:69:3a:00:0a:6a                                                |
|                                                                       |
| Connecting to added network : tplink_conf                             |
|                                                                       |
| [1.226,105] CONNECT:60:32:b1:3a:83:ee Channel:1 rssi:-55 dBm          |
|                                                                       |
| wcm_notify_cb to App Layer - WCM_NOTIFY_MSG_LINK_UP                   |
|                                                                       |
| wcm_notify_cb to App Layer - WCM_NOTIFY_MSG_ADDRESS                   |
|                                                                       |
| [2.324,746] MYIP 192.168.0.155                                        |
|                                                                       |
| [2.324,793] IPv6 [fe80::e269:3aff:fe00:a6a]-link                      |
|                                                                       |
| wcm_notify_cb to App Layer - WCM_NOTIFY_MSG_CONNECTED                 |
|                                                                       |
| Connected to added network : tplink_conf                              |
|                                                                       |
| [APP]URL = ws://192.168.0.166/                                        |
|                                                                       |
| uri/path = /                                                          |
|                                                                       |
| \*\* Test Iterations = 1 \*\*                                         |
|                                                                       |
| [APP]Calling websock_open(). heap size = 264272                       |
|                                                                       |
| [APP] Received Message = Hello World                                  |
|                                                                       |
| [APP]------ Program Exit-------------                                 |
+=======================================================================+
+-----------------------------------------------------------------------+
