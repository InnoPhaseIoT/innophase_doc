.. _st api wlan:

WLAN APIs
~~~~~~~~~

hapi_wcm_create
^^^^^^^^^^^^^^^

Creates the HAPI WLAN manager interface and should be called before any
WLAN APIs.

.. code:: shell

      struct hapi_wcm *hapi_wcm_create(struct hapi *hapi)   


Arguments:

1. hapi: HAPI instance pointer.

Return: a valid pointer points to the HAPI WLAN instance on Success.
NULL pointer on Error.

hapi_wcm_network_profile_add
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Adds a network profile to connect. This API should be called before the
HAPI autoconnect API that starts the WLAN connection.

.. code:: shell

      bool hapi_wcm_network_profile_add(struct hapi_wcm *hapi_wcm, const char *ssid, const char *bssid, const char *passphrase, const char *passphrase_id)


Arguments:

1. hapi_wcm: HAPI WLAN instance pointer.

2. ssid : SSID of the network or empty string if BSSID is set.

3. bssid : BSSID of the network, set to all zeroes if SSID is set.

4. passphrase: passphrase for RSN, key for WEP or empty string for
   unencrypted connection.

5. Passphrase_id : passphrase ID.

Return: Status of add network profile operation. True=Success, False
otherwise.

hapi_wcm_network_profile_add_ext
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Adds a network profile to connect in enterprise mode. This API should be
called before the HAPI autoconnect API which starts the WLAN connection.

.. code:: shell

      bool hapi_wcm_network_profile_add_ext(struct hapi_wcm *hapi_wcm,struct wcm_connect_param *wcm_param)


Arguments:

1. hapi_wcm: HAPI WLAN instance pointer.

2. wcm_param : Pointer to WCM configuration structure. wcm_connect_param
   consists of the following parameters:

   a. ssid: Pointer to the name of the Access Point string

   b. passphrase: Pointer to the AP passphrase string

   c. security_type: Type of enterprise security, which can have anyone
      of the following values:

..

   0: Open

   1: Personal WPA2/3

   2: Enterprise PSK

   3: Enterprise TLS

   4: Enterprise PEAP

d. eap_identity: Pointer to identity string

e. eap_ca_path: Pointer to the path of CA certificate in Talaria TWO
   files system

f. eap_cert_path: Pointer to the path of client certificate in Talaria
   TWO file system

g. eap_pkey_path: Pointer to the path of private key file in Talaria TWO
   file system

h. eap_pkey_pwd: Pointer to the password of private key

i. eap_identity2: Pointer to phase 2 identity

j. eap_password: Pointer to the password of private key

k. eap_phase2auth: Pointer to phase 2 authentication

Return: Status of add network profile operation. True=Success, False
otherwise.

hapi_wcm_network_profile_remove
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Removes the network profile that was added.

.. code:: shell

      bool hapi_wcm_network_profile_remove(struct hapi_wcm *hapi_wcm)


Arguments:

1. hapi_wcm: HAPI WLAN instance pointer.

Return: Status of remove network profile operation. True=Success, False
otherwise.

hapi_wcm_autoconnect
^^^^^^^^^^^^^^^^^^^^

Triggers the scan and connects/disconnects to the AP specified by the
SSID and uses the passphrase that gets configured using the
hapi_wcm_network_profile_add API.

.. code:: shell

      bool hapi_wcm_autoconnect(struct hapi_wcm *hapi_wcm, uint32_t enabled)


Arguments:

1. hapi_wcm: HAPI WLAN instance pointer.

2. enabled: flag allow to connect. 1=enabled, 0=disabled.

Return: Status of auto connect operation. True=Success, False otherwise.

hapi_wcm_set_link_cb
^^^^^^^^^^^^^^^^^^^^

Registers the callback function to the HAPI WLAN interface for the
asynchronous WLAN link change notification.

.. code:: shell

      void hapi_wcm_set_link_cb(struct hapi_wcm *hapi_wcm, hapi_wcm_link_cb cb, void *context)


Arguments:

1. hapi_wcm: HAPI WLAN instance pointer.

2. cb: The call back function to be registered for link change
   notification.

3. context: context pointer to be passed when the call back is getting
   called.

Return: None.

hapi_wcm_destroy
^^^^^^^^^^^^^^^^

Removes the HAPI WLAN manager interface created.

.. code:: shell

      bool hapi_wcm_destroy(struct hapi_wcm *hapi_wcm) 


Arguments:

1. hapi_wcm: HAPI instance pointer.

