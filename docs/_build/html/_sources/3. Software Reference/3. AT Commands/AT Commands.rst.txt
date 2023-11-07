**Note**: *Arguments in [ ] are optional and those in <> are mandatory.
Command response column contains only response description and payload
fields.*

Generic AT Commands 
--------------------

AT – Check State 
~~~~~~~~~~~~~~~~~

+---------+------------------------------------------------------------+
| **Co    | at                                                         |
| mmand** |                                                            |
+=========+============================================================+
| **Res   | Success: OK                                                |
| ponse** |                                                            |
|         | Failure: Error                                             |
+---------+------------------------------------------------------------+
| **Param | NA                                                         |
| eters** |                                                            |
+---------+------------------------------------------------------------+
| **Ex    | at                                                         |
| ample** |                                                            |
+---------+------------------------------------------------------------+

AT+SYSNAME – Set System Name
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------+------------------------------------------------------------+
| **Co    | at+sysname=<Host Name>                                     |
| mmand** |                                                            |
+=========+============================================================+
| **Res   | Success: OK                                                |
| ponse** |                                                            |
|         | Failure: Error                                             |
+---------+------------------------------------------------------------+
| **Param | Host Name: host name to configure at+sysname=T2            |
| eters** |                                                            |
+---------+------------------------------------------------------------+
| **Ex    | at+sysname=T2                                              |
| ample** |                                                            |
+---------+------------------------------------------------------------+

AT+WAKEUPCFG – Configures System Wakeup
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------+------------------------------------------------------------+
| **Co    | at+wakeupcfg=<wakeup pin>, < wakeup level>, <host wakeup   |
| mmand** | pin> , <host wakeup mode>                                  |
+=========+============================================================+
| **Res   | Success: OK                                                |
| ponse** |                                                            |
|         | Failure: Error                                             |
+---------+------------------------------------------------------------+
| **Param | wakeuppin: GPIO pin to be used for Talaria TWO wakeup. 0   |
| eters** | to disable.                                                |
|         |                                                            |
|         | wakeup level: Talaria TWO wakeup level. 1: High ; 0: Low   |
|         |                                                            |
|         | host wakeup pin: GPIO pin to be used for interrupt to wake |
|         | up the host.                                               |
|         |                                                            |
|         | host wakeup mode: Interrupt mode to be used to wake up the |
|         | host: 0: None ; 1: Low ; 2: High                           |
+---------+------------------------------------------------------------+
| **Ex    | at+wakeupcfg=4,1,5,1                                       |
| ample** |                                                            |
|         | **Note**:                                                  |
|         |                                                            |
|         | 1. Ensure command execution is successful in the minicom   |
|         |    terminal and verify the same in the serial console logs |
|         |    as well.                                                |
|         |                                                            |
|         | 2. All the GPIOs are pulled high internally by default     |
|         |    except GPIO18 (pulled low).                             |
|         |                                                            |
|         | 3. To generate a low-level interrupt, GPIO must be pulled  |
|         |    low externally.                                         |
|         |                                                            |
|         | 4. To generate a high-level interrupt, pull down that      |
|         |    particular GPIO externally through a pull down          |
|         |    register. Only then the high interrupt will be          |
|         |    detected.                                               |
|         |                                                            |
|         | 5. Since there is always a pull down on high level         |
|         |    interrupt GPIO, some amount of small current is always  |
|         |    sinking through that pin, which will add onto the power |
|         |    save suspend current.                                   |
|         |                                                            |
|         | 6. Hence it is recommended to use low-level interrupt for  |
|         |    low power use case.                                     |
+---------+------------------------------------------------------------+

AT+SYSSLEEP – Puts System in Suspend Mode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------+------------------------------------------------------------+
| **Co    | at+syssleep=<suspend time>                                 |
| mmand** |                                                            |
+=========+============================================================+
| **Res   | Success: OK                                                |
| ponse** |                                                            |
|         | Failure: Error                                             |
+---------+------------------------------------------------------------+
| **Param | suspend time: Time in milliseconds, 0 indicates infinite   |
| eters** | suspend time.                                              |
+---------+------------------------------------------------------------+
| **Ex    | at+syssleep=100                                            |
| ample** |                                                            |
|         | **Note**:                                                  |
|         |                                                            |
|         | 1. In the case of infinite suspend time, it is mandatory   |
|         |    to set at+wakeupcfg (refer `AT+WAKEUPCFG – Configures   |
|         |    System                                                  |
|         |    Wakeup <#atwakeupcfg-configures-system-wakeup>`__ for   |
|         |    more details) command to use at+syssleep command.       |
|         |                                                            |
|         | 2. Talaria TWO will not enter suspend/deep sleep mode when |
|         |    it is in active state (traffic timeout set to zero).    |
|         |                                                            |
|         | 3. Send a break character on UART to wake up Talaria TWO   |
|         |    temporarily. In such cases, Talaria TWO will wait for a |
|         |    new command from host and goes back to suspend state    |
|         |    immediately after executing the command.                |
+---------+------------------------------------------------------------+

AT+ECHO – Enable/Disable the Command Echo Feature
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------+------------------------------------------------------------+
| **Co    | at+echo=<flag>                                             |
| mmand** |                                                            |
+=========+============================================================+
| **Res   | Success: OK                                                |
| ponse** |                                                            |
|         | Failure: Error                                             |
+---------+------------------------------------------------------------+
| **Param | Flag: Enable/Disable,                                      |
| eters** |                                                            |
|         | -  1: Enable the echo (default)                            |
|         |                                                            |
|         | -  0: Disable the echo                                     |
+---------+------------------------------------------------------------+
| **Ex    | at+echo=1                                                  |
| ample** |                                                            |
+---------+------------------------------------------------------------+

AT+VER – Prints Software Version Number
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------+------------------------------------------------------------+
| **Co    | at+ver                                                     |
| mmand** |                                                            |
+=========+============================================================+
| **Res   | Success: Version number followed by OK                     |
| ponse** |                                                            |
|         | Failure: Error                                             |
+---------+------------------------------------------------------------+
| **Param | NA                                                         |
| eters** |                                                            |
+---------+------------------------------------------------------------+
| **Ex    | at+ver                                                     |
| ample** |                                                            |
+---------+------------------------------------------------------------+

AT+RESET – Resets the Talaria TWO Module
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------+------------------------------------------------------------+
| **Co    | at+reset                                                   |
| mmand** |                                                            |
+=========+============================================================+
| **Res   | Success: Upon successful reset, module responds with       |
| ponse** | command prompt ‘>’, which implies Talaria TWO is ready to  |
|         | accept commands.                                           |
|         |                                                            |
|         | Failure: Error                                             |
+---------+------------------------------------------------------------+
| **Param | NA                                                         |
| eters** |                                                            |
+---------+------------------------------------------------------------+
| **Ex    | at+reset                                                   |
| ample** |                                                            |
+---------+------------------------------------------------------------+

**Note**: This command forcefully resets the Talaria TWO module core and
comes out with a fresh boot.

Wi-Fi AT Commands
-----------------

AT+WCON - Connect to WLAN Network as a Station
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------+-----------------------------------------------------------+
| **C      | at+wcon=<SSID>,[Passphrase],[Timeo                        |
| ommand** | ut],[Enterprise_security_type],[Identity],[ca_certificate |
|          | path],[client_certificate path],[private_key              |
|          | path],[                                                   |
|          | private_key_password],[Identity2],[password],[phase2auth] |
+==========+===========================================================+
| **Re     | Success: OK                                               |
| sponse** |                                                           |
|          | Failure: Error                                            |
+----------+-----------------------------------------------------------+
| **Para   | SSID: Name of the Access Point                            |
| meters** |                                                           |
|          | Passphrase: Password (optional for open security)         |
|          |                                                           |
|          | Timeout: Timeout in seconds, default being 180 seconds    |
|          |                                                           |
|          | Enterprise_security_type:                                 |
|          |                                                           |
|          | 1 - EAP-PSK                                               |
|          |                                                           |
|          | 2 - EAP-TLS                                               |
|          |                                                           |
|          | 3 - EAP-PEAP                                              |
|          |                                                           |
|          | Identity: Identity for enterprise security                |
|          |                                                           |
|          | ca_certificate path: Path to CA certificate in Talaria    |
|          | TWO filesystem                                            |
|          |                                                           |
|          | client_certificate path: Path to client certificate in    |
|          | Talaria TWO filesystem                                    |
|          |                                                           |
|          | private_key path: Path to private key file in Talaria TWO |
|          | filesystem                                                |
|          |                                                           |
|          | private_key_password: Password of private key             |
|          |                                                           |
|          | Identity2: Phase 2 identity                               |
|          |                                                           |
|          | password: Phase 2 password                                |
|          |                                                           |
|          | phase2auth: Phase 2 authentication                        |
+----------+-----------------------------------------------------------+
| **E      | **Open security**                                         |
| xample** |                                                           |
|          | at+wcon=rr,,30                                            |
|          |                                                           |
|          | **Personal security**                                     |
|          |                                                           |
|          | at+wcon=rr,abcd@123,30                                    |
|          |                                                           |
|          | **Enterprise security**                                   |
|          |                                                           |
|          | **TLS**:                                                  |
|          |                                                           |
|          | at+wcon=ssid,abc,30,2,eap-tls@innophaseinc                |
|          | .com,/sys/ca.pem,/sys/client.pem,/sys/client.key,password |
|          |                                                           |
|          | **PSK**:                                                  |
|          |                                                           |
|          | at                                                        |
|          | +wcon=ssid,0123456789abcdef0123456789abcdef,30,1,psk,,,,, |
|          |                                                           |
|          | **PEAP**:                                                 |
|          |                                                           |
|          |    at+wcon=ssid,abc                                       |
|          | ,30,3,anonymous,/sys/ca.pem,,,,eap-peap,password,MSCHAPv2 |
+----------+-----------------------------------------------------------+

AT+WDIS - Disconnect the Connection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------+-----------------------------------------------------------+
| **C      | at+wdis                                                   |
| ommand** |                                                           |
+==========+===========================================================+
| **Re     | Success: OK                                               |
| sponse** |                                                           |
|          | Failure: Error                                            |
+----------+-----------------------------------------------------------+
| **Para   | NA                                                        |
| meters** |                                                           |
+----------+-----------------------------------------------------------+
| **E      | at+wdis                                                   |
| xample** |                                                           |
+----------+-----------------------------------------------------------+

AT+WSTATUS - Get WLAN Status
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------+-----------------------------------------------------------+
| **C      | at+wstatus=<ID>                                           |
| ommand** |                                                           |
+==========+===========================================================+
| **Re     | Success: Respective status values followed by OK          |
| sponse** |                                                           |
|          | Failure: Error                                            |
+----------+-----------------------------------------------------------+
| **Para   | ID: status identifier                                     |
| meters** |                                                           |
|          | The following ID values are used to get the parameters    |
|          |                                                           |
|          | -  0: IP Address. Prints node IP address, subnet mask and |
|          |    gateway address                                        |
|          |                                                           |
|          | -  1: RSSI value                                          |
|          |                                                           |
|          | -  2: Wi-Fi counters (Tx packet count, packet count, and  |
|          |    so on.)                                                |
|          |                                                           |
|          | -  3: WLAN MAC address                                    |
|          |                                                           |
|          | -  4: Tx power                                            |
+----------+-----------------------------------------------------------+
| **E      | at+wstatus=0                                              |
| xample** |                                                           |
|          | at+wstatus=1                                              |
|          |                                                           |
|          | at+wstatus=2                                              |
|          |                                                           |
|          | at+wstatus=3                                              |
|          |                                                           |
|          | at+wstatus=4                                              |
+----------+-----------------------------------------------------------+

