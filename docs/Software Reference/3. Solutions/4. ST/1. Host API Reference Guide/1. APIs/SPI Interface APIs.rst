.. _st api spi interface:

SPI Interface APIs
------------------

hapi_spi_init
~~~~~~~~~~~~~

Registers the SPI.

.. code:: shell

      struct hapi* hapi_spi_init(void* hapi_spi_ptr, CS_HIGH_FN cs_hi, CS_LOW_FN cs_low, IF_TX_FN tx_fn, IF_RX_FN rx_fn)


Arguments:

1. hapi_spi_ptr: pointer to the HAPI SPI instance.

2. CS_HIGH_FN cs_hi: sets the CS to high.

3. CS_LOW_FN cs_low: resets the CS to low

4. IF_TX_FN tx_fn: transmission function.

5. IF_RX_FN rx_fn: Receiving function.

Return: True(1) on Success. False(0) on Error.

hapi_spi_cs_high
~~~~~~~~~~~~~~~~

Sets the CS to high before calling hapi_spi_init().

.. code:: shell

      void hapi_spi_cs_high() 


Arguments: None.

Return: None.

hapi_spi_cs_low
~~~~~~~~~~~~~~~

Resets the CS to low before calling hapi_spi_init().

.. code:: shell

      void hapi_spi_cs_low()  


Arguments: None.

Return: None.

hapi_spi_tx
~~~~~~~~~~~

Used for transmitting an amount of data in blocking mode.

.. code:: shell

      int hapi_spi_tx(void *ptr, char *buff, int len)


Arguments:

1. buff: pointer to character buffer.

2. len: length of the data.

Return: True on Success, False on Failure.

hapi_spi_rx
~~~~~~~~~~~

Used for receiving an amount of data in blocking mode.

.. code:: shell

      int hapi_spi_rx(void *ptr, char *buff, int len) 


Arguments:

1. buff: pointer to character buffer.

2. len: length of the data.

Return: True on Success, False on Failure.

hapi_spi_data_waiting
~~~~~~~~~~~~~~~~~~~~~

This function is used to inform HAPI that Talaria TWO wants to send data
to host. Talaria TWO will raise interrupt when data is to be sent to
host, and from host IRQ handler this function needs to be called.

.. code:: shell

      void hapi_spi_data_waiting()


Arguments: None.

Return: None.

hapi_spi_write
~~~~~~~~~~~~~~

Used to write data to SPI interface.

.. code:: shell

      ssize_t hapi_spi_write(void *dev, const void *data, size_t length)

Arguments:

1. hapi Pointer to HAPI context.

2. data: Pointer to data.

3. length: Length of data.

Return:

1. length: Length of data written.

hapi_spi_read
~~~~~~~~~~~~~

Used to read data from SPI interface.

.. code:: shell

      ssize_t hapi_spi_read(void *dev, void *data, size_t length)


Arguments:

1. hapi: Pointer to HAPI context.

2. data: Pointer to data.

3. length: Length of data.

Return:

1. length: Length of data read.

hapi_spi_multiple_slave_support_enable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Used to enable SPI master to support multiple SPI slaves.

.. code:: shell

      void hapi_spi_multiple_slave_support_enable(int enable, SPI_CS_DELAY cs_change_del_fn)


Arguments:

1. enable: Enable/Disable

   a. 1 – Enable

   b. 0 – Disable

2. SPI_CS_DELAY: To introduce additional delays to support communication
   with multiple SPI slaves

Return: None.
