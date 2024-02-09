.. _cv28 landing:

InnoPhase IoT’s hosted solution on CV28 System-on-Chip Host platform
includes the following features:

1.  PMK Caching
2.  Shadow Service:

    a. This feature enables the Dual-Stack solution to stay connected to
       the cloud/server when Host is powered OFF. Dual-Stack supports
       two types of shadow/Keep-alive services:

    b. TCP Keep-alive and wake word configuration:

       i.  Talaria TWO transmits Keep-alive messages to the server in
           configured time intervals when Host is powered ON and OFF.

       ii. Talaria TWO wakes up the powered OFF Host via configured GPIO
           when the configured wake word is received from the
           cloud/server.

    c. MQTT Keep-alive:

       i. Talaria TWO transmits MQTT Keep-alive frames to the cloud in
          configured time intervals when Host is powered ON and OFF.

    d. Talaria TWO wakes up the powered OFF Host via configured GPIO
       when any wake-up event triggers on the firmware (For example: AP
       Link Loss event)

3.  SPI driver support

4.  Integrated BlueZ stack

5.  Video streaming

6.  Port-range configuration for Host and Talaria TWO

7.  Packet-forward configuration to configure multiple rules for packet
    forwarding.

8.  IP Change Indication

9.  Heartbeat indication to detects firmware crash/hang

10. Wi-Fi provisioning over BLE

11. Example applications to evaluate the various Dual-Stack
    functionalities

This section provides steps to setup and run the Talaria TWO Dual-Stack
Solution with FreeRTOS support using AEK001 cv28 host.

**Getting Started**
-----------------

.. toctree::
    :maxdepth: 3

    1. Getting Started/Prerequisites.rst

**Evaluation Setup and Usage**
-----------------
.. toctree::
    :maxdepth: 2

    2. Evaluation Set-up and Usage/1. Landing Page.rst


**Video Streaming AEK001 cv28 Host**
-----------------
.. toctree::
    :maxdepth: 2

    3. Video Streaming AEK001 cv28 Host/Video streaming AEK001 cv28 Host.rst

**Testing for Basic Operations**
-----------------
.. toctree::
    :maxdepth: 1

    4. Testing for Basic Operations/Testing for Basic Operations
    4. Testing for Basic Operations/Testing for Basic Operations.rst
