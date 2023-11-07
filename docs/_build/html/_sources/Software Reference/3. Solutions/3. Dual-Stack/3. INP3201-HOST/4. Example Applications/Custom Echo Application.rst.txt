Custom Echo Application
-----------------------

Description
~~~~~~~~~~~

Custom echo (custom_echo) can be used to monitor the host interface
(UART/SPI/SDIO) transactions. In this application, host sends data to
which Talaria TWO responds with same data or data with inverted case.

Prerequisites
~~~~~~~~~~~~~

GTKTerm or similar application.

Command Description with Procedure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Open a serial terminal and navigate to the directory where custom
applications are placed and issue the commands in the following sequence
to send the text to Talaria TWO and get a response for it.

Send <text_to_send> to Talaria TWO. Talaria TWO responds with the same
data.

+-----------------------------------------------------------------------+
| $ ./custom_echo <text_to_send>                                        |
+=======================================================================+
+-----------------------------------------------------------------------+

Send <text_to_send> to Talaria TWO. Talaria TWO responds with data in
inverted case.

[1=invert case \| 0=don’t invert case]

+-----------------------------------------------------------------------+
| $ ./custom_echo <text_to_send>                                        |
+=======================================================================+
+-----------------------------------------------------------------------+

Expected Output
~~~~~~~~~~~~~~~

Host Console Logs
^^^^^^^^^^^^^^^^^

|A screenshot of a computer program Description automatically generated|

Figure 1: custom_echo – host serial log

Host console log – text output:

+-----------------------------------------------------------------------+
| # ./custom_echo innophase 0                                           |
|                                                                       |
| Resp status: 0                                                        |
|                                                                       |
| Resp len: 9                                                           |
|                                                                       |
| Resp data: innophase                                                  |
|                                                                       |
| Status : Success                                                      |
|                                                                       |
| # ./custom_echo innophase 1                                           |
|                                                                       |
| Resp status: 0                                                        |
|                                                                       |
| Resp len: 9                                                           |
|                                                                       |
| Resp data: INNOPHASE                                                  |
|                                                                       |
| Status : Success                                                      |
|                                                                       |
| #                                                                     |
+=======================================================================+
+-----------------------------------------------------------------------+

List of Message IDs Used
~~~~~~~~~~~~~~~~~~~~~~~~

This application uses two message IDs and Group number 67:

1. CUSTOM_ECHO_ECHO_REQ

This message is sent to Talaria TWO when application is invoked with
invert as 0. By default, invert is false. Talaria TWO receives this
message and replies with CUSTOM_ECHO_ECHO_RSP, with same data.

2. CUSTOM_ECHO_ECHO_INVERTED_REQ

This message is sent to Talaria TWO when application is invoked with
invert as 1. Talaria TWO receives this message and replies with
CUSTOM_ECHO_ECHO_INVERTED_RSP, with inverted case data.

.. |A screenshot of a computer program Description automatically generated| image:: media/image1.png
   :width: 3.93681in
   :height: 3.29306in
