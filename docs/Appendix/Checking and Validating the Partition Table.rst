Checking and Validating the Partition Table
-------------------------------------------

Standard Programming
~~~~~~~~~~~~~~~~~~~~

Download tool will validate the existing partition table in the EVB, for
the following condition:

.. table:: Table 1: Standard programming: Partition Table – Condition

   +----------------------+-----------------------+-----------------------+
   | **Partition Name**   | **Sector Start**      | **Sector Count**      |
   +======================+=======================+=======================+
   | BOOT                 | 1                     | 63                    |
   +----------------------+-----------------------+-----------------------+
   | VIRT                 | 64                    | >=65                  |
   +----------------------+-----------------------+-----------------------+
   | SYSFS                | 496                   | 16                    |
   +----------------------+-----------------------+-----------------------+

**Case 1: Existing partition matches SSBL programming partition**

If the existing partition does not satisfy the condition mentioned in
Table 1, but matches with the SSBL programming partition, the user is
notified by a pop-up message. The user will then have the option
(Yes/No) to either flash the default partition table or terminate the
action (i.e., correct the deviation manually and try again).

|image26|

Figure 34: Deviation from the standard programming partition – matches
SSBL programming partition

If the user selects ‘No’ and chooses not to back-up to the local system,
action is terminated requiring the user to manually correct the
deviation to proceed further.

|image28|

Figure 35: Standard programming - action terminated

**Case 2: Existing partition neither satisfies Standard programming
partition, nor SSBL programming partition**

If the existing partition neither satisfies the condition mentioned in
Table 1, nor the SSBL programming partition, the user is notified by a
pop-up message. The user will then have the option (Yes/No) to either
flash the default partition table or terminate the action (i.e., correct
the deviation manually and try again).

|image31|

Figure 36: Deviation from the standard programming partition - no match

**Note**: In case the user-defined partition table meets the condition
mentioned in Table 1, but with VIRT partition less than the application
VM image size, a pop-up message notifies the same to the user with an
option of overwriting existing partition with default partition table.

|image32|

Figure 37: VM image does not fit in partition

1. If the user chooses to flash the default partition (option: Yes):

Download tool will back-up the contents of SYSFS and DATA partition of
existing partition table. Once the default partition is flashed
successfully, the backed-up contents of SYSFS and DATA partitions are
re-flashed to the corresponding new location as per the default
partition table.

a. In case the backed-up contents of SYSFS does not fit into the
   corresponding new location as per the default partition table
   (regarding size), user will have an option (Yes/No) to either back-up
   the content to local system and clear the data in EVB or correct the
   deviation manually and try again.

..

   |image34|

Figure 38: Backed-up contents of SYSFS

i. If the user chooses to back-up to local system (option: Yes):

..

   The contents will be saved in the local system and the user will be
   notified with the folder path through a popup message.

   |image36|

   Figure 39: Contents saved in the local system

ii. If the user does not choose to back-up to local system (option: No):

..

   The action will be terminated, and user will be required to correct
   the deviation manually to proceed further.

   |image38|

   Figure 40: Action terminated requiring to correct the deviation
   manually

b. In case the back-up contents of DATA partition do not fit the
   corresponding location in the default partition, the contents will be
   saved in the local system and the user will be notified with the
   folder path through a pop-up message. Also, the user will be
   intimated to write the new certification file to DATA partition using
   Write Files option.

..

   |image40|

Figure 41: Back-up contents of DATA partition

c. However, if the user does not choose to flash the default partition
   (option: No):

..

   The action will be terminated, and the user will be required to
   correct the deviation manually to proceed further.

   |image42|

Figure 42: User does not choose to flash default partition – action
terminated

SSBL Programming
~~~~~~~~~~~~~~~~

Download tool will validate the existing partition table in the EVB, for
the following condition:

.. table:: Table 2: SSBL programming: Partition Table – Condition

   +----------------------+-----------------------+-----------------------+
   | **Partition Name**   | **Sector Start**      | **Sector Count**      |
   +======================+=======================+=======================+
   | BOOT                 | 1                     | 31                    |
   +----------------------+-----------------------+-----------------------+
   | BOOT                 | 32                    | 352                   |
   +----------------------+-----------------------+-----------------------+
   | DATA                 | 384                   | 112                   |
   +----------------------+-----------------------+-----------------------+
   | SYSFS                | 496                   | 16                    |
   +----------------------+-----------------------+-----------------------+

If the existing partition does not satisfy the condition mentioned in
Table 2, but matches with the default programming partition, the user is
notified by a pop-up message.

The user will then have the option (Yes/No) to either flash the default
partition table or terminate the action (i.e., correct the deviation
manually and try again).

|image45|

Figure 43: Deviation from the SSBL programming partition – matches
default programming partition

If the user selects ‘No’ and chooses not to flash the default SSBL
partition table, action is terminated requiring the user to manually
correct the deviation to proceed further.

|image48|

Figure 44: SSBL programming - action terminated

.. |image1| image:: media/image1.png
   :width: 0.7874in
.. |A screenshot of a computer Description automatically generated| image:: media/image2.png
   :width: 7.48031in
   :height: 3.70968in
.. |image2| image:: media/image1.png
   :width: 0.98425in
.. |image3| image:: media/image3.png
   :width: 7.48031in
   :height: 3.69218in
.. |A black rectangle with red border Description automatically generated| image:: media/image4.png
   :width: 2.49375in
   :height: 1.21319in
.. |image4| image:: media/image1.png
   :width: 0.98425in
.. |image5| image:: media/image5.png
   :width: 7.48031in
   :height: 3.70068in
.. |Graphical user interface, text, application Description automatically generated| image:: media/image6.png
   :width: 4.33071in
   :height: 1.63567in
.. |image6| image:: media/image1.png
   :width: 0.98425in
.. |image7| image:: media/image7.png
   :width: 6.69291in
   :height: 3.34609in
.. |image8| image:: media/image1.png
   :width: 0.85897in
.. |image9| image:: media/image8.png
   :width: 5.90551in
   :height: 2.93909in
.. |image10| image:: media/image1.png
   :width: 0.98425in
.. |image11| image:: media/image9.png
   :width: 5.90551in
   :height: 2.93909in
.. |image12| image:: media/image1.png
   :width: 0.98425in
.. |image13| image:: media/image10.png
   :width: 6.29921in
   :height: 3.13502in
.. |image14| image:: media/image1.png
   :width: 0.98425in
.. |image15| image:: media/image11.png
   :width: 6.29921in
   :height: 2.83056in
.. |image16| image:: media/image1.png
   :width: 0.98403in
.. |image17| image:: media/image1.png
   :width: 1.05833in
   :height: 0.11667in
.. |image18| image:: media/image12.png
   :width: 7.48031in
   :height: 3.68752in
.. |image19| image:: media/image1.png
   :width: 0.98403in
.. |image20| image:: media/image1.png
   :width: 1.55128in
.. |image21| image:: media/image13.png
   :width: 7.48031in
   :height: 3.69722in
.. |image26| image:: media/images26.png
   :width: 7.48031in
   :height: 3.69722in

.. |image28| image:: media/images28.png
   :width: 7.48031in
   :height: 3.69722in
.. |image31| image:: media/images31.png
   :width: 7.48031in
   :height: 3.69722in
.. |image32| image:: media/images32.png
   :width: 7.48031in
   :height: 3.69722in
.. |image34| image:: media/images34.png
   :width: 7.48031in
   :height: 3.69722in
.. |image36| image:: media/images36.png
   :width: 7.48031in
   :height: 3.69722in
.. |image38| image:: media/images38.png
   :width: 7.48031in
   :height: 3.69722in
.. |image40| image:: media/images40.png
   :width: 7.48031in
   :height: 3.69722in
.. |image42| image:: media/images42.png
   :width: 7.48031in
   :height: 3.69722in
.. |image45| image:: media/images45.png
   :width: 7.48031in
   :height: 3.69722in
.. |image48| image:: media/images48.png
   :width: 7.48031in
   :height: 3.69722in


