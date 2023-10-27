.. _Tools/Download_Tool/GUI_Overview/GUI_Overview:


Download Tool GUI Overview
==========================

Download Tool supports two types of programming:

1. Standard

2. SSBL

On launching the Download Tool application, the following come into
view:

1. GUI window on top for Standard (default) and SSBL programming,
   represented by two different tabs

2. Console window at the bottom for monitoring Talaria TWO module
   console output **Note**: In case of Windows display setting, if the
   Scale and Layout is more than 125%, GUI window might go out of
   screen.

|A screenshot of a computer Description automatically generated|

Figure 9: Download Tool GUI – Standard Programming

|image1|

Figure 10: Download Tool GUI – SSBL Programming

|image2|

Figure 11: Download Tool Console

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

**Note**:

1. While loading the ELF using this tool, the existing Partition table
   is validated as mentioned in section: `Checking and Validating the
   Partition Table <#_Checking_and_Validating>`__.

2. Keeping this tool idle for a while (around 2 to 3 hours), may lead to
   loss of communication to the EVK device. This is indicated in the
   console as “Error communicating with FTDI device”. Workaround for
   this is as follows:

   a. Close the tool

   b. Unplug & re-plug the EVK

   c. Re-open the tool again

..

   |A screen shot of a computer Description automatically generated|

Figure 12: Error communicating with FTDI device

.. |A screenshot of a computer Description automatically generated| image:: media/image1.png
   :width: 7.4794in
   :height: 3.73194in
.. |image1| image:: media/image2.png
   :width: 7.47936in
   :height: 3.73125in
.. |image2| image:: media/image3.png
   :width: 7.48031in
   :height: 2.35769in
.. |A black and white sign with a down arrow Description automatically generated| image:: media/image4.png
   :width: 0.225in
   :height: 0.24514in
.. |A grey square with a black arrow Description automatically generated| image:: media/image5.png
   :width: 0.21667in
   :height: 0.23194in
.. |image3| image:: media/image6.png
   :width: 0.20764in
   :height: 0.21667in
.. |image4| image:: media/image7.png
   :width: 0.20833in
   :height: 0.21458in
.. |image5| image:: media/image8.png
   :width: 0.21875in
   :height: 0.225in
.. |image6| image:: media/image9.png
   :width: 0.20833in
   :height: 0.20833in
.. |A black and white image of a square and a square with an arrow pointing up Description automatically generated| image:: media/image10.png
   :width: 0.225in
   :height: 0.225in
.. |A screen shot of a computer Description automatically generated| image:: media/image11.png
   :width: 6.69291in
   :height: 1.71992in
