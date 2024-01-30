BLE APIs
~~~~~~~~

hapi_bt_host_create
^^^^^^^^^^^^^^^^^^^

Creates the HAPI BLE interface and should be called before any BLE APIs.

+-----------------------------------------------------------------------+
| struct hapi_bt_host \*hapi_bt_host_create(struct hapi \*hapi)         |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi: HAPI instance pointer.

Return: A valid pointer points to the HAPI BLE instance on Success. NULL
on Error.

hapi_bt_host_gap_addr_set
^^^^^^^^^^^^^^^^^^^^^^^^^

Used to set the address of the BLE/BT of Talaria TWO.

+-----------------------------------------------------------------------+
| bool hapi_bt_host_gap_addr_set(struct hapi_bt_host \*hapi_bt_host,    |
| uint8_t addr_type, uint8_t \*addr)                                    |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi_bt_host: BLE HAPI instance pointer.

2. addr_type: Type of address set. 0=public, 1=random.

3. addr: Address.

Return: True (1) on Success. False (0) on Error.

hapi_bt_host_bt_gap_create
^^^^^^^^^^^^^^^^^^^^^^^^^^

Used to set create the BLE gap device.

+-----------------------------------------------------------------------+
| bool hapi_bt_host_bt_gap_create(struct hapi_bt_host \*hapi_bt_host)   |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi_bt_host: BLE HAPI instance pointer.

Return: True (1) on Success. False (0) on Error.

hapi_bt_host_bt_gap_destroy
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Used to remove the BLE gap service.

+-----------------------------------------------------------------------+
| bool hapi_bt_host_bt_gap_destroy(struct hapi_bt_host \*hapi_bt_host)  |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi_bt_host: BLE HAPI instance pointer.

Return: True (1) on Success. False (0) on Error.

hapi_bt_host_gap_cfg_conn
^^^^^^^^^^^^^^^^^^^^^^^^^

Used to configure the parameter of the BLE gap connection.

+-----------------------------------------------------------------------+
| bool hapi_bt_host_gap_cfg_conn(                                       |
|                                                                       |
| struct hapi_bt_host \*hapi_bt_host, uint16_t conn_interval,           |
|                                                                       |
| uint16_t conn_latency, uint16_t conn_timeout,                         |
|                                                                       |
| uint16_t conn_params_reject, uint16_t conn_params_int_min,            |
|                                                                       |
| uint16_t conn_params_int_max )                                        |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi_bt_host: BLE HAPI instance pointer.

2. conn_interval: The BLE connection interval, in 1.25 ms, range: 0x0006
   to 0x0C80 (default: 80).

3. conn_latency: In intervals, range: 0x0000 to 0x01F3 (default: 0).

4. conn_timeout: In ms, range: 0x000A to 0x0C80 (default: 2000).

5. conn_params_reject: Reject parameter update, 1=True, 0=False
   (default: 0).

6. conn_params_int_min: In 1.25 ms, parameter update min connection
   interval (default: 6)

7. conn_params_int_max: In 1.25 ms, parameter update max connection
   interval (default: 8in 1.25 ms, parameter update min connection
   interval (default: 6)00)

Return: True (1) on Success. False(0) on Error.

hapi_bt_host_gap_cfg_smp
^^^^^^^^^^^^^^^^^^^^^^^^

Used to configure the parameter of the secure BLE gap connection.

+-----------------------------------------------------------------------+
| bool hapi_bt_host_gap_cfg_smp(struct hapi_bt_host \*hapi_bt_host,     |
|                                                                       |
| uint8_t io_cap, uint8_t oob, uint8_t bondable,                        |
|                                                                       |
| uint8_t mitm, uint8_t sc, uint8_t keypress,                           |
|                                                                       |
| uint8_t key_size, uint8_t encrypt)                                    |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi_bt_host: BLE HAPI instance pointer.

2. Io_cap: I/O-capabilities: 0-display_only, 1-display_yes_no,
   2-keyboard_only, 3-no_input_no_output, 4-keyboard_display (default:
   0)

3. oob: OOB exists: 1=True, 0=False (default: 0).

4. bondable: Enable bondable feature: 1=True, 0=False (default: 0).

5. mitm: MITM protection: 1=True, 0=False (default: 0).

6. sc: Secure connection: 1=True, 0=False (default: 0)

7. keypress: Send keypress: 1=True, 0=False (default: 0).

8. keysize: Smallest key size (7..16 octets) (default: 16).

9. encrypt: Automatically encrypt link at connection setup if key
   exists: 1=True, 0=False (default: 0).