Return: Status of destroy operation. True=Success, False otherwise.

hapi_wcm_get_handle
^^^^^^^^^^^^^^^^^^^

Returns the WCM handle address from hapi_wcm.

.. code:: shell

      uint32_t hapi_wcm_get_handle(struct hapi_wcm *hapi_wcm);



Arguments:

1. hapi_wcm: HAPI WLAN instance pointer.

Return: a valid pointer points to the HAPI WLAN instance on Success. 0
on Error.

hapi_wcm_scan
^^^^^^^^^^^^^

Starts the Wi-Fi scan. The scan can be SSID based and/or channel based.
Depends on the parameters provided.

.. code:: shell

      int32_t hapi_wcm_scan(struct hapi_wcm *hapi_wcm, const char *ssid, char channel, int *num)


Arguments:

1. hapi_wcm: HAPI WLAN instance pointer.

2. ssid: The SSID to be scanned.

3. channel: The channel number to be scanned.

4. num: The pointer to the variable that stores the number scanned
   results.

Return: 1 on Success else Error.

hapi_wcm_set_scan_cb
^^^^^^^^^^^^^^^^^^^^

Registers callback function for the scan operation. The callback
function is called when the required number of entries are available
once the scan starts.

.. code:: shell

      void hapi_wcm_set_scan_cb(struct hapi_wcm *hapi_wcm, hapi_wcm_scan_cb cb, void *context)


Arguments:

1. hapi_wcm: HAPI WLAN instance pointer.

2. cb: The callback function to be registered. Callback function
   prototype:

.. code:: shell

      void cb(void *context, struct wcm_scaninfo *scaninfo)

where, struct wcm_scaninfo declaration is as follows:

.. code:: shell

      struct wcm_scaninfo {
      uint32_t num;     /**Number of scan entries ***/
      uint8_t ssid[33]; /**SSID***/
      uint8_t bssid[6]; /**< BSSID */
      uint8_t channel;  /**< channel */
      int16_t rssi; /**< Estimated RSSI for the station */
      uint8_t authstr[32]; /**< security string */            };


3. context: The context to be passed along when the call back getting
   called.

Return: None.

hapi_wcm_setpmconfig
^^^^^^^^^^^^^^^^^^^^

Used to set the WLAN power save parameters.

.. code:: shell

      bool hapi_wcm_setpmconfig(struct hapi_wcm *hapi_wcm, uint32_t listen_interval, uint32_t traffic_tmo, uint32_t pm_flags)


Arguments:

1. hapi_wcm: HAPI WLAN instance pointer.

2. listen_interval: Listen interval in units of beacon intervals.

3. traffic_tmo: Traffic timeout (in ms)

4. pm_flags: power management flags, specified as follows:

   a. ps_poll: bit 0(0x01)

   b. dynamic_listen_intervel: bit 1(0x02)

   c. sta_rx_nap : bit 2(0x04)

   d. sta_only_broadcast : bit 3(0x08)

   e. tx_ps : bit 4(0x10)

   f. mcast_dont_care: bit 5(0x20)

multiple options can be selected as logical ‘or’-ing of above bits.

Return: Status of set pmconfig operation. True=Success, False otherwise.

hapi_wcm_regdomain_set
^^^^^^^^^^^^^^^^^^^^^^

Used to set the WLAN regulatory domain.

.. code:: shell

      bool hapi_wcm_regdomain_set(struct hapi_wcm *hapi_wcm, char *domain)


Arguments:

1. hapi_wcm: HAPI WLAN instance pointer.

2. domain: the regulatory domain name. supported strings are

   a. "FCC",

   b. "ETSI",

   c. "TELEC",

   d. "KCC",

   e. "SRCC"

Return: Status of set regdomain operation. True=Success, False
otherwise.

hapi_wcm_setaddr_4
^^^^^^^^^^^^^^^^^^

Sets the ipv4 address to Talaria TWO device. This APIs is normally
called for setting the static IP.

.. code:: shell

      bool hapi_wcm_setaddr_4(struct hapi_wcm *hapi_wcm, unsigned int *ipaddr, unsigned int *netmask, unsigned int *gw, unsigned int *dns)

Arguments:

1. hapi_wcm: HAPI WLAN instance pointer.

2. ipaddr: Pointer contains IP address.

3. netmask: Pointer contains netmask address.

4. gw: Pointer contains gate way address.

5. dns: Pointer contains DNS address.

Return: True(1) on Success. False(0) on Error.

