New Serial Number to Device – Manual Method
===========================================

There might be certain instances where the user may need to manually
change/add a new EVK serial number to the Talaria TWO (T2) device.

To manually update Talaria TWO EVK’s serial number, follow the
subsequent steps:

1. Ensure the device connected is detected under COM Port as shown in
   Figure 48.

..

   |A screenshot of a computer Description automatically generated|

Figure 48: Device Manager – Composite Device

2. In case the device is not detected under COM Port, follow the
   instruction available in section: `Update Driver from libusbK to COM
   Port <#_Uninstall_Instructions_for>`__ to change the driver to USB
   Composite Device.

3. Once the device is recognized under COM Port, install FT_Prog
   software with the help of `Utilities - FTDI
   (ftdichip.com) <https://ftdichip.com/utilities/>`__ to change the
   FTDI device property as required.

4. Open the FT_Prog software and click on Scan & Parse button to detect
   the COM devices. FT_Prog software shows the identified devices in
   tree with device properties, as shown in Figure 49.

|image1|

Figure 49: FT_Prog - Device detected

5. To update the serial number, click on USB String Descriptor. Add the
   new serial number in the Serial Number field and change the product
   description as InnoPhase T2 Evaluation Board.

|image2|

Figure 50: FT_Prog - Update Serial Number

6. To upload the changes to the device, right click on FT EEPROM and
   click on Program Device.

|image3|

Figure 51: FT_Prog - Program Device

7. The device will now be updated with the new serial number as shown in
   Figure 52.

|image4|

Figure 52: FT_Prog - Updated Serial Number

8. In case the new serial number is not updated in Device Manager,
   unplug and re-plug the device to refresh the connection.

.. |A screenshot of a computer Description automatically generated| image:: media/image1.png
   :width: 7.48031in
   :height: 2.45741in
.. |image1| image:: media/image2.png
   :width: 7.48031in
   :height: 5.83939in
.. |image2| image:: media/image3.png
   :width: 7.08661in
   :height: 2.17321in
.. |image3| image:: media/image4.png
   :width: 7.08661in
   :height: 2.7815in
.. |image4| image:: media/image5.png
   :width: 7.08661in
   :height: 1.82677in
