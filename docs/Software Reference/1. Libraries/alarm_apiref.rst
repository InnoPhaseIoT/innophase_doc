Alarm Api ref
--------------

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
~~~~~~~~~~~~~~~~~~~~~~~~~

Store the alarm date and time from user API.

.. table:: Table : alarm_tm - Data structure definitions

   +-----------+----------------------------------------------------------+
   | **        | Year                                                     |
   | tm_year** |                                                          |
   +===========+==========================================================+
   | *         | Month of the year (1-12)                                 |
   | *tm_mon** |                                                          |
   +-----------+----------------------------------------------------------+
   | *         | Day of the month (0-31)                                  |
   | *tm_day** |                                                          |
   +-----------+----------------------------------------------------------+
   | **        | Hour of the day (0-23)                                   |
   | tm_hour** |                                                          |
   +-----------+----------------------------------------------------------+
   | *         | Minute of the hour (0-59)                                |
   | *tm_min** |                                                          |
   +-----------+----------------------------------------------------------+
   | *         | Seconds of minute(0-59)                                  |
   | *tm_sec** |                                                          |
   +-----------+----------------------------------------------------------+

alarm_info
~~~~~~~~~~~~~~~~~~~~~~~~~
Store alarm information. .

.. table:: Table : alarm_info - Data structure definitions

   +----------+-----------------------------------------------------------+
   | *        | Alarm time in seconds                                     |
   | *alarm_t |                                                           |
   | imesec** |                                                           |
   +==========+===========================================================+
   | **alar   | Alarm type                                                |
   | m_type** |                                                           |
   |          | 0-> Daily alarms                                          |
   |          |                                                           |
   |          | 1-> Weekly alarms                                         |
   +----------+-----------------------------------------------------------+
   | **al     | Alarm ID generated after setting the alarm                |
   | arm_id** |                                                           |
   +----------+-----------------------------------------------------------+
   | **alarm_ | Repeat the alarm                                          |
   | repeat** |                                                           |
   |          | 0-> Once                                                  |
   |          |                                                           |
   |          | 1-> Repeat                                                |
   +----------+-----------------------------------------------------------+
   | **alar   | Alarm name                                                |
   | m_name** |                                                           |
   +----------+-----------------------------------------------------------+

API Reference
~~~~~~~~~~~~~~~~~~~~~~~~~

alarm_init
~~~~~~~~~~~~~~~~~~~~~~~~~

Overview
~~~~~~~~

This API initializes the alarm.

Definition
~~~~~~~~~~

.. table:: Table : alarm_set - parameter descriptions

   +-----------------------------------------------------------------------+
   | void (\* alarm_callback)(uint32_t, void \*)                           |
   +=======================================================================+
   +-----------------------------------------------------------------------+

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

.. table:: Table : alarm_set_time - parameter descriptions

   +-----------------------------------------------------------------------+
   | int32_t                                                               |
   |                                                                       |
   | alarm_set(struct alarm_tm \*alarm_ts, uint8_t alarm_type, uint8_t     |
   | periodic, uint32_t cb_func, uint8_t\* arg)                            |
   +=======================================================================+
   +-----------------------------------------------------------------------+

.. _parameters-1:

Parameters
~~~~~~~~~~

.. table:: Table : alarm_delete - parameter description

   +------------+---------------------------------------------------------+
   | **P        | **Description**                                         |
   | arameter** |                                                         |
   +============+=========================================================+
   | *alarm_ts* | Pointer to alarm_tm structure. Contains date and time   |
   +------------+---------------------------------------------------------+
   | *a         | Alarm type                                              |
   | larm_type* |                                                         |
   +------------+---------------------------------------------------------+
   | *periodic* | Whether the alarm has to be repeated or not             |
   +------------+---------------------------------------------------------+
   | *cb_func*  | Alarm callback function. The definition for this        |
   |            | function is as follows:                                 |
   |            |                                                         |
   |            | .. table:: Table : alarm_display - parameter            |
   |            | description                                             |
   |            |                                                         |
   |            |                                                         |
   |            |  +----------------------------------------------------+ |
   |            |                                                         |
   |            |  | void (\* alarm_callback)(uint32_t alarm_id,        | |
   |            |                                                         |
   |            |  | uint8_t \*alarm_name)                              | |
   |            |                                                         |
   |            |  +====================================================+ |
   |            |                                                         |
   |            |  +----------------------------------------------------+ |
   |            |                                                         |
   |            | where,                                                  |
   |            |                                                         |
   |            | alarm_id – current alarm ID                             |
   |            |                                                         |
   |            | alarm_name – current alarm name                         |
   +------------+---------------------------------------------------------+
   | *arg*      | Call back argument. Used to store alarm name            |
   +------------+---------------------------------------------------------+

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

+-----------------------------------------------------------------------+
| void                                                                  |
|                                                                       |
| alarm_set_time(uint64_t time_toset)                                   |
+=======================================================================+
+-----------------------------------------------------------------------+

.. _parameters-2:

Parameters
~~~~~~~~~~

+---------+------------------------------------------------------------+
| **Para  | **Description**                                            |
| meter** |                                                            |
+=========+============================================================+
| *time_  | Time to be set in seconds.                                 |
| tosett* |                                                            |
+---------+------------------------------------------------------------+

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

+-----------------------------------------------------------------------+
| int8_t                                                                |
|                                                                       |
| alarm_delete(uint32_t alarm_id)                                       |
+=======================================================================+
+-----------------------------------------------------------------------+

.. _parameters-3:

Parameters
~~~~~~~~~~

+---------+------------------------------------------------------------+
| **Param | **Description**                                            |
| eters** |                                                            |
+=========+============================================================+
| *al     | Alarm ID. This is obtained after setting the alarm.        |
| arm_id* |                                                            |
+---------+------------------------------------------------------------+

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

+-----------------------------------------------------------------------+
| void alarm_display(uint32_t cb)                                       |
+=======================================================================+
+-----------------------------------------------------------------------+

.. _parameters-4:

Parameters
~~~~~~~~~~

+---------+------------------------------------------------------------+
| **Para  | **Description**                                            |
| meter** |                                                            |
+=========+============================================================+
| *cb*    | Call back to trigger alarm display. The definition for     |
|         | this callback is as follows:                               |
|         |                                                            |
|         | +-------------------------------------------------------+  |
|         | | typedef void (\* alarm_dsiplay_callback)(struct       |  |
|         | | alarm_infio \*ainfo)                                  |  |
|         | +=======================================================+  |
|         | +-------------------------------------------------------+  |
|         |                                                            |
|         | where,                                                     |
|         |                                                            |
|         | ainfo – pointer to alarm to alarm_info structure, which    |
|         | contains the information for the current alarm.            |
+---------+------------------------------------------------------------+

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

+-----------------------------------------------------------------------+
| struct alarm_info \* alarm_info_get(uint32_t alarm_id)                |
+=======================================================================+
+-----------------------------------------------------------------------+

.. _parameters-5:

Parameters
~~~~~~~~~~

+-----------+----------------------------------------------------------+
| **Pa      | **Description**                                          |
| rameter** |                                                          |
+===========+==========================================================+
| *         | Alarm ID                                                 |
| alarm_id* |                                                          |
+-----------+----------------------------------------------------------+

.. _return-5:

Return
~~~~~~

Success: Return valid pointer to alarm_info structure.

Error: NULL.

Example Application
~~~~~~~~~~~~~~~~~~~~~~~~~

For the example codes, refer: apps\\alarm\\alarm_test.c application.
