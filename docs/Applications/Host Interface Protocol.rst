Introduction 
=============

The Host Interface Protocol (HIO) is a frame-based protocol between a
host and the Talaria TWO device. This protocol can be used over UART or
SPI transports. This application note covers the fundamentals of
developing HIO based application on both host and the Talaria TWO EVK.

HIO Protocol Overview
=====================

There are three types of messages:

1. A request sent from host to device.

2. A response message sent form device to host.

3. An indication message sent from device to host for asynchronous
   information such as Wi-Fi scan results or device wake-up
   notifications.

All requests are preceded by a header:

+-----------------------------------------------------------------------+
| struct hio_msghdr {                                                   |
|                                                                       |
| uint8_t group;                                                        |
|                                                                       |
| uint8_t msgid;                                                        |
|                                                                       |
| uint16_t trxid;                                                       |
|                                                                       |
| };                                                                    |
+=======================================================================+
+-----------------------------------------------------------------------+

where,

1. group: group identifier

2. msgid: message identifier

3. trxid: a number that can be used by the host to sequence requests (it
   is just returned in response messages)

The message header and body are preceded by a two-byte (little endian)
length of the header and body (excluding the length).

|Graphical user interface Description automatically generated with low
confidence|

Figure 1: HIO message framing

Sample Host application: hio_query
==================================

This basic application sends a hio_query_req to Talaria TWO and prints
the output of the response of Talaria TWO.

Programming Talaria TWO
-----------------------

For this sample application any existing Talaria TWO app with HIO
enabled such as the STW application is used:

+-----------------------------------------------------------------------+
| ./script/boot.py --device /dev/ttyUSB2 --reset=evk42_bl --speed       |
| 921600 ./apps/stw/bin/stw.elf                                         |
+=======================================================================+
+-----------------------------------------------------------------------+

Building the host application
-----------------------------

+-----------------------------------------------------------------------+
| cd sdk/examples/using_hio/hio_host                                    |
|                                                                       |
| make                                                                  |
+=======================================================================+
+-----------------------------------------------------------------------+

This generated the hio_query among other sample host applications.

Run hio_query
-------------

+-----------------------------------------------------------------------+
| ./hio_query /dev/ttyUSB2                                              |
+=======================================================================+
+-----------------------------------------------------------------------+

Expected host application output
--------------------------------

+-----------------------------------------------------------------------+
| Status: 0                                                             |
|                                                                       |
| Version: 0                                                            |
|                                                                       |
| Ngroups: 4                                                            |
|                                                                       |
| maxsize: 1020                                                         |
|                                                                       |
| fw_version: $Id: git-                                                 |
|                                                                       |
| patch_rev: $Patch: g                                                  |
|                                                                       |
| nmsg: 7 528 1288 2310                                                 |
+=======================================================================+
+-----------------------------------------------------------------------+

Sending an HIO message from host to Talaria TWO
-----------------------------------------------

To send a HIO message, send_command which is defined in hio_transport.c
is used:

+-----------------------------------------------------------------------+
| int send_command(int group_id, int msg_id, void \*data, int size, int |
| transid)                                                              |
|                                                                       |
| {                                                                     |
|                                                                       |
| int len;                                                              |
|                                                                       |
| char actual_pay_load[512] = {0,};                                     |
|                                                                       |
| struct hio_header_info header = { 0, };                               |
|                                                                       |
| header.groupid = group_id;                                            |
|                                                                       |
| header.msgid = msg_id;                                                |
|                                                                       |
| header.trandid = transid;                                             |
|                                                                       |
| len = sizeof(header) + size;                                          |
|                                                                       |
| header.len = len - 2;                                                 |
|                                                                       |
| if (data)                                                             |
|                                                                       |
| memcpy(actual_pay_load + sizeof(header), data, size);                 |
|                                                                       |
| memcpy(actual_pay_load, &header, sizeof(header));                     |
|                                                                       |
| return write_hio_message(actual_pay_load, len);                       |
|                                                                       |
| }                                                                     |
|                                                                       |
| int write_hio_message(char \*message, int msg_len) {                  |
|                                                                       |
| int bytes_written = 0;                                                |
|                                                                       |
| while (bytes_written < msg_len) {                                     |
|                                                                       |
| bytes_written += write(gfd, message + bytes_written, 1);              |
|                                                                       |
| }                                                                     |
|                                                                       |
| return bytes_written;                                                 |
|                                                                       |
| }                                                                     |
+=======================================================================+
+-----------------------------------------------------------------------+