hapi_wcm_getaddr_4
^^^^^^^^^^^^^^^^^^

Returns the ipv4 address from Talaria TWO device.

.. code:: shell

      bool hapi_wcm_getaddr_4(struct hapi_wcm *hapi_wcm, unsigned int *ipaddr, unsigned int *netmask, unsigned int *gw, unsigned int *dns)


Arguments:

1. hapi_wcm: HAPI WLAN instance pointer.

2. ipaddr: pointer to update IP address.

3. netmask: pointer to update netmask address.

4. gw: pointer to update gate way address.

5. dns: pointer to update DNS address.

Return: True(1) on Success. False (0) on Error.

hapi_wcm_network_profile_add_new
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Adds a network profile in personal or enterprise security mode to
connect.

.. code:: shell

      bool hapi_wcm_network_profile_add_new(struct hapi_wcm *hapi_wcm, struct wcm_connect_param *wcm_param)


Arguments:

1. hapi_wcm: Pointer to HAPI WCM context.

2. wcm_param: Pointer to connection parameters.

Return: Status of add network profile operation. True=Success, False
otherwise.

hapi_wcm_scan_indhandler
^^^^^^^^^^^^^^^^^^^^^^^^^^

Indication callback for scan response from Talaria TWO.

.. code:: shell

      void hapi_wcm_scan_indhandler(void *context, struct hapi_packet *pkt)

Arguments:

1. context: Context pointer to be passed when the call back is being
   called.

2. pkt: Packet to be sent. The packet should be in HAPI packet format.

Return: None.

hapi_wcm_autoconnectcfg
^^^^^^^^^^^^^^^^^^^^^^^

Enables/Disables async connect.

.. code:: shell

      bool hapi_wcm_autoconnectcfg(struct hapi_wcm *hapi_wcm, int flag)

Arguments:

1. hapi_wcm: Pointer to HAPI WCM context.

2. flag: Allows WCM to connect. 1=enabled, 0=disabled.

Return: Status of auto connect operation. True=Success, False otherwise.

hapi_wcm_lastind_get
^^^^^^^^^^^^^^^^^^^^

Returns last indication value.

.. code:: shell

      int hapi_wcm_lastind_get(struct hapi_wcm *hapi_wcm)


Arguments:

1. hapi_wcm: Pointer to HAPI WCM context.

Return: Indication value.

hapi_wcm_reinit
^^^^^^^^^^^^^^^

Re-initializes WCM interface and returns its pointer. This will be used
after host wakeup to initialize the WCM.

.. code:: shell

      struct hapi_wcm * hapi_wcm_reinit(struct hapi *hapi,uint32_t wcm_handle)


Arguments:

1. hapi: Pointer to HAPI context.

Return: Newly created WCM interface context.

hapi_wcm_set_handle
^^^^^^^^^^^^^^^^^^^

Sets WCM handle address after host wakeup.

.. code:: shell

      void hapi_wcm_set_handle(struct hapi_wcm *hapi_wcm, uint32_t wcm_handle)


Arguments:

1. hapi_wcm: Pointer to HAPI WCM context.

2. wcm_handle: WCM handle address.

Return: None.

.. _hapi_wcm_setpmconfig-1:

hapi_wcm_setpmconfig
^^^^^^^^^^^^^^^^^^^^

Sets WLAN power save parameters.

.. code:: shell

      bool hapi_wcm_setpmconfig(struct hapi_wcm *hapi_wcm, uint32_t listen_interval, uint32_t traffic_tmo, uint32_t pm_flags)


Arguments:

1. hapi_wcm: HAPI WLAN instance pointer.

2. listen_interval: Listen interval in units of beacon intervals.

3. traffic_tmo: Traffic timeout (in ms)

4. pm_flags: Power management flags, specified as follows:

   a. ps_poll: Set 1 to use ps_poll when beacon was missed -
      BIT(0)(0x01)

   b. dynamic_listen_intervel: Set 1 to listen to all beacons if there
      was traffic recently - BIT(1)(0x02)

   c. sta_rx_nap: Turn OFF the receiver for uninteresting frames for
      station - BIT(2)(0x04)

   d. sta_only_broadcast: Don't receive multicast frames that are not
      broadcast (only effective if rx_nap is used) - BIT(3)(0x08)

   e. tx_ps: Send outgoing frames without leaving Wi-Fi power save -
      BIT(4)(0x10)

   f. mcast_dont_care: Ignore the multicast flag in beacons. Use this
      function with care. Incoming broadcast ARPs or other important
      broadcast/multicast traffic may be missed. - BIT(5)(0x20)

   g. dtim: Set 1 to listen to only DTIM beacons - BIT(6)(0x40)