Return: True (1) on Success. False (0) on Failure.

hapi_bt_host_gap_connectable
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Used to configure the connectable mode when it used as peripheral.

+-----------------------------------------------------------------------+
| bool hapi_bt_host_gap_connectable(struct hapi_bt_host                 |
|                                                                       |
| \*hapi_bt_host, uint8_t mode, uint8_t own_type,                       |
|                                                                       |
| uint8_t peer_type, uint8_t \*peer_addr)                               |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi_bt_host: BLE HAPI instance pointer.

2. mode: Connectible mode 0=disable, 1=non, 2=direct, 3=undirect.

3. own_type: Type of own address: 0=public, 1=random, 2=resolvable (or
   public), 3=resolvable (or random).

4. peer_type: Peer address type: 0=public, 1=random.

5. peer_addr: Peer address.

Return: True (1) on Success. False(0) on Failure.

hapi_bt_host_gap_authenticate
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Used to configure the parameter of the secure BLE gap connection.

+-----------------------------------------------------------------------+
| bool hapi_bt_host_gap_cfg_smp(struct hapi_bt_host \*hapi_bt_host,     |
|                                                                       |
| uint8_t handle, uint8_t oob, uint8_t bondable,                        |
|                                                                       |
| uint8_t mitm, uint8_t sc, uint8_t key128)                             |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi_bt_host: BLE HAPI instance pointer.

2. handle: Connection handle.

3. oob: OOB exists: 1=True, 0=False (default: 0).

4. bondable: Enable bondable feature: 1=True, 0=False (default: 0).

5. mitm: MITM protection: 1=True, 0=False (default: 0).

6. sc: Secure connection: 1=True, 0=False (default: 0)

7. key128: 128-bits key required: 1=True, 0=False.

Return: True (1) on Success. False(0) on Failure.

hapi_bt_host_gap_set_adv_data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Used to set the advertisement data for the BLE peripheral advertisement.

+-----------------------------------------------------------------------+
| bool hapi_bt_host_gap_set_adv_data(struct hapi_bt_host                |
|                                                                       |
| \*hapi_bt_host, uint8_t length, uint8_t \*data)                       |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi_bt_host: BLE HAPI instance pointer.

2. length: The number of significant octets in the advertising data (1
   to 31).

3. data: Advertising data.

Return: True (1) on Success. False(0) on Failure.

hapi_bt_host_gap_broadcast
^^^^^^^^^^^^^^^^^^^^^^^^^^

Used to start the BLE advertisement.

+-----------------------------------------------------------------------+
| bool hapi_bt_host_gap_broadcast(struct hapi_bt_host \*hapi_bt_host,   |
|                                                                       |
| uint8_t mode, uint8_t own_type, uint8_t peer_type,                    |
|                                                                       |
| uint8_t \*peer_addr)                                                  |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi_bt_host: BLE HAPI instance pointer.

2. mode: Mode, 0=disable, 1=enable.

3. own_type: Type of own address: 0=public, 1=random, 2=resolvable (or
   public), 3=resolvable (or random).

4. peer_type: Peer address type: 0=public, 1=random.

5. peer_addr: Peer address.

Return: True (1) on Success. False(0) on Failure.

hapi_bt_host_gap_terminate
^^^^^^^^^^^^^^^^^^^^^^^^^^

Used to terminate the established BLE connection.

+-----------------------------------------------------------------------+
| bool hapi_bt_host_gap_terminate(struct hapi_bt_host \*hapi_bt_host,   |
|                                                                       |
| uint8_t handle)                                                       |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi_bt_host: BLE HAPI instance pointer.

2. handle: Connection handle.

Return: True (1) on Success. False(0) on Failure.

hapi_bt_host_gap_discoverable
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Used to configure the discoverable parameter of the BLE device.

+-----------------------------------------------------------------------+
| bool hapi_bt_host_gap_discoverable(struct hapi_bt_host                |
|                                                                       |
| \*hapi_bt_host, uint8_t mode, uint8_t own_type,                       |
|                                                                       |
| uint8_t peer_type, uint8_t \*peer_addr )                              |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi_bt_host: BLE HAPI instance pointer.

2. mode: Mode, 0=disable, 1=non, 2=limited, 3=general.

3. own_type: Type of own address: 0=public, 1=random, 2=resolvable (or
   public), 3=resolvable (or random).

4. peer_type: Peer address type: 0=public, 1=random.

5. peer_addr: Peer address.

Return: True (1) on Success. False(0) on Failure.

