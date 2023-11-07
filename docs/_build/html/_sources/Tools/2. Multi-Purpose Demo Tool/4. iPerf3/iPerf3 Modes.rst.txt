Iperf3 Modes
=============

Select the iPerf3 tab on the Demo tool GUI to automatically load the
signed firmware image for iPerf3 application.

The following sections provide information on the different modes in
which the iPerf3 application can be used along with their respective
outputs.

UDP Throughput Test Downlink
----------------------------

Console output of UDP Downlink test:

+-----------------------------------------------------------------------+
| Y-BOOT 208ef13 2019-07-22 12:26:54 -0500 790da1-b-7                   |
|                                                                       |
| ROM yoda-h0-rom-16-0-gd5a8e586                                        |
|                                                                       |
| FLASH:PNWWWWWAEBuild $Id: git-e31bdbe13 $                             |
|                                                                       |
| krn.gpio=--K suspend=1 np_conf_path=/data/nprofile.json               |
| ssid=InnoPhase passphrase=43083191                                    |
|                                                                       |
| addr e0:69:3a:00:2c:42                                                |
|                                                                       |
| [0.690,936] CONNECT:b0:39:56:93:83:31 Channel:6 rssi:-47 dBm          |
|                                                                       |
| [0.732,813] MYIP 192.168.1.131                                        |
|                                                                       |
| [0.732,977] IPv6 [fe80::e269:3aff:fe00:2c42]-link                     |
|                                                                       |
| IPerf3 server @ 192.168.1.131                                         |
|                                                                       |
| ----------------------------------------                              |
|                                                                       |
| Iperf3 TCP/UDP server listening on 5201                               |
|                                                                       |
| ----------------------------------------                              |
|                                                                       |
| Accepted connection from 192.168.1.124 port 47552                     |
|                                                                       |
| [ 1] local 192.168.1.131 port 20756 connected to 192.168.1.124 port   |
| 34976                                                                 |
|                                                                       |
| RSSI start: -46 dBm                                                   |
|                                                                       |
| RSSI end: -48 dBm                                                     |
|                                                                       |
| ------------------------------                                        |
|                                                                       |
| [ ID] Interval Transfer Bitrate                                       |
|                                                                       |
| [ 1] iperf3[S-RX-udp]: 0.0-30 sec 106.4 MBytes 29.7 Mbits/sec         |
|                                                                       |
| User: 23606574 (78%)                                                  |
|                                                                       |
| IRQ: 2906897 (9%)                                                     |
|                                                                       |
| Idle: 3489850 (11%)                                                   |
+=======================================================================+
+-----------------------------------------------------------------------+

Windows console output:

+-----------------------------------------------------------------------+
| C:\                                                                   |
| \Users\\InnoP\\Downloads\\iperf-3.1.3-win64\\iperf-3.1.3-win64>iperf3 |
| -c 192.168.1.131 -u -b30M -i1 -t30                                    |
|                                                                       |
| Connecting to host 192.168.1.131, port 5201                           |
|                                                                       |
| [ 5] local 192.168.1.124 port 34976 connected to 192.168.1.131 port   |
| 5201                                                                  |
|                                                                       |
| [ ID] Interval Transfer Bitrate Total Datagrams                       |
|                                                                       |
| [ 5] 0.00-1.00 sec 3.57 MBytes 30.0 Mbits/sec 2567                    |
|                                                                       |
| [ 5] 1.00-2.00 sec 3.58 MBytes 30.0 Mbits/sec 2568                    |
|                                                                       |
| [ 5] 2.00-3.00 sec 3.58 MBytes 30.0 Mbits/sec 2569                    |
|                                                                       |
| [ 5] 3.00-4.00 sec 3.58 MBytes 30.0 Mbits/sec 2568                    |
|                                                                       |
| .                                                                     |
|                                                                       |
| .                                                                     |
|                                                                       |
| .                                                                     |
|                                                                       |
| .                                                                     |
|                                                                       |
| .                                                                     |
|                                                                       |
| [ 5] 24.00-25.00 sec 3.58 MBytes 30.0 Mbits/sec 2569                  |
|                                                                       |
| [ 5] 25.00-26.00 sec 3.58 MBytes 30.0 Mbits/sec 2568                  |
|                                                                       |
| [ 5] 26.00-27.00 sec 3.58 MBytes 30.0 Mbits/sec 2569                  |
|                                                                       |
| [ 5] 27.00-28.00 sec 3.58 MBytes 30.0 Mbits/sec 2568                  |
|                                                                       |
| [ 5] 28.00-29.00 sec 3.58 MBytes 30.0 Mbits/sec 2569                  |
|                                                                       |
| [ 5] 29.00-30.00 sec 3.58 MBytes 30.0 Mbits/sec 2569                  |
|                                                                       |
| - - - - - - - - - - - - - - - - - - - - - - - - -                     |
|                                                                       |
| [ ID] Interval Transfer Bitrate Jitter Lost/Total Datagrams           |
|                                                                       |
| [ 5] 0.00-30.00 sec 107 MBytes 30.0 Mbits/sec 0.000 ms 0/77054 (0%)   |
| sender                                                                |
|                                                                       |
| [ 5] 0.00-30.00 sec 106 MBytes 29.8 Mbits/sec 0.000 ms 634/77054      |
| (0.82%) receiver                                                      |
|                                                                       |
| iperf Done.                                                           |
+=======================================================================+
+-----------------------------------------------------------------------+