AT+WSCAN - Get the WLAN Scan Operation Results
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------+-----------------------------------------------------------+
| **C      | at+wscan=[SSID],[BSSID],[Channel]                         |
| ommand** |                                                           |
+==========+===========================================================+
| **Re     | Success: Scan results followed by OK                      |
| sponse** |                                                           |
|          | Failure: Error                                            |
|          |                                                           |
|          | Scan results are printed in following order               |
|          |                                                           |
|          | <BSSID>:<channel>:<RSSI>:<SSID>                           |
+----------+-----------------------------------------------------------+
| **Para   | SSID: Name of the Access Point                            |
| meters** |                                                           |
|          | BSSID: Access Point MAC address (optional)                |
|          |                                                           |
|          | Channel: WLAN channel number(optional)                    |
+----------+-----------------------------------------------------------+
| **E      | at+wscan=InnoPhase,,                                      |
| xample** |                                                           |
|          | at+wscan=InnoPhase,,6                                     |
+----------+-----------------------------------------------------------+

AT+WCFGSET - Set WLAN Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------+-----------------------------------------------------------+
| **C      | at+wcfgset=<ID>, <value-1>, ………, <value-N>                |
| ommand** |                                                           |
+==========+===========================================================+
| **Re     | Success: OK                                               |
| sponse** |                                                           |
|          | Failure: Error                                            |
+----------+-----------------------------------------------------------+
| **Para   | ID: Configuration Identifier                              |
| meters** |                                                           |
|          | Value: Configuration Value                                |
|          |                                                           |
|          | The following ID values are used to set the parameters    |
|          |                                                           |
|          | -  0: TX power in dBm (0 to 20)                           |
|          |                                                           |
|          | -  1: Set interface IPv4, netmask, gateway and DNS        |
|          |    addresses                                              |
|          |                                                           |
|          | The following parameters can be set                       |
|          |                                                           |
|          | -  ipaddr4: IP address, as big-endian integer             |
|          |                                                           |
|          | -  netmask: netmask, as big-endian integer                |
|          |                                                           |
|          | -  gw: default-route address, as big-endian integer.      |
|          |                                                           |
|          | -  dns_server: DNS server address, as big-endian integer. |
|          |                                                           |
|          | -  2: Scan configuration parameters                       |
|          |                                                           |
|          | The following parameters can be set:                      |
|          |                                                           |
|          | -  num_probes : Number of probe request to send (default  |
|          |    is 0)                                                  |
|          |                                                           |
|          | -  idle_slots: Maximum number of idle slots to decide if  |
|          |    we should keep listening (default value is 3).         |
|          |                                                           |
|          | -  Txrate: Rate to use for sending probe requests         |
|          |    (default value is 0)                                   |
|          |                                                           |
|          | -  min_listen_time: Minimum amount of time (in            |
|          |    milliseconds) to listen for probe responses on the     |
|          |    channel after transmitting the probe request (default  |
|          |    value is 8000).                                        |
|          |                                                           |
|          | -  max_listen_time: Maximum amount of time (in            |
|          |    milliseconds, including listen and probe requests) to  |
|          |    stay on the channel (default value is 24000).          |
|          |                                                           |
|          | -  wait_time: Idle time between each channel (giving      |
|          |    other parties access to the media) (default value is   |
|          |    0).                                                    |
|          |                                                           |
|          | -  probe_tx_time: Time (in milliseconds) after which a    |
|          |    probe request is aborted if transmission did not       |
|          |    happen.(default value is 8000).                        |
|          |                                                           |
|          | -  3: Set PMK Path                                        |
|          |                                                           |
|          | The PMK Path can be set using the following parameter:    |
|          |                                                           |
|          | -  pmk_path: pmk_path, path should start with ‘/’         |
+----------+-----------------------------------------------------------+
| **E      | at+wcfgset=0,10                                           |
| xample** |                                                           |
|          | at+wcfgset=0,9                                            |
|          |                                                           |
|          | at+wcfgset=0,20                                           |
|          |                                                           |
|          | at+wcfgset=0,0                                            |
|          |                                                           |
|          | at+wc                                                     |
|          | fgset=1,192.168.1.1,255.255.255.0,192.168.1.3,192.168.1.3 |
|          |                                                           |
|          | at+wcfgset=2,0,3,0,8000,24000,0,8000                      |
|          |                                                           |
|          | at+wcfgset=3,/data/pmkpath.data                           |
+----------+-----------------------------------------------------------+

AT+WCFGGET- Get WLAN Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------+-----------------------------------------------------------+
| **C      | at+wcfgget=<ID>                                           |
| ommand** |                                                           |
+==========+===========================================================+
| **Re     | Success: OK                                               |
| sponse** |                                                           |
|          | Failure: Error                                            |
+----------+-----------------------------------------------------------+
| **Para   | ID: Configuration Identifier                              |
| meters** |                                                           |
|          | The following ID values are used to set the parameters:   |
|          |                                                           |
|          | -  0: TX power in dBm ( -10 to 20)                        |
|          |                                                           |
|          | -  1: Get interface IPv4, netmask, gateway and DNS        |
|          |    addresses                                              |
|          |                                                           |
|          | ..                                                        |
|          |                                                           |
|          |    The following parameters can be used for Get           |
|          |                                                           |
|          | -  ipaddr4: IP address, as big-endian integer             |
|          |                                                           |
|          | -  netmask: netmask, as big-endian integer                |
|          |                                                           |
|          | -  gw: default-route address, as big-endian integer.      |
|          |                                                           |
|          | -  dns_server: DNS server address, as big-endian integer. |
|          |                                                           |
|          | -  2: Scan configuration parameters                       |
|          |                                                           |
|          | ..                                                        |
|          |                                                           |
|          |    The following parameters can be modified to get WLAN   |
|          |    configuration                                          |
|          |                                                           |
|          | -  num_probes : Number of probe request to send (default  |
|          |    is 0)                                                  |
|          |                                                           |
|          | -  idle_slots: Max number of idle slots to decide if we   |
|          |    should keep listening (default value is 3).            |
|          |                                                           |
|          | -  txrate: Rate to use for sending probe requests         |
|          |    (default value is 0)                                   |
|          |                                                           |
|          | -  min_listen_time: Minimum amount of time (in            |
|          |    milliseconds) to listen for probe responses on the     |
|          |    channel after transmitting the probe request (default  |
|          |    value is 8000).                                        |
|          |                                                           |
|          | -  max_listen_time: Maximum amount of time (in            |
|          |    milliseconds, including listen and probe requests) to  |
|          |    stay on the channel (default value is 24000)           |
|          |                                                           |
|          | -  wait_time: Idle time between each channel (giving      |
|          |    other parties access to the media) (default value is   |
|          |    0).                                                    |
|          |                                                           |
|          | -  probe_tx_time: Time (in milliseconds) after which a    |
|          |    probe request is aborted if transmission did not       |
|          |    happen (default value is 8000).                        |
|          |                                                           |
|          | -  3: Get PMK Path: Called to retrieve PMK Path.          |
+----------+-----------------------------------------------------------+
| **E      | at+wcfgget=0                                              |
| xample** |                                                           |
|          | at+wcfgget=1                                              |
|          |                                                           |
|          | at+wcfgget=2                                              |
|          |                                                           |
|          | at+wcfgget=3                                              |
+----------+-----------------------------------------------------------+

AT+WPMCFG – Set WLAN Power Management Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------+-----------------------------------------------------------+
| **C      | at+wpmcfg=<listen interval>,<traffic timeout>, <pspoll>,  |
| ommand** | <dyn_listen_int>[,<starx_nap>, <sta_only_bc>, <txps>,     |
|          | <mcast_dont_care>,<dtim>]                                 |
+==========+===========================================================+
| **Re     | Success: OK                                               |
| sponse** |                                                           |
|          | Failure: Error                                            |
+----------+-----------------------------------------------------------+
| **Para   | +-                                                        |
| meters** | ----------------+-----------------+-----------------+---+ |
|          | |                                                         |
|          | **Parameter**   | **Description** | **Min/Max       |   | |
|          | |                                                         |
|          |                 |                 | values**        |   | |
|          | +=                                                        |
|          | ================+=================+=================+===+ |
|          | |                                                         |
|          | listen interval | Beacon listen   | 0/integer range |   | |
|          | |                                                         |
|          |                 | interval        |                 |   | |
|          | +-                                                        |
|          | ----------------+-----------------+-----------------+---+ |
|          | |                                                         |
|          | traffic timeout | Traffic timeout | 0/integer range |   | |
|          | |                                                         |
|          |                 | in              |                 |   | |
|          | |                                                         |
|          |                 | milliseconds.   |                 |   | |
|          | |                                                         |
|          |                 | The traffic     |                 |   | |
|          | |                                                         |
|          |                 | timeout         |                 |   | |
|          | |                                                         |
|          |                 | parameter       |                 |   | |
|          | |                                                         |
|          |                 | specifies the   |                 |   | |
|          | |                                                         |
|          |                 | amount of time  |                 |   | |
|          | |                                                         |
|          |                 | (in             |                 |   | |
|          | |                                                         |
|          |                 | milliseconds)   |                 |   | |
|          | |                                                         |
|          |                 | that the device |                 |   | |
|          | |                                                         |
|          |                 | should stay     |                 |   | |
|          | |                                                         |
|          |                 | awake with the  |                 |   | |
|          | |                                                         |
|          |                 | radio           |                 |   | |
|          | |                                                         |
|          |                 | powered-up      |                 |   | |
|          | |                                                         |
|          |                 | after a         |                 |   | |
|          | |                                                         |
|          |                 | transmission    |                 |   | |
|          | |                                                         |
|          |                 | (to quickly     |                 |   | |
|          | |                                                         |
|          |                 | receive any     |                 |   | |
|          | |                                                         |
|          |                 | replies that    |                 |   | |
|          | |                                                         |
|          |                 | may be the      |                 |   | |
|          | |                                                         |
|          |                 | result of the   |                 |   | |
|          | |                                                         |
|          |                 | transmission)   |                 |   | |
|          | +-                                                        |
|          | ----------------+-----------------+-----------------+---+ |
|          | |                                                         |
|          | pspoll          | Use PS-poll     | 0/1             |   | |
|          | |                                                         |
|          |                 |                 | (True/False)    |   | |
|          | +-                                                        |
|          | ----------------+-----------------+-----------------+---+ |
|          | |                                                         |
|          | dyn_listen_int  | Dynamic listen  | 0/1             |   | |
|          | |                                                         |
|          |                 | interval        |                 |   | |
|          | +-                                                        |
|          | ----------------+-----------------+-----------------+---+ |
|          | |                                                         |
|          | starx_nap       | Turn off        | 0/1             |   | |
|          | |                                                         |
|          |                 | receiver for    |                 |   | |
|          | |                                                         |
|          |                 | inappropriate   |                 |   | |
|          | |                                                         |
|          |                 | frames for      |                 |   | |
|          | |                                                         |
|          |                 | station         |                 |   | |
|          | +-                                                        |
|          | ----------------+-----------------+-----------------+---+ |
|          | |                                                         |
|          | sta_only_bc     | Do not receive  | 0/1             |   | |
|          | |                                                         |
|          |                 | multicast       |                 |   | |
|          | |                                                         |
|          |                 | frames that are |                 |   | |
|          | |                                                         |
|          |                 | not applicable  |                 |   | |
|          | +-                                                        |
|          | ----------------+-----------------+-----------------+---+ |
|          | |                                                         |
|          | txps            | Send outgoing   | 0/1             |   | |
|          | |                                                         |
|          |                 | frames without  |                 |   | |
|          | |                                                         |
|          |                 | leaving Wi-Fi   |                 |   | |
|          | |                                                         |
|          |                 |                 |                 |   | |
|          | |                                                         |
|          |                 | on power save   |                 |   | |
|          | +-                                                        |
|          | ----------------+-----------------+-----------------+---+ |
|          | |                                                         |
|          | mcast_dont_care | Ignore the      | 0/1             |   | |
|          | |                                                         |
|          |                 | multicast flag  |                 |   | |
|          | |                                                         |
|          |                 | in beacons      |                 |   | |
|          | +-                                                        |
|          | ----------------+-----------------+-----------------+---+ |
|          | |                                                         |
|          | dtim            | Wakes up only   | 0/1             |   | |
|          | |                                                         |
|          |                 | at effective    |                 |   | |
|          | |                                                         |
|          |                 | listen interval |                 |   | |
|          | |                                                         |
|          |                 | and does not    |                 |   | |
|          | |                                                         |
|          |                 | switch to       |                 |   | |
|          | |                                                         |
|          |                 | listen every    |                 |   | |
|          | |                                                         |
|          |                 | beacon in case  |                 |   | |
|          | |                                                         |
|          |                 | of beacon miss  |                 |   | |
|          | +-                                                        |
|          | ----------------+-----------------+-----------------+---+ |
+----------+-----------------------------------------------------------+
| **E      | at+wpmcfg=3,100,1,1,0,0,0,0,1                             |
| xample** |                                                           |
+----------+-----------------------------------------------------------+

