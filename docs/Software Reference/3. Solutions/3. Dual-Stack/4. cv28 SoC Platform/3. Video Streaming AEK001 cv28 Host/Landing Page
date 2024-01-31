Video Streaming – AEK001 CV28 Host
==================================

This document describes the steps to setup and run the video streaming
using Talaria TWO Dual-Stack solution with FreeRTOS support on AEK001
CV28 Host.

Getting Started
===============

To get started with the Dual-Stack solution, refer *Prerequisites*,
*Hardware Set-up* and *Programming Talaria TWO Application* sections of
QSG_Talaria_TWO_Dual-Stack_cv28.pdf
(*\\talaria_two_dual_stack\\talaria_two_dual_stack_vx.y*).

**Note**: x and y in *vx.y* refers to the package release version.

Prerequisites
=============

1. VLC player

2. GTKTerm or similar application

AEK001 CV28 Host - Talaria TWO end-to-end Video Setup
=====================================================

After the hardware setup (refer section: *Getting Started*), follow the
subsequent steps to run the video application. Use any serial port
terminal application such as GTKTerm to issue the commands on AEK001
CV28.

1. Configure GPIO on the AEK001 CV28 host to wake up Talaria TWO.

+-----------------------------------------------------------------------+
| echo "26" > /sys/class/gpio/export                                    |
|                                                                       |
| echo "out" > /sys/class/gpio/gpio26/direction                         |
|                                                                       |
| echo "0" > /sys/class/gpio/gpio26/value                               |
+=======================================================================+
+-----------------------------------------------------------------------+

2. Start tunadapter in the background.

+-----------------------------------------------------------------------+
| ./tunadapter tos=160&                                                 |
+=======================================================================+
+-----------------------------------------------------------------------+

|A screen shot of a computer Description automatically generated|

Figure 1: Start tunadapter

3. Connect Talaria TWO to an Access Point.

|image1|

Figure 2: Connect to AP

4. To following kernel modules need to be inserted for enabling video
   streaming:

+-----------------------------------------------------------------------+
| insmod /lib/modules/5.4.120/extra/hw_timer.ko                         |
|                                                                       |
| insmod /lib/modules/5.4.120/extra/ambnl.ko                            |
|                                                                       |
| insmod /lib/modules/5.4.120/extra/ambcma.ko                           |
|                                                                       |
| insmod /lib/modules/5.4.120/extra/dsp.ko                              |
|                                                                       |
| insmod /lib/modules/5.4.120/extra/imgproc.ko                          |
|                                                                       |
| insmod /lib/modules/5.4.120/extra/iav.ko                              |
|                                                                       |
| insmod /lib/modules/5.4.120/extra/jx_f32_mipi.ko                      |
|                                                                       |
| sleep 1                                                               |
|                                                                       |
| test_aaa_service -a &                                                 |
|                                                                       |
| test_encode –hdmi 1080p –resource-cfg /usr/local/bin/scripts/cv28     |
| vin0 1080p linear.lua                                                 |
|                                                                       |
| rtsp_server &                                                         |
|                                                                       |
| test_encode -A -H 1080p -e                                            |
+=======================================================================+
+-----------------------------------------------------------------------+

|A screenshot of a computer Description automatically generated|

|image2|

|A computer screen shot of a program Description automatically
generated|

Figure 3: Insert ko modules and start RTSP server - console logs

5. Get the IP address of tun interface using ifconfig command:

|image3|

Figure 4: ifconfig -output

6. Open VLC application and enter the RTSP URL in the network settings
   using the following command and click on Play. Video starts streaming
   after this.

+-----------------------------------------------------------------------+
| rtsp://<TUN IP ADDR>/stream”                                          |
+=======================================================================+
+-----------------------------------------------------------------------+

|image4|

Figure 5: VLC player

.. |A screen shot of a computer Description automatically generated| image:: media/image1.png
   :width: 6.88976in
   :height: 7.37142in
.. |image1| image:: media/image2.png
   :width: 6.88976in
   :height: 1.14659in
.. |A screenshot of a computer Description automatically generated| image:: media/image3.png
   :width: 6.69291in
   :height: 1.67979in
.. |image2| image:: media/image4.png
   :width: 6.69291in
   :height: 3.86004in
.. |A computer screen shot of a program Description automatically generated| image:: media/image5.png
   :width: 6.69291in
   :height: 2.38126in
.. |image3| image:: media/image6.png
   :width: 6.69291in
   :height: 1.35631in
.. |image4| image:: media/image7.png
   :width: 6.69291in
   :height: 4.1601in