UDP Throughput Test Uplink
--------------------------

Console output for UDP throughput uplink test:

+-----------------------------------------------------------------------+
| ----------------------------------------                              |
|                                                                       |
| Iperf3 TCP/UDP server listening on 5201                               |
|                                                                       |
| ----------------------------------------                              |
|                                                                       |
| Accepted connection from 192.168.1.124 port 47568                     |
|                                                                       |
| [ 1] local 192.168.1.131 port 20756 connected to 192.168.1.124 port   |
| 39126                                                                 |
|                                                                       |
| RSSI start: -47 dBm                                                   |
|                                                                       |
| RSSI end: -49 dBm                                                     |
|                                                                       |
| ------------------------------                                        |
|                                                                       |
| [ ID] Interval Transfer Bitrate                                       |
|                                                                       |
| [ 1] iperf3[S-TX-udp]: 0.0-30 sec 48.8 MBytes 13.6 Mbits/sec          |
|                                                                       |
| User: 10874781 (36%)                                                  |
|                                                                       |
| IRQ: 1501611 (5%)                                                     |
|                                                                       |
| Idle: 17631727 (58%)                                                  |
+=======================================================================+
+-----------------------------------------------------------------------+

Windows console output:

+-----------------------------------------------------------------------+
| C:\\Users\\InnoP\\Downloads\\iperf-3.1.3-win64\\iperf-3.1.3-win64>    |
| iperf3 -c 192.168.1.131 -u -b30M -i1 -t30 -R                          |
|                                                                       |
| Connecting to host 192.168.1.131, port 5201                           |
|                                                                       |
| Reverse mode, remote host 192.168.1.131 is sending                    |
|                                                                       |
| [ 5] local 192.168.1.124 port 39126 connected to 192.168.1.131 port   |
| 5201                                                                  |
|                                                                       |
| [ ID] Interval Transfer Bitrate Jitter Lost/Total Datagrams           |
|                                                                       |
| [ 5] 0.00-1.00 sec 2.62 MBytes 22.0 Mbits/sec 0.605 ms 0/1881 (0%)    |
|                                                                       |
| [ 5] 1.00-2.00 sec 2.62 MBytes 21.9 Mbits/sec 1.475 ms 0/1879 (0%)    |
|                                                                       |
| [ 5] 2.00-3.00 sec 1.26 MBytes 10.6 Mbits/sec 1.434 ms 0/907 (0%)     |
|                                                                       |
| [ 5] 3.00-4.00 sec 1.74 MBytes 14.6 Mbits/sec 0.773 ms 0/1247 (0%)    |
|                                                                       |
| [ 5] 4.00-5.00 sec 1.36 MBytes 11.4 Mbits/sec 0.828 ms 0/976 (0%)     |
|                                                                       |
| [ 5] 5.00-6.00 sec 1.76 MBytes 14.7 Mbits/sec 1.314 ms 0/1262 (0%)    |
|                                                                       |
| [ 5] 6.00-7.00 sec 1.63 MBytes 13.7 Mbits/sec 0.931 ms 0/1173 (0%)    |
|                                                                       |
| .                                                                     |
|                                                                       |
| .                                                                     |
|                                                                       |
| .                                                                     |
|                                                                       |
| [ 5] 26.00-27.00 sec 1.53 MBytes 12.8 Mbits/sec 1.512 ms 0/1096 (0%)  |
|                                                                       |
| [ 5] 27.00-28.00 sec 1.59 MBytes 13.3 Mbits/sec 1.299 ms 0/1142 (0%)  |
|                                                                       |
| [ 5] 28.00-29.00 sec 1.53 MBytes 12.8 Mbits/sec 1.160 ms 0/1097 (0%)  |
|                                                                       |
| [ 5] 29.00-30.00 sec 1.57 MBytes 13.2 Mbits/sec 1.988 ms 0/1128 (0%)  |
|                                                                       |
| - - - - - - - - - - - - - - - - - - - - - - - - -                     |
|                                                                       |
| [ ID] Interval Transfer Bitrate Jitter Lost/Total Datagrams           |
|                                                                       |
| [ 5] 0.00-30.00 sec 48.9 MBytes 13.7 Mbits/sec 0.000 ms 0/35102 (0%)  |
| sender                                                                |
|                                                                       |
| [ 5] 0.00-30.00 sec 48.8 MBytes 13.6 Mbits/sec 1.988 ms 0/35022 (0%)  |
| receiver                                                              |
|                                                                       |
| iperf Done.                                                           |
+=======================================================================+
+-----------------------------------------------------------------------+