hio_query.c

+-----------------------------------------------------------------------+
| …                                                                     |
|                                                                       |
| struct hio_query_req query_req;                                       |
|                                                                       |
| send_command(HIO_GROUP_HIO, HIO_QUERY_REQ, &query_req,                |
| sizeof(query_req), 0);                                                |
|                                                                       |
| ...                                                                   |
+=======================================================================+
+-----------------------------------------------------------------------+

Here, send_command is used and the HIO group, msgid, size of HIO req
structure, and trxid are specified.

After receiving this HIO message, Talaria TWO responds with another HIO
message to the host which has the same header as above. This header can
be used to identify the next action with the HIO message.

To handle the returning HIO message, a thread that reads the serial port
waiting for a valid HIO message is created.

hio_query.c

+-----------------------------------------------------------------------+
| static void\* hio_response_reader(void \*p) {                         |
|                                                                       |
| uint32_t msg_count = 0;                                               |
|                                                                       |
| while (!gExit) {                                                      |
|                                                                       |
| int read_count = 0;                                                   |
|                                                                       |
| uint32_t res_len;                                                     |
|                                                                       |
| char msg_len[4] = {0,};                                               |
|                                                                       |
| while(read_count < 2)                                                 |
|                                                                       |
| {                                                                     |
|                                                                       |
| read_count += read_hio_message(msg_len+read_count, 2-read_count);     |
|                                                                       |
| }                                                                     |
|                                                                       |
| msg_len[2] = 0x00;                                                    |
|                                                                       |
| msg_len[3] = 0x00;                                                    |
|                                                                       |
| res_len = msg_len[0] & 0x000000FF;                                    |
|                                                                       |
| if (msg_len[1] != 0) {                                                |
|                                                                       |
| res_len = ((uint8_t)msg_len[0]&0xFF) + (msg_len[1]<<8) & 0xFFFF;      |
|                                                                       |
| }                                                                     |
|                                                                       |
| sleep(0.2);                                                           |
|                                                                       |
| if(res_len > 0)                                                       |
|                                                                       |
| {                                                                     |
|                                                                       |
| char \*res_payload = malloc(res_len+1);                               |
|                                                                       |
| read_count = 0;                                                       |
|                                                                       |
| while(read_count < res_len)                                           |
|                                                                       |
| {                                                                     |
|                                                                       |
| read_count += read_hio_message((res_payload)+read_count,              |
| res_len-read_count);                                                  |
|                                                                       |
| }                                                                     |
|                                                                       |
| process_response(res_len, res_payload);                               |
|                                                                       |
| }                                                                     |
|                                                                       |
| }                                                                     |
|                                                                       |
| return NULL;                                                          |
|                                                                       |
| }                                                                     |
+=======================================================================+
+-----------------------------------------------------------------------+

There is also a function called process_response() that parses the
received response by its groupid and msgid.

