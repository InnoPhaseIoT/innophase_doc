Common APIs
~~~~~~~~~~~

hapi_start
^^^^^^^^^^

Starts the HAPI interface. Initializes indication semaphore, resets the
variables and starts the receive thread.

+-----------------------------------------------------------------------+
| bool                                                                  |
|                                                                       |
| hapi_start(struct hapi \*hapi)                                        |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi: HAPI instance pointer.

Return: True on Success, False on Failure.

hapi_close
^^^^^^^^^^

Stops HAPI and closes the interface. Destroys the indication semaphore,
releases all indication handlers, destroys receive thread semaphore, and
receives thread itself, and finally, frees the HAPI context itself.

+-----------------------------------------------------------------------+
| void                                                                  |
|                                                                       |
| hapi_close(struct hapi \*hapi)                                        |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi: HAPI instance pointer.

Return: True on Success, False on Failure.

hapi_get_Error_code
^^^^^^^^^^^^^^^^^^^

Returns the currently set Error code in HAPI layer.

+-----------------------------------------------------------------------+
| int hapi_get_Error_code(struct hapi \*hapi)                           |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi: HAPI instance pointer.

Return: integer value corresponding to the Error code.

hapi_get_Error_message
^^^^^^^^^^^^^^^^^^^^^^

Returns the currently set Error message in HAPI layer.

+-----------------------------------------------------------------------+
| const char*hapi_get_Error_message(struct hapi \*hapi)                 |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi: HAPI instance pointer.

Return: Error message in string format corresponding to the Error code.

set_hapi_scarmbling_mode
^^^^^^^^^^^^^^^^^^^^^^^^

Sets the scrambling enable/disable in serial communication.

+-----------------------------------------------------------------------+
| void hapi_set_hio_scrambling(struct hapi \*hapi, int enable, void\*   |
| scrambling_ctx, void\* key, scrambling_fn scrambling_fn,              |
| descrambling_fn descrambling_fn);                                     |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi: HAPI instance pointer.

2. enable: 1 to enable the pass or 0 to disable.

3. scrambling_ctx: Context pointer passed along with
   scrambling/descrambling callback function.

4. key: Scrambling/descrambling key.

5. scrambling \_fn: Scrambling callback function.

6. descrambling \_fn: De-scrambling callback function.

Return: None.

hapi_add_ind_handler
^^^^^^^^^^^^^^^^^^^^

Request to add an indication handler for a message in a group.

+-----------------------------------------------------------------------+
| struct hapi_ind_handler \* hapi_add_ind_handler(                      |
|                                                                       |
| struct hapi \*hapi,                                                   |
|                                                                       |
| uint8_t group_id,                                                     |
|                                                                       |
| uint8_t msg_id,                                                       |
|                                                                       |
| hapi_ind_callback ind_cb,                                             |
|                                                                       |
| void \* context);                                                     |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi: HAPI instance pointer.

2. group_id: The group id to which it the handler registered.

3. msg_id: The message id to which it the handler registered.

4. ind_cb: The callback function to be called.

5. context: The context to be passed when the call back is getting
   called.

Return: The valid pointer on Success or NULL pointer on Failure.

hapi_config
^^^^^^^^^^^

Configures the HAPI interface for sleep wakeup.

+-----------------------------------------------------------------------+
| void hapi_config(struct hapi \*hapi, bool suspend_enable, uint8_t     |
| wakeup_pin, uint8_t wakeup_level, uint8_t irq_pin, uint8_t irq_mode)  |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi: HAPI instance pointer.

2. suspend_enable: suspend enabled or not.

3. wakeup_pin: The pin used to wake up from suspend.

4. wakeup_level: The level of the wake pin state.

5. irq_pin: The interrupt request pin.

6. irq_mode: The IRQ mode to be configured.

Return: None.

hapi_suspend
^^^^^^^^^^^^

Enables/disables suspend mode. The pin settings set with hapi_config
will be retained.

+-----------------------------------------------------------------------+
| void                                                                  |
|                                                                       |
| hapi_suspend(struct hapi \*hapi, bool suspend_enable);                |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi: HAPI instance pointer.

2. Suspend_enable: enable (1)/disable (0) suspend mode.

Return: None.

hapi_hio_query
^^^^^^^^^^^^^^

Checks if Talaria TWO is ready to accept the HIO commands from the host.

+-----------------------------------------------------------------------+
| hapi_hio_query(struct hapi \*hapi)                                    |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi: HAPI instance pointer.

Return: None.

hapi_get_time
^^^^^^^^^^^^^

Gets the current time that can be used for any time synced applications.

+-----------------------------------------------------------------------+
| bool hapi_hio_get_time(struct hapi \*hapi, uint64_t \*time_now)       |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi: HAPI instance pointer.

2. time_now: Pointer which contain the current time.

Return: True on Success, False on Failure.

hapi_nw_misc_app_time_get
^^^^^^^^^^^^^^^^^^^^^^^^^

Gets the network time that can be used for any time synced applications.