AT+WREGDOMAIN – Set WLAN Regulatory Domain
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------+-----------------------------------------------------------+
| **C      | at+wregdomain=<regulatory domain>                         |
| ommand** |                                                           |
+==========+===========================================================+
| **Re     | Success: OK                                               |
| sponse** |                                                           |
|          | Failure: Error                                            |
+----------+-----------------------------------------------------------+
| **Para   | regulatory domain: Regulatory domain configuration.       |
| meters** |                                                           |
|          | The valid values are:                                     |
|          |                                                           |
|          | -  0: FCC                                                 |
|          |                                                           |
|          | -  1: ETSI                                                |
|          |                                                           |
|          | -  2: TELEC                                               |
|          |                                                           |
|          | -  3: KCC                                                 |
|          |                                                           |
|          | -  4: SRCC                                                |
|          |                                                           |
|          | -  ?: Get regulatory domain                               |
+----------+-----------------------------------------------------------+
| **E      | at+wregdomain=0                                           |
| xample** |                                                           |
|          | at+wregdomain=?                                           |
+----------+-----------------------------------------------------------+

AT+SOCSRV - Create Server Socket
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------+-----------------------------------------------------------+
| **C      | at+socsrv=<Domain>,<Type>,<Protocol>, <Port>              |
| ommand** |                                                           |
+==========+===========================================================+
| **Re     | Success: “CONNECT:<Socket identifier>” message followed   |
| sponse** | by OK                                                     |
|          |                                                           |
|          | Failure: Error                                            |
|          |                                                           |
|          | Refer: `Command Response                                  |
|          | Description <#_Command_Response_Description_1>`__ for     |
|          | more details                                              |
+----------+-----------------------------------------------------------+
| **Para   | Domain: Specifies the protocol family of the created      |
| meters** | socket                                                    |
|          |                                                           |
|          |    0: INET: For network protocol IPv4                     |
|          |                                                           |
|          | Type: Specifies the communication semantics               |
|          |                                                           |
|          |    0: STREAM: Reliable stream-oriented service or Stream  |
|          |    Sockets                                                |
|          |                                                           |
|          |    1: DGRAM: Datagram service or Datagram Sockets         |
|          |                                                           |
|          | Protocol: Specifies a transport to be used with the       |
|          | socket:                                                   |
|          |                                                           |
|          |    0: TCP                                                 |
|          |                                                           |
|          |    1: UDP                                                 |
|          |                                                           |
|          | Port: Specifies the port number to create the server      |
+----------+-----------------------------------------------------------+
| **E      | at+socsrv=0,0,0,9000                                      |
| xample** |                                                           |
|          | at+socsrv=0,1,1,9000                                      |
+----------+-----------------------------------------------------------+

AT+SOCCLI - Create Client Socket
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------+----------------------------------------------------------+
| **        | at+soccli=<Domain>,<Type>,<Protocol>, <Port>, <Host>     |
| Command** |                                                          |
+===========+==========================================================+
| **R       | Success: “CONNECTED:<Socket identifier>” message         |
| esponse** | followed by OK                                           |
|           |                                                          |
|           | Failure: Error                                           |
|           |                                                          |
|           | Refer section `Command Response                          |
|           | Description <#_Command_Response_Description_1>`__ for    |
|           | more details                                             |
+-----------+----------------------------------------------------------+
| **Par     | Domain: Specifies the protocol family of the created     |
| ameters** | socket                                                   |
|           |                                                          |
|           |    0: INET: For network protocol IPv4.                   |
|           |                                                          |
|           | Type: Specifies the communication semantics              |
|           |                                                          |
|           |    0: STREAM: Reliable stream-oriented service or Stream |
|           |    Sockets                                               |
|           |                                                          |
|           |    1: DGRAM: Datagram service or Datagram Sockets        |
|           |                                                          |
|           | Protocol: Specifies a transport to be used with the      |
|           | socket:                                                  |
|           |                                                          |
|           |    0: TCP                                                |
|           |                                                          |
|           |    1: UDP                                                |
|           |                                                          |
|           | Port: Specifies the port number to create the server     |
|           |                                                          |
|           | Host: server IP address or host name                     |
+-----------+----------------------------------------------------------+
| **        | at+soccli=0,0,0,23,192.168.2.184                         |
| Example** |                                                          |
+-----------+----------------------------------------------------------+

AT+SOCSEND - Write Data to Socket
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------+----------------------------------------------------------+
| **        | at+socsend=<Socket ID>,<Type>,<Length>, <Data>,          |
| Command** | [Timeout]                                                |
+===========+==========================================================+
| **R       | Success: OK                                              |
| esponse** |                                                          |
|           | Failure: Error                                           |
+-----------+----------------------------------------------------------+
| **Par     | Socket ID: Socket identifier                             |
| ameters** |                                                          |
|           | Type: Data format, binary/ASCII                          |
|           |                                                          |
|           | Length: Number of bytes to send (in decimal). Length is  |
|           | limited to 1024 bytes                                    |
|           |                                                          |
|           | Data: Data to send                                       |
|           |                                                          |
|           | Timeout: Timeout value in seconds. If no value is        |
|           | provided, 90s is taken as default (applicable only for   |
|           | TCP socket)                                              |
+-----------+----------------------------------------------------------+
| **        | at+socsend=1,ASCII,5,data_1,40                           |
| Example** |                                                          |
|           | at+socsend=1,ASCII,1024, data                            |
+-----------+----------------------------------------------------------+

AT+SOCCLOSE - Close Socket
~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------+----------------------------------------------------------+
| **        | at+socclose=<Socket ID>                                  |
| Command** |                                                          |
+===========+==========================================================+
| **R       | Success: OK                                              |
| esponse** |                                                          |
|           | Failure: Error                                           |
+-----------+----------------------------------------------------------+
| **Par     | Socket ID: Socket identifier                             |
| ameters** |                                                          |
+-----------+----------------------------------------------------------+
| **        | at+socclose=0                                            |
| Example** |                                                          |
+-----------+----------------------------------------------------------+

AT+HCSTART - Start HTTP Client
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------+-----------------------------------------------------------+
| **C      | at+hcstart=<Host Name>, <Port>, [<Secured>], [Certificate |
| ommand** | Name]                                                     |
+==========+===========================================================+
| **Re     | Success: HTTP client identifier followed by OK            |
| sponse** |                                                           |
|          | Failure: Error                                            |
|          |                                                           |
|          | Refer section `Command Response                           |
|          | Description <#_Command_Response_Description_1>`__ for     |
|          | more details                                              |
+----------+-----------------------------------------------------------+
| **Para   | Host Name: Remote server host name. It is either the      |
| meters** | domain name or the IP address.                            |
|          |                                                           |
|          | Port: Server port                                         |
|          |                                                           |
|          | Secured:                                                  |
|          |                                                           |
|          |    0: Non-Secured (HTTP),                                 |
|          |                                                           |
|          |    1: HTTPS without server certificate validation,        |
|          |                                                           |
|          |    2: HTTPS with server certificate validation            |
|          |                                                           |
|          |    **Note**: If no secured parameter is provided, 0 will  |
|          |    be taken as the value by default.                      |
|          |                                                           |
|          | Certificate Name: SSL certificate. This is needed only    |
|          | when Secured=2.                                           |
+----------+-----------------------------------------------------------+
| **E      | at+hcstart=192.168.2.184,80                               |
| xample** |                                                           |
+----------+-----------------------------------------------------------+

AT+HCREQSND – Send HTTP Client Request
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------+-----------------------------------------------------------+
| **C      | at+hcreqsnd=<HCID>,<Method>,<URI>, <Length>,<Data>        |
| ommand** |                                                           |
+==========+===========================================================+
| **Re     | Success:  200 - HTTP status code                          |
| sponse** |                                                           |
|          | Failure: ERROR                                            |
+----------+-----------------------------------------------------------+
| **Para   | HC ID: http client identifier                             |
| meters** |                                                           |
|          | Method: operation                                         |
|          |                                                           |
|          | -  1: GET                                                 |
|          |                                                           |
|          | -  2: HEAD                                                |
|          |                                                           |
|          | -  3: POST                                                |
|          |                                                           |
|          | -  4: PUT                                                 |
|          |                                                           |
|          | -  5: DEL                                                 |
|          |                                                           |
|          | URI: URI request string                                   |
|          |                                                           |
|          | Length: Number of bytes to send                           |
|          |                                                           |
|          | Data: Data to send                                        |
+----------+-----------------------------------------------------------+
| **E      | at+hcreqsnd=1,1,http://192.168.2.184/index.html           |
| xample** |                                                           |
|          | at+hcreqsnd =at+hcreqsnd=0,3,/post,6,MAC_ID               |
|          |                                                           |
|          | Note: Recommended practice of retry upon HTTP send        |
|          | failure will be:                                          |
|          |                                                           |
|          | -  Open HTTP client connection                            |
|          |                                                           |
|          | -  Set required headers                                   |
|          |                                                           |
|          | -  Execute HTTP GET/POST                                  |
|          |                                                           |
|          | -  If ERROR occurs, close the connection                  |
|          |                                                           |
|          | -  Reopen HTTP client connection                          |
|          |                                                           |
|          | -  Execute HTTP GET/POST                                  |
|          |                                                           |
|          | ..                                                        |
|          |                                                           |
|          |    so on and so forth...                                  |
+----------+-----------------------------------------------------------+

