Create AWS Security Credentials 
--------------------------------

Execute the following steps to create the AWS security credentials
required to enable video streaming:

1. Login to the AWS kinesis portal:
   https://us-east-1.console.aws.amazon.com/kinesisvideo/home?region=us-east-1#/dashboard

|image1|\ |image2|

Figure 17: Login to AWS kinesis portal

2. Create a user group.

|A screenshot of a computer Description automatically generated|

Figure 18: Create user group

3. Click on Create user.

|image3|

Figure 19: Create user

4. Provide the new user name and click on Next.

|image4|

Figure 20: Enter user name

5. Add the user to the user group created in step 2 and click Next.
   Ensure to provide access to the video streaming resources in the
   policy. For example:

+-----------------------------------------------------------------------+
| {                                                                     |
|                                                                       |
| "Version": "2012-10-17",                                              |
|                                                                       |
| "Statement": [                                                        |
|                                                                       |
| {                                                                     |
|                                                                       |
| "Effect": "Allow",                                                    |
|                                                                       |
| "Action": "\*",                                                       |
|                                                                       |
| "Resource": "\*"                                                      |
|                                                                       |
| }                                                                     |
|                                                                       |
| ]                                                                     |
|                                                                       |
| }                                                                     |
+=======================================================================+
+-----------------------------------------------------------------------+

|image5|

Figure 21: Extend permissions

6. Select the user created previously and click on Create access key.

|image6|

Figure 22: Create access key for the user

7. Select the option Application running on an AWS compute service,
   check the confirmation box and click Next.

|image7|

Figure 23: Application running on AWS compute service

8. Click on Create access key.

|image8|

Figure 24: Create access key

9. Copy the generated access key, secret access key and click Done.

|image9|\ |image10| |image11|

Figure 25: Access and secret access key

10. Click on the Kinesis Video Streams (search for Kinesis Video Streams
    in the search bar).

|image12|

Figure 26: Kinesis video streams

11. Click on Create signaling channel.

|image13|

Figure 27: Create signaling channel

12. Provide a name to the new signaling channel and click on Create
    signaling channel.

|image14|

Figure 28: Enter signaling channel name

13. A new signaling channel will be created. Copy the Signaling channel
    ARN.

|image15|

Figure 29: Signaling channel ARN

14. Upon successfully initiating video streaming from the Host, video
    streaming will be available under Media player viewer.

.. |image1| image:: media/image1.png
   :width: 3.41736in
   :height: 0.12569in
.. |image2| image:: media/image2.png
   :width: 6.69306in
   :height: 3.82708in
.. |A screenshot of a computer Description automatically generated| image:: media/image3.png
   :width: 6.69375in
   :height: 3.1in
.. |image3| image:: media/image4.png
   :width: 6.69375in
   :height: 1.66667in
.. |image4| image:: media/image5.png
   :width: 6.69375in
   :height: 2.08681in
.. |image5| image:: media/image6.png
   :width: 7.00764in
   :height: 3.46944in
.. |image6| image:: media/image7.png
   :width: 7.00764in
   :height: 3.32222in
.. |image7| image:: media/image8.png
   :width: 7.00764in
   :height: 3.34375in
.. |image8| image:: media/image9.png
   :width: 7.00764in
   :height: 1.33958in
.. |image9| image:: media/image10.png
   :width: 0.90551in
.. |image10| image:: media/image11.png
   :width: 0.43307in
.. |image11| image:: media/image12.png
   :width: 7.00764in
   :height: 2.5125in
.. |image12| image:: media/image13.png
   :width: 7.00764in
   :height: 5.63958in
.. |image13| image:: media/image14.png
   :width: 7.00764in
   :height: 3.61667in
.. |image14| image:: media/image15.png
   :width: 7.00764in
   :height: 3.61181in
.. |image15| image:: media/image16.png
   :width: 7.00764in
   :height: 3.62639in
