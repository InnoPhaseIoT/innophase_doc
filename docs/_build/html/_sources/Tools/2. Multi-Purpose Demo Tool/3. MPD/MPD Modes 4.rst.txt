Select the MPD tab on the Demo tool GUI to automatically load the signed
firmware image for MPD application.

**Note**: For all the modes, the Keep Alive Wake time is fixed as 2 in
the application. This time is the time window in milliseconds during
which Talaria TWO will wait in receive mode before going to sleep.

Select the appropriate mode and enter the values specific to the mode
selected. Failure to pass any value will result in an error. Click on
either PROG RAM/Flash as per requirement.

Base Mode
---------

**Expected Result**: Spike should be observed as per the Beacon listen
interval configured. If beacon listen interval is configured as 10, then
radio wakes up to listen beacon for every 1 second.

**Otii log**: Shows an average current consumption of 56.7µA for 30s.

|image1|

Figure : Base mode: Otii log

Console output:

+-----------------------------------------------------------------------+
| UART:SNWWWWWAEBuild $Id: git-ba65998b7 $                              |
|                                                                       |
| mpd.mcast_rx=1 wifi.listen_interval=10 krn.gpio=--K                   |
| wifi.keep_alive_wake_time=2 wifi.arp_grat_period=1800                 |
| wifi.max_idle_period=0 mpd.regdomain=FCC mpd.suspend=1                |
| np_conf_path=/data/nprofile.json mpd.ssid=InnoPhase                   |
| mpd.passphrase=43083191                                               |
|                                                                       |
| $App:git-73e7f910                                                     |
|                                                                       |
| SDK Ver: FREERTOS_SDK_1.0T2 Multipurpose Demp App Version 0.12        |
|                                                                       |
| network profile parse success.                                        |
|                                                                       |
| Suspend Enabled.                                                      |
|                                                                       |
| Multicast reception Enabled.                                          |
|                                                                       |
| Regdomain=FCC                                                         |
|                                                                       |
| addr e0:69:3a:00:13:90                                                |
|                                                                       |
| Applying reg domain: 1-11@20                                          |
|                                                                       |
| Connecting to network                                                 |
|                                                                       |
| .[2.018,216] CONNECT:00:5f:67:cd:c5:a6 Channel:11 rssi:-44 dBm        |
|                                                                       |
| WCM_NOTIFY_MSG_LINK_UP                                                |
|                                                                       |
| .WCM_NOTIFY_MSG_ADDRESS                                               |
|                                                                       |
| [2.837,656] MYIP 192.168.0.104                                        |
|                                                                       |
| [2.837,819] IPv6 [fe80::e269:3aff:fe00:1390]-link                     |
|                                                                       |
| WCM_NOTIFY_MSG_CONNECTED                                              |
|                                                                       |
| Listen interval=10                                                    |
|                                                                       |
| Traffic Timeout=12                                                    |
|                                                                       |
| pm_flags=0x0                                                          |
|                                                                       |
| [3.498,504] WARNING! wcm_pm_config may overwrite the supplied power   |
| management boot arguments!                                            |
|                                                                       |
| WiFi Connection success. proceeding to app..                          |
|                                                                       |
| Timeout not specified.!                                               |
|                                                                       |
| Application Exited..                                                  |
|                                                                       |
| Going for indefinite sleep...                                         |
+=======================================================================+
+-----------------------------------------------------------------------+

Keep Alive Mode
---------------

**Note**:

To reduce power consumption, the Keep Alive messages are aligned to the
next beacon reception period. The actual Keepalive Interval can
therefore be longer than specified, especially if the
wifi.listen_interval is set to a high value.

**Wireshark log**:

**Expected Result**:

Based on the configured keepalive interval (10s), QoS Null function
packet is observed.

|image2|

Figure : Keep alive: Wireshark log

**Otii log**: Shows an average current consumption of 64.4µA for 30s. In
idle cases, the average current consumption is 55.3µA.

|image3|

Figure : Keep alive - Otii logs

Console output:

+-----------------------------------------------------------------------+
| Y-BOOT 208ef13 2019-07-22 12:26:54 -0500 790da1-b-7                   |
|                                                                       |
| ROM yoda-h0-rom-16-0-gd5a8e586                                        |
|                                                                       |
| FLASH:PNWWWWWAEBuild $Id: git-ba65998b7 $                             |
|                                                                       |
| mpd.mcast_rx=1 mpd.proto=none wifi.max_idle_period=10                 |
| wifi.listen_interval=10 krn.gpio=--K wifi.keep_alive_wake_time=2      |
| wifi.arp_grat_period=0 mpd.regdomain=FCC mpd.suspend=1                |
| np_conf_path=/data/nprofile.json mpd.ssid=InnoPhase                   |
| mpd.passphrase=43083191                                               |
|                                                                       |
| $App:git-73e7f910                                                     |
|                                                                       |
| SDK Ver: FREERTOS_SDK_1.0                                             |
|                                                                       |
| T2 Multipurpose Demp App Version 0.12                                 |
|                                                                       |
| network profile parse success.                                        |
|                                                                       |
| Suspend Enabled.                                                      |
|                                                                       |
| Multicast reception Enabled.                                          |
|                                                                       |
| Regdomain=FCC                                                         |
|                                                                       |
| addr e0:69:3a:00:13:90                                                |
|                                                                       |
| Applying reg domain: 1-11@20                                          |
|                                                                       |
| Connecting to network                                                 |
|                                                                       |
| .[0.893,908] CONNECT:00:5f:67:cd:c5:a6 Channel:11 rssi:-49 dBm        |
|                                                                       |
| WCM_NOTIFY_MSG_LINK_UP                                                |
|                                                                       |
| .WCM_NOTIFY_MSG_ADDRESS                                               |
|                                                                       |
| [1.865,748] MYIP 192.168.0.104                                        |
|                                                                       |
| [1.865,795] IPv6 [fe80::e269:3aff:fe00:1390]-link                     |
|                                                                       |
| WCM_NOTIFY_MSG_CONNECTED                                              |
|                                                                       |
| Listen interval=10                                                    |
|                                                                       |
| Traffic Timeout=12                                                    |
|                                                                       |
| pm_flags=0x0                                                          |
|                                                                       |
| [2.200,625] WARNING! wcm_pm_config may overwrite the supplied power   |
| management boot arguments!                                            |
|                                                                       |
| WiFi Connection success. proceeding to app..                          |
|                                                                       |
| Timeout not specified.!                                               |
|                                                                       |
| Application Exited..                                                  |
|                                                                       |
| Going for indefinite sleep...                                         |
+=======================================================================+
+-----------------------------------------------------------------------+

TCP
---

**Note**: Both the Host and Talaria TWO are connected to the same
network.

Console output:

+-----------------------------------------------------------------------+
| UART:SNWWWWWAEBuild $Id: git-ba65998b7 $                              |
|                                                                       |
| mpd.mcast_rx=1 mpd.proto=tcp mpd.tcp.msginterval=10                   |
| mpd.tcp.msglen=100 mpd.port=80 wifi.listen_interval=10 krn.gpio=--K   |
| wifi.keep_alive_wake_time=2 wifi.arp_grat_period=1800                 |
| wifi.max_idle_period=0 mpd.regdomain=FCC mpd.suspend=1                |
| np_conf_path=/data/nprofile.json mpd.ssid=InnoPhase                   |
| mpd.passphrase=43083191                                               |
|                                                                       |
| $App:git-73e7f910                                                     |
|                                                                       |
| SDK Ver: FREERTOS_SDK_1.0                                             |
|                                                                       |
| T2 Multipurpose Demp App Version 0.12                                 |
|                                                                       |
| network profile parse success.                                        |
|                                                                       |
| Suspend Enabled.                                                      |
|                                                                       |
| Multicast reception Enabled.                                          |
|                                                                       |
| Regdomain=FCC                                                         |
|                                                                       |
| addr e0:69:3a:00:13:90                                                |
|                                                                       |
| Applying reg domain: 1-11@20                                          |
|                                                                       |
| Connecting to network                                                 |
|                                                                       |
| .[2.070,557] CONNECT:00:5f:67:cd:c5:a6 Channel:11 rssi:-56 dBm        |
|                                                                       |
| WCM_NOTIFY_MSG_LINK_UP                                                |
|                                                                       |
| .WCM_NOTIFY_MSG_ADDRESS                                               |
|                                                                       |
| [2.805,664] MYIP 192.168.0.104                                        |
|                                                                       |
| [2.805,711] IPv6 [fe80::e269:3aff:fe00:1390]-link                     |
|                                                                       |
| WCM_NOTIFY_MSG_CONNECTED                                              |
|                                                                       |
| Listen interval=10                                                    |
|                                                                       |
| Traffic Timeout=12                                                    |
|                                                                       |
| pm_flags=0x0                                                          |
|                                                                       |
| [3.563,103] WARNING! wcm_pm_config may overwrite the supplied power   |
| management boot arguments!                                            |
|                                                                       |
| WiFi Connection success. proceeding to app..                          |
|                                                                       |
| Timeout not specified.!                                               |
|                                                                       |
| listening socket success.. sd=0                                       |
|                                                                       |
| Binding to port: 80                                                   |
|                                                                       |
| bind success..                                                        |
|                                                                       |
| listen success...                                                     |
|                                                                       |
| Config:                                                               |
|                                                                       |
| Proto :tcp                                                            |
|                                                                       |
| Port :80                                                              |
|                                                                       |
| Interval:10                                                           |
|                                                                       |
| msg len :100                                                          |
|                                                                       |
| Waiting for incoming connections..                                    |
|                                                                       |
| Calling accept()                                                      |
|                                                                       |
| msg=Times=1:ABCDEFGHIJKLMNOPQRSTUV                                    |
| WXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLM |
|                                                                       |
| send returned 100.                                                    |
|                                                                       |
| msg=Times=2:ABCDEFGHIJKLMNOPQRSTUV                                    |
| WXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLM |
|                                                                       |
| send returned 100.                                                    |
|                                                                       |
| msg=Times=3:ABCDEFGHIJKLMNOPQRSTUV                                    |
| WXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLM |
|                                                                       |
| send returned 100.                                                    |
|                                                                       |
| msg=Times=4:ABCDEFGHIJKLMNOPQRSTUV                                    |
| WXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLM |
|                                                                       |
| send returned 100.                                                    |
|                                                                       |
| msg=Times=5:ABCDEFGHIJKLMNOPQRSTUV                                    |
| WXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLM |
|                                                                       |
| send returned 100.                                                    |
|                                                                       |
| msg=Times=6:ABCDEFGHIJKLMNOPQRSTUV                                    |
| WXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLM |
|                                                                       |
| send returned 100.                                                    |
|                                                                       |
| msg=Times=7:ABCDEFGHIJKLMNOPQRSTUV                                    |
| WXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLM |
|                                                                       |
| send returned 100.                                                    |
+=======================================================================+
+-----------------------------------------------------------------------+

