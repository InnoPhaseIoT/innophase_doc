.. _alarm apiref:

Alarm
```````

**Alarm API Reference**

Alarm provides the mechanism to schedule activities for the future which
are either repeating or are executed in one shot. This section provides
information about the alarm APIs and data structures that can be used by
user in applications.

Features and Limitations
~~~~~~~~~~~~~~~~~~~~~~~~~

Following are the salient features of the alarm implementation:
1. Supports weekly and daily alarms
2. Supports periodic and one short alarms.
3. Provides functions to set system time.
4. Alarm can be deleted.
5. Automatically synchronize the alarm after changing system time.

Following are the limitations:

1. A maximum 6 alarms are supported.

Header file/s
~~~~~~~~~~~~~~~~~~~~~~~~~

*Components/alarm/inc/alarm.h*.

Data Structure Definitions
~~~~~~~~~~~~~~~~~~~~~~~~~

alarm_tm
~~~~~~~~~

Store the alarm date and time from user API.

.. table:: Table 1: alarm_tm - Data structure definitions

   +--------------------+----------------------------------------------------------+
   | **tm_year**        | Year                                                     |
   +====================+==========================================================+
   | **tm_mon**         | Month of the year (1-12)                                 |
   +--------------------+----------------------------------------------------------+
   | **tm_day**         | Day of the month (0-31)                                  |
   +--------------------+----------------------------------------------------------+
   | **tm_hour**        | Hour of the day (0-23)                                   |
   +--------------------+----------------------------------------------------------+
   | **tm_min**         | Minute of the hour (0-59)                                |
   +--------------------+----------------------------------------------------------+
   | **tm_sec**         | Seconds of minute(0-59)                                  |
   +--------------------+----------------------------------------------------------+

alarm_info
~~~~~~~~~~
Store alarm information. .

.. table:: Table 2: alarm_info - Data structure definitions

   +--------------------------+-----------------------------------------------------------+
   | **alarm_timesec**        | Alarm time in seconds                                     |
   +==========================+===========================================================+
   | **alarm_type**           | Alarm type                                                |
   |                          | 0-> Daily alarms                                          |
   |                          | 1-> Weekly alarms                                         |
   +--------------------------+-----------------------------------------------------------+
   | **alarm_id**             | Alarm ID generated after setting the alarm                |
   +--------------------------+-----------------------------------------------------------+
   | **alarm_repeat**         | Repeat the alarm                                          |
   |                          | 0-> Once                                                  |
   |                          | 1-> Repeat                                                |
   +--------------------------+-----------------------------------------------------------+
   | **alarm_name**           | Alarm name                                                |
   +--------------------------+-----------------------------------------------------------+

API Reference
~~~~~~~~~~~~~~~~~~~~~~~~~

alarm_init
~~~~~~~~~~~~~~~~~~~~~~~~~

Overview
~~~~~~~~

This API initializes the alarm.

Definition
~~~~~~~~~~

.. code:: shell

    void (* alarm_callback)(uint32_t, void *)

Parameters
~~~~~~~~~~

None.

Return
~~~~~~

Success: 0

Error: 1 (already initialized).

alarm_set
~~~~~~~~~~~~~~~~~~~~~~~~~

.. _overview-1:

Overview
~~~~~~~~~

This function is used to set the alarm with given configuration.

.. _definition-1:

Definition
~~~~~~~~~~

.. code:: shell

    int32_t
    alarm_set(struct alarm_tm \*alarm_ts, uint8_t alarm_type, uint8_t periodic, uint32_t cb_func, uint8_t\* arg)

.. _parameters-1:

Parameters
~~~~~~~~~~

.. table:: Table 3: alarm_delete - parameter description

   +----------------------+-----------------------------------------------------------------------+
   | **Parameter**        | **Description**                                                       |
   +======================+=======================================================================+
   | *alarm_ts*           | Pointer to alarm_tm structure. Contains date and time                 |
   +----------------------+-----------------------------------------------------------------------+
   | *alarm_type*         | Alarm type                                                            |
   +----------------------+-----------------------------------------------------------------------+
   | *periodic*           | Whether the alarm has to be repeated or not                           |
   +----------------------+-----------------------------------------------------------------------+
   | *cb_func*            | Alarm callback function. The definition for this function is a follow |
   |                      |                                                                       |
   |                      | .. code:: shell                                                          |
   |                      |                                                                       |
   |                      |     void (\* alarm_callback)(uint32_t alarm_id,uint8_t \*alarm_name)  |
   |                      |                                                                       |
   |                      | where,                                                                |
   |                      |     - alarm_id – current alarm ID                                     |
   |                      |     - alarm_name – current alarm name                                 |
   +----------------------+-----------------------------------------------------------------------+
   | *arg*                | Call back argument. Used to store alarm name                          |
   +----------------------+-----------------------------------------------------------------------+

.. _return-1:

Return
~~~~~~~

Success: 0

Error:

   -1 -> Alarm not initialized.

   -2 -> Alarm memory allocation failed

   -3 -> Invalid alarm type

   -4 -> Invalid time

   -5 -> Max alarms present

alarm_set_time
~~~~~~~~~~~~~~~~~~~~~~~~~

.. _overview-2:

Overview
~~~~~~~~~

Set system time.

.. _definition-2:

Definition
~~~~~~~~~~~

.. code:: shell

    void
    alarm_set_time(uint64_t time_toset)


.. _parameters-2:

Parameters
~~~~~~~~~~

.. table:: Table 4: alarm_set time - parameter description

    +----------------+------------------------------------------------------------+
    | **Parameter**  | **Description**                                            |
    +================+============================================================+
    | *time_tosett*  | Time to be set in seconds.                                 |
    +----------------+------------------------------------------------------------+

.. _return-2:

Return
~~~~~~

None.

alarm_delete
~~~~~~~~~~~~~~~~~~~~~~~~~

.. _overview-3:

Overview
~~~~~~~~

Delete the alarm.

.. _definition-3:

Definition
~~~~~~~~~~~

.. code:: shell

    int8_t
    alarm_delete(uint32_t alarm_id)


.. _parameters-3:

Parameters
~~~~~~~~~~
.. table:: Table 5: alarm_delete - parameter description

    +----------------+-----------------------------------------------------+
    | **Parameters** | **Description**                                     |
    +================+=====================================================+
    | *alarm_id*     | Alarm ID. This is obtained after setting the alarm. |
    +----------------+-----------------------------------------------------+

.. _return-3:

Return
~~~~~~

Success: 0

Error: 1

alarm_display
~~~~~~~~~~~~~~~~~~~~~~~~~

.. _overview-4:

Overview
~~~~~~~~

Display all alarms. User defined call back will be triggered for each
alarm with the alarm information.

.. _definition-4:

Definition
~~~~~~~~~~~

.. code:: shell

    void alarm_display(uint32_t cb)

.. _parameters-4:

Parameters
~~~~~~~~~~

.. table:: Table 3: alarm_display - parameter description

    +----------------+-------------------------------------------------------------------------+
    | **Parameter**  | **Description**                                                         |
    +================+=========================================================================+
    | *cb*           | Call back to trigger alarm display. The definition for this callback is |
    |                | as follows:                                                             |
    |                |                                                                         |
    |                | .. code:: shell                                                             |
    |                |                                                                         |
    |                |     typedef void (\* alarm_dsiplay_callback)(structalarm_infio \*ainfo) |
    |                |                                                                         |
    |                | where,                                                                  |
    |                |     - ainfo – pointer to alarm to alarm_info structure, which           |
    |                |     - contains the information for the current alarm.                   |
    +----------------+-------------------------------------------------------------------------+

.. _return-4:

Return
~~~~~~

None.

alarm_info_get
~~~~~~~~~~~~~~~~~~~~~~~~~

.. _overview-5:

Overview
~~~~~~~~

Get information about a specific alarm.

.. _definition-5:

Definition
~~~~~~~~~~~

.. code:: shell

    struct alarm_info * alarm_info_get(uint32_t alarm_id)

.. _parameters-5:

Parameters
~~~~~~~~~~

+--------------------+---------------------+
| **Parameter**      | **Description**     |
+====================+=====================+
| *alarm_id*         | Alarm ID            |
+--------------------+---------------------+

.. _return-5:

Return
~~~~~~

Success: Return valid pointer to alarm_info structure.

Error: NULL.

Example Application
~~~~~~~~~~~~~~~~~~~~~~~~~

For the example codes, refer: apps\\alarm\\alarm_test.c application.