+-----------------------------------------------------------------------+
| bool hapi_nw_misc_app_time_get(struct hapi \*hapi, uint64_t           |
| \*current_time)                                                       |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi: HAPI instance pointer.

2. current_time: Pointer which contain the current network time.

Return: True on Success, False on Failure.

hapi_get_dbg_info
^^^^^^^^^^^^^^^^^

Gets more debug information from Talaria TWO.

+-----------------------------------------------------------------------+
| bool hapi_get_dbg_info(struct hapi \*hapi, struct                     |
| hapi_demo_dbg_info_get_rsp \*dbg_info)                                |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi: HAPI instance pointer.

2. dbg_info: Debug information received from Talaria TWO to be copied
   here.

Return: True on Success, False on Failure.

hapi_get_ver
^^^^^^^^^^^^

Gets the HAPI version.

+-----------------------------------------------------------------------+
| char \* hapi_ger_ver()                                                |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments: None

Return: the version string.

hapi_setup
^^^^^^^^^^

Set-up HAPI.

+-----------------------------------------------------------------------+
| struct hapi \*hapi_setup(void \*hapi_uart, void \*hapi_spi)           |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi_uart :pointer to HAPI UART.

2. hapi_spi : pointer to HAPI SPI.

Return: valid pointer pointing to HAPI instance on Success.

show_hapi_ver
^^^^^^^^^^^^^

Shows information about the HAPI library.

+-----------------------------------------------------------------------+
| static void show_hapi_ver(struct hapi \* hapi, struct hio_query_rsp   |
| \*hio_query_rsp)                                                      |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi: HAPI instance pointer.

2. hio_query_rsp: Response to HIO query

Return: True on Success, False on Failure.

hapi_console_init
^^^^^^^^^^^^^^^^^

Initializes HAPI console.

+-----------------------------------------------------------------------+
| void hapi_console_init(struct hapi \*hapi,CONSOLE_PRINT_FN            |
| \*console_print_fn);                                                  |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi: HAPI instance pointer.

2. console_print: Print debug message on the console UART.

Return: True on Success, False on Failure.

hapi_get_scrambled_data_len
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns scrambled data length.

+-----------------------------------------------------------------------+
| int hapi_get_scrambled_data_len(int len)                              |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. len: Length of non-scrambled data.

Return: Length of scrambled data.

hapi \_hio_scrambling_init
^^^^^^^^^^^^^^^^^^^^^^^^^^

Initializes the HIO scrambling context.

+-----------------------------------------------------------------------+
| void hapi_hio_scrambling_init(struct hapi \*hapi, void                |
| \*scrambling_ctx, void\* key,scrambling_fn scrambling_fn,             |
| descrambling_fn descrambling_fn)                                      |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi: Pointer to HAPI context.

2. scrambling_ctx: Context for scrambling and descrambling.

3. key: Key for scrambling/descrambling.

4. scrambling_fn: Function implementing scrambling.

5. descrambling_fn: Function implementing descrambling.

Return: None

hapi_disp_pkt_info
^^^^^^^^^^^^^^^^^^

Prints input output packet information.

+-----------------------------------------------------------------------+
| void hapi_disp_pkt_info(struct hapi \*hapi, int val)                  |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi: Pointer to HAPI context.

2. val: Enables/disables packet information print.

Return: None.

hapi_init_interface
^^^^^^^^^^^^^^^^^^^

Registers interface parameters.

+-----------------------------------------------------------------------+
| void hapi_init_interface(struct hapi \*hapi, struct hapi_ops          |
| \*hapi_ops, void \*dev)                                               |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi: Pointer to HAPI context.

2. hapi_ops: Device options.

3. dev: Pointer to interface device.

Return: None.

hapi_custom_msg_proc
^^^^^^^^^^^^^^^^^^^^

Sends the command to Talaria TWO and waits for response. Once the
response is received, it reverts the response data to the sender
application.

+-----------------------------------------------------------------------+
| int hapi_custom_msg_proc(struct hapi \*hapi, uint8_t \*group_id,      |
| uint8_t \*msg_id,uint8_t \*data, uint16_t \*len, int data_max_rx_len) |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi: Pointer to HAPI context.

2. group_id: Group ID.

3. msg_id: Message ID.

4. data: Message data.

5. len: Payload size of packet.

6. data_max_rx_len: Maximum reception data length.

Return: -1 if packet reception Fails and 0 on Success.

hapi_pkt_free
^^^^^^^^^^^^^

Frees the HAPI packet, and message buffer associated to packet.

+-----------------------------------------------------------------------+
| void hapi_pkt_free(struct hapi_packet\* pkt)                          |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. pkt: Packet to be freed.

Return: None.

hapi_rx_disable
^^^^^^^^^^^^^^^

Disables reception by killing the thread.

+-----------------------------------------------------------------------+
| void hapi_rx_disable(struct hapi \*hapi)                              |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi: Pointer to HAPI context.

Return: None.

hapi_set_Error
^^^^^^^^^^^^^^

Prints error.

+-----------------------------------------------------------------------+
| hapi_set_Error(struct hapi \*hapi, int Error_code, const char \*fmt,  |
| ...)                                                                  |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi: Pointer to HAPI context.