TCP client windows console output:

+-----------------------------------------------------------------------+
| C:\\Program Files (x86)\\Nmap>ncat.exe 192.168.0.104 80               |
|                                                                       |
| Times=1:ABCDEFGHIJKLMNOPQRSTUV                                        |
| WXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLM |
|                                                                       |
| Times=2:ABCDEFGHIJKLMNOPQRSTUV                                        |
| WXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLM |
|                                                                       |
| Times=3:ABCDEFGHIJKLMNOPQRSTUV                                        |
| WXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLM |
|                                                                       |
| Times=4:ABCDEFGHIJKLMNOPQRSTUV                                        |
| WXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLM |
|                                                                       |
| Times=5:ABCDEFGHIJKLMNOPQRSTUV                                        |
| WXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLM |
|                                                                       |
| Times=6:ABCDEFGHIJKLMNOPQRSTUV                                        |
| WXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLM |
|                                                                       |
| Times=7:ABCDEFGHIJKLMNOPQRSTUV                                        |
| WXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLM |
+=======================================================================+
+-----------------------------------------------------------------------+

To start ncat in the host computer, follow the following steps:

1. Download and Install ncat using the following link:
   https://nmap.org/ncat/.

2. Open command prompt and pass command.

3. Ncat.exe IP-address (from console) and port_number (from console).

**Expected Result**: When client connects to the TCP server (server port
configured with port boot argument), the TCP server sends a message to
client after every <interval> seconds which is configured in
Message_Send Interval.

**
**

**Wireshark log**:

1. The [SYN], [SYN,ACK] and [ACK] is observed for the TCP three-way
   handshake during the connection establishment.

2. [PSH,ACK] is observed for the TCP data sent from Talaria TWO.

3. [FIN,ACK] is observed for the TCP disconnection done from the
   application end point (TCP client).

|image4|

Figure : TCP - Wireshark log

**Otii log**: Shows an average current consumption of 109µA for 30s. In
idle cases, the average current consumption is 58.1µA.

|image5|

Figure : TCP - Otii log

*
*

UDP
---

**Note**: Both the Host and Talaria TWO are connected to the same
network.

Console output:

+-----------------------------------------------------------------------+
| UART:SNWWWWWAEBuild $Id: git-ba65998b7 $                              |
|                                                                       |
| mpd.mcast_rx=1 mpd.proto=udp mpd.udp.msginterval=10                   |
| mpd.udp.msglen=100 mpd.port=6009 wifi.listen_interval=10 krn.gpio=--K |
| wifi.keep_alive_wake_time=2 wifi.arp_grat_period=1800                 |
| wifi.max_idle_period=0 mpd.regdomain=FCC mpd.suspend=1                |
| np_conf_path=/data/nprofile.json mpd.ssid=InnoPhase                   |
| mpd.passphrase=43083191                                               |
|                                                                       |
| $App:git-73e7f910                                                     |
|                                                                       |
| SDK Ver: FREERTOS_SDK_1.0                                             |
|                                                                       |
| T2 Multipurpose Demp App Version 0.12                                 |
|                                                                       |
| network profile parse success.                                        |
|                                                                       |
| Suspend Enabled.                                                      |
|                                                                       |
| Multicast reception Enabled.                                          |
|                                                                       |
| Regdomain=FCC                                                         |
|                                                                       |
| addr e0:69:3a:00:13:90                                                |
|                                                                       |
| Applying reg domain: 1-11@20                                          |
|                                                                       |
| Connecting to network                                                 |
|                                                                       |
| .[2.083,508] CONNECT:00:5f:67:cd:c5:a6 Channel:11 rssi:-44 dBm        |
|                                                                       |
| WCM_NOTIFY_MSG_LINK_UP                                                |
|                                                                       |
| .WCM_NOTIFY_MSG_ADDRESS                                               |
|                                                                       |
| [3.027,081] MYIP 192.168.0.104                                        |
|                                                                       |
| [3.027,130] IPv6 [fe80::e269:3aff:fe00:1390]-link                     |
|                                                                       |
| WCM_NOTIFY_MSG_CONNECTED                                              |
|                                                                       |
| Listen interval=10                                                    |
|                                                                       |
| Traffic Timeout=12                                                    |
|                                                                       |
| pm_flags=0x0                                                          |
|                                                                       |
| [3.567,973] WARNING! wcm_pm_config may overwrite the supplied power   |
| management boot arguments!                                            |
|                                                                       |
| WiFi Connection success. proceeding to app..                          |
|                                                                       |
| Timeout not specified.!                                               |
|                                                                       |
| UDP socket success                                                    |
|                                                                       |
| Config:                                                               |
|                                                                       |
| Proto :udp                                                            |
|                                                                       |
| Port :6009                                                            |
|                                                                       |
| Interval:10                                                           |
|                                                                       |
| msg len :100                                                          |
|                                                                       |
| sendto returned 100.                                                  |
|                                                                       |
| sendto returned 100.                                                  |
|                                                                       |
| sendto returned 100.                                                  |
|                                                                       |
| sendto returned 100.                                                  |
|                                                                       |
| sendto returned 100.                                                  |
|                                                                       |
| sendto returned 100.                                                  |
|                                                                       |
| sendto returned 100.                                                  |
|                                                                       |
| sendto returned 100.                                                  |
|                                                                       |
| sendto returned 100.                                                  |
|                                                                       |
| sendto returned 100.                                                  |
|                                                                       |
| sendto returned 100.                                                  |
+=======================================================================+
+-----------------------------------------------------------------------+

UDP client windows console output:

+-----------------------------------------------------------------------+
| C:\\Program Files (x86)\\Nmap>ncat.exe -u -l 6009                     |
|                                                                       |
| Times=3:ABCDEFGHIJKLMNOPQRSTUV                                        |
| WXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLM |
|                                                                       |
| Times=4:ABCDEFGHIJKLMNOPQRSTUV                                        |
| WXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLM |
|                                                                       |
| Times=5:ABCDEFGHIJKLMNOPQRSTUV                                        |
| WXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLM |
|                                                                       |
| Times=6:ABCDEFGHIJKLMNOPQRSTUV                                        |
| WXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLM |
|                                                                       |
| Times=7:ABCDEFGHIJKLMNOPQRSTUV                                        |
| WXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLM |
|                                                                       |
| Times=8:ABCDEFGHIJKLMNOPQRSTUV                                        |
| WXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLM |
|                                                                       |
| Times=9:ABCDEFGHIJKLMNOPQRSTUV                                        |
| WXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLM |
|                                                                       |
| Times=10:ABCDEFGHIJKLMNOPQRSTU                                        |
| VWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKL |
|                                                                       |
| Times=11:ABCDEFGHIJKLMNOPQRSTU                                        |
| VWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKL |
|                                                                       |
| Times=12:ABCDEFGHIJKLMNOPQRSTU                                        |
| VWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKL |
|                                                                       |
| Times=13:ABCDEFGHIJKLMNOPQRSTU                                        |
| VWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKL |
|                                                                       |
| Times=14:ABCDEFGHIJKLMNOPQRSTU                                        |
| VWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKL |
|                                                                       |
| Times=15:ABCDEFGHIJKLMNOPQRSTU                                        |
| VWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKL |
|                                                                       |
| Times=16:ABCDEFGHIJKLMNOPQRSTU                                        |
| VWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKL |
+=======================================================================+
+-----------------------------------------------------------------------+

To start ncat in the host computer, follow the following steps:

1. Download and install ncat using the following link:
   https://nmap.org/ncat/..

2. Open command prompt and pass the following command (from console):

+-----------------------------------------------------------------------+
| ncat.exe -u -l port_number                                            |
+=======================================================================+
+-----------------------------------------------------------------------+