hapi_bt_host_gap_discovery
^^^^^^^^^^^^^^^^^^^^^^^^^^

Used to start the discovery of BLE devices.

+-----------------------------------------------------------------------+
| bool hapi_bt_host_gap_discovery(struct hapi_bt_host \*hapi_bt_host,   |
|                                                                       |
| uint8_t mode, uint8_t own_type, uint8_t peer_type,                    |
|                                                                       |
| uint8_t \*peer_addr)                                                  |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi_bt_host: BLE HAPI instance pointer.

2. Mode: Mode, 0=disable, 1=limited, 2=general, 3=name.

3. own_type: Own address type: 0=public, 1=random, 2=resolvable (or
   public), 3=resolvable (or random).

4. peer_type: Peer address type (only for mode "name"): 0=public,
   1=random, 2=public identity, 3=random identity.

5. peer_addr: Peer address (only for mode "name").

Return: True (1) on Success. False(0) on Failure.

hapi_bt_host_gap_connection
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Used to connect to the BLE peripheral.

+-----------------------------------------------------------------------+
| bool hapi_bt_host_gap_connection( struct hapi_bt_host \*hapi_bt_host, |
| uint8_t mode,uint8_t own_type, uint8_t peer_type, uint8_t             |
| \*peer_addr)                                                          |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi_bt_host: BLE HAPI instance pointer.

2. mode: The mode of connection. 0=disable, 1=auto, 2=general,
   3=selective, 4=direct ("auto" and "selective" require a white list).

3. own_type: Own address type: 0=public, 1=random, 2=resolvable (or
   public), 3=resolvable (or random).

4. peer_type: Peer address type (only for mode "name"): 0=public,
   1=random, 2=public identity, 3=random identity.

5. peer_addr: Peer address (only for mode "name").

Return: True (1) on Success. False(0) on Failure.

hapi_bt_host_gap_connection_update
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Used to update the existing BLE connection parameters when it is
configured as a peripheral.

+-----------------------------------------------------------------------+
| bool hapi_bt_host_gap_connection_update(                              |
|                                                                       |
| struct hapi_bt_host \*hapi_bt_host, uint16_t handle,                  |
|                                                                       |
| uint16_t interval_min, uint16_t interval_max,                         |
|                                                                       |
| uint16_t latency, uint16_t timeout)                                   |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi_bt_host: BLE HAPI instance pointer.

2. handle: The connection handle.

3. Interval_min: In 1.25 ms, range: 0x0006 to 0x0C80.

4. Interval_max: In 1.25 ms, range: 0x0006 to 0x0C80.

5. latency: In intervals, range: 0x0000 to 0x01F3.

6. timeout: In ms, range: 0x000A to 0x0C80.

Return: True (1) on Success. False(0) on Failure.

hapi_bt_host_gap_add_device_to_white_list
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Used to update the device in white list.

+-----------------------------------------------------------------------+
| bool hapi_bt_host_gap_add_device_to_white_list(                       |
|                                                                       |
| struct hapi_bt_host \*hapi_bt_host, uint8_t addr_type,                |
|                                                                       |
| uint8_t \*addr)                                                       |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi_bt_host: BLE HAPI instance pointer.

2. addr_type: The address type: 0=public, 1=random.

3. addr: public or random device address.

Return: True (1) on Success. False(0) on Failure.

hapi_bt_host_gap_remove_device_from_white_list
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Used to remove the device addressed from the white list.

+-----------------------------------------------------------------------+
| bool hapi_bt_host_gap_remove_device_from_white_list(                  |
|                                                                       |
| struct hapi_bt_host \*hapi_bt_host,                                   |
|                                                                       |
| uint8_t addr_type, uint8_t \*addr)                                    |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi_bt_host: BLE HAPI instance pointer.

2. addr_type: The address type: 0=public, 1=random.

3. addr: public or random device address.

Return: True (1) on Success. False(0) on Failure.

hapi_bt_host_gap_clear_white_list
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Used to clear the white list.

+-----------------------------------------------------------------------+
| bool hapi_bt_host_gap_clear_white_list(                               |
|                                                                       |
| struct hapi_bt_host \*hapi_bt_host)                                   |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi_bt_host: BLE HAPI instance pointer.

Return: True (1) on Success. False(0) on Failure.

hapi_bt_host_gap_add_device_to_resolving_list
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Used to update the resolving list with the device.

