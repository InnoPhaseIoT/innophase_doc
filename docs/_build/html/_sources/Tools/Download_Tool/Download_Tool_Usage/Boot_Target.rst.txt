Boot Target
===========

Connected EVKs appear in the EVK serial number drop-down and the
appropriate EVK can be selected.

|image1|

Figure 13: Boot target - EVK selection

**Note**:

If any connected EVK devices do not have a serial number, the Download
tool will automatically handle this by generating a new serial number
and update the same onto the corresponding device. During this process,
the tool will indicate this in the status bar, as shown in Figure 14.

Format of the new serial number:

+-----------------------------------------------------------------------+
| <year_stamp>-<integer>                                                |
+=======================================================================+
+-----------------------------------------------------------------------+

where,

- <year_stamp>: Current year. For example: 2023

- <integer>: Formed from the sum of last 3 octets (in decimal) of the
MAC address found in the device.

|image2|

Figure 14: Boot target – Serial number update

Since a new serial number is generated from the MAC address of the
device, devices with the same MAC address will get updated with the same
serial number. This is an expected behavior.

User can manually update the new serial number to the device following
the instructions mentioned in section: `New Serial Number to Device –
Manual Method <#_New_Serial_Number>`__.

.. |image1| image:: media/image1.png
   :width: 7.48031in
   :height: 1.33166in
.. |image2| image:: media/image2.png
   :width: 7.48031in
   :height: 0.70955in