2. Error_code: Error code.

3. fmt: Printf style formatting arguments.

Return: None.

hapi_clear_Error
^^^^^^^^^^^^^^^^

Clears error.

+-----------------------------------------------------------------------+
| void hapi_clear_Error(struct hapi \*hapi)                             |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi: Pointer to HAPI context.

Return: None.

hapi_suspend_enabled_get
^^^^^^^^^^^^^^^^^^^^^^^^

Checks suspend status.

+-----------------------------------------------------------------------+
| bool hapi_suspend_enabled_get(struct hapi \*hapi)                     |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi: Pointer to HAPI context.

Return: 1: if suspend mode is enabled, else 0.

hapi_sig_wakeup
^^^^^^^^^^^^^^^

Used to wake Talaria TWO from suspended state.

+-----------------------------------------------------------------------+
| void hapi_sig_wakeup(struct hapi \*hapi)                              |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi: Pointer to HAPI context.

Return: None.

hapi_get_git_id
^^^^^^^^^^^^^^^

Gets the git ID.

+-----------------------------------------------------------------------+
| char \* hapi_get_git_id()                                             |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments: None.

Return: Git ID string.

is_hapi_hio_scrambling_enabled
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Used to check whether HIO scrambling is enabled or not.

+-----------------------------------------------------------------------+
| int                                                                   |
|                                                                       |
| is_hapi_hio_scrambling_enabled(struct hapi \*hapi)                    |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi: Pointer to HAPI context.

Return: HIO scrambling state. 1=enabled, 0=disabled.

hapi_set_scrambling_enabled
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Enables HIO scrambling.

+-----------------------------------------------------------------------+
| int                                                                   |
|                                                                       |
| hapi_set_scrambling_enabled(struct hapi \*hapi,int val)               |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi: Pointer to HAPI context.

2. val: set ‘1’ to enable and ‘0’ to disable.

Return: None.

hapi_pkt_msg_alloc
^^^^^^^^^^^^^^^^^^

Used for allocating a packet and sending a message.

+-----------------------------------------------------------------------+
| struct hapi_packet \*                                                 |
|                                                                       |
| hapi_pkt_msg_alloc(struct hapi \*hapi,                                |
|                                                                       |
| uint8_t msg_group,                                                    |
|                                                                       |
| uint8_t msg_id,                                                       |
|                                                                       |
| size_t msg_hdr_size,                                                  |
|                                                                       |
| size_t msg_payload_size)                                              |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi: Pointer to HAPI context.

2. msg_group: Message group ID.

3. msg_id: Message ID.

4. msg_hdr_size: Size of header.

5. msg_payload_size: Payload size of packet.

Return: Allocated packet.

hapi_send_recv_validate
^^^^^^^^^^^^^^^^^^^^^^^

Sends the packet and validates the reply packet.

+-----------------------------------------------------------------------+
| struct hapi_packet \*                                                 |
|                                                                       |
| hapi_send_recv_validate(struct hapi \*hapi, struct hapi_packet \*pkt, |
|                                                                       |
| uint8_t rsp_group_id,                                                 |
|                                                                       |
| uint8_t rsp_msg_id)                                                   |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi: Pointer to HAPI context.

2. hapi_packet \*pkt: Packet to be sent.

3. rsp_group_id: Expected group ID of reply packet.

4. rsp_msg_id: Expected msg ID of reply packet.

Return: Packets received from Talaria TWO device.

hapi_send_recv_no_validate
^^^^^^^^^^^^^^^^^^^^^^^^^^

Send the packet, and does not validate the reply packet.

+-----------------------------------------------------------------------+
| struct hapi_packet \* hapi_send_recv_validate(struct hapi \*hapi,     |
| struct hapi_packet \*pkt, uint8_t rsp_group_id, uint8_t rsp_msg_id)   |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi: Pointer to HAPI context.

2. hapi_packet \*pkt: Packet to be sent.

3. rsp_group_id: Expected group ID of reply packet.

4. rsp_msg_id: Expected msg ID of reply packet.

Return: Packets received from Talaria TWO device.

hapi_pkt_validate
^^^^^^^^^^^^^^^^^

Used for packet validation.

+-----------------------------------------------------------------------+
| bool hapi_pkt_validate(struct hapi \*hapi, struct hapi_packet \*pkt,  |
| uint8_t msg_group, uint8_t msg_id, bool check_trxid)                  |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi: Pointer t HAPI context.

2. hapi_packet \*pkt: Packet to be sent.

3. msg_group: Expected group ID.

4. msg_id: Expected message ID.

5. check_trxid: Specifies whether to check trxid of the received packet.

Return: Returns packet validate status. True=expected packet received,
False otherwise.

hapi_get_max_msg_size
^^^^^^^^^^^^^^^^^^^^^

Used to get maximum size of the message.

+-----------------------------------------------------------------------+
| unsigned int hapi_get_max_msg_size(struct hapi \*hapi)                |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi: Pointer to HAPI context.

Return:

1. msg_max_size: Maximum message size of communication.