+-----------------------------------------------------------------------+
| bool hapi_bt_host_gap_add_device_to_resolving_list(                   |
|                                                                       |
| struct hapi_bt_host \*hapi_bt_host, uint8_t addr_type,                |
|                                                                       |
| uint8_t \*addr, uint8_t \*peer_irk, uint8_t \*local_irk)              |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi_bt_host: BLE HAPI instance pointer.

2. addr_type: The address type: 0=public, 1=random.

3. addr: public or random device address.

4. peer_irk: IRK of the peer device.

5. local_irk: IRK of the local device.

Return: True (1) on Success. False(0) on Failure.

hapi_bt_host_gap_remove_device_from_resolving_list
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Used to remove the device from the resolving list.

+-----------------------------------------------------------------------+
| bool hapi_bt_host_gap_remove_device_from_resolving_list(              |
|                                                                       |
| struct hapi_bt_host \*hapi_bt_host, uint8_t addr_type,                |
|                                                                       |
| uint8_t \*addr)                                                       |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi_bt_host: BLE HAPI instance pointer.

2. addr_type: The address type: 0=public, 1=random.

3. addr: public or random device address.

Return: True (1) on Success. False(0) on Failure.

hapi_bt_host_gap_clear_resolving_list
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Used to update the white list with the device.

+-----------------------------------------------------------------------+
| bool hapi_bt_host_gap_clear_resolving_list(                           |
|                                                                       |
| struct hapi_bt_host \*hapi_bt_host                                    |
|                                                                       |
| )                                                                     |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi_bt_host: BLE HAPI instance pointer.

Return: True (1) on Success. False(0) on Failure.

bt_host_gap_set_address_resolution_enable
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Used to enable/disable the address resolution of the device addressed.

+-----------------------------------------------------------------------+
| bool hapi_bt_host_gap_set_address_resolution_enable(                  |
|                                                                       |
| struct hapi_bt_host \*hapi_bt_host, uint16_t timeout,                 |
|                                                                       |
| uint8_t)                                                              |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi_bt_host: BLE HAPI instance pointer.

2. timeout: The Resolvable private address timeout in s (default: 900s).

3. enable:Enable: 1=True, 0=False (default: 0).

Return: True (1) on Success. False(0) on Failure.

hapi_bt_host_common_server_create
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Used create the common server functionality when it configured as a BLE
peripheral.

+-----------------------------------------------------------------------+
| bool hapi_bt_host_common_server_create(struct hapi_bt_host            |
|                                                                       |
| \*hapi_bt_host, char \*name, uint16_t appearance,                     |
|                                                                       |
| char \*manufacture_name)                                              |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi_bt_host: BLE HAPI instance pointer.

2. name: Name of the server.

3. appearance: Appearance of the server.

4. manufacture_name: Server manufacturer name.

Return: True (1) on Success. False(0) on Failure.

hapi_bt_host_gatt_add_service
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Used to add a BLE service when configured as a server.

+-----------------------------------------------------------------------+
| bool hapi_bt_host_gatt_add_service(struct hapi_bt_host                |
|                                                                       |
| \*hapi_bt_host, uint32_t handle)                                      |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi_bt_host: BLE HAPI instance pointer.

2. handle: The handle of the service.

Return: True (1) on Success. False(0) on Failure.

hapi_bt_host_gatt_destroy_service
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Used to destroy an added BLE service.

+-----------------------------------------------------------------------+
| bool hapi_bt_host_gatt_destroy_service(                               |
|                                                                       |
| struct hapi_bt_host \*hapi_bt_host, uint32_t handle)                  |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi_bt_host: BLE HAPI instance pointer.

2. handle: The handle of the service.

Return: True (1) on Success. False(0) on Failure.

hapi_bt_host_comon_server_destroy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Used to destroy the common BLE server created.

+-----------------------------------------------------------------------+
| bool hapi_bt_host_comon_server_destroy(                               |
|                                                                       |
| struct hapi_bt_host \*hapi_bt_host)                                   |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi_bt_host: BLE HAPI instance pointer.

Return: True (1) on Success. False(0) on Failure.

hapi_bt_host_gatt_exchange_mtu
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Used to exchange the BLE MTU size when it tries to connect to a
peripheral device.

+-----------------------------------------------------------------------+
| bool hapi_bt_host_gatt_exchange_mtu(                                  |
|                                                                       |
| struct hapi_bt_host \*hapi_bt_host, uint16_t size)                    |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi_bt_host: BLE HAPI instance pointer.

2. size: Client RX MTU size (23 - 251) (default: 23).

Return: True (1) on Success. False(0) on Failure.

