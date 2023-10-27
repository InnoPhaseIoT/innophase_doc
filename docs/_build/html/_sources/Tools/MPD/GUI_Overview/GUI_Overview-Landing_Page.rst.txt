GUI - Overview
==============

On launching the application, the GUI window as shown in Figure 11 will
come into view.

**Note**: In case of windows display setting Scale and layout is more
than 125%, GUI window might go out of screen.

|image1|

Figure 11: Demo Tool GUI

1. **Boot Target**: Connected EVKs appear in the EVK serial number
   drop-down and the appropriate EVK can be selected.

..

   **Note**:

   If any connected EVK devices do not have a serial number, the
   Download tool will automatically handle this by generating a new
   serial number and update the same onto the corresponding device.
   During this process, the tool will indicate this in the status bar,
   as shown in Figure 12.

   Format of the new serial number:

+-----------------------------------------------------------------------+
| <year_stamp>-<integer>                                                |
+=======================================================================+
+-----------------------------------------------------------------------+

..

   where,

   - <year_stamp>: Current year. For example: 2023

   - <integer>: Formed from the sum of last 3 octets (in decimal) of the
   MAC address found in the device.

   |A screenshot of a login screen Description automatically generated|

   Figure 12: Boot target – Serial number update

   Since a new serial number is generated from the MAC address of the
   device, devices with the same MAC address will get updated with the
   same serial number. This is an expected behavior.

   User can manually update the new serial number to the device
   following the instructions mentioned in section: `New Serial Number
   to Device – Manual Method <#_References>`__.

2. **AP Options**: The SSID and Passphrase entered in the respective
   fields will connect the EVK board to the Access Point. Once
   connected, as per requirement MPD/iPerf3/Scan applications can be
   loaded by selecting the appropriate tab.

3. **Configure the Application**: Configure the Setup Parameters:

   a. **Turn On deep sleep mode**: When the processor is idle or is
      waiting for an event or data to occur or be received, turning ON
      the Turn On deep sleep mode feature by checking the box adjacent
      to the field will put Talaria TWO in a power saving mode.

   b. **Select Regulatory Domain**: Depending on their region of
      operation, the user can select any one of the following
      appropriate regulatory domains to establish a connection between
      the EVK board and the Access Point:

      i.   FCC

      ii.  ETSI

      iii. TELEC

      iv.  KCC

4. **Program and Reset the Device**:

   a. **Reset**:

..

   Reload the application in Flash memory

b. **CLEAR Flash**:

..

   Erase the application in Flash memory

c. **PROG RAM**:

..

   Program the application to RAM memory

d. **PROG Flash**:

..

   Program the application to Flash memory

**Note**:

PROG RAM will clear the application from Flash. The user is alerted of
the same during PROG RAM through a pop-up message as shown in Figure 13.
User can select the Do not show again checkbox to stop this pop-up
message from appearing next time.

|image2|

Figure 13: PROG RAM alert message

The console window is as shown in Figure 14.

|A screenshot of a computer Description automatically generated|

Figure 14: Console window

The console window has the following icons (with Hover Text):

1. **Auto Scroll** |A black and white sign with a down arrow Description
   automatically generated|: Enables scrolling of console content till
   the end (default mode).

2. **Pause Scroll** |A grey square with a black arrow Description
   automatically generated|: Turns OFF Auto Scroll mode.

3. **Clear Console** |image3|: Clears console window content.

4. **Save Logs** |image4|: Opens a file dialog with Console_Output.log
   as the default file name to save the logs.

Note: Only upcoming data after starting the Save Logs is saved in the
file.

5. **Stop Save Logs** |image5| : Stops saving console logs to the file.
   This icon appears after Save Logs is started successfully.

6. **Pop Out** |image6|: Pops out the console window separate from the
   GUI window.

7. **Pop In** |A black and white image of a square and a square with an
   arrow pointing up Description automatically generated|: Embeds the
   console and GUI window together.

Keeping this tool idle for a while (around 2 to 3 hours), may lead to
loss of communication to the EVK device. This is indicated in the
console as “Error communicating with FTDI device”, as show in Figure 15.
Workaround for this is as follows:

1. Close the tool

2. Unplug & re-plug the EVK

3. Re-open the tool again

|image7|

Figure 15: Error communicating with FTDI device

.. |image1| image:: media/image1.png
   :width: 7.48031in
   :height: 3.6638in
.. |A screenshot of a login screen Description automatically generated| image:: media/image2.png
   :width: 7.10382in
   :height: 1.01295in
.. |image2| image:: media/image3.png
   :width: 7.48031in
   :height: 1.98921in
.. |A screenshot of a computer Description automatically generated| image:: media/image4.png
   :width: 7.47986in
   :height: 1.92917in
.. |A black and white sign with a down arrow Description automatically generated| image:: media/image5.png
   :width: 0.225in
   :height: 0.24514in
.. |A grey square with a black arrow Description automatically generated| image:: media/image6.png
   :width: 0.21667in
   :height: 0.23194in
.. |image3| image:: media/image7.png
   :width: 0.20764in
   :height: 0.21667in
.. |image4| image:: media/image8.png
   :width: 0.20833in
   :height: 0.21458in
.. |image5| image:: media/image9.png
   :width: 0.21875in
   :height: 0.225in
.. |image6| image:: media/image10.png
   :width: 0.20833in
   :height: 0.20833in
.. |A black and white image of a square and a square with an arrow pointing up Description automatically generated| image:: media/image11.png
   :width: 0.225in
   :height: 0.225in
.. |image7| image:: media/image12.png
   :width: 7.48031in
   :height: 1.56384in