+-----------------------------------------------------------------------+
| static void process_response(uint32_t res_len, char\* res_payload)    |
|                                                                       |
| {                                                                     |
|                                                                       |
| struct hio_res_header res_header = {0,};                              |
|                                                                       |
| memcpy(&res_header, res_payload, sizeof(struct hio_res_header));      |
|                                                                       |
| uint32_t payloadLength = res_len - sizeof(struct hio_res_header);     |
|                                                                       |
| char\* payload = malloc(payloadLength);                               |
|                                                                       |
| if(res_header.group_id == HIO_GROUP_HIO)                              |
|                                                                       |
| {                                                                     |
|                                                                       |
| switch(res_header.res_code)                                           |
|                                                                       |
| {                                                                     |
|                                                                       |
| case 0x80:                                                            |
|                                                                       |
| {                                                                     |
|                                                                       |
| struct hio_query_rsp \*rsp = malloc(sizeof(struct hio_query_rsp));    |
|                                                                       |
| memcpy(rsp, res_payload+sizeof(struct hio_res_header), sizeof(struct  |
| hio_query_rsp));                                                      |
|                                                                       |
| printf("Status: %d\\n", rsp->status);                                 |
|                                                                       |
| printf("Version: %d\\n", rsp->version);                               |
|                                                                       |
| printf("Ngroups: %d\\n", rsp->ngroups);                               |
|                                                                       |
| printf("maxsize: %d\\n", rsp->maxsize);                               |
|                                                                       |
| printf("fw_version: %s\\n", rsp->fw_rev);                             |
|                                                                       |
| printf("patch_rev: %s\\n", rsp->patch_rev);                           |
|                                                                       |
| uint16_t nmsg[rsp->ngroups];                                          |
|                                                                       |
| memcpy(nmsg, (res_payload+sizeof(struct hio_res_header)+sizeof(struct |
| hio_query_rsp)), (rsp->ngroups)*2);                                   |
|                                                                       |
| printf("nmsg: ");                                                     |
|                                                                       |
| for(int i = 0; i < rsp->ngroups; i++)                                 |
|                                                                       |
| {                                                                     |
|                                                                       |
| printf("%d ", nmsg[i]);                                               |
|                                                                       |
| }                                                                     |
|                                                                       |
| printf("\\n");                                                        |
|                                                                       |
| break;                                                                |
|                                                                       |
| }                                                                     |
|                                                                       |
| default:                                                              |
|                                                                       |
| break;                                                                |
|                                                                       |
| }                                                                     |
|                                                                       |
| }                                                                     |
|                                                                       |
| else                                                                  |
|                                                                       |
| {                                                                     |
|                                                                       |
| printf("Group Code: 0x%X\\n", res_header.group_id);                   |
|                                                                       |
| printf("Response Code: 0x%X\\n", res_header.res_code);                |
|                                                                       |
| printf("payload length: %d\\n", payloadLength);                       |
|                                                                       |
| printf("Payload: \\n" );                                              |
|                                                                       |
| for(int i = 0; i < payloadLength; i ++)                               |
|                                                                       |
| {                                                                     |
|                                                                       |
| printf("%X", \*(payload+i));                                          |
|                                                                       |
| }                                                                     |
|                                                                       |
| printf("\\n");                                                        |
|                                                                       |
| }                                                                     |
|                                                                       |
| }                                                                     |
+=======================================================================+
+-----------------------------------------------------------------------+

Creating custom HIO group and commands
======================================

Host side application
---------------------

To create custom set of commands, select an available groupid. The
highest possible groupid value is 0xFF. Each HIO message request,
response, and indication will need its own msgid. An appropriate
reference for this is: hio_custom_def.h

For this sample application, custom HIO command group with a single
request, response, and indication structure is created.

The sample application sends a ping message from the host and Talaria
TWO will send a HIO message response pong back to the host. An
indication to the host is sent every 5 seconds.

hio_custom_def.h

+-----------------------------------------------------------------------+
| #define HIO_GROUP_CUSTOM 0xFF                                         |
|                                                                       |
| #define CUSTOM_PING_REQ 0x00                                          |
|                                                                       |
| #define CUSTOM_PING_RSP 0x80                                          |
|                                                                       |
| #define CUSTOM_PING_IND 0xC0                                          |
|                                                                       |
| struct custom_ping_req {                                              |
|                                                                       |
| uint32_t msg_length;                                                  |
|                                                                       |
| char msg[0]; };                                                       |
|                                                                       |
| struct custom_ping_rsp {                                              |
|                                                                       |
| uint32_t cpr_status;                                                  |
|                                                                       |
| uint32_t msg_length;                                                  |
|                                                                       |
| char msg[0]; };                                                       |
|                                                                       |
| struct custom_ping_ind {                                              |
|                                                                       |
| uint32_t msg_len;                                                     |
|                                                                       |
| char msg[0]; };                                                       |
+=======================================================================+
+-----------------------------------------------------------------------+