Multiple options can be selected as logical ‘or’-ing of above bits.

Return: Status of setpmconfig operation. True=Success, False otherwise.

hapi_wcm_getpmconfig
^^^^^^^^^^^^^^^^^^^^

Gets WLAN power save parameters.

.. code:: shell

      bool hapi_wcm_getpmconfig(struct hapi_wcm *hapi_wcm, uint32_t listen_interval, uint32_t traffic_tmo, uint32_t pm_flags)


Arguments:

5. hapi_wcm: HAPI WLAN instance pointer.

6. listen_interval: Listen interval in units of beacon intervals.

7. traffic_tmo: Traffic timeout (in ms)

8. pm_flags: Power management flags, specified as follows:

   a. ps_poll: bit 0(0x01)

   b. dynamic_listen_intervel: bit 1(0x02)

   c. sta_rx_nap : bit 2(0x04)

   d. sta_only_broadcast : bit 3(0x08)

   e. tx_ps : bit 4(0x10)

   f. mcast_dont_care: bit 5(0x20)

Multiple options can be selected as logical ‘or’-ing of above bits.

Return: Status of getpmconfig operation. True=Success, False otherwise.

hapi_wcm_tx_pow_set
^^^^^^^^^^^^^^^^^^^

Sets Tx power.

.. code:: shell

      bool hapi_wcm_tx_pow_set(struct hapi_wcm *hapi_wcm, int8_t tx_power 


Arguments:

1. hapi_wcm: Pointer to HAPI WCM context.

2. tx_power: Tx power in dBm (-10…20 (max)).

Return: True (1) on Success. False (0) on Error.

hapi_wcm_tx_pow_get 
^^^^^^^^^^^^^^^^^^^^

Gets Tx power.

.. code:: shell

      bool hapi_wcm_tx_pow_get(struct hapi_wcm *hapi_wcm, int8_t *tx_pow)

Arguments:

1. hapi_wcm: Pointer to HAPI WCM context.

2. tx_pow: Tx power in dBm (-10…20 (max)).

Return: Status of acquiring the Tx power. True=Success, False otherwise.

hapi_wcm_rssi_get 
^^^^^^^^^^^^^^^^^^

Gets the RSSI of WCM connection.

.. code:: shell

      bool hapi_wcm_rssi_get(struct hapi_wcm *hapi_wcm, int32_t *rssi)


Arguments:

1. hapi_wcm: Pointer to HAPI WCM context.

2. rssi: RSSI of WCM connection.

Return: Current average RSSI (0 if not associated). True=Success, False
otherwise.

hapi_wcm_scan_updatechannel 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Scans the updated channel.

.. code:: shell

      void hapi_wcm_scan_updatechannel(const unsigned char *ie_pkt, int ie_len,unsigned char *channel)

Arguments:

1. ie_pkt: WLAN information element packet.

2. ie_len: WLAN information element length .

3. channel: Channel specified.

Return: NULL.

hapi_wcm_scan_updateauth 
^^^^^^^^^^^^^^^^^^^^^^^^^

Scans the updated authentication mode.

.. code:: shell

      int hapi_wcm_scan_updateauth(unsigned char *ie_list, int ie_len, int *authmode)


Arguments:

1. ie_list: WLAN information element list.

2. ie_len: WLAN information element length.

3. authmode: Specified authentication mode.

Return: 0 on success, -1 on failure.

hapi_wcm_scan_updatessid 
^^^^^^^^^^^^^^^^^^^^^^^^^

Scans the updated SSID.

.. code:: shell

      void hapi_wcm_scan_updatessid(const unsigned char *ie_pkt, int ie_len,unsigned char *ssid)

Arguments:

1. ie_pkt: WLAN information element packet.

2. ie_len: WLAN information element length.

3. ssid: Specified SSID

Return: NULL.

hapi_wcm_authmode_tostr 
^^^^^^^^^^^^^^^^^^^^^^^^

Returns the authentication mode name.

.. code:: shell

      size_t hapi_wcm_authmode_tostr(uint32_t authmask, char *mode_name, size_t size)


Arguments:

1. authmask: Provided authentication mode.

2. mode_name: Provided authentication mode name (is a buffer).

3. size: Maximum number of bytes for mode_name.

Return: mode_name and size of mode_name.
