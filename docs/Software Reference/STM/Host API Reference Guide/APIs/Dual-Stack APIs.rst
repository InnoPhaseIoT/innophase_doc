Dual-Stack APIs 
----------------

hapi_packet_forward_config_set 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Adds new packet forward configuration rule.

+-----------------------------------------------------------------------+
| bool hapi_packet_forward_config_set(struct hapi \*hapi, uint32_t      |
| ip_type, uint32_t \*remote_ip, uint16_t remote_port, uint16_t         |
| remote_port_start, uint16_t remote_port_end, const uint16_t           |
| local_port, uint16_t local_port_start, uint16_t local_port_end,       |
| uint8_t proto, uint32_t direction, uint32_t rule_selection, uint32_t  |
| \*rule_id);                                                           |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1.  hapi: Pointer to HAPI instance.

2.  ip_type: 0: ipv4, 1: ipv6.

3.  remote_ip: Remote IP address.

4.  remote_port: Remote port address.

5.  remote_port_start: Remote port start address. Used to specify the
    port range.

6.  remote_port_end: Remote port end address. Used to specify the port
    range.

7.  local_port: Local (source) port address.

8.  local_port_start: Local port start address. Used to specify the port
    range.

9.  local_port_end: Local port end address. Used to specify the port
    range.

10. proto: Protocol to apply the rule. Standard protocol values are:
    1-ICMP, 6-TCP, 17-UDP.

11. direction: The direction to forward the packet. Whether to Talaria
    TWO(0) or host(1).

12. rule_selection: To select the rule to apply.

13. rule_id: Rule ID in the packet forward configuration list.

Return: FALSE(0) on Success, TRUE(1) on Error.

hapi_packet_forward_config_del 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Deletes one packet forward configuration rule from the existing list.

+-----------------------------------------------------------------------+
| bool hapi_packet_forward_config_del(struct hapi \*hapi, uint32_t      |
| ip_tye, uint32_t \*remote_ip, uint16_t remote_port, uint16_t          |
| remote_port_start, uint16_t remote_port_end, const uint16_t           |
| local_port, uint16_t local_port_start, uint16_t local_port_end,       |
| uint8_t proto, uint32_t direction, uint32_t rule_selection);          |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1.  hapi: Pointer to HAPI instance.

2.  ip_type: 0: ipv4, 1: ipv6.

3.  remote_ip: Remote IP address.

4.  remote_port: Remote port address.

5.  remote_port_start: Remote port start address. Used to specify the
    port range.

6.  remote_port_end: Remote port end address. Used to specify the port
    range.

7.  local_port: Local (source) port address.

8.  local_port_start: Local port start address. Used to specify the port
    range.

9.  local_port_end: Local port end address. Used to specify the port
    range.

10. proto: Protocol to apply the rule. Standard protocol values are:
    1-ICMP, 6-TCP, 17-UDP.

11. direction: The direction to forward the packet. Whether to Talaria
    TWO(0) or Host(1).

12. rule_selection: To select the rule to apply.

Return: FALSE(0) on Success, TRUE(1) on Error.

hapi_packet_forward_dir_set 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Changes the packet forward direction to Talaria TWO/HOST based on the
input.

+-----------------------------------------------------------------------+
| bool hapi_packet_forward_dir_set(struct hapi \*hapi, uint32_t         |
| direction);                                                           |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi: Pointer to HAPI instance.

2. direction: Sets the direction to forward the packet. Whether to
   Talaria TWO(0) or host(1).

Return: TRUE(1) on Success, FALSE(0) on Error.

hapi_packet_forward_dir_get 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Gets the current packet forward direction- Talaria TWO/HOST.

+-----------------------------------------------------------------------+
| bool hapi_packet_forward_dir_get(struct hapi \*hapi, uint32_t         |
| \*direction);                                                         |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi: Pointer to HAPI instance.

2. direction: Gets the direction to forward the packet. Whether to
   Talaria TWO(0) or host(1).

Return: TRUE(1) on Success, FALSE(0) on Error.

hapi_packet_forward_config_query 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Queries and reverts with the list of packet forward rules configured.

+-----------------------------------------------------------------------+
| bool hapi_packet_forward_config_query(struct hapi \*hapi, uint32_t    |
| ip_type, uint32_t size);                                              |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi: Pointer to HAPI instance.

2. ip_type: 0: ipv4, 1: ipv6.

3. size: Sets size to '0' to get the total number of rules.

Return: TRUE(1) on Success, FALSE(0) on Error.

hapi_packet_forward_config_del_byid 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Deletes one packet forward configuration rule from the existing list by
taking rule_id as input.

+-----------------------------------------------------------------------+
| bool hapi_packet_forward_config_del_byid(struct hapi \*hapi, uint32_t |
| ip_type, uint32_t rule_id);                                           |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. hapi: Pointer to HAPI instance.

2. ip_type: 0: ipv4, 1: ipv6.

3. rule_id: Rule ID to delete the rule in the packet forward
   configuration list.

Return: FALSE(0) on Success, TRUE(1) on Error.