AT+HCHDRSET – Set HTTP Client Header
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------+-----------------------------------------------------------+
| **C      | at+hchdrset=<Header ID>,<Value>                           |
| ommand** |                                                           |
+==========+===========================================================+
| **Re     | Success:  OK                                              |
| sponse** |                                                           |
|          | Failure: ERROR                                            |
+----------+-----------------------------------------------------------+
| **Para   | Header ID: header ID                                      |
| meters** |                                                           |
|          | value: header value                                       |
|          |                                                           |
|          | The following values are valid header IDs and its         |
|          | corresponding header:                                     |
|          |                                                           |
|          | +---------+-------------------------------------------+   |
|          | |         |    **Header Name**                        |   |
|          | |  **ID** |                                           |   |
|          | +=========+===========================================+   |
|          | |    1    |    Allow                                  |   |
|          | +---------+-------------------------------------------+   |
|          | |    2    |    Authorization                          |   |
|          | +---------+-------------------------------------------+   |
|          | |    3    |    Connection type                        |   |
|          | +---------+-------------------------------------------+   |
|          | |    4    |    Content encoding                       |   |
|          | +---------+-------------------------------------------+   |
|          | |    5    |    Content length                         |   |
|          | +---------+-------------------------------------------+   |
|          | |    6    |    Content range                          |   |
|          | +---------+-------------------------------------------+   |
|          | |    7    |    Content type                           |   |
|          | +---------+-------------------------------------------+   |
|          | |    8    |    Http cookie                            |   |
|          | +---------+-------------------------------------------+   |
|          | |    9    |    Http cookie2 header                    |   |
|          | +---------+-------------------------------------------+   |
|          | |    10   |    Date and time                          |   |
|          | +---------+-------------------------------------------+   |
|          | |    11   |    Header expire date and time            |   |
|          | +---------+-------------------------------------------+   |
|          | |    12   |    Email address of user making the       |   |
|          | |         |    request.                               |   |
|          | +---------+-------------------------------------------+   |
|          | |    13   |    Domain name of server                  |   |
|          | +---------+-------------------------------------------+   |
|          | |    14   |    Resource modified date and time        |   |
|          | +---------+-------------------------------------------+   |
|          | |    15   |    Date and time which resource was last  |   |
|          | |         |    modified                               |   |
|          | +---------+-------------------------------------------+   |
|          | |    16   |    Redirect URL                           |   |
|          | +---------+-------------------------------------------+   |
|          | |    17   |    :mark:`Implementation specific header` |   |
|          | +---------+-------------------------------------------+   |
|          | |    18   |    Request only part of remote resource   |   |
|          | +---------+-------------------------------------------+   |
|          | |    19   |    Address of previous page from where it |   |
|          | |         |    requested current page                 |   |
|          | +---------+-------------------------------------------+   |
|          | |    20   |    Address of server generated response   |   |
|          | +---------+-------------------------------------------+   |
|          | |    21   |    Header to send cookie form server      |   |
|          | +---------+-------------------------------------------+   |
|          | |    22   |    Encoding Used                          |   |
|          | +---------+-------------------------------------------+   |
|          | |    23   |    String to specify the client           |   |
|          | +---------+-------------------------------------------+   |
|          | |    34   |    Authentication method used for access  |   |
|          | +---------+-------------------------------------------+   |
+----------+-----------------------------------------------------------+
| **E      | at+hchdrset=3,keep-alive                                  |
| xample** |                                                           |
|          | at+hchdrset=13,192.168.2.184                              |
+----------+-----------------------------------------------------------+

AT+HCHDRDEL – Delete HTTP Client Header
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------+----------------------------------------------------------+
| **        | at+hchdrdel=<HC ID>                                      |
| Command** |                                                          |
+===========+==========================================================+
| **R       | Success:  OK                                             |
| esponse** |                                                          |
|           | Failure: ERROR                                           |
+-----------+----------------------------------------------------------+
| **Par     | <if applicable>                                          |
| ameters** |                                                          |
+-----------+----------------------------------------------------------+
| **        | at+hchdrdel=0                                            |
| Example** |                                                          |
+-----------+----------------------------------------------------------+

AT+HCCLOSE – Close HTTP Connection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------+----------------------------------------------------------+
| **        | at+hcclose=<HC ID>                                       |
| Command** |                                                          |
+===========+==========================================================+
| **R       | Success:  OK                                             |
| esponse** |                                                          |
|           | Failure: ERROR                                           |
+-----------+----------------------------------------------------------+
| **Par     | HC ID: HTTP client identifier                            |
| ameters** |                                                          |
+-----------+----------------------------------------------------------+
| **        | at+hcclose=0                                             |
| Example** |                                                          |
+-----------+----------------------------------------------------------+

AT+MDNSREG – Register MDNS Service
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------+----------------------------------------------------------+
| **        | at+mdnsreg=<Service Name>,<Service type>, <Service       |
| Command** | Proto>,<Service Port>,<Service Description>              |
+===========+==========================================================+
| **R       | Success:“SER-ID:<Serviced ID>” message  followed OK      |
| esponse** |                                                          |
|           | Failure: ERROR                                           |
+-----------+----------------------------------------------------------+
| **Par     | Service Name: The service name                           |
| ameters** |                                                          |
|           | Service type: Type of service (HTTP)                     |
|           |                                                          |
|           | Service type: The service protocol                       |
|           |                                                          |
|           |    0: UDP                                                |
|           |                                                          |
|           |    1: TCP                                                |
|           |                                                          |
|           | Service Port: Port number used                           |
|           |                                                          |
|           | Service Description: Service description                 |
+-----------+----------------------------------------------------------+
| **        | at+mdnsreg=<servicename>,_HTTP,0,6553,<servicedesc>      |
| Example** |                                                          |
+-----------+----------------------------------------------------------+

AT+MDNSDREG – De-Register MDNS Service
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------+----------------------------------------------------------+
| **        | at+mdnsdreg=<Service ID>                                 |
| Command** |                                                          |
+===========+==========================================================+
| **R       | Success: OK                                              |
| esponse** |                                                          |
|           | Failure: ERROR                                           |
+-----------+----------------------------------------------------------+
| **Par     | Service ID: The service identifier                       |
| ameters** |                                                          |
+-----------+----------------------------------------------------------+
| **        | at+mdnsdreg=0                                            |
| Example** |                                                          |
+-----------+----------------------------------------------------------+

AT+MDNSSTART – Start MDNS
~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------+----------------------------------------------------------+
| **        | at+mdnsstart                                             |
| Command** |                                                          |
+===========+==========================================================+
| **R       | Success: OK                                              |
| esponse** |                                                          |
|           | Failure: ERROR                                           |
+-----------+----------------------------------------------------------+
| **Par     | NA                                                       |
| ameters** |                                                          |
+-----------+----------------------------------------------------------+
| **        | at+mdnsstart                                             |
| Example** |                                                          |
+-----------+----------------------------------------------------------+

AT+MDNSSTOP – Stop MDNS
~~~~~~~~~~~~~~~~~~~~~~~

+-----------+----------------------------------------------------------+
| **        | at+mdnsstop                                              |
| Command** |                                                          |
+===========+==========================================================+
| **R       | Success: OK                                              |
| esponse** |                                                          |
|           | Failure: ERROR                                           |
+-----------+----------------------------------------------------------+
| **Par     | NA                                                       |
| ameters** |                                                          |
+-----------+----------------------------------------------------------+
| **        | at+mdnsstop                                              |
| Example** |                                                          |
+-----------+----------------------------------------------------------+

AT+NHOSTIPGET – Get Host IP by Name
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------+----------------------------------------------------------+
| **        | at+nhostipget=<Host name>,[Family]                       |
| Command** |                                                          |
+===========+==========================================================+
| **R       | Success: “IP<family>:<ip address>” message followed by   |
| esponse** | OK                                                       |
|           |                                                          |
|           | Failure: ERROR                                           |
|           |                                                          |
|           | Refer section `Command Response                          |
|           | Description <#_Command_Response_Description_1>`__ for    |
|           | more details                                             |
+-----------+----------------------------------------------------------+
| **Par     | Host Name: The host name                                 |
| ameters** |                                                          |
|           | Family: protocol family                                  |
|           |                                                          |
|           |    0: IPv4                                               |
|           |                                                          |
|           |    1: IPv6                                               |
|           |                                                          |
|           | Default: It will be trying to resolve IPv4 first. If     |
|           | that fails, then tries IPv6.                             |
+-----------+----------------------------------------------------------+
| **        | at+nhostipget=www.google.com,0                           |
| Example** |                                                          |
+-----------+----------------------------------------------------------+

AT+NPING – Send Ping to Host
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------+----------------------------------------------------------+
| **        | at+nping=<IP address>                                    |
| Command** |                                                          |
+===========+==========================================================+
| **R       | Success: standard ping response followed by OK           |
| esponse** |                                                          |
|           | Failure: ERROR                                           |
|           |                                                          |
|           | Refer section `Command Response                          |
|           | Description <#_Command_Response_Description_1>`__ for    |
|           | more details                                             |
+-----------+----------------------------------------------------------+
| **Par     | IP address: IP address to ping.                          |
| ameters** |                                                          |
+-----------+----------------------------------------------------------+
| **        | at+nping=192.168.2.184                                   |
| Example** |                                                          |
+-----------+----------------------------------------------------------+

AT+CERTADD – Stores Certificate
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------+----------------------------------------------------------+
| **        | at+certadd=<Cert Name>,<Cert Len>                        |
| Command** |                                                          |
+===========+==========================================================+
| **R       | Success: OK                                              |
| esponse** |                                                          |
|           | Failure: ERROR                                           |
+-----------+----------------------------------------------------------+
| **Par     | Cert Name: Name of certificate.                          |
| ameters** |                                                          |
|           | Cert Len: Certificate length in bytes                    |
|           |                                                          |
|           | Procedure to send certificate                            |
|           |                                                          |
|           | -  After command validation Talaria TWO will send “<” as |
|           |    response to command.                                  |
|           |                                                          |
|           | -  Send certificate after receiving the command response |
|           |                                                          |
|           | -  OK/ERROR status message will send as response.        |
|           |                                                          |
|           | If certificate name already exists in T2, it will be     |
|           | overwritten.                                             |
|           |                                                          |
|           | **Certificate will be stored in RAM.**                   |
+-----------+----------------------------------------------------------+
| **        | at+certadd=ssl.pem,2614                                  |
| Example** |                                                          |
+-----------+----------------------------------------------------------+

AT+CERTDEL – Deletes Certificate
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------+----------------------------------------------------------+
| **        | at+certdel=<Cert name>                                   |
| Command** |                                                          |
+===========+==========================================================+
| **R       | Success: OK                                              |
| esponse** |                                                          |
|           | Failure: ERROR                                           |
+-----------+----------------------------------------------------------+
| **Par     | Cert Name: Name of certificate                           |
| ameters** |                                                          |
+-----------+----------------------------------------------------------+
| **        | at+certdel=ssl.pem                                       |
| Example** |                                                          |
+-----------+----------------------------------------------------------+

