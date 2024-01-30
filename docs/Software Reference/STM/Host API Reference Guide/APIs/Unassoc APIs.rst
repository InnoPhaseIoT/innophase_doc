Unassoc APIs
------------

hapi_unassoc_create
~~~~~~~~~~~~~~~~~~~

Creates the unassociation.

+-----------------------------------------------------------------------+
| bool hapi_unassoc_create(struct hapi \*hapi, uint8_t \*addr);         |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi: instance of pointer.

2. addr: pointer to address

Return: True(1) on Success. False(0) on Error.

hapi_unassoc_config
~~~~~~~~~~~~~~~~~~~

For configuring the parameters of unassociation in HAPI.

+-----------------------------------------------------------------------+
| bool hapi_unassoc_config(struct hapi \*hapi,                          |
|                                                                       |
| uint32_t num_probes, uint32_t interval_ms, uint32_t verbose,          |
|                                                                       |
| char \*ssid, uint32_t rate, uint32_t suspend_en,                      |
|                                                                       |
| uint8_t ie_len, uint8_t \*ie);                                        |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi: instance of the pointer.

2. num_probes: number of probes used.

3. interval_ms: interval in ms.

4. verbose: number of verbose.

5. ssid: SSID used for configuration.

6. rate: rate used for the unassociation configuration.

7. suspend_en: suspend encryption.

8. ie_len: length of optional, additional information elements included
   in the probe request frames.

9. ie: length

Return: True(1) on Success. False(0) on Error.

hapi_unassoc_start
~~~~~~~~~~~~~~~~~~

To start un-association in HAPI.

+-----------------------------------------------------------------------+
| bool hapi_unassoc_start(struct hapi \*hapi)                           |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi: Pointer to HAPI context.

Return: True(1) on Success. False(0) on Error.

hapi_unassoc_stop
~~~~~~~~~~~~~~~~~

To stop un-association in HAPI.

+-----------------------------------------------------------------------+
| bool hapi_unassoc_stop(struct hapi \*hapi)                            |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi: Pointer to HAPI context.

Return: True(1) on Success. False(0) on Error.