hapi_bt_host_gatt_create_service_128
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Used to create a BLE service (128-bit UUID) when it acts as a peripheral
with a GATT server.

+-----------------------------------------------------------------------+
| void\* hapi_bt_host_gatt_create_service_128(                          |
|                                                                       |
| struct hapi_bt_host \*hapi_bt_host, uint8_t \*uuid)                   |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi_bt_host: BLE HAPI instance pointer.

2. uuid: The UUID of service.

Return: Handle of newly created service or NULL pointer if it failed.

bt_host_gatt_create_service_16
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Used to create a BLE service (16-bit) when it acts as a peripheral with
a GATT server.

+-----------------------------------------------------------------------+
| void\* hapi_bt_host_gatt_create_service_16(                           |
|                                                                       |
| struct hapi_bt_host \*hapi_bt_host, uint16_t uuid16)                  |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi_bt_host: BLE HAPI instance pointer.

2. uuid16: The uuid of service.

Return: Handle of newly created service or NULL pointer if it failed.

hapi_bt_host_gatt_notification
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Used to create a BLE GATT notification.

+-----------------------------------------------------------------------+
| bool hapi_bt_host_gatt_notification(                                  |
|                                                                       |
| struct hapi_bt_host \*hapi_bt_host, uint8_t value)                    |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi_bt_host: BLE HAPI instance pointer.

2. value: The value in notification.

Return: True (1) on Success. False(0) on Failure.

hapi_bt_host_gatt_indication
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Used to create a BLE GATT notification.

+-----------------------------------------------------------------------+
| bool hapi_bt_host_gatt_indication(                                    |
|                                                                       |
| struct hapi_bt_host \*hapi_bt_host, uint8_t value)                    |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi_bt_host: BLE HAPI instance pointer.

2. value: The value in indication.

Return: True (1) on Success. False(0) on Failure.

hapi_bt_host_gatt_write_characteristic_descriptor
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Used to write the BLE characteristics value.

+-----------------------------------------------------------------------+
| bool hapi_bt_host_gatt_write_characteristic_descriptor(               |
|                                                                       |
| struct hapi_bt_host \*hapi_bt_host, uint16_t handle,                  |
|                                                                       |
| uint32_t len, uint8_t \*value)                                        |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi_bt_host: BLE HAPI instance pointer.

2. handle: The handle for the characteristic descriptor.

3. length: The length of value to write.

4. value: The value to write.

Return: True (1) on Success. False(0) on Failure.

hapi_bt_host_gatt_discover_all_primary_services
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Used to discover all the supported BLE primary services.

+-----------------------------------------------------------------------+
| bool hapi_bt_host_gatt_discover_all_primary_services(                 |
|                                                                       |
| struct hapi_bt_host \*hapi_bt_host)                                   |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi_bt_host: BLE HAPI instance pointer.

Return: True (1) on Success. False(0) on Failure.

hapi_bt_host_gatt_discover_all_characteristic_descriptors
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Used to discover all BLE characteristics descriptors of a service.

+-----------------------------------------------------------------------+
| bool hapi_bt_host_gatt_discover_all_characteristic_descriptors(       |
|                                                                       |
| struct hapi_bt_host \*hapi_bt_host, uint16_t start_handle,            |
|                                                                       |
| uint16_t end_handle)                                                  |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi_bt_host: BLE HAPI instance pointer.

2. start_handle: The starting handle of the specified service.

3. end_handle: The ending handle of the specified service.

Return: True (1) on Success. False(0) on Failure.

hapi_bt_host_gatt_discover_all_characteristics_of_a_service
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Used to discover all BLE characteristics of a service.

+-----------------------------------------------------------------------+
| bool hapi_bt_host_gatt_discover_all_characteristic_descriptors(       |
|                                                                       |
| struct hapi_bt_host \*hapi_bt_host, uint16_t start_handle, uint16_t   |
| end_handle)                                                           |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi_bt_host: BLE HAPI instance pointer.

2. start_handle: The starting handle of the specified service.

3. end_handle: The ending handle of the specified service.

Return: True (1) on Success. False(0) on Failure

hapi_bt_host_gatt_discover_characteristics_by_uuid
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Used to discover BLE characteristics by a specified UUID.

+-----------------------------------------------------------------------+
| bool hapi_bt_host_gatt_discover_characteristics_by_uuid(              |
|                                                                       |
| struct hapi_bt_host \*hapi_bt_host, uint16_t start_handle, uint16_t   |
| end_handle, uint16_t size, uint8_t \*uuid)                            |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi_bt_host: BLE HAPI instance pointer.