AT+HSSTART – Start HTTP Server
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------+----------------------------------------------------------+
| **        | at+hsstart=<Port number>                                 |
| Command** |                                                          |
+===========+==========================================================+
| **R       | Success: OK                                              |
| esponse** |                                                          |
|           | Failure: ERROR                                           |
+-----------+----------------------------------------------------------+
| **Par     | Port number: port number                                 |
| ameters** |                                                          |
+-----------+----------------------------------------------------------+
| **        | at+hcstart=192.168.2.184,80                              |
| Example** |                                                          |
+-----------+----------------------------------------------------------+

AT+MQTTCONF – Set MQTT configurations.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

One or more MQTT configurations can be set using this command. <key> is
the name of the configuration and <val> is the value for the <key> to be
set.

+------------+---------------------------------------------------------+
| *          | at+mqttconf=<key>,<val>,<key>,<val>….                   |
| *Command** |                                                         |
+============+=========================================================+
| **         | Success: OK                                             |
| Response** |                                                         |
|            | Failure: ERROR                                          |
+------------+---------------------------------------------------------+
| **Pa       | key: The name of the parameter to be set.               |
| rameters** |                                                         |
|            | The supported parameters are:                           |
|            |                                                         |
|            | -  clientid : MQTT client id (Connection will fail if   |
|            |    this is not set)                                     |
|            |                                                         |
|            | -  username : MQTT username                             |
|            |                                                         |
|            | -  password : MQTT password                             |
|            |                                                         |
|            | -  cleansession : 0/1 (Default 1)                       |
|            |                                                         |
|            | -  kainterval : Keep alive interval (Default 60 Sec)    |
+------------+---------------------------------------------------------+
| *          | at+mqttconf=clientid,123456                             |
| *Example** |                                                         |
|            | at+mqttconf=username,admin                              |
|            |                                                         |
|            | at+mqttconf=password,xyz                                |
|            |                                                         |
|            | at+mqttconf=kainterval,10 /\*keepalive interval of 10   |
|            | sec*/                                                   |
+------------+---------------------------------------------------------+

AT+MQTTCONN – Connect to MQTT Broker
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------+----------------------------------------------------------+
| **        | at+mqttconn<host name/IP address>,<port                  |
| Command** | number>,[<transport>],[cert verify],[<CA cert file       |
|           | name>],[<ws url>],[<client cert file name>],[<client key |
|           | file name>],[<connection timeout>]                       |
+===========+==========================================================+
| **R       | Connection ID followed by command response               |
| esponse** |                                                          |
|           | Success: OK                                              |
|           |                                                          |
|           | Failure: ERROR                                           |
+-----------+----------------------------------------------------------+
| **Par     | host name/IP address: It is either Fully Qualified       |
| ameters** | Domain name (FQDN) of the server or the IP address of    |
|           | the server to which the MQTT client opens the            |
|           | connection.                                              |
|           |                                                          |
|           | For example: mqtt.eclipseprojects.io or 137.135.83.217   |
|           |                                                          |
|           | port number: This gives the port number of the server to |
|           | which the MQTT client opens the connection to. The       |
|           | client can specify the port when the server is running   |
|           | on a non-standard port.                                  |
|           |                                                          |
|           | Default standard port: 1833: MQTT client, 8883: MQTT     |
|           | over SSL.                                                |
|           |                                                          |
|           | transport:                                               |
|           |                                                          |
|           | 0: MQTT over TCP (Default)                               |
|           |                                                          |
|           | 1: MQTT over TLS (Secured MQTT)                          |
|           |                                                          |
|           | 2: WebSocket                                             |
|           |                                                          |
|           | 3: MQTT over secured WebSocket                           |
|           |                                                          |
|           | cert verify: Used to enable certificate verification in  |
|           | case SSL is enabled.                                     |
|           |                                                          |
|           | CA cert file name: Name of the CA certificate to be used |
|           | for server certificate authentication in case SSL is     |
|           | enabled. The CA certificate must be provisioned before   |
|           | authentication.                                          |
|           |                                                          |
|           | ws url: WebSocket URL (Default is “/”).                  |
|           |                                                          |
|           | client cert file name: Name of the client certificate to |
|           | be used for client authentication. Client certificate    |
|           | must be provisioned before authentication.               |
|           |                                                          |
|           | client key file name: Name of the client key file to be  |
|           | used for client authentication. Client key must be       |
|           | provisioned before authentication.                       |
|           |                                                          |
|           | connection timeout: Maximum time to wait for the         |
|           | connection to go through. Maximum time being ~300s.      |
+-----------+----------------------------------------------------------+
| **        | at+mqttconn=test.mosquitto.org,8884,1,1,/data/m          |
| Example** | osquitto.org.crt,/mqtt,/data/client.crt,/data/client.key |
+-----------+----------------------------------------------------------+

AT+MQTTDISCONN – Disconnect MQTT Client Connection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------+----------------------------------------------------------+
| **        | at+mqttdisconn=<:mark:`nwid >`                           |
| Command** |                                                          |
+===========+==========================================================+
| **R       | Success: OK                                              |
| esponse** |                                                          |
|           | Failure: ERROR                                           |
+-----------+----------------------------------------------------------+
| **Par     | nwid: Network ID                                         |
| ameters** |                                                          |
+-----------+----------------------------------------------------------+
| **        | at+mqttdisconn=0                                         |
| Example** |                                                          |
+-----------+----------------------------------------------------------+

AT+MQTTSUB – Subscribe to the MQTT topic
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------+----------------------------------------------------------+
| **        | at+mqttsub=<:mark:`nwid `>,<:mark:`topic>,<qos>`         |
| Command** |                                                          |
+===========+==========================================================+
| **R       | Success: OK                                              |
| esponse** |                                                          |
|           | Failure: ERROR                                           |
+-----------+----------------------------------------------------------+
| **Par     | nwid: Network ID                                         |
| ameters** |                                                          |
|           | topic: Topic to subscribe                                |
|           |                                                          |
|           | qos: Qos of the topic                                    |
+-----------+----------------------------------------------------------+
| **        | at+mqttsub=0,inno/test,0                                 |
| Example** |                                                          |
+-----------+----------------------------------------------------------+

AT+MQTTUNSUB – Un-Subscribe to the MQTT Topic
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------+----------------------------------------------------------+
| **        | at+mqttunsub=<:mark:`nwid `>,<:mark:`topic>`             |
| Command** |                                                          |
+===========+==========================================================+
| **R       | Success: OK                                              |
| esponse** |                                                          |
|           | Failure: ERROR                                           |
+-----------+----------------------------------------------------------+
| **Par     | nwid: Network ID                                         |
| ameters** |                                                          |
|           | topic: Topic to un-subscribe                             |
+-----------+----------------------------------------------------------+
| **        | at+mqttunsub=0,inno/test                                 |
| Example** |                                                          |
+-----------+----------------------------------------------------------+

AT+MQTTPUB-Publish the MQTT Topic with Payload
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------+----------------------------------------------------------+
| **        | at+mqttpub=<:mark:`nwid `>, <topic:mark:`>, <qos>`,      |
| Command** | <len>,<payload>                                          |
+===========+==========================================================+
| **R       | Success: OK                                              |
| esponse** |                                                          |
|           | Failure: ERROR                                           |
+-----------+----------------------------------------------------------+
| **Par     | nwid: Network id                                         |
| ameters** |                                                          |
|           | topic: Topic to publish                                  |
|           |                                                          |
|           | qos: Qos of the topic                                    |
|           |                                                          |
|           | len: Data length                                         |
|           |                                                          |
|           | payload: Message payload                                 |
+-----------+----------------------------------------------------------+
| **        | at+mqttpub=0,inno/test,0,5,Hello                         |
| Example** |                                                          |
+-----------+----------------------------------------------------------+

AT+NTPTIMEGET – Gets time from NTP server
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------+----------------------------------------------------------+
| **        | at+ntptimeget                                            |
| Command** |                                                          |
+===========+==========================================================+
| **R       | Epoch time in µ seconds followed by:                     |
| esponse** |                                                          |
|           | Success: OK                                              |
|           |                                                          |
|           | Failure: ERROR                                           |
|           |                                                          |
|           | **Note**: Default server address is pool.ntp.org         |
+-----------+----------------------------------------------------------+
| **Par     | NA                                                       |
| ameters** |                                                          |
+-----------+----------------------------------------------------------+
| **        | at+ntptimeget                                            |
| Example** |                                                          |
+-----------+----------------------------------------------------------+

AT+FOTA – Start FOTA Operation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------+----------------------------------------------------------+
| **        | at+fota=<option>                                         |
| Command** |                                                          |
+===========+==========================================================+
| **R       | Success: Upon successful firmware upgrade, module        |
| esponse** | undergoes reset and provides AT command                  |
|           | serial-to-wireless prompt                                |
|           |                                                          |
|           | Failure: ERROR                                           |
+-----------+----------------------------------------------------------+
| **Par     | Option: Currently supported value is 1.                  |
| ameters** |                                                          |
|           | This parameter is used to start firmware upgrade. It     |
|           | uses fota_config.json file and starts the HTTP           |
|           | connection, downloads the new firmware and starts        |
|           | upgrading the firmware.                                  |
+-----------+----------------------------------------------------------+
| **        | at+fota=1                                                |
| Example** |                                                          |
+-----------+----------------------------------------------------------+

AT+FOTACFGADD – Update FOTA Configuration File (fota_config.json)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------+----------------------------------------------------------+
| **        | at+fotacfgadd=<len>                                      |
| Command** |                                                          |
+===========+==========================================================+
| **R       | Success:  OK                                             |
| esponse** |                                                          |
|           | Failure: ERROR                                           |
+-----------+----------------------------------------------------------+
| **Par     | len: size of the fota_config.json file in bytes.         |
| ameters** |                                                          |
|           | Procedure to send the certificate:                       |
|           |                                                          |
|           | -  Execute at+fotacfgadd=<len> command on the serial     |
|           |       terminal. Now the AT command application will be   |
|           |       waiting to receive the config file.                |
|           |                                                          |
|           | -  Send fota_config.json file from the serial terminal.  |
|           |                                                          |
|           | -  OK/ERROR response is sent upon success/failure of the |
|           |       command respectively.                              |
|           |                                                          |
|           | -  The fota_config.json file sent using this command     |
|           |       will replace the existing fota_config.json file in |
|           |       root fs.                                           |
+-----------+----------------------------------------------------------+
| **        | at+fotacfgadd=652                                        |
| Example** |                                                          |
+-----------+----------------------------------------------------------+

BT/BLE Commands
---------------

AT+BTNIT – Initialize BLE Stack
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------+----------------------------------------------------------+
| **        | at+btinit                                                |
| Command** |                                                          |
+===========+==========================================================+
| **R       | Success: OK                                              |
| esponse** |                                                          |
|           | Failure: ERROR                                           |
+-----------+----------------------------------------------------------+
| **Par     | NA                                                       |
| ameters** |                                                          |
+-----------+----------------------------------------------------------+
| **        | at+btinit                                                |
| Example** |                                                          |
+-----------+----------------------------------------------------------+

