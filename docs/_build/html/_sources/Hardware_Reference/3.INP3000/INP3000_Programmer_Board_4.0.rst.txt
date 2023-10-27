.. _Hardware_Reference/3.INP3000/INP3000_Programmer_Board_4.0:

INP3000 Programmer Board 4.0
============================

VERSION 4.0
-----------

|Diagram Description automatically generated|

Figure 1: INP3000 programmer kit contents - version 4.0

|A picture containing text, electronics, circuit Description
automatically generated|

Figure 2: INP3000 programmer board – version 4.0

J6 SWD Connector Pin-out:

.. table:: Table 1: J6 SWD Connector Pin-out

   +--------------------------+--------+-----------+---------------------+
   | **Description**          | *      | **PIN**   | **Description**     |
   |                          | *PIN** |           |                     |
   +==========================+========+===========+=====================+
   | +3V3                     | 1      | 2         | SWDIO               |
   +--------------------------+--------+-----------+---------------------+
   | GND                      | 3      | 4         | SWCLK               |
   +--------------------------+--------+-----------+---------------------+
   | GND                      | 5      | 6         | NC                  |
   +--------------------------+--------+-----------+---------------------+
   | GPIO17_CONSOLE_RX        | 7      | 8         | NC                  |
   +--------------------------+--------+-----------+---------------------+
   | GND                      | 9      | 10        | EN_CHIP/\_RST       |
   +--------------------------+--------+-----------+---------------------+

The INP3000 version 4.0 board supports only SWD programming and does not
support JTAG programming. JTAG is supported in versions 3.0 and lower.
All the other connectors are same as version 3.0 board.

.. |Diagram Description automatically generated| image:: media/image1.jpeg
   :width: 5.11811in
   :height: 5.46412in
.. |A picture containing text, electronics, circuit Description automatically generated| image:: media/image2.jpeg
   :width: 5.11811in
   :height: 3.9166in