2. start_handle: Starting handle of the specified service.

3. end_handle: Ending handle of the specified service.

4. size: The UUID size in bytes, 2-uuid16, 16-uuid128.

5. uuid: The UUID - 16 or 128 bits.

Return: True (1) on Success. False(0) on Failure

hapi_bt_host_gatt_discover_primary_service_by_service_uuid
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Used to discover the primary service supported with the specified UUID.

+-----------------------------------------------------------------------+
| bool hapi_bt_host_gatt_discover_primary_service_by_service_uuid(      |
|                                                                       |
| struct hapi_bt_host \*hapi_bt_host, uint16_t size, uint8_t \*uuid )   |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi_bt_host: BLE HAPI instance pointer.

2. size: Uuid size in bytes, 2-uuid16, 16-uuid128.

3. uuid: The uuid - 16 or 128 bits.

Return: True (1) on Success. False(0) on Failure.

hapi_bt_host_gatt_read_characteristic_value
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Used to read the characteristics value using a handle.

+-----------------------------------------------------------------------+
| bool hapi_bt_host_gatt_read_characteristic_value(                     |
|                                                                       |
| struct hapi_bt_host \*hapi_bt_host, uint16_t value_handle)            |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi_bt_host: BLE HAPI instance pointer.

2. value_handle: The value_handle to be read from remote server.

Return: True (1) on Success. False(0) on Failure.

hapi_bt_host_gatt_read_using_characteristic_uuid
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Used to read the characteristics value using a specified UUID.

+-----------------------------------------------------------------------+
| bool hapi_bt_host_gatt_read_using_characteristic_uuid(                |
|                                                                       |
| struct hapi_bt_host \*hapi_bt_host, uint16_t start_handle,            |
|                                                                       |
| uint16_t end_handle, uint16_t size, uint8_t \*uuid )                  |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi_bt_host: BLE HAPI instance pointer.

2. start_handle: The starting handle of the service handle range.

3. end_handle: The ending handle of the service handle range.

4. size: The UUID size in bytes, 2-uuid16, 16-uuid128.

5. uuid: The UUID - 16 or 128 bits.

Return: True (1) on Success. False(0) on Failure.

hapi_bt_host_gatt_read_long_characteristic_value
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Used to read the characteristics value using a service handle from an
offset.

+-----------------------------------------------------------------------+
| bool hapi_bt_host_gatt_read_long_characteristic_value(                |
|                                                                       |
| struct hapi_bt_host \*hapi_bt_host, uint16_t value_handle,            |
|                                                                       |
| uint16_t value_offset)                                                |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi_bt_host: BLE HAPI instance pointer.

2. value_handle: The value_handle to be read from remote server.

3. value_offset: The value_offset to be read.

Return: True (1) on Success. False(0) on Failure.

hapi_bt_host_gatt_read_multiple_characteristic_values
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Used to read multiple characteristics value using service handle.

+-----------------------------------------------------------------------+
| bool hapi_bt_host_gatt_read_multiple_characteristic_values(           |
|                                                                       |
| struct hapi_bt_host \*hapi_bt_host, uint16_t nof_handles,             |
|                                                                       |
| uint8_t \*handles)                                                    |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi_bt_host: BLE HAPI instance pointer.

2. nof_handle: The number of handles to be read.

3. handles: The handles to be read (two bytes per handle (lsb,msb)).

Return: True (1) on Success. False(0) on Failure.

hapi_bt_host_gatt_read_characteristic_descriptor
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Used to read multiple characteristics descriptor using handle.

+-----------------------------------------------------------------------+
| bool hapi_bt_host_gatt_read_characteristic_descriptor(                |
|                                                                       |
| struct hapi_bt_host \*hapi_bt_host, uint16_t handle )                 |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi_bt_host: BLE HAPI instance pointer.

2. handle: The handle of the characteristics descriptor to read.

Return: True (1) on Success. False(0) on Failure.

hapi_bt_host_gatt_write_without_response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Used to write the characteristics value using a handle. This API will
not generate any response from the remote.

+-----------------------------------------------------------------------+
| bool hapi_bt_host_gatt_write_without_response(                        |
|                                                                       |
| struct hapi_bt_host \*hapi_bt_host, uint16_t value_handle,            |
|                                                                       |
| uint8_t \*value,int len)                                              |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi_bt_host: BLE HAPI instance pointer.

2. value_handle: The value_handle to be write on the remote server.

3. value: The value to write.

4. len: The length of the data to be written.

Return: True (1) on Success. False(0) on Failure.

