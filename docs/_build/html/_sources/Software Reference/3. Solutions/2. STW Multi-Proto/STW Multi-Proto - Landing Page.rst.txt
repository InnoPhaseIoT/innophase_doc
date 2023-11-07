This section describes the procedure to evaluate the STW Multi-Proto
(SMP) application used in the hosted mode of operation. The following
section describes Talaria TWO’s different modes of operation.

This application receives/sends the commands/data from the host
application in a specific packet format and performs the required task,
which includes connecting to an AP over Wi-Fi and supporting MQTT, HTTP
operations on Talaria TWO.

SMP Application Flow
---------------------

SMP application works by receiving a request from the host application,
servicing it, and sending a response to the host. The SMP application
also sends asynchronous messages to the host. These messages are
referred to as indication messages.

For example, Talaria TWO’s wake up notifications, scan results, etc.,
are sent to the host as indication messages. To understand how the host
and SMP applications exchange data, it is required to understand the
architecture and the control flow of the host application, and the
library used. The subsequent section describes the following:

1. Host application working.

2. Types of messages used to communicate between host and Talaria TWO.

3. Library used by the host application to frame a packet and send the
   same.

Prerequisites
--------------
.. toctree::
   :maxdepth: 2

   1. Prerequisites/Prerequisites.rst

Build Environment
------------------

.. toctree:: 
   :maxdepth: 2

   2. Build Environment/Setting up the Build Environment.rst

Evaluating the Application
--------------------------
.. toctree::
   :maxdepth: 2

   3. Evaluating the Application/Evaluating the Application.rst

Host Application
------------------
.. toctree:: 
   :maxdepth: 2

   4. Host Application/Host Application.rst

STW Multi Proto Application
---------------------------------
.. toctree::
   :maxdepth: 2

   5. STW Multi-Proto Application/STW Multi-Proto Application.rst