Testing the Basic Operation on setup with SPI interface
=======================================================

Use Case 1: Talaria2 Low Power WiFi Demo Application
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Open STM32CubeIDE and select Open Projects from the file system from
file.

1. Open the Talaria2_LP_WiFi project from EVK package available at
   location:

*I-CUBE-T2-U5-Alpha-lib/Application/Talaria2_LP_WiFi with the
STM32CubeIDE.*

|A screenshot of a computer Description automatically generated|

Figure 6: Loading Talaria2_LP_WiFi project

2. Click and open app_freertos.c by navigating to Core->Src.

3. Configure network details (SSID and Passphrase) and save the file.

4. Select Project and choose Build Project in the dropdown menu.

5. Click on debug to load the application on to the STM32 board.

|image1|

Figure 7: Modifying SSID and PASSPHRASE

6. Once the loading of the application is complete, open Tera term (or
   any preferred serial terminal) and configure the serial port.

|image2|

Figure 8: Configuring serial port

|image3|

Figure 9: Tera Term Setup

7. Reset STM32 and check the console logs on Tera term. STM32 will boot
   and the Wi-Fi connection will be established. It starts the TCP
   server and waits for a connection on port 9000.

|A computer screen shot of a black screen Description automatically
generated|

Figure 9: Expected Output

.. |A screenshot of a computer Description automatically generated| image:: media/image1.png
   :width: 7.08661in
   :height: 3.86811in
.. |image1| image:: media/image2.png
   :width: 6.69291in
   :height: 6.73501in
.. |image2| image:: media/image3.png
   :width: 5.90551in
   :height: 2.88078in
.. |image3| image:: media/image4.png
   :width: 5.90551in
   :height: 3.19614in
.. |A computer screen shot of a black screen Description automatically generated| image:: media/image5.png
   :width: 7.08661in
   :height: 4.10433in