hapi_bt_host_gatt_write_characteristic_value
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Used to write the characteristics value using a handle.

+-----------------------------------------------------------------------+
| bool hapi_bt_host_gatt_write_characteristic_value(                    |
|                                                                       |
| struct hapi_bt_host \*hapi_bt_host, uint16_t value_handle,            |
|                                                                       |
| uint8_t \*value, int len)                                             |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi_bt_host: BLE HAPI instance pointer.

2. value_handle: The value_handle to be write on the remote server.

3. value: The value to write.

4. len: The length of the data to be written.

Return: True (1) on Success. False(0) on Failure.

hapi_bt_host_smp_passkey
^^^^^^^^^^^^^^^^^^^^^^^^

Used to set the key for secure BLE connection.

+-----------------------------------------------------------------------+
| bool hapi_bt_host_smp_passkey(                                        |
|                                                                       |
| struct hapi_bt_host \*hapi_bt_host, uint32_t key0,                    |
|                                                                       |
| uint32_t oob1, uint32_t oob2, uint32_t oob3)                          |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi_bt_host: BLE HAPI instance pointer.

2. Key0: The 20 bits passkey or OOB0 (bits 0..31).

3. oob1: OOB1 (bits 32..63).

4. oob2: OOB2 (bits 64..95).

5. oob3: OOB3 (bits 96..127).

Return: True (1) on Success. False(0) on Failure.

hapi_bt_host_gatt_char_rd_data_update
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Used to update the data for read operation.

+-----------------------------------------------------------------------+
| bool hapi_bt_host_gatt_char_rd_data_update(                           |
|                                                                       |
| struct hapi_bt_host \*hapi_bt_host, uint32_t ctx,                     |
|                                                                       |
| uint8_t uuid_len, uint8_t \*uuid, uint16_t len,                       |
|                                                                       |
| uint8_t \*data)                                                       |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi_bt_host: BLE HAPI instance pointer.

2. ctx: The context of read.

3. uuid_len: The length of UUID.

4. uuid: The uuid of service.

5. len: The length of data.

6. data: The data to give caller.

Return: True (1) on Success. False(0) on Failure.

hapi_bt_host_gatt_char_wr_data_update
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Used to update that data is written.

+-----------------------------------------------------------------------+
| bool hapi_bt_host_gatt_char_wr_data_update(                           |
|                                                                       |
| struct hapi_bt_host \*hapi_bt_host, uint32_t ctx,                     |
|                                                                       |
| uint8_t uuid_len, uint8_t \*uuid, uint32_t status)                    |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi_bt_host: BLE HAPI instance pointer.

2. ctx: The context of write.

3. uuid_len: The length of UUID.

4. uuid: The UUID of service.

5. status: The status of write operation.

Return: True (1) on Success. False(0) on Failure.

hapi_bt_host_gatt_add_chr_16
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Used to add a characteristic for a created BLE service.

+-----------------------------------------------------------------------+
| Bool hapi_bt_host_gatt_add_chr_16(                                    |
|                                                                       |
| struct hapi_bt_host \*hapi_bt_host, uint32_t handle,                  |
|                                                                       |
| uint16_t uuid16, uint8_t permission, uint8_t property)                |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi_ble: BLE HAPI instance pointer.

2. handle: The handle of service.

3. uuid16: The UUID of service.

4. permission: The Permission of service.

5. property: The Property of service.

Return: True (1) on Success. False(0) on Failure.

hapi_bt_host_gap_cfg_scan
^^^^^^^^^^^^^^^^^^^^^^^^^

Used to scan the characteristics of a created BLE service.

+-----------------------------------------------------------------------+
| bool hapi_bt_host_gap_cfg_scan(                                       |
|                                                                       |
| struct hapi_bt_host \*hapi_bt_host, uint16_t scan_period, uint16_t    |
| scan_int, uint16_t scan_win, uint16_t scan_bkg_int, uint16_t          |
| scan_bkg_win, uint8_t scan_filter_duplicates )                        |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. scan_period : Foreground scanning in ms (no connected link) (default:
   10240).

2. scan_int: In 625 µs, range: 0x0004 to 0x4000 (default: 96)

3. scan_win: In 625 µs, range: 0x0004 to 0x4000 (default: 48)

4. scan_bkg_int: In 625 µs, range: 0x0004 to 0x4000 (default: 2048)

5. scan_bkg_win: In 625 µs, range: 0x0004 to 0x4000 (default: 18)

6. scan_filter_duplicates: 1=True, 0=False (default: 1).