AT+BLECFG – Configure BLE Device
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------+----------------------------------------------------------+
| **        | at+blecfg=<address>,<address type>,<Device Name>         |
| Command** |                                                          |
+===========+==========================================================+
| **R       | Success: OK                                              |
| esponse** |                                                          |
|           | Failure: ERROR                                           |
+-----------+----------------------------------------------------------+
| **Par     | Address: BLE mac address.                                |
| ameters** |                                                          |
|           | Address type: BLE address type                           |
|           |                                                          |
|           |    0: BLE public address                                 |
|           |                                                          |
|           |    1: BLE random address                                 |
|           |                                                          |
|           | Device Name: BLE device name                             |
+-----------+----------------------------------------------------------+
| **        | at+blecfg=02:03:04:04:03:02, 0,testble                   |
| Example** |                                                          |
+-----------+----------------------------------------------------------+

AT+BLEADVCFG – Configure Advertisement Parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------+----------------------------------------------------------+
| **        | at+bleadvcfg=<Fast adv interval>,<Fast adv               |
| Command** | Duration>,<Slow adv interval>,<Slow adv Duration>        |
+===========+==========================================================+
| **R       | Success: OK                                              |
| esponse** |                                                          |
|           | Failure: ERROR                                           |
+-----------+----------------------------------------------------------+
| **Par     | Fast adv interval: Fast adverting interval in 625µs,     |
| ameters** | range: -0x0020 to 0x4000 (default:160)                   |
|           |                                                          |
|           | Fast adv duration: Fast advertisement duration in µs     |
|           |                                                          |
|           | Slow adv interval: Slow advertising interval in 625µs,   |
|           | range: -0x0020 to 0x4000                                 |
|           |                                                          |
|           | Slow adv duration: Slow advertisement duration in µs.    |
|           | After this time advertisement will be disabled           |
+-----------+----------------------------------------------------------+
| **        | at+bleadvcfg=160, 10, 160, 10                            |
| Example** |                                                          |
+-----------+----------------------------------------------------------+

AT+ BLEEXTADVCFG – Creates BLE Extended Advertisement
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------+----------------------------------------------------------+
| **        | at+bleextadvcfg= <use>, <adv_pri_phy>, <adv_sec_phy>,    |
| Command** | <adv_sid>, <conn_phy>, <conn_len>                        |
+===========+==========================================================+
| **R       | Success: OK                                              |
| esponse** |                                                          |
|           | Failure: ERROR                                           |
+-----------+----------------------------------------------------------+
| **Par     | use: Extended (5.0) usage: 1-legacy, 2-extended,         |
| ameters** | 3-legacy+extended (default: 1)                           |
|           |                                                          |
|           | adv_pri_phy: Primary PHY: 1-LE 1M, 3-LE Coded S2, 4-LE   |
|           | Coded S8 (default: 3)                                    |
|           |                                                          |
|           | adv_sec_phy: Secondary PHY: 1-LE 1M, 2-LE 2M, 3-LE Coded |
|           | (S2 or S8 according to adv_pri_phy) (default: 3)         |
|           |                                                          |
|           | adv_sid: Advertising SID (0..15) (default: 13)           |
|           |                                                          |
|           | conn_phy: Preferred phy(s) during connection - bit0: 1M, |
|           | bit1: 2M, bit2: CodedS2, bit3: CodedS8, 0=no preference  |
|           | (default: 2M)                                            |
|           |                                                          |
|           | conn_len: Maximum length of transmitted data during      |
|           | connection (27..251) (default: 27)                       |
+-----------+----------------------------------------------------------+
| **        | at+bleextadvcfg=2,1,1,1,1,251                            |
| Example** |                                                          |
+-----------+----------------------------------------------------------+

AT+BLEADVSTART – Start BLE Advertisement
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------+---------------------------------------------------------+
| *          | at+bleadvstart=[Adv data]                               |
| *Command** |                                                         |
+============+=========================================================+
| **         | Success: OK                                             |
| Response** |                                                         |
|            | Failure: ERROR                                          |
+------------+---------------------------------------------------------+
| **Pa       | Adv data: Advertisement data                            |
| rameters** |                                                         |
|            | **Note**: Advertisement data needs to be added          |
|            | according to the Bluetooth SIGS assigned numbers for    |
|            | the AD types                                            |
+------------+---------------------------------------------------------+
| *          | at+bleadvstart=0                                        |
| *Example** | 2010618ff55aa0100686f6e657977656c6c00686f6e657977656c6c |
+------------+---------------------------------------------------------+

AT+BLEADVSTOP – Stop BLE Advertisement
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------+---------------------------------------------------------+
| *          | at+bleadvstop                                           |
| *Command** |                                                         |
+============+=========================================================+
| **         | Success: OK                                             |
| Response** |                                                         |
|            | Failure: ERROR                                          |
+------------+---------------------------------------------------------+
| **Pa       | NA                                                      |
| rameters** |                                                         |
+------------+---------------------------------------------------------+
| *          | at+bleadvstop                                           |
| *Example** |                                                         |
+------------+---------------------------------------------------------+

AT+BLESERVCFG – Creates BLE GATT Service
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------+---------------------------------------------------------+
| *          | at+bleservcfg=<UUID>                                    |
| *Command** |                                                         |
+============+=========================================================+
| **         | Success: OK                                             |
| Response** |                                                         |
|            | Failure: ERROR                                          |
+------------+---------------------------------------------------------+
| **Pa       | UUID: Universal unique identifier, it can be either 16  |
| rameters** | bit, 32 bit or 128 bit.                                 |
+------------+---------------------------------------------------------+
| *          | at+bleservcfg=0x1111                                    |
| *Example** |                                                         |
+------------+---------------------------------------------------------+

AT+BLESERVADD – Adds BLE GATT Service
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------+---------------------------------------------------------+
| *          | at+bleservadd=<UUID >                                   |
| *Command** |                                                         |
+============+=========================================================+
| **         | Success: OK                                             |
| Response** |                                                         |
|            | Failure: ERROR                                          |
+------------+---------------------------------------------------------+
| **Pa       | UUID: Universal unique identifier, it can be either 16  |
| rameters** | bit, 32 bit or 128 bit.                                 |
+------------+---------------------------------------------------------+
| *          | at+bleservadd=0x1111                                    |
| *Example** |                                                         |
+------------+---------------------------------------------------------+

AT+BLESERVDEL – Removes BLE GATT Service
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------+---------------------------------------------------------+
| *          | at+bleservdel=<UUID >                                   |
| *Command** |                                                         |
+============+=========================================================+
| **         | Success: OK                                             |
| Response** |                                                         |
|            | Failure: ERROR                                          |
+------------+---------------------------------------------------------+
| **Pa       | UUID: Universal unique identifier, it can be either 16  |
| rameters** | bit, 32 bit or 128 bit.                                 |
+------------+---------------------------------------------------------+
| *          | at+bleservdel=0x1111                                    |
| *Example** |                                                         |
+------------+---------------------------------------------------------+

AT+BLECHRADD - Add Characteristic to Service
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------+---------------------------------------------------------+
| *          | at+blechradd= <Services uuid>,<Char uuid>,              |
| *Command** | <Properties>,<Permission>                               |
+============+=========================================================+
| **         | Success: OK                                             |
| Response** |                                                         |
|            | Failure: ERROR                                          |
+------------+---------------------------------------------------------+
| **Pa       | Services uuid: Service UUID                             |
| rameters** |                                                         |
|            | Char uuid: Characteristic Universal unique identifier   |
|            |                                                         |
|            | Properties: Properties for the characteristic. The      |
|            | valid values are:                                       |
|            |                                                         |
|            | -  0x01: broadcast                                      |
|            |                                                         |
|            | -  0x02: read                                           |
|            |                                                         |
|            | -  0x04: write without response                         |
|            |                                                         |
|            | -  0x08: write                                          |
|            |                                                         |
|            | -  0x10: notify                                         |
|            |                                                         |
|            | -  0x20: indicate                                       |
|            |                                                         |
|            | -  0x40: signed write (not supported)                   |
|            |                                                         |
|            | -  0x80: extended properties (not supported)            |
|            |                                                         |
|            | **Note**: To set multiple properties, pass the logical  |
|            | or the above values and set the required properties.    |
|            |                                                         |
|            | Permission: Permissions for the characteristic. The     |
|            | valid values are:                                       |
|            |                                                         |
|            | -  0x01: Read                                           |
|            |                                                         |
|            | -  0x02: Write                                          |
|            |                                                         |
|            | -  0x03: Read and Write                                 |
|            |                                                         |
|            | -  0x04: Encrypt                                        |
|            |                                                         |
|            | -  0x08: Authenticate                                   |
|            |                                                         |
|            | -  0x10: Authorize                                      |
|            |                                                         |
|            | -  0x20: Encode with key size 128                       |
|            |                                                         |
|            | -  0x80: Signed                                         |
|            |                                                         |
|            | -  0x100: Signed MITM                                   |
|            |                                                         |
|            | **Note**:                                               |
|            |                                                         |
|            | 1. To set multiple permissions, pass the logical or     |
|            |    the above values and set the required permissions.   |
|            |                                                         |
|            | 2. The values for permission and properties must be     |
|            |    configured in hexadecimal format.                    |
+------------+---------------------------------------------------------+
| *          | at+blechradd=0x1111,0x2a19,0x0c,0x03                    |
| *Example** |                                                         |
|            | at+blechradd=0x1111,0x2a19,0x5c,0x03                    |
+------------+---------------------------------------------------------+

AT+BLEDESCADD - Add Descriptor to Characteristics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-------------+--------------------------------------------------------+
| **Command** | at+bledescadd=<characteristics uuid>,<descriptor       |
|             | uuid>, <Properties>,<Permission >                      |
+=============+========================================================+
| *           | Success: OK                                            |
| *Response** |                                                        |
|             | Failure: ERROR                                         |
+-------------+--------------------------------------------------------+
| **P         | characteristics uuid: Characteristics UUID             |
| arameters** |                                                        |
|             | descriptor uuid: UUID of descriptor                    |
|             |                                                        |
|             | Properties: Properties for the characteristic. The     |
|             | valid values are:                                      |
|             |                                                        |
|             | -  0x01: broadcast                                     |
|             |                                                        |
|             | -  0x02: read                                          |
|             |                                                        |
|             | -  0x04: write without response                        |
|             |                                                        |
|             | -  0x08: write                                         |
|             |                                                        |
|             | -  0x10: notify                                        |
|             |                                                        |
|             | -  0x20: indicate                                      |
|             |                                                        |
|             | -  0x40: signed write (not supported)                  |
|             |                                                        |
|             | -  0x80: extended properties (not supported)           |
|             |                                                        |
|             | **Note**: To set multiple properties, pass the logical |
|             | or the above values and set the required properties.   |
|             |                                                        |
|             | Permission: Permissions for the characteristic. The    |
|             | valid values are                                       |
|             |                                                        |
|             | -  0x03: Read and write                                |
|             |                                                        |
|             | **Note**: Permission and properties values must be     |
|             | configured in hexadecimal format.                      |
+-------------+--------------------------------------------------------+
| **Example** | at+bledescadd=0x2a19,0x2901,0x0c,0x03                  |
|             |                                                        |
|             | at+bledescadd=0x2a19,0x2901,0x5c,0x03                  |
+-------------+--------------------------------------------------------+

AT+BLESRVSTART – Start BLE GATT Server
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-------------+--------------------------------------------------------+
| **Command** | at+blesrvstart                                         |
+=============+========================================================+
| *           | Success: OK                                            |
| *Response** |                                                        |
|             | Failure: ERROR                                         |
+-------------+--------------------------------------------------------+
| **P         | NA                                                     |
| arameters** |                                                        |
+-------------+--------------------------------------------------------+
| **Example** | at+blesrvstart                                         |
+-------------+--------------------------------------------------------+

