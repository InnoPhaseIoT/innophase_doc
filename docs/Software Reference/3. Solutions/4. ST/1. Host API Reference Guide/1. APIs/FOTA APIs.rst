.. _st api fota:

FOTA APIs 
~~~~~~~~~~

hapi_fota_start 
^^^^^^^^^^^^^^^^

Starts Firmware Over the Air Upgrade.

.. code:: shell

    bool hapi_fota_start(struct hapi *hapi_p,uint32_t check_for_update,uint32_t auto_reset)


Arguments:

1. hapi_p: HAPI instance pointer.

2. check_for_update: Check for update.

3. auto_reset: Reset Talaria TWO after FOTA is successful.

Return: Status of FOTA start function. True=Success, False otherwise.

hapi_fota_cfgadd 
^^^^^^^^^^^^^^^^^

Sends Firmware Over-The-Air configuration data.

.. code:: shell

    bool hapi_fota_cfgadd(struct hapi *hapi_p, uint32_t data_len, char* data)


Arguments:

1. hapi_p: HAPI instance pointer.

2. data_len: Length of the configuration data.

3. data: Configuration file data.

Return: Status of sending configuration data. True=Success, False
otherwise.