Return: True on Success and False on Failure.

hapi_bt_host_gatt_service_changed
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Used to message gatt_service_changed.

+-----------------------------------------------------------------------+
| bool                                                                  |
|                                                                       |
| hapi_bt_host_gatt_service_changed(struct hapi_bt_host \*hapi_bt_host) |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi_bt_host: BLE HAPI instance pointer.

Return: True on Success and False on Failure.

hapi_bt_host_gatt_find_included_services
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Used to message gatt_find_included_services.

+-----------------------------------------------------------------------+
| bool hapi_bt_host_gatt_find_included_services(                        |
|                                                                       |
| struct hapi_bt_host \*hapi_bt_host, uint16_t start_handle, uint16_t   |
| end_handle)                                                           |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi_bt_host: BLE HAPI instance pointer.

2. start_handle: Starting handle of the specified service

3. end_handle: Ending handle of the specified service.

Return: True (0) on Success. False on Failure.

hapi_prov_start
^^^^^^^^^^^^^^^

Used to start the provisioning.

+-----------------------------------------------------------------------+
| bool hapi_prov_start(struct hapi \*hapi_p,prov_start_cfg_t \*cfg)     |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi_p: HAPI instance pointer.

2. prov_start_cfg_t: Structure holds the provisioning configuration
   details, which is defined as:

+-----------------------------------------------------------------------+
| typedef struct{                                                       |
|                                                                       |
| char \*name;/\**<Device name. if NULL, PROV_DFLT_NAME is set*/        |
|                                                                       |
| uint16_t appearance; /\**< appearance. deafult to 0*/                 |
|                                                                       |
| char \*manufacturer_name;/\**<Manufacturer name. if NULL,             |
|                                                                       |
| PROV_DFLT_MANUFCTR_NAME is set*/                                      |
|                                                                       |
| prov_data_cb_t cb; /\* prov_data callback*/                           |
|                                                                       |
| void \* cbd_ctx;                                                      |
|                                                                       |
| }prov_start_cfg_t;                                                    |
+=======================================================================+
+-----------------------------------------------------------------------+

Return: Provisioning status. True=Success, False otherwise.

hapi_prov_stop
^^^^^^^^^^^^^^

Used to stop the provisioning.

+-----------------------------------------------------------------------+
| bool hapi_prov_stop(struct hapi \*hapi_p, prov_close_ifc_type_t ifc)  |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi_p: HAPI instance pointer.

2. prov_close_ifc_type_t: Structure olds the provisioning configuration
   details, which is defined as:

+-----------------------------------------------------------------------+
| typedef enum {                                                        |
|                                                                       |
| PROV_CLOSE_IFC_WIFI = 1,                                              |
|                                                                       |
| PROV_CLOSE_IFC_BLE = PROV_CLOSE_IFC_WIFI << 1,                        |
|                                                                       |
| PROV_CLOSE_IFC_ALL = PROV_CLOSE_IFC_WIFI \| PROV_CLOSE_IFC_BLE,       |
|                                                                       |
| }prov_close_ifc_type_t;                                               |
+=======================================================================+
+-----------------------------------------------------------------------+

Return: Provisioning status. True=Success, False otherwise.

hapi_prov_set_wcm_handle
^^^^^^^^^^^^^^^^^^^^^^^^

Used to get the existing WCM handle.

+-----------------------------------------------------------------------+
| bool hapi_prov_set_wcm_handle(struct hapi \*hapi_p, uint32_t          |
| wcm_handle)                                                           |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi_p: HAPI instance pointer.

2. wcm_handle: gives the WCM_handle if available.

Return: Existing WCM handle.

hapi_bt_host_gap_tx_power_set
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Used set BT Tx power.

+-----------------------------------------------------------------------+
| bool hapi_bt_host_gap_tx_power_set(struct hapi_bt_host                |
| \*hapi_bt_host, int8_t tx_power);                                     |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi_bt_host: BLE HAPI instance pointer.

2. tx_power: Set Tx power in dBm (-20 to 10 (max)).

Return: True (1) on Success. False (0) on Error.

hapi_bt_host_gap_tx_power_get
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Used get BT Tx power.

+-----------------------------------------------------------------------+
| bool hapi_bt_host_gap_tx_power_get(struct hapi_bt_host                |
| \*hapi_bt_host, int8_t tx_power);                                     |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi_bt_host: BLE HAPI instance pointer.

2. tx_power: Set Tx power in dBm (-20 to 10 (max)).

Return: Status of acquiring the Tx power. True=Success, False otherwise.