**Wireshark log**:

**Expected Result**: Talaria TWO sends broadcast UDP message to the
configured port number in MPD tool, every configured interval (10s).

|image6|

Figure : UDP - Wireshark log

**Otii log**: Shows an average current consumption of 107µA for 30s. In
idle cases, the average current consumption is 59.1µA.

|image7|

Figure : UDP - Otii log

HTTP
----

**Wireshark log**:

**Expected Result**: At configured interval (10s), application connects
to URL, performs HTTP Get and hexdumps the page.

1. The first three packets (SYN, SYN/ACK, ACK) are the TCP three-way
   handshake.

2. HTTP GET message is observed for the GET operation.

3. HTTP/1.1 200 OK is the response from the server for the successful
   HTTP connection.

|image8|

Figure : HTTP - Wireshark log

**Otii log:** Shows an average current consumption of 171µA for 30s. In
idle cases, the average current consumption is 58.4µA.

|image9|

Figure : HTTP - Otii log

Console output:

+-----------------------------------------------------------------------+
| UART:SNWWWWWAEBuild $Id: git-ba65998b7 $                              |
|                                                                       |
| mpd.mcast_rx=1 mpd.proto=http mpd.http.httpgetinterval=10             |
| mpd.url=http://example.com wifi.listen_interval=10 krn.gpio=--K       |
| wifi.keep_alive_wake_time=2 wifi.arp_grat_period=1800                 |
| wifi.max_idle_period=0 mpd.regdomain=FCC mpd.suspend=1                |
| np_conf_path=/data/nprofile.json mpd.ssid=InnoPhase                   |
| mpd.passphrase=43083191                                               |
|                                                                       |
| $App:git-73e7f910                                                     |
|                                                                       |
| SDK Ver: FREERTOS_SDK_1.0                                             |
|                                                                       |
| T2 Multipurpose Demp App Version 0.12                                 |
|                                                                       |
| network profile parse success.                                        |
|                                                                       |
| Suspend Enabled.                                                      |
|                                                                       |
| Multicast reception Enabled.                                          |
|                                                                       |
| url=http://example.com                                                |
|                                                                       |
| Regdomain=FCC                                                         |
|                                                                       |
| addr e0:69:3a:00:13:90                                                |
|                                                                       |
| Applying reg domain: 1-11@20                                          |
|                                                                       |
| Connecting to network                                                 |
|                                                                       |
| .[2.049,462] CONNECT:00:5f:67:cd:c5:a6 Channel:11 rssi:-49 dBm        |
|                                                                       |
| WCM_NOTIFY_MSG_LINK_UP                                                |
|                                                                       |
| .WCM_NOTIFY_MSG_ADDRESS                                               |
|                                                                       |
| [2.733,731] MYIP 192.168.0.104                                        |
|                                                                       |
| [2.733,779] IPv6 [fe80::e269:3aff:fe00:1390]-link                     |
|                                                                       |
| WCM_NOTIFY_MSG_CONNECTED                                              |
|                                                                       |
| Listen interval=10                                                    |
|                                                                       |
| Traffic Timeout=12                                                    |
|                                                                       |
| pm_flags=0x0                                                          |
|                                                                       |
| [3.541,272] WARNING! wcm_pm_config may overwrite the supplied power   |
| management boot arguments!                                            |
|                                                                       |
| WiFi Connection success. proceeding to app..                          |
|                                                                       |
| Timeout not specified.!                                               |
|                                                                       |
| after parsing. port=80                                                |
|                                                                       |
| Config:                                                               |
|                                                                       |
| Proto :http                                                           |
|                                                                       |
| Port :0                                                               |
|                                                                       |
| Interval:10                                                           |
|                                                                       |
| msg len :0                                                            |
|                                                                       |
| http_send_keepalive: times=1                                          |
|                                                                       |
| [APP]Calling http_client_open(). cfg.port=80                          |
|                                                                       |
| [APP]HTTP Get. path=/callback entry                                   |
|                                                                       |
| [APP]Response:                                                        |
|                                                                       |
| 1120 ----------------------                                           |
|                                                                       |
| 200                                                                   |
|                                                                       |
| Age: 471654                                                           |
|                                                                       |
| Cache-Control: max-age=604800                                         |
|                                                                       |
| Content-Type: text/html; charset=UTF-8                                |
|                                                                       |
| Date: Thu, 07 Jul 2022 10:23:01 GMT                                   |
|                                                                       |
| Etag: "3147526947+gzip+ident"                                         |
|                                                                       |
| Expires: Thu, 14 Jul 2022 10:23:01 GMT                                |
|                                                                       |
| Last-Modified: Thu, 17 Oct 2019 07:18:26 GMT                          |
|                                                                       |
| Server: ECS (dcb/7EA2)                                                |
|                                                                       |
| Vary: Accept-Encoding                                                 |
|                                                                       |
| X-Cache: HIT                                                          |
|                                                                       |
| Accept-Ranges: none                                                   |
|                                                                       |
| Content-Length: 1256                                                  |
|                                                                       |
| [APP]Body:                                                            |
|                                                                       |
| Hexdump of http data, len=1120                                        |
|                                                                       |
| 3C 21 64 6F 63 74 79 70 65 20 68 74 6D 6C 3E 0A \| <!doctype html>.   |
|                                                                       |
| 3C 68 74 6D 6C 3E 0A 3C 68 65 61 64 3E 0A 20 20 \| <html>.<head>.     |
|                                                                       |
| 20 20 3C 74 69 74 6C 65 3E 45 78 61 6D 70 6C 65 \| <title>Example     |
|                                                                       |
| 20 44 6F 6D 61 69 6E 3C 2F 74 69 74 6C 65 3E 0A \| Domain</title>.    |
|                                                                       |
| 0A 20 20 20 20 3C 6D 65 74 61 20 63 68 61 72 73 \| . <meta chars      |
|                                                                       |
| 65 74 3D 22 75 74 66 2D 38 22 20 2F 3E 0A 20 20 \| et="utf-8" />.     |
|                                                                       |
| 20 20 3C 6D 65 74 61 20 68 74 74 70 2D 65 71 75 \| <meta http-equ     |
|                                                                       |
| 69 76 3D 22 43 6F 6E 74 65 6E 74 2D 74 79 70 65 \| iv="Content-type   |
|                                                                       |
| 22 20 63 6F 6E 74 65 6E 74 3D 22 74 65 78 74 2F \| " content="text/   |
|                                                                       |
| 68 74 6D 6C 3B 20 63 68 61 72 73 65 74 3D 75 74 \| html; charset=ut   |
|                                                                       |
| 66 2D 38 22 20 2F 3E 0A 20 20 20 20 3C 6D 65 74 \| f-8" />. <met      |
|                                                                       |
| 61 20 6E 61 6D 65 3D 22 76 69 65 77 70 6F 72 74 \| a name="viewport   |
|                                                                       |
| 22 20 63 6F 6E 74 65 6E 74 3D 22 77 69 64 74 68 \| " content="width   |
|                                                                       |
| 3D 64 65 76 69 63 65 2D 77 69 64 74 68 2C 20 69 \| =device-width, i   |
|                                                                       |
| 6E 69 74 69 61 6C 2D 73 63 61 6C 65 3D 31 22 20 \| nitial-scale=1"    |
|                                                                       |
| 2F 3E 0A 20 20 20 20 3C 73 74 79 6C 65 20 74 79 \| />. <style ty      |
|                                                                       |
| 70 65 3D 22 74 65 78 74 2F 63 73 73 22 3E 0A 20 \| pe="text/css">.    |
|                                                                       |
| 20 20 20 62 6F 64 79 20 7B 0A 20 20 20 20 20 20 \| body {.            |
|                                                                       |
| 20 20 62 61 63 6B 67 72 6F 75 6E 64 2D 63 6F 6C \| background-col     |
|                                                                       |
| 6F 72 3A 20 23 66 30 66 30 66 32 3B 0A 20 20 20 \| or: #f0f0f2;.      |
|                                                                       |
| 20 20 20 20 20 6D 61 72 67 69 6E 3A 20 30 3B 0A \| margin: 0;.        |
|                                                                       |
| 20 20 20 20 20 20 20 20 70 61 64 64 69 6E 67 3A \| padding:           |
|                                                                       |
| 20 30 3B 0A 20 20 20 20 20 20 20 20 66 6F 6E 74 \| 0;. font           |
|                                                                       |
| 2D 66 61 6D 69 6C 79 3A 20 2D 61 70 70 6C 65 2D \| -family: -apple-   |
|                                                                       |
| 73 79 73 74 65 6D 2C 20 73 79 73 74 65 6D 2D 75 \| system, system-u   |
|                                                                       |
| 69 2C 20 42 6C 69 6E 6B 4D 61 63 53 79 73 74 65 \| i, BlinkMacSyste   |
|                                                                       |
| 6D 46 6F 6E 74 2C 20 22 53 65 67 6F 65 20 55 49 \| mFont, "Segoe UI   |
|                                                                       |
| 22 2C 20 22 4F 70 65 6E 20 53 61 6E 73 22 2C 20 \| ", "Open Sans",    |
|                                                                       |
| 22 48 65 6C 76 65 74 69 63 61 20 4E 65 75 65 22 \| "Helvetica Neue"   |
|                                                                       |
| 2C 20 48 65 6C 76 65 74 69 63 61 2C 20 41 72 69 \| , Helvetica, Ari   |
|                                                                       |
| 61 6C 2C 20 73 61 6E 73 2D 73 65 72 69 66 3B 0A \| al, sans-serif;.   |
|                                                                       |
| 20 20 20 20 20 20 20 20 0A 20 20 20 20 7D 0A 20 \| . }.               |
|                                                                       |
| 20 20 20 64 69 76 20 7B 0A 20 20 20 20 20 20 20 \| div {.             |
|                                                                       |
| 20 77 69 64 74 68 3A 20 36 30 30 70 78 3B 0A 20 \| width: 600px;.     |
|                                                                       |
| 20 20 20 20 20 20 20 6D 61 72 67 69 6E 3A 20 35 \| margin: 5          |
|                                                                       |
| 65 6D 20 61 75 74 6F 3B 0A 20 20 20 20 20 20 20 \| em auto;.          |
|                                                                       |
| 20 70 61 64 64 69 6E 67 3A 20 32 65 6D 3B 0A 20 \| padding: 2em;.     |
|                                                                       |
| 20 20 20 20 20 20 20 62 61 63 6B 67 72 6F 75 6E \| backgroun          |
|                                                                       |
| 64 2D 63 6F 6C 6F 72 3A 20 23 66 64 66 64 66 66 \| d-color: #fdfdff   |
|                                                                       |
| 3B 0A 20 20 20 20 20 20 20 20 62 6F 72 64 65 72 \| ;. border          |
|                                                                       |
| 2D 72 61 64 69 75 73 3A 20 30 2E 35 65 6D 3B 0A \| -radius: 0.5em;.   |
|                                                                       |
| 20 20 20 20 20 20 20 20 62 6F 78 2D 73 68 61 64 \| box-shad           |
|                                                                       |
| 6F 77 3A 20 32 70 78 20 33 70 78 20 37 70 78 20 \| ow: 2px 3px 7px    |
|                                                                       |
| 32 70 78 20 72 67 62 61 28 30 2C 30 2C 30 2C 30 \| 2px rgba(0,0,0,0   |
|                                                                       |
| 2E 30 32 29 3B 0A 20 20 20 20head>..<b                                |
|                                                                       |
| 6F 64 79 3E 0A 3C 64 69 76 3E 0A 20 20 20 20 3C \| ody>.<div>. <      |
|                                                                       |
| 68 31 3E 45 78 61 6D 70 6C 65 20 44 6F 6D 61 69 \| h1>Example Domai   |
|                                                                       |
| 6E 3C 2F 68 31 3E 0A 20 20 20 20 3C 70 3E 54 68 \| n</h1>. <p>Th      |
|                                                                       |
| 69 73 20 64 6F 6D 61 69 6E 20 69 73 20 66 6F 72 \| is domain is for   |
|                                                                       |
| 20 75 73 65 20 69 6E 20 69 6C 6C 75 73 74 72 61 \| use in illustra    |
|                                                                       |
| 74 69 76 65 20 65 78 61 6D 70 6C 65 73 20 69 6E \| tive examples in   |
|                                                                       |
| 20 64 6F 63 75 6D 65 6E 74 73 2E 20 59 6F 75 20 \| documents. You     |
|                                                                       |
| 6D 61 79 20 75 73 65 20 74 68 69 73 0A 20 20 20 \| may use this.      |
|                                                                       |
| 20 64 6F 6D 61 69 6E 20 69 6E 20 6C 69 74 65 72 \| domain in liter    |
|                                                                       |
| 61 74 75 72 65 20 77 69 74 68 6F 75 74 20 70 72 \| ature without pr   |
|                                                                       |
| 69 6F 72 20 63 6F 6F 72 64 69 6E 61 74 69 6F 6E \| ior coordination   |
|                                                                       |
| callback exit                                                         |
|                                                                       |
| callback entry                                                        |
|                                                                       |
| Hexdump of http data, len=136                                         |
|                                                                       |
| 20 6F 72 20 61 73 6B 69 6E 67 20 66 6F 72 20 70 \| or asking for p    |
|                                                                       |
| 65 72 6D 69 73 73 69 6F 6E 2E 3C 2F 70 3E 0A 20 \| ermission.</p>.    |
|                                                                       |
| 20 20 20 3C 70 3E 3C 61 20 68 72 65 66 3D 22 68 \| <p><a href="h      |
|                                                                       |
| 74 74 70 73 3A 2F 2F 77 77 77 2E 69 61 6E 61 2E \| ttps://www.iana.   |
|                                                                       |
| 6F 72 67 2F 64 6F 6D 61 69 6E 73 2F 65 78 61 6D \| org/domains/exam   |
|                                                                       |
| 70 6C 65 22 3E 4D 6F 72 65 20 69 6E 66 6F 72 6D \| ple">More inform   |
|                                                                       |
| 61 74 69 6F 6E 2E 2E 2E 3C 2F 61 3E 3C 2F 70 3E \| ation...</a></p>   |
|                                                                       |
| 0A 3C 2F 64 69 76 3E 0A 3C 2F 62 6F 64 79 3E 0A \| .</div>.</body>.   |
|                                                                       |
| 3C 2F 68 74 6D 6C 3E 0A \| </html>.                                   |
|                                                                       |
| callback exit                                                         |
+=======================================================================+
+-----------------------------------------------------------------------+

HTTPS
-----

**Wireshark log**:

**Expected Result**: At the configured interval, Message_Send Interval,
application connects to URL, performs HTTPs Get and hexdumps the page.

1. The first three packets (SYN, SYN/ACK, ACK) are the TCP three-way
   handshake.

2. [Client hello], [Server hello], [Certificate, Server Key Exchange,
   Server Hello Done], [Client Key Exchange, Change Cipher Spec,
   Encrypted Handshake Message], [New Session ticket] are the SSL/TLS
   handshake, which indicates successful TLS connection.

3. All the data packets over TLS connection are observed as Application
   data which is encrypted.

|image10|

Figure : HTTPS - Wireshark log

**Otii log**: Shows an average current consumption of 640µA for 30s. In
idle cases, the average current consumption is 58.1µA.

|image11|

Figure : HTTPS - Otii log

Console output:

+-----------------------------------------------------------------------+
| UART:SNWWWWWAEBuild $Id: git-ba65998b7 $                              |
|                                                                       |
| mpd.mcast_rx=1 mpd.proto=https mpd.https.httpsgetinterval=10          |
| mpd.url=https://example.com wifi.listen_interval=10 krn.gpio=--K      |
| wifi.keep_alive_wake_time=2 wifi.arp_grat_period=1800                 |
| wifi.max_idle_period=0 mpd.regdomain=FCC mpd.suspend=1                |
| np_conf_path=/data/nprofile.json mpd.ssid=InnoPhase                   |
| mpd.passphrase=43083191                                               |
|                                                                       |
| $App:git-73e7f910                                                     |
|                                                                       |
| SDK Ver: FREERTOS_SDK_1.0                                             |
|                                                                       |
| T2 Multipurpose Demp App Version 0.12                                 |
|                                                                       |
| network profile parse success.                                        |
|                                                                       |
| Suspend Enabled.                                                      |
|                                                                       |
| Multicast reception Enabled.                                          |
|                                                                       |
| url=https://example.com                                               |
|                                                                       |
| Regdomain=FCC                                                         |
|                                                                       |
| addr e0:69:3a:00:13:90                                                |
|                                                                       |
| Applying reg domain: 1-11@20                                          |
|                                                                       |
| Connecting to network                                                 |
|                                                                       |
| .[2.171,820] CONNECT:00:5f:67:cd:c5:a6 Channel:11 rssi:-57 dBm        |
|                                                                       |
| WCM_NOTIFY_MSG_LINK_UP                                                |
|                                                                       |
| .WCM_NOTIFY_MSG_ADDRESS                                               |
|                                                                       |
| [2.917,496] MYIP 192.168.0.104                                        |
|                                                                       |
| [2.917,543] IPv6 [fe80::e269:3aff:fe00:1390]-link                     |
|                                                                       |
| WCM_NOTIFY_MSG_CONNECTED                                              |
|                                                                       |
| Listen interval=10                                                    |
|                                                                       |
| Traffic Timeout=12                                                    |
|                                                                       |
| pm_flags=0x0                                                          |
|                                                                       |
| [3.543,978] WARNING! wcm_pm_config may overwrite the supplied power   |
| management boot arguments!                                            |
|                                                                       |
| WiFi Connection success. proceeding to app..                          |
|                                                                       |
| Timeout not specified.!                                               |
|                                                                       |
| after parsing. port=443                                               |
|                                                                       |
| Config:                                                               |
|                                                                       |
| Proto :https                                                          |
|                                                                       |
| Port :0                                                               |
|                                                                       |
| Interval:10                                                           |
|                                                                       |
| msg len :0                                                            |
|                                                                       |
| http_send_keepalive: times=1                                          |
|                                                                       |
| [APP]Calling http_client_open(). http_cmn_ctx.cfg.port=443            |
|                                                                       |
| . [SSL_WRAP]Checking input configurations...                          |
|                                                                       |
| . [SSL_WRAP]Seeding the random number generator...                    |
|                                                                       |
| . [SSL_WRAP]Connecting to tcp example.com:443...                      |
|                                                                       |
| . [SSL_WRAP]Setting up the SSL/TLS structure...                       |
|                                                                       |
| . [SSL_WRAP]setting configurations..                                  |
|                                                                       |
| >auth mode = 0 (0- skip, 1- optional, 2- required                     |
|                                                                       |
| >max fragment len = 0                                                 |
|                                                                       |
| >Handshake timeout = 30 Sec                                           |
|                                                                       |
| . [SSL_WRAP]Performing the SSL/TLS handshake...                       |
|                                                                       |
| . [SSL_WRAP] Handshake done. ok                                       |
|                                                                       |
| . [SSL_WRAP]Verifying peer X.509 certificate.                         |
|                                                                       |
| [APP]HTTP Get. path=/                                                 |
|                                                                       |
| [APP]Response:                                                        |
|                                                                       |
| 0 ----------------------                                              |
|                                                                       |
| 200                                                                   |
|                                                                       |
| Age: 378199                                                           |
|                                                                       |
| Cache-Control: max-age=604800                                         |
|                                                                       |
| Content-Type: text/html; charset=UTF-8                                |
|                                                                       |
| Date: Thu, 07 Jul 2022 11:04:16 GMT                                   |
|                                                                       |
| Etag: "3147526947+ident"                                              |
|                                                                       |
| Expires: Thu, 14 Jul 2022 11:04:16 GMT                                |
|                                                                       |
| Last-Modified: Thu, 17 Oct 2019 07:18:26 GMT                          |
|                                                                       |
| Server: ECS (dcb/7F80)                                                |
|                                                                       |
| Vary: Accept-Encoding                                                 |
|                                                                       |
| X-Cache: HIT                                                          |
|                                                                       |
| Content-Length: 1256                                                  |
|                                                                       |
| [APP]Body:                                                            |
|                                                                       |
| Hexdump of http data, len=0                                           |
|                                                                       |
| Hexdump of http data, len=1256                                        |
|                                                                       |
| 3C 21 64 6F 63 74 79 70 65 20 68 74 6D 6C 3E 0A \| <!doctype html>.   |
|                                                                       |
| 3C 68 74 6D 6C 3E 0A 3C 68 65 61 64 3E 0A 20 20 \| <html>.<head>.     |
|                                                                       |
| 20 20 3C 74 69 74 6C 65 3E 45 78 61 6D 70 6C 65 \| <title>Example     |
|                                                                       |
| 20 44 6F 6D 61 69 6E 3C 2F 74 69 74 6C 65 3E 0A \| Domain</title>.    |
|                                                                       |
| 0A 20 20 20 20 3C 6D 65 74 61 20 63 68 61 72 73 \| . <meta chars      |
|                                                                       |
| 65 74 3D 22 75 74 66 2D 38 22 20 2F 3E 0A 20 20 \| et="utf-8" />.     |
|                                                                       |
| 20 20 3C 6D 65 74 61 20 68 74 74 70 2D 65 71 75 \| <meta http-equ     |
|                                                                       |
| 69 76 3D 22 43 6F 6E 74 65 6E 74 2D 74 79 70 65 \| iv="Content-type   |
|                                                                       |
| 22 20 63 6F 6E 74 65 6E 74 3D 22 74 65 78 74 2F \| " content="text/   |
|                                                                       |
| 68 74 6D 6C 3B 20 63 68 61 72 73 65 74 3D 75 74 \| html; charset=ut   |
|                                                                       |
| 66 2D 38 22 20 2F 3E 0A 20 20 20 20 3C 6D 65 74 \| f-8" />. <met      |
|                                                                       |
| 61 20 6E 61 6D 65 3D 22 76 69 65 77 70 6F 72 74 \| a name="viewport   |
|                                                                       |
| 22 20 63 6F 6E 74 65 6E 74 3D 22 77 69 64 74 68 \| " content="width   |
|                                                                       |
| 3D 64 65 76 69 63 65 2D 77 69 64 74 68 2C 20 69 \| =device-width, i   |
|                                                                       |
| 6E 69 74 69 61 6C 2D 73 63 61 6C 65 3D 31 22 20 \| nitial-scale=1"    |
|                                                                       |
| 2F 3E 0A 20 20 20 20 3C 73 74 79 6C 65 20 74 79 \| />. <style ty      |
|                                                                       |
| 70 65 3D 22 74 65 78 74 2F 63 73 73 22 3E 0A 20 \| pe="text/css">.    |
|                                                                       |
| 20 20 20 62 6F 64 79 20 7B 0A 20 20 20 20 20 20 \| body {.            |
|                                                                       |
| 20 20 62 61 63 6B 67 72 6F 75 6E 64 2D 63 6F 6C \| background-col     |
|                                                                       |
| 6F 72 3A 20 23 66 30 66 30 66 32 3B 0A 20 20 20 \| or: #f0f0f2;.      |
|                                                                       |
| 20 20 20 20 20 6D 61 72 67 69 6E 3A 20 30 3B 0A \| margin: 0;.        |
|                                                                       |
| 20 20 20 20 20 20 20 20 70 61 64 64 69 6E 67 3A \| padding:           |
|                                                                       |
| 20 30 3B 0A 20 20 20 20 20 20 20 20 66 6F 6E 74 \| 0;. font           |
|                                                                       |
| 2D 66 61 6D 69 6C 79 3A 20 2D 61 70 70 6C 65 2D \| -family: -apple-   |
|                                                                       |
| 73 79 73 74 65 6D 2C 20 73 79 73 74 65 6D 2D 75 \| system, system-u   |
|                                                                       |
| 69 2C 20 42 6C 69 6E 6B 4D 61 63 53 79 73 74 65 \| i, BlinkMacSyste   |
|                                                                       |
| 6D 46 6F 6E 74 2C 20 22 53 65 67 6F 65 20 55 49 \| mFont, "Segoe UI   |
|                                                                       |
| 22 2C 20 22 4F 70 65 6E 20 53 61 6E 73 22 2C 20 \| ", "Open Sans",    |
|                                                                       |
| 22 48 65 6C 76 65 74 69 63 61 20 4E 65 75 65 22 \| "Helvetica Neue"   |
|                                                                       |
| 2C 20 48 65 6C 76 65 74 69 63 61 2C 20 41 72 69 \| , Helvetica, Ari   |
|                                                                       |
| 61 6C 2C 20 73 61 6E 73 2D 73 65 72 69 66 3B 0A \| al, sans-serif;.   |
|                                                                       |
| 20 20 20 20 20 20 20 20 0A 20 20 20 20 7D 0A 20 \| . }.               |
|                                                                       |
| 20 20 20 64 69 76 20 7B 0A 20 20 20 20 20 20 20 \| div {.             |
|                                                                       |
| 20 77 69 64 74 68 3A 20 36 30 30 70 78 3B 0A 20 \| width: 600px;.     |
|                                                                       |
| 20 20 20 20 20 20 20 6D 61 72 67 69 6E 3A 20 35 \| margin: 5          |
|                                                                       |
| 65 6D 20 61 75 74 6F 3B 0A 20 20 20 20 20 20 20 \| em auto;.          |
|                                                                       |
| 20 70 61 64 64 69 6E 67 3A 20 32 65 6D 3B 0A 20 \| padding: 2em;.     |
|                                                                       |
| 20 20 20 20 20 20 20 62 61 63 6B 67 72 6F 75 6E \| backgroun          |
|                                                                       |
| 64 2D 63 6F 6C 6F 72 3A 20 23 66 64 66 64 66 66 \| d-color: #fdfdff   |
|                                                                       |
| 3B 0A 20 20 20 20 20 20 20 20 62 6F 72 64 65 72 \| ;. border          |
|                                                                       |
| 2D 72 61 64 69 75 73 3A 20 30 2E 35 65 6D 3B 0A \| -radius: 0.5em;.   |
|                                                                       |
| 20 20 20 20 20 20 20 20 62 6F 78 2D 73 68 61 64 \| box-shad           |
|                                                                       |
| 6F 77 3A 20 32 70 78 20 33 70 78 }.                                   |
|                                                                       |
| 20 20 7D 0A 20 20 20 20 3C 2F 73 74 79 6C 65 3E \| }. </style>        |
|                                                                       |
| 20 20 20 20 0A 3C 2F 68 65 61 64 3E 0A 0A 3C 62 \| .</head>..<b       |
|                                                                       |
| 6F 64 79 3E 0A 3C 64 69 76 3E 0A 20 20 20 20 3C \| ody>.<div>. <      |
|                                                                       |
| 68 31 3E 45 78 61 6D 70 6C 65 20 44 6F 6D 61 69 \| h1>Example Domai   |
|                                                                       |
| 6E 3C 2F 68 31 3E 0A 20 20 20 20 3C 70 3E 54 68 \| n</h1>. <p>Th      |
|                                                                       |
| 69 73 20 64 6F 6D 61 69 6E 20 69 73 20 66 6F 72 \| is domain is for   |
|                                                                       |
| 20 75 73 65 20 69 6E 20 69 6C 6C 75 73 74 72 61 \| use in illustra    |
|                                                                       |
| 74 69 76 65 20 65 78 61 6D 70 6C 65 73 20 69 6E \| tive examples in   |
|                                                                       |
| 20 64 6F 63 75 6D 65 6E 74 73 2E 20 59 6F 75 20 \| documents. You     |
|                                                                       |
| 6D 61 79 20 75 73 65 20 74 68 69 73 0A 20 20 20 \| may use this.      |
|                                                                       |
| 20 64 6F 6D 61 69 6E 20 69 6E 20 6C 69 74 65 72 \| domain in liter    |
|                                                                       |
| 61 74 75 72 65 20 77 69 74 68 6F 75 74 20 70 72 \| ature without pr   |
|                                                                       |
| 69 6F 72 20 63 6F 6F 72 64 69 6E 61 74 69 6F 6E \| ior coordination   |
|                                                                       |
| 20 6F 72 20 61 73 6B 69 6E 67 20 66 6F 72 20 70 \| or asking for p    |
|                                                                       |
| 65 72 6D 69 73 73 69 6F 6E 2E 3C 2F 70 3E 0A 20 \| ermission.</p>.    |
|                                                                       |
| 20 20 20 3C 70 3E 3C 61 20 68 72 65 66 3D 22 68 \| <p><a href="h      |
|                                                                       |
| 74 74 70 73 3A 2F 2F 77 77 77 2E 69 61 6E 61 2E \| ttps://www.iana.   |
|                                                                       |
| 6F 72 67 2F 64 6F 6D 61 69 6E 73 2F 65 78 61 6D \| org/domains/exam   |
|                                                                       |
| 70 6C 65 22 3E 4D 6F 72 65 20 69 6E 66 6F 72 6D \| ple">More inform   |
|                                                                       |
| 61 74 69 6F 6E 2E 2E 2E 3C 2F 61 3E 3C 2F 70 3E \| ation...</a></p>   |
|                                                                       |
| 0A 3C 2F 64 69 76 3E 0A 3C 2F 62 6F 64 79 3E 0A \| .</div>.</body>.   |
|                                                                       |
| 3C 2F 68 74 6D 6C 3E 0A \| </html>.                                   |
|                                                                       |
| [APP]Success: http_client_get(), rval = 2                             |
|                                                                       |
| http_send_keepalive: times=2                                          |
|                                                                       |
| [APP]Calling http_client_open(). http_cmn_ctx.cfg.port=443            |
|                                                                       |
| . [SSL_WRAP]Checking input configurations...                          |
|                                                                       |
| . [SSL_WRAP]Seeding the random number generator...                    |
|                                                                       |
| . [SSL_WRAP]Connecting to tcp example.com:443...                      |
|                                                                       |
| . [SSL_WRAP]Setting up the SSL/TLS structure...                       |
|                                                                       |
| . [SSL_WRAP]setting configurations..                                  |
|                                                                       |
| >auth mode = 0 (0- skip, 1- optional, 2- required                     |
|                                                                       |
| >max fragment len = 0                                                 |
|                                                                       |
| >Handshake timeout = 30 Sec                                           |
|                                                                       |
| . [SSL_WRAP]Performing the SSL/TLS handshake...                       |
|                                                                       |
| . [SSL_WRAP] Handshake done. ok                                       |
|                                                                       |
| . [SSL_WRAP]Verifying peer X.509 certificate.                         |
|                                                                       |
| [APP]HTTP Get. path=/                                                 |
+=======================================================================+
+-----------------------------------------------------------------------+

MQTT
----

To observe Publish messages and to Subscribe any message run the
following commands:

1. To Publish:

**mosquitto_sub -d -v -h mqtt-dashboard.com -t PUBMSG**

2. To Subscribe:

**mosquitto_pub -d -h mqtt-dashboard.com -t SUBMSG1 -m "msg1"**

**Note**: Mosquitto.exe can be downloaded from the following link:
http://mosquitto.org/download/.

MQTT - Command Prompt Output (Subscribe message):

+-----------------------------------------------------------------------+
| synergic@synergic-vostro-3470:~/Downloads$ mosquitto_pub -d -h        |
| mqtt-dashboard.com -t SUBMSG1 -m "msg1"                               |
|                                                                       |
| Client mosq-7XNzxTypruvc9Bkybj sending CONNECT                        |
|                                                                       |
| Client mosq-7XNzxTypruvc9Bkybj received CONNACK (0)                   |
|                                                                       |
| Client mosq-7XNzxTypruvc9Bkybj sending PUBLISH (d0, q0, r0, m1,       |
| 'SUBMSG1', ... (4 bytes))                                             |
|                                                                       |
| Client mosq-7XNzxTypruvc9Bkybj sending DISCONNECT                     |
+=======================================================================+
+-----------------------------------------------------------------------+

MQTT - Command Prompt Output (Publish message):

+-----------------------------------------------------------------------+
| synergic@synergic-vostro-3470:~/Downloads$ mosquitto_sub -d -v -h     |
| mqtt-dashboard.com -t PUBMSG                                          |
|                                                                       |
| Client mosq-3SHpQMGOLvcW97fbtH sending CONNECT                        |
|                                                                       |
| Client mosq-3SHpQMGOLvcW97fbtH received CONNACK (0)                   |
|                                                                       |
| Client mosq-3SHpQMGOLvcW97fbtH sending SUBSCRIBE (Mid: 1, Topic:      |
| PUBMSG, QoS: 0, Options: 0x00)                                        |
|                                                                       |
| Client mosq-3SHpQMGOLvcW97fbtH received SUBACK                        |
|                                                                       |
| Subscribed (mid: 1): 0                                                |
|                                                                       |
| Client mosq-3SHpQMGOLvcW97fbtH received PUBLISH (d0, q0, r0, m0,      |
| 'PUBMSG', ... (99 bytes))                                             |
|                                                                       |
| PUBMSG                                                                |
| Times=7:ABCDEFGHIJKLMNOPQRSTUV                                        |
| WXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLM |
|                                                                       |
| Client mosq-3SHpQMGOLvcW97fbtH received PUBLISH (d0, q0, r0, m0,      |
| 'PUBMSG', ... (99 bytes))                                             |
|                                                                       |
| PUBMSG                                                                |
| Times=8:ABCDEFGHIJKLMNOPQRSTUV                                        |
| WXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLM |
|                                                                       |
| Client mosq-3SHpQMGOLvcW97fbtH received PUBLISH (d0, q0, r0, m0,      |
| 'PUBMSG', ... (99 bytes))                                             |
|                                                                       |
| PUBMSG                                                                |
| Times=9:ABCDEFGHIJKLMNOPQRSTUV                                        |
| WXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLM |
|                                                                       |
| Client mosq-3SHpQMGOLvcW97fbtH received PUBLISH (d0, q0, r0, m0,      |
| 'PUBMSG', ... (99 bytes))                                             |
|                                                                       |
| PUBMSG                                                                |
| Times=10:ABCDEFGHIJKLMNOPQRSTU                                        |
| VWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKL |
|                                                                       |
| Client mosq-3SHpQMGOLvcW97fbtH received PUBLISH (d0, q0, r0, m0,      |
| 'PUBMSG', ... (99 bytes))                                             |
|                                                                       |
| PUBMSG                                                                |
| Times=11:ABCDEFGHIJKLMNOPQRSTU                                        |
| VWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKL |
|                                                                       |
| Client mosq-3SHpQMGOLvcW97fbtH received PUBLISH (d0, q0, r0, m0,      |
| 'PUBMSG', ... (99 bytes))                                             |
|                                                                       |
| PUBMSG                                                                |
| Times=0:ABCDEFGHIJKLMNOPQRSTUV                                        |
| WXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLM |
|                                                                       |
| Client mosq-3SHpQMGOLvcW97fbtH sending PINGREQ                        |
|                                                                       |
| Client mosq-3SHpQMGOLvcW97fbtH received PINGRESP                      |
|                                                                       |
| Client mosq-3SHpQMGOLvcW97fbtH received PUBLISH (d0, q0, r0, m0,      |
| 'PUBMSG', ... (99 bytes))                                             |
|                                                                       |
| PUBMSG                                                                |
| Times=1:ABCDEFGHIJKLMNOPQRSTUV                                        |
| WXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLM |
|                                                                       |
| Client mosq-3SHpQMGOLvcW97fbtH received PUBLISH (d0, q0, r0, m0,      |
| 'PUBMSG', ... (99 bytes))                                             |
|                                                                       |
| PUBMSG                                                                |
| Times=2:ABCDEFGHIJKLMNOPQRSTUV                                        |
| WXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLM |
|                                                                       |
| Client mosq-3SHpQMGOLvcW97fbtH received PUBLISH (d0, q0, r0, m0,      |
| 'PUBMSG', ... (99 bytes))                                             |
+=======================================================================+
+-----------------------------------------------------------------------+

Console output:

+-----------------------------------------------------------------------+
| Y-BOOT 208ef13 2019-07-22 12:26:54 -0500 790da1-b-7                   |
|                                                                       |
| ROM yoda-h0-rom-16-0-gd5a8e586                                        |
|                                                                       |
| FLASH:PNWWWWWAEBuild $Id: git-d198c0771 $                             |
|                                                                       |
| mpd.mcast_rx=1 mpd.proto=mqtt mpd.port=8883                           |
| mpd.mqtt.publishinterval=10 mpd.url=mqtt-dashboard.com                |
| mpd.mqtt.clientid=T2_TALARIA mpd.mqtt.username=t2_user                |
| mpd.mqtt.password=t2_pass mpd.mqtt.pub_msg=PUBMSG                     |
| mpd.mqtt.sub_msg1=SUBMSG1 mpd.mqtt.sub_msg2=SUBMSG2                   |
| mpd.mqtt.ping_interval=60 wifi.listen_interval=10 krn.gpio=--K        |
| wifi.keep_alive_wake_time=2 wifi.arp_grat_period=1800                 |
| wifi.max_idle_period=0 mpd.regdomain=FCC mpd.suspend=1                |
| np_conf_path=/data/nprofile.json mpd.ssid=low_rssi                    |
| mpd.passphrase=12345678                                               |
|                                                                       |
| $App:git-fdceeca3                                                     |
|                                                                       |
| SDK Ver: FREERTOS_SDK_1.0                                             |
|                                                                       |
| T2 Multipurpose Demp App Version 0.12                                 |
|                                                                       |
| network profile parse success.                                        |
|                                                                       |
| Suspend Enabled.                                                      |
|                                                                       |
| Multicast reception Enabled.                                          |
|                                                                       |
| url=mqtt-dashboard.com                                                |
|                                                                       |
| Regdomain=FCC                                                         |
|                                                                       |
| addr e0:69:3a:00:01:24                                                |
|                                                                       |
| Applying reg domain: 1-11@20                                          |
|                                                                       |
| Connecting to network                                                 |
|                                                                       |
| .[0.900,792] CONNECT:74:da:88:a6:9c:ea Channel:11 rssi:-4 dBm         |
|                                                                       |
| WCM_NOTIFY_MSG_LINK_UP                                                |
|                                                                       |
| .WCM_NOTIFY_MSG_ADDRESS                                               |
|                                                                       |
| [1.612,858] MYIP 192.168.1.100                                        |
|                                                                       |
| [1.613,022] IPv6 [fe80::e269:3aff:fe00:124]-link                      |
|                                                                       |
| WCM_NOTIFY_MSG_CONNECTED                                              |
|                                                                       |
| Listen interval=10                                                    |
|                                                                       |
| Traffic Timeout=12                                                    |
|                                                                       |
| pm_flags=0x0                                                          |
|                                                                       |
| [2.214,225] WARNING! wcm_pm_config may overwrite the supplied power   |
| management boot arguments!                                            |
|                                                                       |
| WiFi Connection success. proceeding to app..                          |
|                                                                       |
| Timeout not specified.!                                               |
|                                                                       |
| url=mqtt-dashboard.com hostname=mqtt-dashboard.com, port=8883, page=/ |
|                                                                       |
| starting mqtt.. Ping interval=60 Secs                                 |
|                                                                       |
| . Seeding the random number generator... ok                           |
|                                                                       |
| . Loading the CA root certificate ... ok (0 skipped)                  |
|                                                                       |
| Connect success. Returning :0                                         |
|                                                                       |
| ok                                                                    |
|                                                                       |
| . Setting up the SSL/TLS structure... ok                              |
|                                                                       |
| . Performing the SSL/TLS handshake... ok                              |
|                                                                       |
| init_ssl_and_connect success... proceeding..on retry (1)              |
|                                                                       |
| \_mqtt_cycle : packet_type = 2                                        |
|                                                                       |
| \_mqtt_cycle : packet_type = 9Subscribed to "SUBMSG1"                 |
|                                                                       |
| \_mqtt_cycle : packet_type = 9Subscribed to "SUBMSG2"                 |
|                                                                       |
| MQTT init: returning 0                                                |
|                                                                       |
| Config:                                                               |
|                                                                       |
| Proto :mqtt                                                           |
|                                                                       |
| Port :1883                                                            |
|                                                                       |
| Interval:10                                                           |
|                                                                       |
| msg len :100                                                          |
|                                                                       |
| mqtt_loop entry                                                       |
|                                                                       |
| publish_data, value=1, interval=10Secs                                |
|                                                                       |
| publish_data, value=2, interval=10Secs                                |
|                                                                       |
| publish_data, value=3, interval=10Secs                                |
|                                                                       |
| publish_data, value=4, interval=10Secs                                |
|                                                                       |
| publish_data, value=5, interval=10Secs                                |
|                                                                       |
| publish_data, value=6, interval=10Secs                                |
|                                                                       |
| publish_data, value=7, interval=10Secs                                |
|                                                                       |
| \_mqtt_cycle : packet_type = 13publish_data, value=8, interval=10Secs |
|                                                                       |
| publish_data, value=9, interval=10Secs                                |
|                                                                       |
| publish_data, value=10, interval=10Secs                               |
|                                                                       |
| publish_data, value=11, interval=10Secs                               |
|                                                                       |
| publish_data, value=0, interval=10Secs                                |
|                                                                       |
| publish_data, value=1, interval=10Secs                                |
|                                                                       |
| \_mqtt_cycle : packet_type = 13publish_data, value=2, interval=10Secs |
|                                                                       |
| \_mqtt_cycle : packet_type = 3messageArrived: SUBMSG1 msg1            |
|                                                                       |
| publish_data, value=3, interval=10Secs                                |
|                                                                       |
| publish_data, value=4, interval=10Secs                                |
|                                                                       |
| publish_data, value=5, interval=10Secs                                |
|                                                                       |
| publish_data, value=6, interval=10Secs                                |
|                                                                       |
| publish_data, value=7, interval=10Secs                                |
|                                                                       |
| publish_data, value=8, interval=10Secs                                |
|                                                                       |
| \_mqtt_cycle : packet_type = 13publish_data, value=9, interval=10Secs |
|                                                                       |
| publish_data, value=10, interval=10Secs                               |
|                                                                       |
| publish_data, value=11, interval=10Secs                               |
|                                                                       |
| publish_data, value=0, interval=10Secs                                |
|                                                                       |
| publish_data, value=1, interval=10Secs                                |
|                                                                       |
| publish_data, value=2, interval=10Secs                                |
|                                                                       |
| publish_data, value=3, interval=10Secs                                |
|                                                                       |
| \_mqtt_cycle : packet_type = 13publish_data, value=4, interval=10Secs |
|                                                                       |
| publish_data, value=5, interval=10Secs                                |
|                                                                       |
| publish_data, value=6, interval=10Secs                                |
|                                                                       |
| publish_data, value=7, interval=10Secs                                |
|                                                                       |
| publish_data, value=8, interval=10Secs                                |
|                                                                       |
| publish_data, value=9, interval=10Secs                                |
|                                                                       |
| \_mqtt_cycle : packet_type = 13publish_data, value=10,                |
| interval=10Secs                                                       |
|                                                                       |
| publish_data, value=11, interval=10Secs                               |
|                                                                       |
| publish_data, value=0, interval=10Secs                                |
|                                                                       |
| publish_data, value=1, interval=10Secs                                |
|                                                                       |
| publish_data, value=2, interval=10Secs                                |
|                                                                       |
| publish_data, value=3, interval=10Secs                                |
|                                                                       |
| \_mqtt_cycle : packet_type = 13publish_data, value=4, interval=10Secs |
|                                                                       |
| publish_data, value=5, interval=10Secs                                |
|                                                                       |
| publish_data, value=6, interval=10Secs                                |
|                                                                       |
| publish_data, value=7, interval=10Secs                                |
|                                                                       |
| publish_data, value=8, interval=10Secs                                |
|                                                                       |
| publish_data, value=9, interval=10Secs                                |
|                                                                       |
| \_mqtt_cycle : packet_type = 13publish_data, value=10,                |
| interval=10Secs                                                       |
|                                                                       |
| publish_data, value=11, interval=10Secs                               |
|                                                                       |
| publish_data, value=0, interval=10Secs                                |
|                                                                       |
| publish_data, value=1, interval=10Secs                                |
|                                                                       |
| publish_data, value=2, interval=10Secs                                |
|                                                                       |
| publish_data, value=3, interval=10Secs                                |
|                                                                       |
| \_mqtt_cycle : packet_type = 13publish_data, value=4, interval=10Secs |
|                                                                       |
| publish_data, value=5, interval=10Secs                                |
|                                                                       |
| publish_data, value=6, interval=10Secs                                |
|                                                                       |
| publish_data, value=7, interval=10Secs                                |
|                                                                       |
| publish_data, value=8, interval=10Secs                                |
|                                                                       |
| publish_data, value=9, interval=10Secs                                |
|                                                                       |
| publish_data, value=10, interval=10Secs                               |
|                                                                       |
| publish_data, value=11, interval=10Secs                               |
|                                                                       |
| \_mqtt_cycle : packet_type = 13publish_data, value=0, interval=10Secs |
|                                                                       |
| publish_data, value=1, interval=10Secs                                |
|                                                                       |
| publish_data, value=2, interval=10Secs                                |
|                                                                       |
| publish_data, value=3, interval=10Secs                                |
|                                                                       |
| publish_data, value=4, interval=10Secs                                |
|                                                                       |
| publish_data, value=5, interval=10Secs                                |
|                                                                       |
| \_mqtt_cycle : packet_type = 13publish_data, value=6, interval=10Secs |
|                                                                       |
| publish_data, value=7, interval=10Secs                                |
|                                                                       |
| publish_data, value=8, interval=10Secs                                |
|                                                                       |
| publish_data, value=9, interval=10Secs                                |
|                                                                       |
| publish_data, value=10, interval=10Secs                               |
|                                                                       |
| publish_data, value=11, interval=10Secs                               |
|                                                                       |
| \_mqtt_cycle : packet_type = 13publish_data, value=0, interval=10Secs |
|                                                                       |
| publish_data, value=1, interval=10Secs                                |
|                                                                       |
| publish_data, value=2, interval=10Secs                                |
|                                                                       |
| publish_data, value=3, interval=10Secs                                |
|                                                                       |
| publish_data, value=4, interval=10Secs                                |
|                                                                       |
| publish_data, value=5, interval=10Secs                                |
+=======================================================================+
+-----------------------------------------------------------------------+

**Wireshark log**:

1. The connection sequence of the MQTT is as shown in Figure 12.

|image12|

Figure : MQTT connection flow - Wireshark log

2. The Connect command is sent from Talaria TWO to MQTT broker,
   connection is established when the connect acknowledgement is
   received by Talaria TWO from broker.

|image13|

Figure : MQTT connection packet - Wireshark log

3. SUBMSG1 and SUBMSG2 are the two configured topic to subscribe,
   Talaria TWO gets registered to the topics from the subscription
   request.

|image14|

Figure : MQTT subscribe package - Wireshark log

4. Publish message is observed from Talaria TWO for the configured
   interval of seconds (10s) with the topic PUBMSG.

|image15|

Figure : MQTT publish packet - Wireshark log

5. At configured interval of seconds (60s) a ping request and response
   is observed from Talaria TWO.

|image16|

Figure : MQTT ping - Wireshark log

6. Data is sent from MQTT broker to Talaria TWO with the subscribed
   topic SUBMSG1.

|image17|

Figure : MQTT subscribe packet - Wireshark log

   **
   **

**Otii log**:

**Case 1**: Shows an average current consumption of 200µA for 30s for
MQTT subscribe. In idle cases, the average current consumption is
57.6µA.

|image18|

Figure : MQTT subscribe - Otii log

**Case 2**: Shows an average current consumption of 173µA for 30s for
MQTT publish. In idle cases, the average current consumption is 59.3µA.

   |image19|

Figure : MQTT publish - Otii log

Multicast Reception OFF GRAT ARP ON
-----------------------------------

Console output:

+-----------------------------------------------------------------------+
| UART:SNWWWWWAEBuild $Id: git-ba65998b7 $                              |
|                                                                       |
| mpd.proto=none --flash=vm --reset=evk42 mpd.mcast_rx=0                |
| wifi.arp_grat_period=10 wifi.max_idle_period=0                        |
| wifi.listen_interval=10 krn.gpio=--K wifi.keep_alive_wake_time=2      |
| mpd.regdomain=FCC mpd.suspend=1 np_conf_path=/data/nprofile.json      |
| mpd.ssid=InnoPhase mpd.passphrase=43083191                            |
|                                                                       |
| $App:git-73e7f910                                                     |
|                                                                       |
| SDK Ver: FREERTOS_SDK_1.0                                             |
|                                                                       |
| T2 Multipurpose Demp App Version 0.12                                 |
|                                                                       |
| network profile parse success.                                        |
|                                                                       |
| Suspend Enabled.                                                      |
|                                                                       |
| Multicast reception Disabled.                                         |
|                                                                       |
| Regdomain=FCC                                                         |
|                                                                       |
| addr e0:69:3a:00:13:90                                                |
|                                                                       |
| Applying reg domain: 1-11@20                                          |
|                                                                       |
| Connecting to network                                                 |
|                                                                       |
| .[2.062,636] CONNECT:00:5f:67:cd:c5:a6 Channel:11 rssi:-53 dBm        |
|                                                                       |
| WCM_NOTIFY_MSG_LINK_UP                                                |
|                                                                       |
| .WCM_NOTIFY_MSG_ADDRESS                                               |
|                                                                       |
| [2.770,812] MYIP 192.168.0.104                                        |
|                                                                       |
| [2.770,975] IPv6 [fe80::e269:3aff:fe00:1390]-link                     |
|                                                                       |
| WCM_NOTIFY_MSG_CONNECTED                                              |
|                                                                       |
| Listen interval=10                                                    |
|                                                                       |
| Traffic Timeout=12                                                    |
|                                                                       |
| pm_flags=0x0                                                          |
|                                                                       |
| [3.543,107] WARNING! wcm_pm_config may overwrite the supplied power   |
| management boot arguments!                                            |
|                                                                       |
| WiFi Connection success. proceeding to app..                          |
|                                                                       |
| Timeout not specified.!                                               |
|                                                                       |
| Application Exited..                                                  |
|                                                                       |
| Going for indefinite sleep...                                         |
+=======================================================================+
+-----------------------------------------------------------------------+

**Expected output**:

1. To verify if the GRAT ARP and multicast reception is disabled,
   connect the PC to the same AP to which the Talaria TWO is connected
   and flash the application using tool.

2. Further, the ARP table needs be cleared from the PC. This ensures
   that the ARP table does not contain entries of Talaria TWO IP
   address.

3. When the PC tries to ping, ARP does not pass as the mcast rx at
   Talaria TWO is turned off. However, Talaria TWO keeps sending the
   GRAT ARPs at configured intervals. The PC receives the GRAT ARP and
   the ARP table at the laptop gets updated, and the ping is executed.

Windows console output:

+-----------------------------------------------------------------------+
| C:\\WINDOWS\\system32>ping 192.168.1.173                              |
|                                                                       |
| PING 192.168.1.173 (192.168.1.173) 56(84) bytes of data.              |
|                                                                       |
| From 192.168.1.173 icmp_seq=1 Destination Host unreachable            |
|                                                                       |
| From 192.168.1.173 icmp_seq=2 Destination Host unreachable            |
|                                                                       |
| From 192.168.1.173 icmp_seq=3 Destination Host unreachable            |
|                                                                       |
| 64 bytes from 192.168.1.173: icmp_seq=6 ttl=255 time=676 ms           |
|                                                                       |
| 64 bytes from 192.168.1.173: icmp_seq=7 ttl=255 time=676 ms           |
|                                                                       |
| 64 bytes from 192.168.1.173: icmp_seq=8 ttl=255 time=676 ms           |
|                                                                       |
| 64 bytes from 192.168.1.173: icmp_seq=9 ttl=255 time=676 ms           |
|                                                                       |
| 64 bytes from 192.168.1.173: icmp_seq=10 ttl=255 time=676 ms          |
|                                                                       |
| 64 bytes from 192.168.1.173: icmp_seq=11 ttl=255 time=676 ms          |
+=======================================================================+
+-----------------------------------------------------------------------+

**Wireshark log**:

|image20|

Figure : Multicast Reception OFF GRAT ARP ON - Wireshark log

**Multicast OFF**:

Multicast reception disabled flag can be checked from the beacon frame
if the Multicast flag is set to false as shown in Figure 21.

|image21|

Figure : Multicast Reception OFF GRAT ARP ON - Multicast disabled
Wireshark log

**Otii log**: Shows an average current consumption of 116µA for 30s. In
idle cases, the average current consumption is 58.5µA.

|image22|

Figure : Multicast Reception OFF GRAT ARP ON - Otii log

.. |image1| image:: media/image2.png
   :width: 6.29921in
   :height: 4.71059in
.. |image2| image:: media/image3.png
   :width: 5.90551in
   :height: 5.87934in
.. |image3| image:: media/image4.png
   :width: 6.29921in
   :height: 4.65883in
.. |image4| image:: media/image5.png
   :width: 6.29921in
   :height: 3.85952in
.. |image5| image:: media/image6.png
   :width: 6.29921in
   :height: 4.66295in
.. |image6| image:: media/image7.png
   :width: 5.51181in
   :height: 2.79245in
.. |image7| image:: media/image8.png
   :width: 5.51181in
   :height: 4.06927in
.. |image8| image:: media/image9.png
   :width: 5.90551in
   :height: 3.62436in
.. |image9| image:: media/image10.png
   :width: 5.90551in
   :height: 3.98002in
.. |image10| image:: media/image11.png
   :width: 6.29921in
   :height: 3.66954in
.. |image11| image:: media/image12.png
   :width: 6.29921in
   :height: 4.25006in
.. |image12| image:: media/image13.png
   :width: 6.29921in
   :height: 1.61745in
.. |image13| image:: media/image14.png
   :width: 6.29921in
   :height: 3.00021in
.. |image14| image:: media/image15.png
   :width: 6.29921in
   :height: 3.04374in
.. |image15| image:: media/image16.png
   :width: 6.29921in
   :height: 3.49427in
.. |image16| image:: media/image17.png
   :width: 6.29921in
   :height: 3.05491in
.. |image17| image:: media/image18.png
   :width: 6.29921in
   :height: 3.90964in
.. |image18| image:: media/image19.png
   :width: 5.11811in
   :height: 3.4589in
.. |image19| image:: media/image20.png
   :width: 5.11811in
   :height: 3.47083in
.. |image20| image:: media/image21.png
   :width: 6.29921in
   :height: 3.40663in
.. |image21| image:: media/image22.png
   :width: 6.29921in
   :height: 4.59272in
.. |image22| image:: media/image23.png
   :width: 6.29921in
   :height: 4.24535in
