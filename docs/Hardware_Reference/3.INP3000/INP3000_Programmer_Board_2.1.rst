.. _Hardware_Reference/3.INP3000/INP3000_Programmer_Board_2.1:

INP3000 Programmer Board 2.1
===========================

VERSION 2.1
-----------

|A picture containing text, electronics Description automatically
generated|

Figure 6: INP3000 programmer board – version 2.1

Table 8 provides the description of each jumper:

.. table:: Table 8: INP3000 jumpers with description

   +-------------------+--------------------------------------------------+
   | **Jumper**        | **Description**                                  |
   +===================+==================================================+
   | J1                | Enable 3.3V supply                               |
   +-------------------+--------------------------------------------------+
   | J2                | Select between 2.5V and 3.3V                     |
   +-------------------+--------------------------------------------------+
   | J3                | GPIO headers                                     |
   +-------------------+--------------------------------------------------+
   | J6                | JTAG header                                      |
   +-------------------+--------------------------------------------------+
   | J7                | UART/SPI programming interface selector          |
   +-------------------+--------------------------------------------------+
   | J8                | GPIO headers                                     |
   +-------------------+--------------------------------------------------+
   | J10               | Enable 3.3V on programming header                |
   +-------------------+--------------------------------------------------+
   | J11               | Programming header                               |
   +-------------------+--------------------------------------------------+

When programming a Talaria TWO module on an INP1014, they can be
connected using a 20-pin ribbon cable as shown in Figure 7.

|A close-up of a circuit board Description automatically generated with
low confidence|

Figure 7: INP3000 programmer board with Talaria TWO module

Connecting via UART interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|Graphical user interface, text, application, chat or text message
Description automatically generated|

   Figure 8: UART connection diagram

Figure 8 is the connection diagram showing the connection of INP3000
programmer board to a Talaria TWO module via UART. Table 9 provides the
description of each connection:

.. table:: Table 9: UART Connection & Description

   +------------------------+---------------------------------------------+
   | **Connection**         | **Description**                             |
   +========================+=============================================+
   | GPIO01                 | UART TX                                     |
   +------------------------+---------------------------------------------+
   | GPIO02                 | UART RX                                     |
   +------------------------+---------------------------------------------+
   | EN_CHIP                | Used for resetting the Talaria TWO module   |
   +------------------------+---------------------------------------------+
   | GPIO17                 | Talaria TWO console debug output (default   |
   |                        | baud is 2457600)                            |
   +------------------------+---------------------------------------------+

To use UART, ensure that the J7 jumpers are configured as shown in
Figure 9.

|A picture containing text, electronics, circuit Description
automatically generated|

Figure 9: INP3000 programmer board version 2.1 - UART jumper setting

Once connected as shown in Figure 8 and Figure 9, Talaria TWO module can
be programmed via the factory loader script or the Talaria TWO download
tool.

For more information on the factory loader, refer:
UG_Factory_Loader.pdf.

Connecting via SPI interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|image1|

Figure 10: SPI connection diagram

Figure 10 is the connection diagram showing the connection of INP3000
programmer board to a Talaria TWO module via SPI. Table 10 provides the
description for each connection:

.. table:: Table 10: SPI Connection & Description

   +--------------------+-------------------------------------------------+
   | **Connection**     | **Description**                                 |
   +====================+=================================================+
   | GPIO01             | MOSI                                            |
   +--------------------+-------------------------------------------------+
   | GPIO02             | MISO                                            |
   +--------------------+-------------------------------------------------+
   | GPIO00             | SCLK                                            |
   +--------------------+-------------------------------------------------+
   | GPIO05             | CS                                              |
   +--------------------+-------------------------------------------------+
   | EN_CHIP            | Used for resetting Talaria TWO module           |
   +--------------------+-------------------------------------------------+
   | GPIO17             | Talaria TWO console debug output (default baud  |
   |                    | is 2457600)                                     |
   +--------------------+-------------------------------------------------+

To use SPI, ensure that the J7 jumpers are as shown in Figure 11.

|A model of a building Description automatically generated with low
confidence|

Figure 11: INP3000 programmer board version 2.1 - SPI jumper setting

.. |A picture containing text, electronics Description automatically generated| image:: media/image1.png
   :width: 5.11811in
   :height: 4.06154in
.. |A close-up of a circuit board Description automatically generated with low confidence| image:: media/image2.png
   :width: 4.72441in
   :height: 3.14077in
.. |Graphical user interface, text, application, chat or text message Description automatically generated| image:: media/image3.png
   :width: 3.34375in
   :height: 2.30208in
.. |A picture containing text, electronics, circuit Description automatically generated| image:: media/image4.jpeg
   :width: 4.72441in
   :height: 3.44826in
.. |image1| image:: media/image5.png
   :width: 3.34375in
   :height: 3.03125in
.. |A model of a building Description automatically generated with low confidence| image:: media/image6.jpeg
   :width: 4.72441in
   :height: 2.92874in