TCP Throughput Test Downlink 
-----------------------------

Console output of TCP Throughput Downlink test:

+-----------------------------------------------------------------------+
| ----------------------------------------                              |
|                                                                       |
| Iperf3 TCP/UDP server listening on 5201                               |
|                                                                       |
| ----------------------------------------                              |
|                                                                       |
| Accepted connection from 192.168.1.124 port 47556                     |
|                                                                       |
| [ 1] local 192.168.1.131 port 5201 connected to 192.168.1.124 port    |
| 47558                                                                 |
|                                                                       |
| RSSI start: -47 dBm                                                   |
|                                                                       |
| RSSI end: -48 dBm                                                     |
|                                                                       |
| ------------------------------                                        |
|                                                                       |
| [ ID] Interval Transfer Bitrate                                       |
|                                                                       |
| [ 1] iperf3[S-RX-tcp]: 0.0-30 sec 84.8 MBytes 23.7 Mbits/sec          |
|                                                                       |
| User: 26877186 (88%)                                                  |
|                                                                       |
| IRQ: 3241560 (10%)                                                    |
|                                                                       |
| Idle: 124208 (0%)                                                     |
+=======================================================================+
+-----------------------------------------------------------------------+

Windows console output:

+-----------------------------------------------------------------------+
| C:\                                                                   |
| \Users\\InnoP\\Downloads\\iperf-3.1.3-win64\\iperf-3.1.3-win64>iperf3 |
| -c 192.168.1.131 -i1 -t30                                             |
|                                                                       |
| Connecting to host 192.168.1.131, port 5201                           |
|                                                                       |
| [ 5] local 192.168.1.124 port 47558 connected to 192.168.1.131 port   |
| 5201                                                                  |
|                                                                       |
| [ ID] Interval Transfer Bitrate Retr Cwnd                             |
|                                                                       |
| [ 5] 0.00-1.00 sec 3.14 MBytes 26.3 Mbits/sec 0 67.0 KBytes           |
|                                                                       |
| [ 5] 1.00-2.00 sec 2.91 MBytes 24.4 Mbits/sec 0 67.0 KBytes           |
|                                                                       |
| [ 5] 2.00-3.00 sec 2.79 MBytes 23.4 Mbits/sec 0 67.0 KBytes           |
|                                                                       |
| [ 5] 3.00-4.00 sec 2.91 MBytes 24.4 Mbits/sec 0 67.0 KBytes           |
|                                                                       |
| [ 5] 4.00-5.00 sec 2.91 MBytes 24.4 Mbits/sec 10 47.1 KBytes          |
|                                                                       |
| [ 5] 5.00-6.00 sec 2.76 MBytes 23.1 Mbits/sec 21 17.1 KBytes          |
|                                                                       |
| [ 5] 6.00-7.00 sec 2.91 MBytes 24.4 Mbits/sec 20 34.2 KBytes          |
|                                                                       |
| [ 5] 7.00-8.00 sec 2.76 MBytes 23.1 Mbits/sec 9 28.5 KBytes           |
|                                                                       |
| .                                                                     |
|                                                                       |
| .                                                                     |
|                                                                       |
| .                                                                     |
|                                                                       |
| .                                                                     |
|                                                                       |
| [ 5] 23.00-24.00 sec 2.79 MBytes 23.4 Mbits/sec 0 67.0 KBytes         |
|                                                                       |
| [ 5] 24.00-25.00 sec 2.91 MBytes 24.4 Mbits/sec 22 14.3 KBytes        |
|                                                                       |
| [ 5] 25.00-26.00 sec 2.76 MBytes 23.1 Mbits/sec 28 15.7 KBytes        |
|                                                                       |
| [ 5] 26.00-27.00 sec 2.76 MBytes 23.1 Mbits/sec 22 24.2 KBytes        |
|                                                                       |
| [ 5] 27.00-28.00 sec 2.91 MBytes 24.4 Mbits/sec 9 29.9 KBytes         |
|                                                                       |
| [ 5] 28.00-29.00 sec 2.79 MBytes 23.4 Mbits/sec 7 14.3 KBytes         |
|                                                                       |
| [ 5] 29.00-30.00 sec 2.94 MBytes 24.7 Mbits/sec 8 32.8 KBytes         |
|                                                                       |
| - - - - - - - - - - - - - - - - - - - - - - - - -                     |
|                                                                       |
| [ ID] Interval Transfer Bitrate Retr                                  |
|                                                                       |
| [ 5] 0.00-30.00 sec 84.8 MBytes 23.7 Mbits/sec 296 sender             |
|                                                                       |
| [ 5] 0.00-30.00 sec 84.8 MBytes 23.7 Mbits/sec receiver               |
|                                                                       |
| iperf Done.                                                           |
|                                                                       |
| -----------------                                                     |
+=======================================================================+
+-----------------------------------------------------------------------+

