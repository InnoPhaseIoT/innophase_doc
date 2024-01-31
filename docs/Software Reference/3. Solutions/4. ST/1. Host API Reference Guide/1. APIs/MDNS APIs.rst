MDNS APIs
~~~~~~~~~

hapi_setup_mdns
^^^^^^^^^^^^^^^

Used to setup the MDNS service.

+-----------------------------------------------------------------------+
| struct hapi_mdns\*                                                    |
|                                                                       |
| hapi_setup_mdns(struct hapi \*hapi, struct hapi_wcm \*hapi_wcm,       |
|                                                                       |
| const char \*host_name)                                               |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi: HAPI instance pointer.

2. host_name: The hostname to be used for the MDNS service.

Return: On Success hapi_mdns pointer, else NULL

hapi_mdns_set_ind_cb
^^^^^^^^^^^^^^^^^^^^

Used to set MDNS notification callback function. This callback is
getting called when there is a notification from MDNS service.

+-----------------------------------------------------------------------+
| void hapi_mdns_set_ind_cb(struct hapi_mdns \*hapi_mdns,               |
|                                                                       |
| hapi_mdns_ind_cb cb,void \*context)                                   |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi: HAPI instance pointer.

2. cb: The callback function to be set.

3. context: The context pointer to be passed along when the callback is
   getting called.

Return: None.

hapi_add_mdns_service
^^^^^^^^^^^^^^^^^^^^^

Used to add a MDNS service so that the MDNS operation get started.

+-----------------------------------------------------------------------+
| bool hapi_add_mdns_service(struct hapi \*hapi, \*hapi_wcm,const char  |
|                                                                       |
| \*host_name, const char \*type,uint32_t proto,uint32_t                |
|                                                                       |
| port, char \*description, uint32_t \*serviceId)                       |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi: HAPI instance pointer.

2. hapi_wcm: HAPI WCM pointer.

3. host_name: The MDNS host name.

4. type: The host type.

5. proto: The protocol type.

6. port: The port number.

7. description: Description about the service.

8. serviceid: The MDNS service identifier of the service getting added.

Return: True(1) on Success. False(0) on Error

hapi_remove_mdns_service
^^^^^^^^^^^^^^^^^^^^^^^^

Used to remove a MDNS service being added.

+-----------------------------------------------------------------------+
| bool hapi_remove_mdns_service(struct hapi \*hapi, struct hapi_wcm     |
|                                                                       |
| \*hapi_wcm, uint32_t service_id)                                      |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi: HAPI instance pointer.

2. hapi_wcm: HAPI WCM pointer.

3. serviceid: The MDNS service identifier, being added with
   hapi_add_mdns_service API.

Return: True(1) on Success. False(0) on Error.

hapi_stop_mdns
^^^^^^^^^^^^^^

Used to stop the MDNS service.

+-----------------------------------------------------------------------+
| bool hapi_stop_mdns(struct hapi \*hapi, struct hapi_wcm \*hapi_wcm)   |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi: HAPI instance pointer.

2. hapi_wcm: Hapi wcm pointer.

Return: True(1) on Success. False(0) on Error.

hapi_resolve_mdns
^^^^^^^^^^^^^^^^^

Used to resolve the MDNS host name to get the IP address.

+-----------------------------------------------------------------------+
| bool hapi_resolve_mdns(struct hapi \*hapi, const char \*host_name,    |
| uint8_t addrtype, uint8_t \*ipaddr, uint16_t\* addrlen)               |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi: HAPI instance pointer.

2. host_name: The MDNS host name.

3. addrtype: The address type.

4. ipaddr: The pointer that will contain the IP address to be filled.

5. addrlen: The length of the IP address to be resolved.

Return: True(1) on Success. False(0) on Error.