AT+BLESRVSTOP – Stop BLE GATT Server
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-------------+--------------------------------------------------------+
| **Command** | at+blesrvstop                                          |
+=============+========================================================+
| *           | Success: OK                                            |
| *Response** |                                                        |
|             | Failure: ERROR                                         |
+-------------+--------------------------------------------------------+
| **P         | NA                                                     |
| arameters** |                                                        |
+-------------+--------------------------------------------------------+
| **Example** | at+blesrvstop                                          |
+-------------+--------------------------------------------------------+

AT+BLENOTIFY – Notify BLE GATT Characteristic
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-------------+--------------------------------------------------------+
| **Command** | at+blenotify=<char uuid>,<len>, <data>                 |
+=============+========================================================+
| *           | Success: OK                                            |
| *Response** |                                                        |
|             | Failure: ERROR                                         |
+-------------+--------------------------------------------------------+
| **P         | Char uuid: Characteristic UUID                         |
| arameters** |                                                        |
|             | Len: Length of data, in hexadecimal format             |
|             |                                                        |
|             | Data: Notification data, in ASCII format               |
+-------------+--------------------------------------------------------+
| **Example** | at+blenotify=0x1234,a,Hello12345                       |
+-------------+--------------------------------------------------------+

AT+BLEIND – Indicates BLE GATT Characteristic
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-------------+--------------------------------------------------------+
| **Command** | at+bleind=<char uuid>,<len>,<data>                     |
+=============+========================================================+
| *           | Success: OK                                            |
| *Response** |                                                        |
|             | Failure: ERROR                                         |
+-------------+--------------------------------------------------------+
| **P         | char uuid: Characteristic UUID                         |
| arameters** |                                                        |
|             | len: Length of data, in hexadecimal format             |
|             |                                                        |
|             | data: Indication data, in ASCII format                 |
+-------------+--------------------------------------------------------+
| **Example** | at+bleind=2a19,a,12345hello                            |
+-------------+--------------------------------------------------------+

AT+BLECHARRDDATA – Sends data for BLE Characteristic Read Request
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-------------+--------------------------------------------------------+
| **Command** | at+blecharrddata=<uuid>,<data len>,<data>              |
+=============+========================================================+
| *           | Success: OK                                            |
| *Response** |                                                        |
|             | Failure: ERROR                                         |
+-------------+--------------------------------------------------------+
| **P         | uuid: Characteristic UUID                              |
| arameters** |                                                        |
|             | data len: Length of data in hexadecimal format         |
|             |                                                        |
|             | data: Actual data for characteristic read request, in  |
|             | ASCII format                                           |
|             |                                                        |
|             | If the data contains a special character, then it has  |
|             | to be pre-appended with a slash (0x5C)                 |
+-------------+--------------------------------------------------------+
| **Example** | at+blecharrddata=2a29,a,6162636465                     |
+-------------+--------------------------------------------------------+

AT+BLEDESCRDDATA – Sends data for BLE Descriptor Read Request
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-------------+--------------------------------------------------------+
| **Command** | at+bledescrddata=<uuid>,<data len>,<data>              |
+=============+========================================================+
| *           | Success: OK                                            |
| *Response** |                                                        |
|             | Failure: ERROR                                         |
+-------------+--------------------------------------------------------+
| **P         | uuid: Descriptor UUID                                  |
| arameters** |                                                        |
|             | data len: Length of data in hexadecimal format         |
|             |                                                        |
|             | data: Actual data for characteristic read request, in  |
|             | ASCII format                                           |
+-------------+--------------------------------------------------------+
| **Example** | at+bledescrddata=2902,a,6162636465                     |
+-------------+--------------------------------------------------------+

AT+BLECHARWRDATA – Acknowledges BLE Characteristic Write Request
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-------------+--------------------------------------------------------+
| **Command** | at+blecharwrdata=<uuid>,<data len>                     |
+=============+========================================================+
| *           | Success: OK                                            |
| *Response** |                                                        |
|             | Failure: ERROR                                         |
+-------------+--------------------------------------------------------+
| **P         | uuid: Characteristic UUID                              |
| arameters** |                                                        |
|             | data len: Length of data written in hexadecimal format |
+-------------+--------------------------------------------------------+
| **Example** | at+blecharwrdata=2a29,4                                |
+-------------+--------------------------------------------------------+

AT+BLEDESCWRDATA – Acknowledges BLE Descriptor Write Request
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-------------+--------------------------------------------------------+
| **Command** | at+bledescwrdata=<uuid>,<data len>,<data>              |
+=============+========================================================+
| *           | Success: OK                                            |
| *Response** |                                                        |
|             | Failure: ERROR                                         |
+-------------+--------------------------------------------------------+
| **P         | uuid: Descriptor UUID                                  |
| arameters** |                                                        |
|             | data len: Length of data in hexadecimal format         |
|             |                                                        |
|             | data: Actual data for characteristic read request      |
|             | (ASCII format)                                         |
+-------------+--------------------------------------------------------+
| **Example** | at+bledescwrdata=2a29,4,1234                           |
+-------------+--------------------------------------------------------+

AT+BLESCANCFG – Configure BLE Scan Parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------+-------------------------------------------------------------+
| **Com  | at+blescancfg=<scan_period>,<scan_inte                      |
| mand** | rval>,<scan_win>,<bscan_interval>,<bscan_win>,<scan_filter> |
+========+=============================================================+
| **Resp | Success: OK                                                 |
| onse** |                                                             |
|        | Failure: ERROR                                              |
+--------+-------------------------------------------------------------+
| **     | scan_period: Foreground scan period in ms (default: 10240)  |
| Parame |                                                             |
| ters** | scan_interval: Scan interval in 625 µs, range: 4 to 16384   |
|        | (default: 96)                                               |
|        |                                                             |
|        | scan_win: Scan window in 625 µs, range: 4 to 16384          |
|        | (default: 48)                                               |
|        |                                                             |
|        | bscan_interval: Background scan interval in 625 µs, range:  |
|        | 4 to 16384 (default: 2048)                                  |
|        |                                                             |
|        | bscan_win: Background scan window in 625 µs, range: 4 to    |
|        | 16384 (default: 18)                                         |
|        |                                                             |
|        | scan_filter: Filter duplicates (1=True, 0=False) (default:  |
|        | 1)                                                          |
|        |                                                             |
|        | **Note**: Background scan is used if the device has         |
|        | existing connections. All the above parameters are in       |
|        | decimal.                                                    |
+--------+-------------------------------------------------------------+
| **Exa  | at+blescancfg=5000,96,48,96,24,1                            |
| mple** |                                                             |
+--------+-------------------------------------------------------------+

AT+BLECONCFG – Configure BLE Connection Parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-------------+--------------------------------------------------------+
| **Command** | at+bleconcfg=<con_interval>, <con_latency>,            |
|             | <con_timeout>, <con_storeparam>, <con_interval_min>,   |
|             | <con_interval_max>                                     |
+=============+========================================================+
| *           | Success: OK                                            |
| *Response** |                                                        |
|             | Failure: ERROR                                         |
+-------------+--------------------------------------------------------+
| **P         | con_interval: Connection interval in 1.25ms, range: 6  |
| arameters** | to 3200 (default: 80)                                  |
|             |                                                        |
|             | con_latency: Connection latency in interval, range: 0  |
|             | to 499 (default: 0)                                    |
|             |                                                        |
|             | con_timeout: Connection timeout in ms, range: 10 to    |
|             | 3200 (default: 2000)                                   |
|             |                                                        |
|             | con_storeparam: Rejects parameter update (1=True,      |
|             | 0=False) (default: 0)                                  |
|             |                                                        |
|             | con_interval_min: Minimum connection interval in       |
|             | 1.25ms (default: 6)                                    |
|             |                                                        |
|             | con_interval_max: Maximum connection interval in       |
|             | 1.25ms (default: 800)                                  |
|             |                                                        |
|             | **Note**: All above parameters are in decimal.         |
+-------------+--------------------------------------------------------+
| **Example** | at+bleconcfg=80,0,2000,0,6,800                         |
+-------------+--------------------------------------------------------+

AT+BLESCAN – Start/Stop BLE Scan
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-------------+--------------------------------------------------------+
| **Command** | at+blescan                                             |
+=============+========================================================+
| *           | Success: OK                                            |
| *Response** |                                                        |
|             | Failure: ERROR                                         |
|             |                                                        |
|             | Following scan results are sent:                       |
|             |                                                        |
|             | <mac address>:<RSSI>:<address type>:<data len>:<data>  |
+-------------+--------------------------------------------------------+
| **P         | NA                                                     |
| arameters** |                                                        |
+-------------+--------------------------------------------------------+
| **Example** | at+blescan                                             |
+-------------+--------------------------------------------------------+

AT+BLECON – Connects to BLE Device
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-------------+--------------------------------------------------------+
| **Command** | at+blecon=<Peer address>,<Peer address type>           |
+=============+========================================================+
| *           | Success: connection id with OK                         |
| *Response** |                                                        |
|             | Failure: ERROR                                         |
+-------------+--------------------------------------------------------+
| **P         | Peer address: Address of remote BLE device.            |
| arameters** |                                                        |
|             | Peer address type: Peer address type                   |
|             |                                                        |
|             |    0: Public address                                   |
|             |                                                        |
|             |    1: Random address                                   |
|             |                                                        |
|             | **Note**: If BLE connection issues are observed due to |
|             | noisy environments or extended distance, BLE Tx power  |
|             | can be increased to a maximum of 10dBm.                |
+-------------+--------------------------------------------------------+
| **Example** | at+blecon=00-01-02-03-04-05,0                          |
+-------------+--------------------------------------------------------+

AT+BLEDISCON – Disconnects the BLE Device
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-------------+--------------------------------------------------------+
| **Command** | at+blediscon=<connection id>                           |
+=============+========================================================+
| *           | Success: OK                                            |
| *Response** |                                                        |
|             | Failure: ERROR                                         |
+-------------+--------------------------------------------------------+
| **P         | Connection id: Connection identifier                   |
| arameters** |                                                        |
+-------------+--------------------------------------------------------+
| **Example** | at+blediscon=0                                         |
+-------------+--------------------------------------------------------+

AT+BLESERDIS – Discover All Services
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-------------+--------------------------------------------------------+
| **Command** | at+bleserdis=<connection id>                           |
+=============+========================================================+
| *           | Success: service information followed by OK            |
| *Response** |                                                        |
|             | Failure: ERROR                                         |
|             |                                                        |
|             | Service information is sent as described:              |
|             |                                                        |
|             | <start handle>:<end handle>:<len>:<uuid>               |
|             |                                                        |
|             | **Note**: All parameters are to be sent in hexadecimal |
|             | format                                                 |
+-------------+--------------------------------------------------------+
| **P         | Connection id: Connection identifier                   |
| arameters** |                                                        |
+-------------+--------------------------------------------------------+
| **Example** | at+bleserdis=0                                         |
+-------------+--------------------------------------------------------+

