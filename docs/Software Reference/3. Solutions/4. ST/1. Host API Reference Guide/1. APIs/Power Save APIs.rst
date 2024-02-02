.. _st api power-save:

Power Save APIs
~~~~~~~~~~~~~~~

hapi_send_sleep
^^^^^^^^^^^^^^^

Requests to enable sleep in Talaria TWO.

.. code:: shell

    void hapi_send_sleep(struct hapi *hapi)


Arguments:

1. hapi: HAPI instance pointer.

Return: None.

hapi_set_sleep_del
^^^^^^^^^^^^^^^^^^

Provides a delay after initiating sleep.

.. code:: shell

    void hapi_set_sleep_del(struct hapi *hapi, int usecs)   


Arguments:

1. hapi: HAPI instance pointer.

2. usecs: delay in microseconds.

Return: None.

hapi_t2_wakeup_config
~~~~~~~~~~~~~~~~~~~~~

Used for configuring the Talaria TWO pins.

.. code:: shell

    void hapi_t2_wakeup_config(void *hapi, uint8_t type)  


Arguments:

1. hapi: pointer to HAPI.

2. type: wake-up type.

Return: None.

hapi_spi_t2_wakeup_fn
~~~~~~~~~~~~~~~~~~~~~

Used to wake-up the SPI function in Talaria TWO.

.. code:: shell

    void hapi_spi_t2_wakeup_fn(void *hapi, void *wakeup_t2);    


Arguments:

1. hapi: pointer to HAPI.

2. wakeup_t2: pointer to wakeup_t2 through spi

Return: None.

hapi_uart_t2_wakeup_fn
~~~~~~~~~~~~~~~~~~~~~~

Used to wake-up the UART function in Talaria TWO.

.. code:: shell

    void hapi_uart_t2_wakeup_fn(void *hapi, void *wakeup_t2);   


Arguments:

1. hapi: pointer to HAPI.

2. wakeup_t2: pointer to wakeup_t2 through uart

Return: None.
