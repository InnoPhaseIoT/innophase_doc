.. _3201 custom nw test:


Custom Network Test Application
-------------------------------

Description
~~~~~~~~~~~

Custom network test application (custom_nw) demonstrates the use of TCP
client in Talaria TWO, to execute the network test by establishing a TCP
connection to a remote Host in the network. Once Talaria TWO receives
data on TCP client socket from TCP server, it loops back the received
data.

This application also enables closing of the TCP connection.

Prerequisites
~~~~~~~~~~~~~

1. GTKTerm or similar application.

Command Description
~~~~~~~~~~~~~~~~~~~

Connect to an Access Point with the specified SSID and passphrase.

.. code:: shell

    $ ./conmgr connect <SSID> <passphrase>


Connect to a remote Host over TCP from Talaria TWO.

.. code:: shell

    # ./custom_nw cli <hostname> <port>         


where,

1. hostname – host-name/ipaddress of the remote Host.

2. Port – TCP server port number on the remote host.

Close TCP connection with remote Host.

.. code:: shell

    # ./custom_nw close      


Procedure
~~~~~~~~~

Execute the following operations on Talaria TWO:

Step 1: Connect Talaria TWO to the desired network by providing SSID and
passphrase.

Step 2: On a Windows Host machine, start TCP server on port 8080 using
Hercules application. This Host

machine should be connected to the same network as Talaria TWO.

Step 3: On Talaria TWO, start the TCP client socket on port 8080.

Step 4: Send data from Hercules application to Talaria TWO.

Expected Output
~~~~~~~~~~~~~~~

Host Console Logs
^^^^^^^^^^^^^^^^^

.. code:: shell

    pi@raspberrypi:~/dualstack_redesign/hapi $ ./dual_stack/bins/conmgr connect WifiVirus stonewall300
    Connected
    Status : Success
    pi@raspberrypi:~/dualstack_redesign/hapi $ ./dual_stack/bins/custom_nw cli 1 192.168.1.155 20022
    Status : Success
    pi@raspberrypi:~/dualstack_redesign/hapi $ ./dual_stack/bins/custom_nw close
    Status : Success


List of Message IDs Used
~~~~~~~~~~~~~~~~~~~~~~~~

This application demonstrates the use of custom Wi-Fi connection in
Dual-Stack custom applications and uses Group number 66. Following are
the message IDs used:

1. CUSTOM_NW_CLIENT_REQ

This message is sent to Talaria TWO to start the client. Talaria TWO
receives this message and replies with CUSTOM_NW_CLIENT_RSP.

2. CUSTOM_NW_CLOSE_REQ

This message is sent to Talaria TWO to close the client connection.
Talaria TWO receives this message and replies with CUSTOM_NW_CLOSE_RSP.