AT+BLECHARDIS – Discover All GATT Characteristic of a Service
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-------------+--------------------------------------------------------+
| **Command** | at+blechardis=<Connection id>, <Start handle>, <End    |
|             | Handle>                                                |
+=============+========================================================+
| *           | Success: Characteristic information followed by OK     |
| *Response** |                                                        |
|             | Failure: ERROR                                         |
|             |                                                        |
|             | Characteristic information is sent as described:       |
|             |                                                        |
|             | <handle>:<properties>:<value handle>:length>:<uuid>    |
|             |                                                        |
|             | **Note**: All parameters are to be sent in hexadecimal |
|             | format                                                 |
+-------------+--------------------------------------------------------+
| **P         | Connection id: Connection identifier                   |
| arameters** |                                                        |
|             | Start handle: Attribute start handle of the service    |
|             |                                                        |
|             | End handle: Attribute end handle of the service        |
+-------------+--------------------------------------------------------+
| **Example** | at+blechardis=0,31,ffff                                |
+-------------+--------------------------------------------------------+

AT+BLEDESDIS – Discover All GATT Characteristic Descriptors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------+----------------------------------------------------------+
| **        | at+bledesdis=<connection id>, <Start handle>, <End       |
| Command** | Handle>                                                  |
+===========+==========================================================+
| **R       | Success: Characteristic descriptor information followed  |
| esponse** | by OK                                                    |
|           |                                                          |
|           | Failure: ERROR                                           |
|           |                                                          |
|           | Characteristic descriptor information is sent as:        |
|           |                                                          |
|           | <handle>:<len>:<uuid>                                    |
|           |                                                          |
|           | **Note**: All parameters are to be sent in hexadecimal   |
|           | format                                                   |
+-----------+----------------------------------------------------------+
| **Par     | Connection id: Connection identifier                     |
| ameters** |                                                          |
|           | Start handle: Attribute start handle of the              |
|           | characteristic                                           |
|           |                                                          |
|           | End handle: Attribute end handle of the characteristic   |
+-----------+----------------------------------------------------------+
| **        | at+bledesdis=0,31,ffff                                   |
| Example** |                                                          |
+-----------+----------------------------------------------------------+

AT+BLECHARRD – Reads GATT Characteristic Value
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------+----------------------------------------------------------+
| **        | at+blecharrd=<connection id>,<Handle>                    |
| Command** |                                                          |
+===========+==========================================================+
| **R       | Success: Characteristic value followed by OK.            |
| esponse** |                                                          |
|           | Failure: ERROR.                                          |
+-----------+----------------------------------------------------------+
| **Par     | Connection id: Connection identifier                     |
| ameters** |                                                          |
|           | Handle: Attribute handle, in hexadecimal format          |
+-----------+----------------------------------------------------------+
| **        | at+blecharrd=0,0033                                      |
| Example** |                                                          |
+-----------+----------------------------------------------------------+

AT+BLECHARWR – Writes GATT Characteristic Value
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------+----------------------------------------------------------+
| **        | at+blecharwr=<connection id>,<type>,<Handle>, <Length>,  |
| Command** | <data>                                                   |
+===========+==========================================================+
| **R       | Success: OK followed by characteristic value             |
| esponse** |                                                          |
|           | Failure: ERROR                                           |
+-----------+----------------------------------------------------------+
| **Par     | Connection id: Connection identifier                     |
| ameters** |                                                          |
|           | Type: Write type                                         |
|           |                                                          |
|           |    0: Write                                              |
|           |                                                          |
|           |    1: Write with response                                |
|           |                                                          |
|           |    2: Signed write (currently not supported)             |
|           |                                                          |
|           | Handle: Attribute handle, in decimal format              |
|           |                                                          |
|           | Length: Number of bytes to write, in decimal format      |
|           |                                                          |
|           | Data: Data to write, in ASCII format                     |
+-----------+----------------------------------------------------------+
| **        | at+blecharwr=0,1,51,1,1                                  |
| Example** |                                                          |
+-----------+----------------------------------------------------------+

AT+BLESMPCFG – Configure the SMP (Security)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------+----------------------------------------------------------+
| **        | at+blesmpcfg=<io                                         |
| Command** | cap>,<oob>,<bondable>,<mitm>,<sc>,<keypress>,< key size  |
|           | min>,<encrypt>                                           |
+===========+==========================================================+
| **R       | Success: OK followed by characteristic value.            |
| esponse** |                                                          |
|           | Failure: ERROR.                                          |
+-----------+----------------------------------------------------------+
| **Par     | Iocap: IO capabilities (default: display_only=0)         |
| ameters** |                                                          |
|           | oob: OOB data present (default: 0).                      |
|           |                                                          |
|           | bondable: Bondable (1=True, 0=False) (default: 0)        |
|           |                                                          |
|           | mitm: MITM (Man In The Middle) protection requested      |
|           | (1=True, 0=False) (default: 0)                           |
|           |                                                          |
|           | sc: Secure Connection supported (1=True, 0=False)        |
|           | (default: 0)                                             |
|           |                                                          |
|           | keypress: Generate keypress notifications (1=True,       |
|           | 0=False) (default: 0)                                    |
|           |                                                          |
|           | key size min: Minimal key size (bytes) that is accepted  |
|           | (7..16) (default: 16)                                    |
|           |                                                          |
|           | encrypt: Automatically encrypt link at connection setup  |
|           | if key exists: 1=True, 0=False (default: 0)              |
+-----------+----------------------------------------------------------+
| **        | at+blesmpcfg=0,0,1,0,0,0,16,1                            |
| Example** |                                                          |
+-----------+----------------------------------------------------------+

AT+BLEAUTH – Configure the SMP (Security)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------+----------------------------------------------------------+
| **        | at+bleauth=< Connection id>,<oob>, <bondable>, <mitm>,   |
| Command** | <sc>, <key>                                              |
+===========+==========================================================+
| **R       | Success: OK followed by characteristic value             |
| esponse** |                                                          |
|           | Failure: ERROR                                           |
+-----------+----------------------------------------------------------+
| **Par     | connection id: Connection identifier.                    |
| ameters** |                                                          |
|           | oob: OOB data present (default: 0)                       |
|           |                                                          |
|           | bondable: Bondable (1=True, 0=False) (default: 0)        |
|           |                                                          |
|           | mitm: MITM (Man In The Middle) protection requested      |
|           | (1=True, 0=False) (default: 0)                           |
|           |                                                          |
|           | sc: Secure Connection supported (1=True, 0=False)        |
|           | (default: 0)                                             |
|           |                                                          |
|           | keypress: 128-bits key required (1=True, 0=False)        |
+-----------+----------------------------------------------------------+
| **        | at+bleauth=0,0,0,0,1,128                                 |
| Example** |                                                          |
+-----------+----------------------------------------------------------+

AT+BLFOTACONF – BLE FOTA Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------+----------------------------------------------------------+
| **        | at+blefotaconf=<Service id>,<Characteristics id>         |
| Command** |                                                          |
+===========+==========================================================+
| **R       | Success: OK followed by characteristic value             |
| esponse** |                                                          |
|           | Failure: ERROR                                           |
+-----------+----------------------------------------------------------+
| **Par     | Service id: Service identifier.                          |
| ameters** |                                                          |
|           | Characteristics id: Characteristics identifier           |
+-----------+----------------------------------------------------------+
| **        | at+blefotaconf=0x1111,2Af9                               |
| Example** |                                                          |
+-----------+----------------------------------------------------------+

**Note**: The characteristics id used for FOTA service should not be
shared with any other characteristics.

AT+BTBONDLIST – BLE BOND Information Display
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------+----------------------------------------------------------+
| **        | at+btbondlist                                            |
| Command** |                                                          |
+===========+==========================================================+
| **R       | Success: Each entry of the bonded information followed   |
| esponse** | by OK. Each entry will be in the format:                 |
|           | macaddress,type. Multiple entries are separated by a     |
|           | colon.                                                   |
|           |                                                          |
|           | Failure: ERROR                                           |
+-----------+----------------------------------------------------------+
| **Par     | None.                                                    |
| ameters** |                                                          |
+-----------+----------------------------------------------------------+
| **        | at+blebondlist                                           |
| Example** |                                                          |
+-----------+----------------------------------------------------------+

**Note**: The current BLE bond feature supports storage of 10 keys. In
case of more keys, it will overwrite the oldest one created so that at
any given time, the maximum number of keys stored is 10.

AT+BTBONDDEL – Delete a BLE BOND Information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------+---------------------------------------------------------+
| *          | at+btbonddel=<mac address>                              |
| *Command** |                                                         |
+============+=========================================================+
| **         | Success: OK                                             |
| Response** |                                                         |
|            | Failure: ERROR                                          |
+------------+---------------------------------------------------------+
| **Pa       | macaddress: The mac address of the bonded device. The   |
| rameters** | mac address should be provided with colons.             |
+------------+---------------------------------------------------------+
| *          | at+btbonddel=01:02:fe:a2:22:88                          |
| *Example** |                                                         |
+------------+---------------------------------------------------------+

AT+PROVSTART – BLE PROVISIONING
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------+----------------------------------------------------------+
| **        | at+provstart=<0/1>                                       |
| Command** |                                                          |
+===========+==========================================================+
| **R       | Success: OK                                              |
| esponse** |                                                          |
|           | Failure: ERROR                                           |
+-----------+----------------------------------------------------------+
| **Par     | 0: after provisioned, the provision info stores in       |
| ameters** | Talaria TWO flash, set the provisioned flag to 1 and     |
|           | system restarts and connect to provided SSID             |
|           |                                                          |
|           | 1: after provisioned, the provision info sends to Host   |
+-----------+----------------------------------------------------------+
| **        | at+provstart =1                                          |
| Example** |                                                          |
+-----------+----------------------------------------------------------+

**Note**: part.json file needs to be loaded from the prov example
application.

AT+PROVSTOP – STOP BLE PROVISIONING
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------+----------------------------------------------------------+
| **        | at+provstop                                              |
| Command** |                                                          |
+===========+==========================================================+
| **R       | Success: OK                                              |
| esponse** |                                                          |
|           | Failure: ERROR                                           |
+-----------+----------------------------------------------------------+
| **Par     | None                                                     |
| ameters** |                                                          |
+-----------+----------------------------------------------------------+
| **        | at+provstop                                              |
| Example** |                                                          |
+-----------+----------------------------------------------------------+

AT+BTTXPOWSET – Set BLE TX Power 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------+----------------------------------------------------------+
| **        | at+bttxpowset=<tx_power>                                 |
| Command** |                                                          |
+===========+==========================================================+
| **R       | Success: OK                                              |
| esponse** |                                                          |
|           | Failure: ERROR                                           |
+-----------+----------------------------------------------------------+
| **Par     | tx_power: TX power in dBm (-20 to 10)                    |
| ameters** |                                                          |
+-----------+----------------------------------------------------------+
| **        | at+bttxpowset=10                                         |
| Example** |                                                          |
+-----------+----------------------------------------------------------+

AT+BTTXPOWGET – Get BLE TX Power 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------+----------------------------------------------------------+
| **        | at+bttxpowget                                            |
| Command** |                                                          |
+===========+==========================================================+
| **R       | Success: OK                                              |
| esponse** |                                                          |
|           | Failure: ERROR                                           |
+-----------+----------------------------------------------------------+
| **Par     | NA.                                                      |
| ameters** |                                                          |
|           | Gets the set BLE TX power.                               |
+-----------+----------------------------------------------------------+
| **        | at+bttxpowget                                            |
| Example** |                                                          |
+-----------+----------------------------------------------------------+