TCP Throughput Test Uplink
--------------------------

Console output of TCP Throughput Uplink test.

+-----------------------------------------------------------------------+
| ----------------------------------------                              |
|                                                                       |
| Iperf3 TCP/UDP server listening on 5201                               |
|                                                                       |
| ----------------------------------------                              |
|                                                                       |
| Accepted connection from 192.168.1.124 port 47564                     |
|                                                                       |
| [ 1] local 192.168.1.131 port 5201 connected to 192.168.1.124 port    |
| 47566                                                                 |
|                                                                       |
| RSSI start: -47 dBm                                                   |
|                                                                       |
| RSSI end: -48 dBm                                                     |
|                                                                       |
| ------------------------------                                        |
|                                                                       |
| [ ID] Interval Transfer Bitrate                                       |
|                                                                       |
| [ 1] iperf3[S-TX-tcp]: 0.0-30 sec 48.7 MBytes 13.6 Mbits/sec          |
|                                                                       |
| User: 13556511 (45%)                                                  |
|                                                                       |
| IRQ: 1300291 (4%)                                                     |
|                                                                       |
| Idle: 15148431 (50%)                                                  |
+=======================================================================+
+-----------------------------------------------------------------------+

Windows console output:

+-----------------------------------------------------------------------+
| C:\\Users\\InnoP\\Downloads\\iperf-3.1.3-win64\\iperf-3.1.3-win64>    |
| iperf3 -c 192.168.1.131 -i1 -t30 -R                                   |
|                                                                       |
| Connecting to host 192.168.1.131, port 5201                           |
|                                                                       |
| Reverse mode, remote host 192.168.1.131 is sending                    |
|                                                                       |
| [ 5] local 192.168.1.124 port 47566 connected to 192.168.1.131 port   |
| 5201                                                                  |
|                                                                       |
| [ ID] Interval Transfer Bitrate                                       |
|                                                                       |
| [ 5] 0.00-1.00 sec 2.03 MBytes 17.0 Mbits/sec                         |
|                                                                       |
| [ 5] 1.00-2.00 sec 2.43 MBytes 20.4 Mbits/sec                         |
|                                                                       |
| [ 5] 2.00-3.00 sec 2.48 MBytes 20.8 Mbits/sec                         |
|                                                                       |
| [ 5] 3.00-4.00 sec 2.46 MBytes 20.6 Mbits/sec                         |
|                                                                       |
| [ 5] 4.00-5.00 sec 2.51 MBytes 21.0 Mbits/sec                         |
|                                                                       |
| [ 5] 5.00-6.00 sec 1.87 MBytes 15.7 Mbits/sec                         |
|                                                                       |
| .                                                                     |
|                                                                       |
| .                                                                     |
|                                                                       |
| .                                                                     |
|                                                                       |
| [ 5] 27.00-28.00 sec 1.31 MBytes 11.0 Mbits/sec                       |
|                                                                       |
| [ 5] 28.00-29.00 sec 1.35 MBytes 11.3 Mbits/sec                       |
|                                                                       |
| [ 5] 29.00-30.00 sec 1.38 MBytes 11.6 Mbits/sec                       |
|                                                                       |
| - - - - - - - - - - - - - - - - - - - - - - - - -                     |
|                                                                       |
| [ ID] Interval Transfer Bitrate Retr                                  |
|                                                                       |
| [ 5] 0.00-30.00 sec 48.8 MBytes 13.6 Mbits/sec 0 sender               |
|                                                                       |
| [ 5] 0.00-30.00 sec 48.7 MBytes 13.6 Mbits/sec receiver               |
|                                                                       |
| iperf Done.                                                           |
+=======================================================================+
+-----------------------------------------------------------------------+
