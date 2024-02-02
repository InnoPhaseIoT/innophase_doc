.. _st api fos:

FOS APIs 
~~~~~~~~~

hapi_fos_start 
^^^^^^^^^^^^^^^

Starts Firmware upgrade Over Serial.

.. code:: shell

    bool hapi_fos_start(struct hapi *hapi_p,char *fw_name, char *fw_hash,uint32_t  image_size,uint32_t auto_reset)


Arguments:

1. hapi_p: HAPI instance pointer.

2. fw_name: Name of the firmware as specified in the part.json file.

3. fw_hash: sha256 hash of the image being downloaded.

4. image_size: Size of the image.

5. auto_reset: Reset Talaria TWO after FOTA is successful.

Return: Status of firmware upgrade. True=Success, False otherwise.

hapi_fos_image_send 
^^^^^^^^^^^^^^^^^^^^

Sends Firmware upgrade Over Serial configuration data.

.. code:: shell

    bool hapi_fos_image_send(struct hapi *hapi_p,uint32_t data_len, char* data)


Arguments:

1. hapi_p: HAPI instance pointer.

2. data_len: Configuration data length.

3. data: Pointer to configuration data.

Return: Status of sending firmware configuration data. True=Success,
False otherwise.

hapi_fos_commit 
^^^^^^^^^^^^^^^^

Executes Firmware upgrade Over Serial commit. This marks the end of
image data and Talaria TWO will set the newly downloaded image as the
boot image.

.. code:: shell

    bool hapi_fos_commit(struct hapi *hapi_p) 


Arguments:

1. hapi_p: HAPI instance pointer.

Return: Status FOS commit. True=Success, False otherwise.
