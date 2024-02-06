.. _st api uart interface:

UART Interface APIs
-------------------

hapi_uart_init
~~~~~~~~~~~~~~

Initializes the UART interface.

.. code:: shell

    struct hapi*  hapi_uart_init(void* hapi_uart_ptr, IF_TX_FN tx_fn, IF_RX_FN rx_fn, IF_ERR_FN err_fn, IF_UART_INIT uart_init)


Arguments:

1. hapi_uart_ptr: pointer to the HAPI UART instance.

2. IF_TX_FN tx_fn: transmitter function.

3. TF_RX_FN rx_fn: receiver function.

4. IF_ERR_FN err_fn: Error function.

5. IF_UART_INIT uart_init: UART initialization.

Return: HAPI instance on Success and NULL on Failure.

hapi_uart_tx
~~~~~~~~~~~~

Used for transmitting an amount of data in blocking mode in the UART
interface.

.. code:: shell

    int hapi_uart_tx(void *ptr, char *buff, int len)   


Arguments:

1. buff: pointer to character buff.

2. len: length of the data to be transmitted.

Return: on Success returns the number of bytes transmitted and -1 on
failure.

hapi_uart_rx
~~~~~~~~~~~~

Used for Receiving an amount of data in blocking mode.

.. code:: shell

    int hapi_uart_tx(void *ptr, char *buff, int len)  


Arguments:

1. buff: pointer to character buff.

2. len: length of the data to be received.

Return: on Success returns number of bytes received else -1 on failure.

hapi_uart_read
~~~~~~~~~~~~~~

Used to read data from UART interface.

.. code:: shell

    ssize_t hapi_uart_read(void *dev, void *data, size_t length)  


Arguments:

1. hapi Pointer to HAPI context.

2. data: Pointer to data.

3. length: Length of data to be read in bytes.

Return:

1. length: Number of bytes read.

hapi_uart_write
~~~~~~~~~~~~~~~

Used to write data to UART interface.

.. code:: shell

    ssize_t hapi_uart_write(void *dev, void *data, size_t length) 


Arguments:

1. hapi: Pointer to HAPI context.

2. data: Pointer to data.

3. length: Length of data to be written in bytes.

Return:

1. length: Number of bytes of data written.