Here, custom HIO group with a single req, rsp, and ind structure is
created.

hio_custom.c

+-----------------------------------------------------------------------+
| …                                                                     |
|                                                                       |
| int main(int argc, char \*argv[])                                     |
|                                                                       |
| {                                                                     |
|                                                                       |
| int ping_req_count = 0;                                               |
|                                                                       |
| if (init_hio_transport(argv[1]) < 0) {                                |
|                                                                       |
| printf("Failed to open serial device %s\\n", argv[1]);                |
|                                                                       |
| return -1;                                                            |
|                                                                       |
| }                                                                     |
|                                                                       |
| pthread_t thread_id;                                                  |
|                                                                       |
| pthread_create(&thread_id, NULL, hio_response_reader, NULL);          |
|                                                                       |
| uint16_t trxid = 0;                                                   |
|                                                                       |
| char\* msg = "ping";                                                  |
|                                                                       |
| uint32_t index = 0;                                                   |
|                                                                       |
| for(ping_req_count = 0;ping_req_count < 10;ping_req_count++)          |
|                                                                       |
| {                                                                     |
|                                                                       |
| struct custom_ping_req \*ping_req = malloc(sizeof(struct              |
| custom_ping_req) + strlen(msg) + 1);                                  |
|                                                                       |
| ping_req->msg_length = strlen(msg);                                   |
|                                                                       |
| memset(ping_req->msg,0, ping_req->msg_length+1);                      |
|                                                                       |
| memcpy(ping_req->msg, msg, ping_req->msg_length);                     |
|                                                                       |
| send_command(HIO_GROUP_CUSTOM, CUSTOM_PING_REQ, ping_req,             |
| sizeof(struct custom_ping_req) + strlen(msg), trxid++);               |
|                                                                       |
| printf("\***Sending ping request from host:%u*******\\r\\n",index);   |
|                                                                       |
| index++;                                                              |
|                                                                       |
| sleep(1);                                                             |
|                                                                       |
| free(ping_req);                                                       |
|                                                                       |
| sleep(2);                                                             |
|                                                                       |
| …                                                                     |
+=======================================================================+
+-----------------------------------------------------------------------+

Like the hio_query example, send_command()is used to send a HIO message
to Talaria TWO.

To process the HIO message response from Talaria TWO, the groupid and
msgid are added to process_response method which processes the HIO
messages.

+-----------------------------------------------------------------------+
| …                                                                     |
|                                                                       |
| else if(res_header.group_id == HIO_GROUP_CUSTOM)                      |
|                                                                       |
| {                                                                     |
|                                                                       |
| switch(res_header.res_code)                                           |
|                                                                       |
| {                                                                     |
|                                                                       |
| case 0x80:                                                            |
|                                                                       |
| {                                                                     |
|                                                                       |
| struct custom_ping_rsp \*ping_rsp = malloc(payloadLength);            |
|                                                                       |
| memcpy(ping_rsp, res_payload+sizeof(struct hio_res_header),           |
| payloadLength);                                                       |
|                                                                       |
| printf("Status: %u\\n", ping_rsp->cpr_status);                        |
|                                                                       |
| printf("Message: %s\\n\\n", ping_rsp->msg);                           |
|                                                                       |
| free(ping_rsp);                                                       |
|                                                                       |
| break;                                                                |
|                                                                       |
| }                                                                     |
|                                                                       |
| case 0xC0:                                                            |
|                                                                       |
| {                                                                     |
|                                                                       |
| struct custom_ping_ind \*ping_ind = malloc(payloadLength);            |
|                                                                       |
| memcpy(ping_ind, res_payload+sizeof(struct hio_res_header),           |
| payloadLength);                                                       |
|                                                                       |
| printf("\***Received custom_ping_ind***\\n");                         |
|                                                                       |
| printf("Message: %s\\n\\n", ping_ind->msg);                           |
|                                                                       |
| free(ping_ind);                                                       |
|                                                                       |
| break;                                                                |
|                                                                       |
| }                                                                     |
|                                                                       |
| case 0xC2:                                                            |
|                                                                       |
| {                                                                     |
|                                                                       |
| struct custom_datafromt2_ind \*t2data_ind = malloc(payloadLength);    |
|                                                                       |
| memcpy(t2data_ind, res_payload+sizeof(struct hio_res_header),         |
| payloadLength);                                                       |
|                                                                       |
| printf("\***Received t2data_ind***\\n");                              |
|                                                                       |
| printf("Message: %s\\n\\n", t2data_ind->msg);                         |
|                                                                       |
| free(t2data_ind);                                                     |
|                                                                       |
| break;                                                                |
|                                                                       |
| }                                                                     |
|                                                                       |
| default:                                                              |
|                                                                       |
| break;                                                                |
|                                                                       |
| }                                                                     |
|                                                                       |
| }                                                                     |
|                                                                       |
| …                                                                     |
+=======================================================================+
+-----------------------------------------------------------------------+

Talaria TWO Application
-----------------------

As with the host side application, there is also a need to specify the
grpid and msgid to create custom set of commands and the req, rsp, ind
structures. They are defined in hio_custom_def.h.

Before using any HIO commands, first register them using hio_api_init
and create custom hio_api stuct.

+-----------------------------------------------------------------------+
| …                                                                     |
|                                                                       |
| static const struct hio_api custom_api = {                            |
|                                                                       |
| .group = HIO_GROUP_CUSTOM,                                            |
|                                                                       |
| .num_handlers = 2,                                                    |
|                                                                       |
| .handler = {                                                          |
|                                                                       |
| custom_ping,                                                          |
|                                                                       |
| custom_datafromhost,                                                  |
|                                                                       |
| NULL,                                                                 |
|                                                                       |
| }                                                                     |
|                                                                       |
| };                                                                    |
|                                                                       |
| …                                                                     |
|                                                                       |
| int                                                                   |
|                                                                       |
| int main(void)                                                        |
|                                                                       |
| {                                                                     |
|                                                                       |
| os_printf("Custom HIO api\\n");                                       |
|                                                                       |
| if(hio_api_register(&custom_api, NULL) == 0){                         |
|                                                                       |
| os_printf("Successfully registered HIO message group\\r\\n");         |
|                                                                       |
| }else{                                                                |
|                                                                       |
| os_printf("Failed to register HIO message group\\r\\n");              |
|                                                                       |
| }                                                                     |
|                                                                       |
| while (true) {                                                        |
|                                                                       |
| os_msleep(5000);                                                      |
|                                                                       |
| os_printf("Available heap:%d\\r\\n",os_avail_heap());                 |
|                                                                       |
| }                                                                     |
|                                                                       |
| return 0;                                                             |
|                                                                       |
| }                                                                     |
|                                                                       |
| …                                                                     |
+=======================================================================+
+-----------------------------------------------------------------------+

In this code, the struct custom_api contains the handlers for each of
the HIO message request to be received. The first handler, custom_ping,
coincides with HIO message req with msgid = 0x00 and if there is a
second one it will be msgid= 0x01.

Since each handler coincides with a HIO message request, this is also
where HIO message response would be sent back. This can be done with
hio_write_msg or hio_response_status if status value needs to be
returned.

+-----------------------------------------------------------------------+
| static struct packet\* custom_ping(void \*ctx, struct packet \*msg)   |
|                                                                       |
| { uint32_t status = 0;                                                |
|                                                                       |
| struct custom_ping_req\* ping_req = packet_data(msg);                 |
|                                                                       |
| uint32_t msg_length = ping_req->msg_length;                           |
|                                                                       |
| struct pfrag \*frag = NULL;                                           |
|                                                                       |
| os_printf("Got ping req: %.*s \\n",msg_length, ping_req->msg);        |
|                                                                       |
| char\* pong = "pong";                                                 |
|                                                                       |
| uint32_t pong_length = strlen(pong);                                  |
|                                                                       |
| struct packet \*rsp;                                                  |
|                                                                       |
| frag = pfrag_alloc(pong_length);                                      |
|                                                                       |
| memcpy(pfrag_insert_tail(frag,pong_length), pong, pong_length);       |
|                                                                       |
| rsp = create_custom_ping_rsp(pong_length, status);                    |
|                                                                       |
| packet_add_frag(rsp, frag);                                           |
|                                                                       |
| hio_write_msg(rsp, HIO_GROUP_CUSTOM , CUSTOM_PING_RSP, 0);            |
|                                                                       |
| return NULL;                                                          |
|                                                                       |
| }                                                                     |
+=======================================================================+
+-----------------------------------------------------------------------+

Run custom HIO Sample applications
----------------------------------

1. Build Talaria TWO sample application

+-----------------------------------------------------------------------+
| cd sdk/examples/using_hio                                             |
|                                                                       |
| make                                                                  |
+=======================================================================+
+-----------------------------------------------------------------------+

..

   This should generate t2_hio_custom.elf.

2. Programming the Talaria TWO

+-----------------------------------------------------------------------+
| cd sdk                                                                |
|                                                                       |
| ./script/boot.py --device /dev/ttyUSB2 --reset=evk42_bl --speed       |
| 921600 ./examples/using_hio/bin/t2_hio_custom.elf                     |
+=======================================================================+
+-----------------------------------------------------------------------+

3. Build the Host application

+-----------------------------------------------------------------------+
| cd sdk/examples/using_hio/hio_host                                    |
|                                                                       |
| make                                                                  |
+=======================================================================+
+-----------------------------------------------------------------------+

4. Run the Host application

+-----------------------------------------------------------------------+
| ./hio_custom /dev/ttyUSB2                                             |
+=======================================================================+
+-----------------------------------------------------------------------+

5. Expected Output

a. Talaria TWO output:

+-----------------------------------------------------------------------+
| Got ping req: ping                                                    |
|                                                                       |
| Sent ping Response                                                    |
|                                                                       |
| Got data: InnoPhase is a fabless semiconductor company specializing   |
| in extreme low power wireless solutions. The company s developed the  |
| industry’s first digital PolaRFusion radio architecture to shatter    |
| the low power barrier of wireless communications. Combining this      |
| groundbreaking RF signal processing Technology with embedded          |
| processing will enable our company to revolutionize the IoT           |
| edge-computing industry. …                                            |
+=======================================================================+
+-----------------------------------------------------------------------+

b. Host application output:

+-----------------------------------------------------------------------+
| Received custom_ping_rsp                                              |
|                                                                       |
| Status: 0                                                             |
|                                                                       |
| Message: pong                                                         |
|                                                                       |
| Received custom_ping_rsp                                              |
|                                                                       |
| Status: 0                                                             |
|                                                                       |
| Message: pong                                                         |
|                                                                       |
| Received custom_ping_rsp                                              |
|                                                                       |
| Status: 0                                                             |
|                                                                       |
| Message: pong                                                         |
|                                                                       |
| Received custom_ping_rsp                                              |
|                                                                       |
| Status: 0                                                             |
|                                                                       |
| Message: pong                                                         |
+=======================================================================+
+-----------------------------------------------------------------------+

.. |Graphical user interface Description automatically generated with low confidence| image:: media/image1.png
   :width: 7.08661in
   :height: 1.28436in
