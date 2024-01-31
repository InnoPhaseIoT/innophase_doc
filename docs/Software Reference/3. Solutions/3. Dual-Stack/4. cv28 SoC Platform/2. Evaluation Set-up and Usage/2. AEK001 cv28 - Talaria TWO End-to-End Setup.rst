AEK001 cv28 - Talaria TWO End-to-End Setup
------------------------------------------

1. For SPI connections, connect the GPIO pins from AEK001 cv28 to
   Talaria TWO EVB as shown in section: *Hardware Set-up and PIN
   Configuration*.

2. Copy the applications such as tunadapter, conmgr from:
   *host\\cv28\\dual-stack\\bins* to AEK001 cv28 host using TFTP.

3. Enable the following kernel component:

   a. Universal TUN adapter:

..

   Path: Device Drivers -> Network support -> Universal Tun/TAP device
   driver support

4. Start the tunadapter in the background.

+-----------------------------------------------------------------------+
| ./tunadapter &                                                        |
+=======================================================================+
+-----------------------------------------------------------------------+

|A screenshot of a computer program Description automatically generated|

Figure 6: tunadapter output

5. For serial logging on AEK001 cv28, connect the GPIO from AEK001 cv28
   to FT232 USB UART board as shown in Figure 5.

6. Install any serial application on the Host machine to access AEK001
   cv28’s serial console.

For example:

a. Install PuTTy Ref:
   https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html

b. Open Putty Choose Connection - - - >Serial 11/23/2021 2/5 Serial line
   connect to : (See the Device Manager- - > USB Serial Port number)
   Speed (baud) : 115200 Data bits : 8 Stop bits : 1 Parity : none Flow
   Control : none

7. To copy files onto AEK001 cv28 host:

   a. Connect the ethernet cable between the host machine and AEK001
      cv28.

   b. Set-up tftpd server on the host machine.

   c. Extract tunadapter and conmgr files from host package (location:
      *talaria_two_dual_stack_v0.1\\host\\cv28\\dual-stack\\bins*) and
      push it on to AEK001 cv28 using tftpd server using the following
      commands (Default IP of AEK001 cv28 is 10.0.0.2).

+-----------------------------------------------------------------------+
| tftp -g -r conmgr <tftp server ip>                                    |
|                                                                       |
| tftp -g -r tunadapter <tftp server ip>                                |
|                                                                       |
| -example tftp -g -r tunadapter 10.0.0.1                               |
+=======================================================================+
+-----------------------------------------------------------------------+

..

   where,

i.   tftp: Trivial File Transfer Protocol

ii.  -g: Get file

iii. -r: Remote file

8. Enter the username as root and click enter.

9. Start the tunadapter on the AEK001 cv28 host using: ./tunadapter.
   Ensure the tunadapter starts successfully as shown in Figure 7.

|Graphical user interface Description automatically generated with
medium confidence|

Figure 7: Starting tunadapter

10. Now use the conmgr command to scan, connect etc.

For example: ./conmgr connect <AP SSID> <AP PWD>

.. |A screenshot of a computer program Description automatically generated| image:: media/image1.png
   :width: 6.9685in
   :height: 5.92514in
.. |Graphical user interface Description automatically generated with medium confidence| image:: media/image2.png
   :width: 7.48031in
   :height: 4.9683in
