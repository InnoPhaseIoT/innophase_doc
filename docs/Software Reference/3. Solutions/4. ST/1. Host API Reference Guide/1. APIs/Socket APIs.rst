.. _st api socket:

Socket APIs
~~~~~~~~~~~

socket_create
^^^^^^^^^^^^^

Creates a socket according to the parameter passed.

.. code:: shell

      int socket_create(struct hapi *hapi, int proto, char *server, char *port)


Arguments:

1. hapi: HAPI instance pointer

2. proto: specifies the protocol used for the socket to create. The
   valid combinations are TCP client, UDP client, TCP server and UDP
   server

3. tcp_client=0, tcp_server=1, udp_client=2, udp_server=3, raw=4.

4. server: The server URL for the TCP or UDP client connection

5. port: the port number to connect. If the proto is TCP/UDP server this
   is the port on which the Talaria TWO waits for connection

Return: Socket descriptor on Success or -1 on Failure.

hapi_socket_send_tcp
^^^^^^^^^^^^^^^^^^^^

Used to send data on a TCP socket.

.. code:: shell

      bool hapi_sock_send_tcp(struct hapi *hapi, uint32_t socket, const void *data, size_t len)


Arguments:

1. hapi: HAPI instance pointer

2. socket: The socket ID which has been created

3. data: The data to be sent on the socket

4. len: The length of the data to be sent

Return: True(1) on Success. False(0) on Error

hapi_sock_send_udp
^^^^^^^^^^^^^^^^^^

Used to send data on a UDP socket.

.. code:: shell

      bool hapi_sock_send_udp(struct hapi *hapi, uint32_t socket, uint32_t *addr, uint16_t port, uint16_t addrlen, const void *data, size_t len)


Arguments:

1. hapi: HAPI instance pointer

2. socket: The socket ID which has been created

3. addr: destination IP address

4. port: destination port

5. addrlen: size of the address IPv4(4)/IPv6(16)

6. data: The data to be sent on the socket

7. len: The length of the data to be sent

Return: True(1) on Success. False(0) on Error

hapi_socket_receive
^^^^^^^^^^^^^^^^^^^

Used to receive data from a socket.

.. code:: shell

      size_t hapi_socket_receive(struct hapi *hapi, uint32_t socket, void *data, size_t len)


Arguments:

1. hapi: HAPI instance pointer.

2. socket: The socket ID which has been created.

3. data: The data pointer on which the data is to be received from the
   socket.

4. len: The length of the data to be received.

Return: The length of the actual data received.

hapi_socket_getavailable
^^^^^^^^^^^^^^^^^^^^^^^^

Used to check received data available on a socket.

.. code:: shell

      int hapi_socket_getavailable(struct hapi \*hapi, uint32_t socket)     


Arguments:

1. hapi: HAPI instance pointer.

2. socket: The socket ID which has been created.

Return: The length of the data available on the socket which can be
read.

hapi_sock_notify
^^^^^^^^^^^^^^^^

Registers notification for socket creation.

.. code:: shell

      bool hapi_sock_notify(struct hapi *hapi, uint32_t socket, uint32_t threshold, uint32 flags)


Arguments:

1. hapi: HAPI instance pointer.

2. socket: The socket ID which has been created.

3. threshold: Threshold of data

4. flags: To read flags

   a. SOCKET_EVENT (Default):

..

   Data packet(s) of N bytes will arrive to the RX socket at any time.

b. SOCKET_POLL:

..

   Data packet(s) with indication of N bytes available will be sent at
   any time. Receiver needs to use REQ/RSP to get the available data
   from buffer.

Return: Whether socket notification indication request was Successful.
0=Success, non-zero otherwise.

hapi_socket_close
^^^^^^^^^^^^^^^^^

Used to close a socket which has been opened.

.. code:: shell

      void hapi_socket_close(struct hapi *hapi, uint32_t socket)  


Arguments:

1. hapi: HAPI instance pointer.

2. socket: The socket ID which has been created.

Return: None.

hapi_sock_getavailable
^^^^^^^^^^^^^^^^^^^^^^

Gets the number of bytes available to read in a socket.

.. code:: shell

      int hapi_sock_getavailable(struct hapi *hapi, uint32_t socket)    

Arguments:

1. hapi: HAPI pointer to HAPI context.

2. socket: Socket handle.

Return: Number of bytes available at socket to read.

hapi_sock_burst_send
^^^^^^^^^^^^^^^^^^^^

Writes multiple packets of data bytes into the socket.

.. code:: shell

      bool hapi_sock_burst_send(struct hapi *hapi, uint32_t socket, uint32_t *addr, uint16_t port, uint16_t addrlen, uint32_t num_pkt, const void *data, size_t len)


Arguments:

1. hapi: HAPI pointer to HAPI context.

2. socket: Socket handle.

3. addr: Destination IP address.

4. port: Port destination.

5. addrlen: Size of the address IPv4(4)/IPv6(16).

6. num_packets: Number of packets to send to the socket.

7. data: Data to be sent.

8. len: Length of data.

Return: Socket send was Successful. True=Success, False otherwise.

hapi_sock_burst_receive
^^^^^^^^^^^^^^^^^^^^^^^

Reads multiple packets up to the size of the data bytes from the socket.

.. code:: shell

      size_t hapi_sock_burst_receive(struct hapi *hapi, uint32_t socket, void *data, size_t len, int *status, int *flags)

Arguments:

1. socket: Socket descriptor.

2. size: Number of bytes to receive.

3. flags: Reserved for future use.

Return:

1. num_pks: Number of packets to send to the socket.

hapi_sock_close
^^^^^^^^^^^^^^^

Closes the socket.

.. code:: shell

      bool hapi_sock_close(struct hapi *hapi, uint32_t socket)  


Arguments:

1. hapi: Pointer to HAPI context.

2. socket: Specified socket handle.

Return: Socket close status. True=Success, False otherwise.

hapi_sock_receive
^^^^^^^^^^^^^^^^^

Receives data on socket.

.. code:: shell

      size_t hapi_sock_receive(struct hapi *hapi, uint32_t socket, void *data, size_t len)


Arguments:

1. hapi: Pointer to HAPI context.

2. socket: Socket handle.

3. data: Received data.

4. len: Length of the received data.

Return: Number of bytes of data received.
