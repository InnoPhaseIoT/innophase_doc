Introduction
============

This application note provides a brief about the Timer and Callout
functionalities available in the SDK, the benefit of Callouts as
compared to Timers, and their corresponding APIs.

Example codes are accompanied with this application note, for showcasing
various Timer and Callout-related APIs available in the Talaria TWO SDK,
explaining how to create, start, handle, and stop timers and callouts.

Timers in Talaria TWO
=====================

Talaria TWO device has four 64-bit hardware timer counters.

+-----------------------------------------------------------------------+
| enum timer_base {                                                     |
|                                                                       |
| TIMER_BASE_US, /\**< System clock (1 MHz) \*/                         |
|                                                                       |
| TIMER_BASE_BT, /\**< Bluetooth clock (1.6384 MHz) \*/                 |
|                                                                       |
| TIMER_BASE_APP, /\**< Application use \*/                             |
|                                                                       |
| TIMER_BASE_HFC /\**< Hardware clock (80 MHz) \*/                      |
|                                                                       |
| };                                                                    |
+=======================================================================+
+-----------------------------------------------------------------------+

Time counter TIMER_BASE_US is dedicated as a system timer and is
configured to count at a frequency of 1MHz. The counter TIMER_BASE_BT is
set up to count at a frequency suitable for the Bluetooth protocol stack
(using 1.6384 MHz).

The third counter TIMER_BASE_APP is available for application use with a
configurable counter frequency. The fourth counter TIMER_BASE_HFC is
fixed at the core frequency; 80MHz.

In addition to the four counters, there are 16 timer match units. Each
of these units can be set up to generate an interrupt when one specific
counter reaches a certain value. The match-unit values are only 32-bit
wide, so it is only the lower 32-bits of each counter that are
considered when generating the match.

The kernel provides API functions for allocating any of these match
units for application use. The caller can choose which available counter
and time unit to use for the allocated timer.

The calling code can specify a pointer to a callback function, to be
invoked when the match-unit signals an interrupt. The callback will be
invoked in the hardware interrupt context. No blocking calls may be
performed in this callback.

Then this timer can be started, stopped, can be made capable to wake up
the device from suspend, the lower 32 bits or full 64 bits value of the
hardware linked to the timer can be read, can be set, reset, or released
through various Timer APIs available. Few APIs are demonstrated in the
example code.

But instead of using this low-level Timer interface, it is recommended
to use the callout interface which is explained in the next section.

Callouts in Talaria TWO
=======================

Callouts are objects representing a callback function to be invoked at
some point in the future when a specified timeout expires.

Callouts are a better-managed way to use OS Timers as they internally
work in a less power-consuming manner and have features, such as they
can be differed to be invoked in a way that we can minimize the number
of wakeups from suspend state of the system. The expiration time of a
particular callout at init (or expiration time of all the pending
callouts at once), can be moved to the closest non-soft timer, later
than requested, and this could lead to savings in power consumption.

Invocation to the callback function can be scheduled either after a
specified number of microseconds elapsed or at an absolute time.

The initialization function used for callout decides it is a soft or
hard deadline callout.

The callbacks will be invoked in an interrupt context. All the Callouts
interrupt the device from the suspended system state.

Various operations are possible for managing the callouts, for example,
querying the status of the callout if it’s scheduled or not, stopping
the callout timer and removing it from the list of pending callouts, and
so on.

Few of these callout APIs are demonstrated in the example code.

Timer and Callout APIs
======================

Timer APIs
----------

os_timer_allocate() 
~~~~~~~~~~~~~~~~~~~~

Used to allocate one of the sixteen hardware match-units.

+-----------------------------------------------------------------------+
| os_timer_id_t                                                         |
|                                                                       |
| os_timer_allocate(enum timer_base base, unsigned idx,                 |
| timer_callback_t callback, void \*userdata)                           |
+=======================================================================+
+-----------------------------------------------------------------------+

Following parameters are passed as arguments to this API:

1. The hardware counter to use from the four available counters in enum
   timer_base as listed earlier in the document

2. The timer ID to allocate (or TIMER_ANY for any free timer available)

3. The Function to be called when a timer match occurs

4. The userdata passed to this callback

API returns an ID representing the timer, or TIMER_INVALID if one of the
arguments is incorrect or if there is no free timer.

os_timer_set()
~~~~~~~~~~~~~~

Sets the timer match value in absolute time ticks. The timer will match
when the counter reaches the value specified.

+-----------------------------------------------------------------------+
| void os_timer_set(os_timer_id_t timer, uint32_t ticks)                |
+=======================================================================+
+-----------------------------------------------------------------------+

os_timer_reset() 
~~~~~~~~~~~~~~~~~

Clears the timer match and prevents the timer from generating an
interrupt.

+-----------------------------------------------------------------------+
| void os_timer_reset(os_timer_id_t timer)                              |
+=======================================================================+
+-----------------------------------------------------------------------+

os_timer_read () 
~~~~~~~~~~~~~~~~~

Reads the lower 32-bit value of the hardware counter linked to the
timer.

+-----------------------------------------------------------------------+
| uint32_t os_timer_read(os_timer_id_t timer)                           |
+=======================================================================+
+-----------------------------------------------------------------------+

os_timer\_ read64() 
~~~~~~~~~~~~~~~~~~~~

Reads the full 64-bit value of the hardware counter linked to the timer.

+-----------------------------------------------------------------------+
| uint32_t os_timer_read64(os_timer_id_t timer)                         |
+=======================================================================+
+-----------------------------------------------------------------------+

os_timer_release() 
~~~~~~~~~~~~~~~~~~~

Frees a previously allocated match unit.

+-----------------------------------------------------------------------+
| void os_timer_release(os_timer_id_t timer)                            |
+=======================================================================+
+-----------------------------------------------------------------------+

os_timer_wakeup_enable() 
~~~~~~~~~~~~~~~~~~~~~~~~~

Makes a specified timer capable of waking up the device from suspension
when expired.

+-----------------------------------------------------------------------+
| void os_timer_wakeup_enable(os_timer_id_t timer)                      |
+=======================================================================+
+-----------------------------------------------------------------------+

os_timer_wakeup_disable()
~~~~~~~~~~~~~~~~~~~~~~~~~

Restores the specified timer’s capability to the default state that it
will not cause the device to wake-up from suspension.

+-----------------------------------------------------------------------+
| void os_timer_wakeup_disable(os_timer_id_t timer)                     |
+=======================================================================+
+-----------------------------------------------------------------------+

Callout APIs
------------

callout_init()
~~~~~~~~~~~~~~

Takes a pointer to the callout object and a pointer to the callback
function to be invoked on this callout as input parameters and
initializes the callout object.

+-----------------------------------------------------------------------+
| static inline void callout_init(struct callout \*co, void             |
| (\*fn)(struct callout \*))                                            |
+=======================================================================+
+-----------------------------------------------------------------------+

callout_schedule()
~~~~~~~~~~~~~~~~~~

Schedules callback function to be invoked after the specified number of
microseconds.

+-----------------------------------------------------------------------+
| int callout_schedule(struct callout \*co, uint32_t time)              |
+=======================================================================+
+-----------------------------------------------------------------------+

Returns True if the callout was previously pending, false otherwise.

callout_schedule_at()
~~~~~~~~~~~~~~~~~~~~~

Schedules callback function to be invoked at a specified absolute time.

+-----------------------------------------------------------------------+
| int callout_schedule_at(struct callout \*co, uint32_t time)           |
+=======================================================================+
+-----------------------------------------------------------------------+

Returns True if the callout was previously pending, false otherwise.
Passed parameter time is matched against the lower 32-bits of the system
time.

callout_pending()
~~~~~~~~~~~~~~~~~

Checks the state of a callout object if this callout is scheduled or
not.

+-----------------------------------------------------------------------+
| static inline int callout_pending(const struct callout \*co)          |
+=======================================================================+
+-----------------------------------------------------------------------+

Returns True if the specified callout object is scheduled.

callout_init_soft()
~~~~~~~~~~~~~~~~~~~

Initializes callout object with a soft deadline.

+-----------------------------------------------------------------------+
| static inline void callout_init_soft(struct callout \*co,             |
| void(\*fn)(struct callout \*))                                        |
+=======================================================================+
+-----------------------------------------------------------------------+

A soft callout timeout accepts the timeout to be invoked later than
requested if this could lead to savings in power consumption.

A soft callout expiration will be aligned to the closest non-soft one
when entering suspend.

callout_stop()
~~~~~~~~~~~~~~

Used to stop the callout timer and remove it from the list of pending
callouts.

+-----------------------------------------------------------------------+
| int callout_stop(struct callout \*co)                                 |
+=======================================================================+
+-----------------------------------------------------------------------+

Returns True if the callout object was stopped while pending, false
otherwise.

Code Walkthrough
================

**Note**: All the applicable ELFs are available in the following
location of the SDK release package: sdk_x.y\\examples\\
innoos_timers_callouts\\bin).

x and y in sdk_x.y refer to the SDK release version. For example:
*sdk_2.4\\examples\\* *innoos_timers_callouts\\bin*.

Timer Example
-------------

Overview
~~~~~~~~

The sample code in the path:
examples/innoos_timers_callouts/timer/main.c showcases:

1. Functionality of allocating and filling timer user data

2. Setting the timer callback

3. Setting user data

4. Starting the timer for the required timeout

5. Creating a timer for demonstrating of canceling the timer

6. Clearing the timer or setting it again from the timer callback

In this sample, one-timer is created for 2 seconds, and a callback is
received after the timer elapses. A second timer is created and stopped
before it elapses.

Sample Code Walkthrough
~~~~~~~~~~~~~~~~~~~~~~~

Header file for the timer functions is kernel/timer.h

+-----------------------------------------------------------------------+
| #include <kernel/timer.h>                                             |
+=======================================================================+
+-----------------------------------------------------------------------+

Defining Timer Context Data
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Upon timer elapse, to understand the context of the timer, the user can
set a context or user data. As a first step, a data structure for the
user data must be defined (optional).

+-----------------------------------------------------------------------+
| /\*timer context data structure*/                                     |
|                                                                       |
| typedefstruct timer_user_data_t                                       |
|                                                                       |
| {                                                                     |
|                                                                       |
| unsignedint timer_created_at;                                         |
|                                                                       |
| unsignedint timeout;                                                  |
|                                                                       |
| os_timer_id_t timer_id;                                               |
|                                                                       |
| }timer_user_data;                                                     |
+=======================================================================+
+-----------------------------------------------------------------------+

Defining the Timer Callback function 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

After the timer’s timeout elapses, the timer callback function will be
invoked. Timer and user context data must be released in this callback.

+-----------------------------------------------------------------------+
| static void on_timer_event_callback(void \*user_data);                |
|                                                                       |
| /\*creating a timer*/                                                 |
|                                                                       |
| /\*allocating and filling timer user data*/                           |
|                                                                       |
| timer_user_data \*ptimer_user_data;                                   |
|                                                                       |
| ptimer_user_data = os_alloc(sizeof(timer_user_data));                 |
|                                                                       |
| ptimer_user_data->timer_created_at = os_systime();                    |
|                                                                       |
| ptimer_user_data->timeout =                                           |
| os_systime()+(TIMER_SAMPLE_TIMEOUT_2_SEC_IN_MICRO);                   |
+=======================================================================+
+-----------------------------------------------------------------------+

The Timer can be repeated from the callback. To do that, instead of
calling os_timer_release() to free up the user data, use os_timer_set()
with a new timeout.

Creating and Starting Timer
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Here, the user data is allocated and filled. Then the timer is created
using os_timer_allocate(). This will associate the timer callback and
user data for the timer. Using os_timer_set(), timer is set for the
required timeout value. The timeout value is in microseconds.

+-----------------------------------------------------------------------+
| /\*allocating and filling timer user data*/                           |
|                                                                       |
| timer_user_data \*ptimer_user_data;                                   |
|                                                                       |
| ptimer_user_data = os_alloc(sizeof(timer_user_data));                 |
|                                                                       |
| ptimer_user_data->timer_created_at = os_systime();                    |
|                                                                       |
| ptimer_user_data->timeout =                                           |
| os_systime()+(TIMER_SAMPLE_TIMEOUT_2_SEC_IN_MICRO);                   |
|                                                                       |
| /\*setting the timer callback and user data*/                         |
|                                                                       |
| ptimer_user_data->timer_id = os_timer_allocate(TIMER_BASE_US,         |
|                                                                       |
| TIMER_ANY, on_timer_event_callback, ptimer_user_data);                |
|                                                                       |
| /\*starting the timer for required timeout. timeout time is in        |
| microseconds*/                                                        |
|                                                                       |
| os_timer_set(ptimer_user_data->timer_id, ptimer_user_data->timeout);  |
+=======================================================================+
+-----------------------------------------------------------------------+

Creating another timer, checking the remaining time, and canceling the timer
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A timer is created with 5 seconds as the timeout and we intend to cancel
it before the timeout. Timer callback and timer user data are not set
since even if timer call back is set, it will not be called in case the
timer has been stopped before the timeout.

A timer’s time to timeout can be checked using os_timer_read(). Timer
can be reset by os_timer_reset(). Release the timer when the timer is no
longer required using os_timer_release(). After calling
os_timer_release(), timer is no longer valid.

os_timer_read64() can be used to get 64-bit resolution timer reading.

+-----------------------------------------------------------------------+
| /\*create a timer for demonstrating cancelling a timer*/              |
|                                                                       |
| os_timer_id_t timer_id;                                               |
|                                                                       |
| timer_id = os_timer_allocate(TIMER_BASE_US,                           |
|                                                                       |
| TIMER_ANY, NULL, NULL);                                               |
|                                                                       |
| os_timer_set(timer_id,                                                |
| os_systime()+(TIMER_SAMPLE_TIMEOUT_5_SEC_IN_MICRO));                  |
|                                                                       |
| /\* at timeout, if the device in suspend mode,                        |
|                                                                       |
| \* below function will wakeup the device*/                            |
|                                                                       |
| os_timer_wakeup_enable(timer_id);                                     |
|                                                                       |
| int nTimerReader = 3;                                                 |
|                                                                       |
| while (nTimerReader--)                                                |
|                                                                       |
| {                                                                     |
|                                                                       |
| os_printf ("\\nTimer read current ticks:%u",                          |
| os_timer_read(timer_id));                                             |
|                                                                       |
| os_msleep(1000);                                                      |
|                                                                       |
| }                                                                     |
|                                                                       |
| /\*clearing the timer.*/                                              |
|                                                                       |
| os_timer_reset(timer_id);                                             |
|                                                                       |
| os_timer_release(timer_id);                                           |
|                                                                       |
| os_printf ("\\nTimer canceled. Timer call back will not be called");  |
+=======================================================================+
+-----------------------------------------------------------------------+

Running the Application 
~~~~~~~~~~~~~~~~~~~~~~~~

Program timer.elf using the Download tool:

1. Launch the Download tool provided with InnoPhase Talaria TWO SDK.

2. In the GUI window:

   a. Boot Target: Select the appropriate EVK from the drop-down.

   b. ELF Input: Load the timer.elf by clicking on Select ELF File.

   c. Programming: Prog RAM or Prog Flash as per requirement.

For more details on using the Download tool, refer to the document:
UG_Download_Tool.pdf (path: *sdk_x.y/pc_tools/Download_Tool/doc*).

**Note**: x and y refer to the SDK release version. For example:
sdk_2.4/doc.

Expected Output
~~~~~~~~~~~~~~~

timer.elf is created when compiling the code mentioned in section 6.1.2
and gives the following console output when programmed to Talaria TWO.

+-----------------------------------------------------------------------+
| UART:NWWWWWAE4 DWT comparators, range 0x8000                          |
|                                                                       |
| Build $Id: git-7e2fd6a94 $                                            |
|                                                                       |
| app=gordon                                                            |
|                                                                       |
| flash: Gordon ready!                                                  |
|                                                                       |
| Y-BOOT 208ef13 2019-07-22 12:26:54 -0500 790da1-b-7                   |
|                                                                       |
| ROM yoda-h0-rom-16-0-gd5a8e586                                        |
|                                                                       |
| FLASH:PNWWWAEBuild $Id: git-65f6c1f46 $                               |
|                                                                       |
| $App:git-46e2bea7                                                     |
|                                                                       |
| SDK Ver: sdk_2.4                                                      |
|                                                                       |
| Innos Timer Demo App                                                  |
|                                                                       |
| b2ee0:Timer started. current time:[84929]                             |
|                                                                       |
| Timer read current ticks:34651392                                     |
|                                                                       |
| Timer read current ticks:34651392                                     |
|                                                                       |
| be768:First Timer: Timer Event occured. Current time[2084930] timer   |
| created at[84927]                                                     |
|                                                                       |
| Timer read current ticks:34651392                                     |
|                                                                       |
| Timer canceled. Timer call back will not be called                    |
+=======================================================================+
+-----------------------------------------------------------------------+

Callout Basics Example 1
------------------------

.. _overview-1:

Overview
~~~~~~~~

The sample code in the path /examples/innoos_timers_callouts/src/
callout_basics_1.c showcases:

1. Creating and forming the application context for the callout

2. Initializing the callout with a callback function

3. Scheduling the callout after the given time

4. Checking the callout status

5. Confirming that the callout has occurred using waitq

6. Scheduling a callout at a specific absolute time.

In this example, callouts are initiated and scheduled one after another.
The first one is scheduled relatively while the second one is scheduled
in an absolute way.

.. _sample-code-walkthrough-1:

Sample Code Walkthrough
~~~~~~~~~~~~~~~~~~~~~~~

Header file for the callout functions is kernel/callout.h

+-----------------------------------------------------------------------+
| #include <kernel/callout.h>                                           |
+=======================================================================+
+-----------------------------------------------------------------------+

Initializing an os_waitq and a static flag
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To programmatically confirm that the callout call-back has occurred, a
waitq is used and the program flow blocks on it after resetting a flag
gf_callout_occurred.

Later from the callback, this flag is set and waitq API
os_wakeup_all(&waitq) is called for waitq to unblock the flow.

+-----------------------------------------------------------------------+
| static struct os_waitq waitq = OS_WAITQ_INITIALIZER(waitq);           |
|                                                                       |
| static int gf_callout_occurred = 0;                                   |
+=======================================================================+
+-----------------------------------------------------------------------+

Defining the Callout Context Data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The callback is invoked with a pointer to the callout objects for the
function. This pointer can be used by the callback function to obtain
its context. This is achieved by embedding the struct callout object
within another struct, that represents the context or state on which the
callback should operate. Data structure for this is defined.

+-----------------------------------------------------------------------+
| typedef struct co_msg_info_t                                          |
|                                                                       |
| {                                                                     |
|                                                                       |
| struct callout timeout;                                               |
|                                                                       |
| /\*application specific info*/                                        |
|                                                                       |
| char callout_reason_str[64];                                          |
|                                                                       |
| int index;                                                            |
|                                                                       |
| unsigned int created_at;                                              |
|                                                                       |
| }callout_msg_info;                                                    |
+=======================================================================+
+-----------------------------------------------------------------------+

Defining the Callout Call-back Function 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

After the callout timeout elapses, the call-back function will be
invoked. The callout pointer passed to this callback is stored in member
timeout. This pointer is used by the callback function to obtain its
context.

This is achieved by using the macro container_of(ptr, type,member) which
takes three arguments:

1. A pointer

2. Type of the container

3. Name of the member the pointer refers to.

The macro will then expand to a new address pointing to the container
which accommodates the respective member.

+-----------------------------------------------------------------------+
| static void on_callout_callback_fn(struct callout \*co)               |
|                                                                       |
| {                                                                     |
|                                                                       |
| struct co_msg_info_t \*co_msg;                                        |
|                                                                       |
| co_msg = container_of(co, struct co_msg_info_t, timeout);             |
|                                                                       |
| /\*apply the business logic*/                                         |
|                                                                       |
| os_printf("\\n%x:%u:Timeout occured [%s] index[%d] created at[%u]",   |
|                                                                       |
| CALLOUT_SAMPLE_CURRENT_THREAD_ID,                                     |
|                                                                       |
| os_systime(),co_msg->callout_reason_str,                              |
|                                                                       |
| co_msg->index,                                                        |
|                                                                       |
| co_msg->created_at);                                                  |
|                                                                       |
| gf_callout_occurred = 1;                                              |
|                                                                       |
| os_wakeup_all(&waitq);                                                |
|                                                                       |
| }                                                                     |
+=======================================================================+
+-----------------------------------------------------------------------+

This way, we can access all the members of the struct created and get
the context or state on which the callback should operate. This
structure was originally initialized in
/examples/innoos_timers_callouts/timer/main.c as shown in section 6.2.2.

Creating, Initializing and Scheduling the Callout with Relative Time
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Here, the co_msg_info_t struct is allocated and filled. A callout reason
string, an index, and the time it got created are filled in as the
context. Then the callout is initialized with the function
callout_init()and a callback is associated through this API.

Before a callout object is used, it must be initialized via a call to
either callout_init() or callout_init_soft(). The flag
gf_callout_occurred is reset and callout is scheduled with
callout_schedule(). Its status is checked using callout_pending() before
and after the sleep gave equivalent to the timeout scheduled.

struct co_msg_info_t \*co_msg creates and formats the application
context for the callout.

+-----------------------------------------------------------------------+
| struct co_msg_info_t \*co_msg = NULL;                                 |
|                                                                       |
| co_msg = os_alloc(sizeof(struct co_msg_info_t));                      |
|                                                                       |
| sn                                                                    |
| printf(co_msg->callout_reason_str,sizeof(co_msg->callout_reason_str), |
|                                                                       |
| "Callout sample data. Created at[%u]", os_systime());                 |
|                                                                       |
| co_msg->index = 1;                                                    |
|                                                                       |
| co_msg->created_at = os_systime();                                    |
+=======================================================================+
+-----------------------------------------------------------------------+

callout_init()initiates the callout with a callback function.

+-----------------------------------------------------------------------+
| callout_init(&co_msg->timeout, on_callout_callback_fn);               |
+=======================================================================+
+-----------------------------------------------------------------------+

callout_schedule()schedules the callout for the given time.

+-----------------------------------------------------------------------+
| gf_callout_occurred = 0;                                              |
|                                                                       |
| callout_schedule(&co_msg->timeout,                                    |
| CALLOUT_SAMPLE_2SEC_IN_MICRO_SECONDS);                                |
|                                                                       |
| os_printf("\\n%x:%u:callout created for [%d]",                        |
|                                                                       |
| CALLOUT_SAMPLE_CURRENT_THREAD_ID,os_systime(),                        |
|                                                                       |
| CALLOUT_SAMPLE_2SEC_IN_MICRO_SECONDS);                                |
+=======================================================================+
+-----------------------------------------------------------------------+

callout_pending()checks the status of the callout.

+-----------------------------------------------------------------------+
| os_printf("\\n%x:%u:callout pending status                            |
| [%s]",CALLOUT_SAMPLE_CURRENT_THREAD_ID,                               |
|                                                                       |
| os_systime(),                                                         |
|                                                                       |
| callout_pending(&co_msg->timeout)?"Pending":"Completed");             |
+=======================================================================+
+-----------------------------------------------------------------------+

os_wait_event()function ensures the callout has occurred.

+-----------------------------------------------------------------------+
| os_wait_event(&waitq, gf_callout_occurred);                           |
+=======================================================================+
+-----------------------------------------------------------------------+

os_free()releases the context data.

+-----------------------------------------------------------------------+
| os_free(co_msg);                                                      |
|                                                                       |
| co_msg = NULL;                                                        |
|                                                                       |
| ...                                                                   |
|                                                                       |
| ...                                                                   |
|                                                                       |
| ...                                                                   |
|                                                                       |
| }                                                                     |
+=======================================================================+
+-----------------------------------------------------------------------+

By using waitq, the occurrence of the callback is doubly confirmed, and
co_msg is freed.

Creating, Initializing and Scheduling the Callout with Absolute Time
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence similar to the one mentioned in section 6.2.2.4 is followed
except callout_schedule_at()is used instead of the previously used
callout_schedule().

.. _running-the-application-1:

Running the Application 
~~~~~~~~~~~~~~~~~~~~~~~~

Program callout_basics_1.elf using the Download tool:

1. Launch the Download tool provided with InnoPhase Talaria TWO SDK.

2. In the GUI window:

   a. Boot Target: Select the appropriate EVK from the drop-down.

   b. ELF Input: Load the callout_basics_1.elf by clicking on Select ELF
      File.

   c. Programming: Prog RAM or Prog Flash as per requirement.

For more details on using the Download tool, refer to the document:
UG_Download_Tool.pdf (path: *sdk_x.y/pc_tools/Download_Tool/doc*).

**Note**: x and y refer to the SDK release version. For example:
sdk_2.4/doc.

.. _expected-output-1:

Expected Output
~~~~~~~~~~~~~~~

callout_basics_1.elf is created when compiling which provides the
following console output when programmed to Talaria TWO.

+-----------------------------------------------------------------------+
| UART:NWWWWWAE4 DWT comparators, range 0x8000                          |
|                                                                       |
| Build $Id: git-7e2fd6a94 $                                            |
|                                                                       |
| app=gordon                                                            |
|                                                                       |
| flash: Gordon ready!                                                  |
|                                                                       |
| Y-BOOT 208ef13 2019-07-22 12:26:54 -0500 790da1-b-7                   |
|                                                                       |
| ROM yoda-h0-rom-16-0-gd5a8e586                                        |
|                                                                       |
| FLASH:PNWWWAEBuild $Id: git-65f6c1f46 $                               |
|                                                                       |
| $App:git-46e2bea7                                                     |
|                                                                       |
| SDK Ver: sdk_2.4                                                      |
|                                                                       |
| Callout Basic App 1                                                   |
|                                                                       |
| b2ee0:84999:callout created for [2000000]                             |
|                                                                       |
| b2ee0:85045:callout pending status [Pending]                          |
|                                                                       |
| be768:2085000:Timeout occured [Callout sample data. Created           |
| at[84865]] index[1] created at[84995]                                 |
|                                                                       |
| b2ee0:2085100:callout pending status [Completed]                      |
|                                                                       |
| b2ee0:2085173:callout schedule at [6085173]                           |
|                                                                       |
| be768:6085175:Timeout occured [This is a scheduled timer created at   |
| [2085154]] index[999] created at[2085170]                             |
|                                                                       |
| Callout example completed                                             |
+=======================================================================+
+-----------------------------------------------------------------------+

Callout Basics Example 2
------------------------

.. _overview-2:

Overview
~~~~~~~~

The sample code in the path /examples/innoos_timers_callouts/src/
callout_basics_2.c showcases callout functionality of repeat and cancel.

.. _sample-code-walkthrough-2:

Sample Code Walkthrough
~~~~~~~~~~~~~~~~~~~~~~~

In this example, a callout is programmed to be scheduled at 1 second and
the callback rescheduled for every 1 second. A global flag is toggled in
every callout call-back.

+-----------------------------------------------------------------------+
| static void on_callout_callback_fn(struct callout \*co)               |
|                                                                       |
| {                                                                     |
|                                                                       |
| callout_sample_msg_info \*co_msg;                                     |
|                                                                       |
| co_msg = container_of(co, callout_sample_msg_info, timeout);          |
|                                                                       |
| os_printf("\\n%x:%u:callout event occured",                           |
|                                                                       |
| CALLOUT_SAMPLE_CURRENT_THREAD_ID,os_systime());                       |
|                                                                       |
| /\*toggle the value*/                                                 |
|                                                                       |
| gbToggleValue = !gbToggleValue;                                       |
|                                                                       |
| /\*repeating or resetting the callout*/                               |
|                                                                       |
| callout_schedule(&co_msg->timeout,                                    |
| CALLOUT_SAMPLE_1SEC_IN_MICRO_SECONDS);                                |
|                                                                       |
| }                                                                     |
+=======================================================================+
+-----------------------------------------------------------------------+

The main thread sleeps for 10 seconds after which the callout is
stopped. While main sleep, callouts still occur as they are called from
the other context. One thread is created which wakes up every 100
milliseconds, checks, and prints the toggle flag.

Hence, ten such prints can be passed before a toggle event occurs
through the callout which is periodic at 1 second.

This continues until another flag called terminate is toggled from main,
in which case this thread stops printing and returns. This termination
happens after 20 seconds.

+-----------------------------------------------------------------------+
| static void\* gh_application_logic_thread(void \*p)                   |
|                                                                       |
| {                                                                     |
|                                                                       |
| while (!gfTerminate)                                                  |
|                                                                       |
| {                                                                     |
|                                                                       |
| os_printf("\\n%x:%u:Current state of toggle value[%s]",               |
| CALLOUT_SAMPLE_CURRENT_THREAD_ID,os_systime(),                        |
|                                                                       |
| gbToggleValue==true?"ON":"OFF");                                      |
|                                                                       |
| os_msleep(100);                                                       |
|                                                                       |
| }                                                                     |
|                                                                       |
| os_printf("\\n%x:%u:Current state of toggle value[%s]",               |
|                                                                       |
| CALLOUT_SAMPLE_CURRENT_THREAD_ID,os_systime(),                        |
|                                                                       |
| gbToggleValue==true?"ON":"OFF");                                      |
|                                                                       |
| return NULL;                                                          |
|                                                                       |
| }                                                                     |
+=======================================================================+
+-----------------------------------------------------------------------+

Overall output in console is ten consecutive toggles ON or OFF prints
per 100 milliseconds until toggle event happens per second. These toggle
events happen ten times and then stop. The other thread keeps printing
the fixed last toggle flag value until it terminated after another 10
seconds.

.. _running-the-application-2:

Running the Application 
~~~~~~~~~~~~~~~~~~~~~~~~

Program callout_basics_2.elf using the Download tool:

1. Launch the Download tool provided with InnoPhase Talaria TWO SDK.

2. In the GUI window:

   a. Boot Target: Select the appropriate EVK from the drop-down.

   b. ELF Input: Load the call_out_basics_2.elf by clicking on Select
      ELF File.

   c. Programming: Prog RAM or Prog Flash as per requirement.

For more details on using the Download tool, refer to the document:
UG_Download_Tool.pdf (path: *sdk_x.y/pc_tools/Download_Tool/doc*).

**Note**: x and y refer to the SDK release version. For example:
sdk_2.4/doc.

.. _expected-output-2:

Expected Output
~~~~~~~~~~~~~~~

callout_basics_2.elf is created when compiling which gives a console
output as follows when programmed to Talaria TWO.

+-----------------------------------------------------------------------+
| WWWWAE4 DWT comparators, range 0x8000                                 |
|                                                                       |
| Build $Id: git-7e2fd6a94 $                                            |
|                                                                       |
| app=gordon                                                            |
|                                                                       |
| flash: Gordon ready!                                                  |
|                                                                       |
| Y-BOOT 208ef13 2019-07-22 12:26:54 -0500 790da1-b-7                   |
|                                                                       |
| ROM yoda-h0-rom-16-0-gd5a8e586                                        |
|                                                                       |
| FLASH:PNWWWAEBuild $Id: git-65f6c1f46 $                               |
|                                                                       |
| $App:git-46e2bea7                                                     |
|                                                                       |
| SDK Ver: sdk_2.4                                                      |
|                                                                       |
| Callout Basic App 2                                                   |
|                                                                       |
| b2de0:85021:callout created for [1000000]                             |
|                                                                       |
| bf780:85074:Current state of toggle value[OFF]                        |
|                                                                       |
| bf780:185130:Current state of toggle value[OFF]                       |
|                                                                       |
| bf780:285187:Current state of toggle value[OFF]                       |
|                                                                       |
| bf780:385244:Current state of toggle value[OFF]                       |
|                                                                       |
| bf780:485301:Current state of toggle value[OFF]                       |
|                                                                       |
| bf780:585358:Current state of toggle value[OFF]                       |
|                                                                       |
| bf780:685415:Current state of toggle value[OFF]                       |
|                                                                       |
| bf780:785472:Current state of toggle value[OFF]                       |
|                                                                       |
| bf780:885529:Current state of toggle value[OFF]                       |
|                                                                       |
| bf780:985586:Current state of toggle value[OFF]                       |
|                                                                       |
| bfe68:1085022:callout event occured                                   |
|                                                                       |
| bf780:1085643:Current state of toggle value[ON]                       |
|                                                                       |
| bf780:1185700:Current state of toggle value[ON]                       |
|                                                                       |
| bf780:1285757:Current state of toggle value[ON]                       |
|                                                                       |
| bf780:1385814:Current state of toggle value[ON]                       |
|                                                                       |
| bf780:1485871:Current state of toggle value[ON]                       |
|                                                                       |
| bf780:1585928:Current state of toggle value[ON]                       |
|                                                                       |
| bf780:1685985:Current state of toggle value[ON]                       |
|                                                                       |
| bf780:1786042:Current state of toggle value[ON]                       |
|                                                                       |
| bf780:1886099:Current state of toggle value[ON]                       |
|                                                                       |
| bf780:1986156:Current state of toggle value[ON]                       |
|                                                                       |
| bfe68:2085064:callout event occured                                   |
|                                                                       |
| .                                                                     |
|                                                                       |
| .                                                                     |
|                                                                       |
| .                                                                     |
|                                                                       |
| bf780:16894649:Current state of toggle value[ON]                      |
|                                                                       |
| bf780:16994706:Current state of toggle value[ON]                      |
|                                                                       |
| bf780:17094763:Current state of toggle value[ON]                      |
|                                                                       |
| bf780:17194820:Current state of toggle value[ON]                      |
|                                                                       |
| bf780:17294877:Current state of toggle value[ON]                      |
|                                                                       |
| bf780:17394934:Current state of toggle value[ON]                      |
|                                                                       |
| bf780:17494991:Current state of toggle value[ON]                      |
|                                                                       |
| bf780:17595048:Current state of toggle value[ON]                      |
|                                                                       |
| bf780:17695105:Current state of toggle value[ON]                      |
|                                                                       |
| bf780:17795162:Current state of toggle value[ON]                      |
|                                                                       |
| bf780:17895219:Current state of toggle value[ON]                      |
|                                                                       |
| bf780:17995276:Current state of toggle value[ON]                      |
|                                                                       |
| bf780:18095333:Current state of toggle value[ON]                      |
|                                                                       |
| bf780:18195390:Current state of toggle value[ON]                      |
|                                                                       |
| bf780:18295447:Current state of toggle value[ON]                      |
|                                                                       |
| bf780:18395504:Current state of toggle value[ON]                      |
|                                                                       |
| bf780:18495561:Current state of toggle value[ON]                      |
|                                                                       |
| bf780:18595618:Current state of toggle value[ON]                      |
|                                                                       |
| bf780:18695675:Current state of toggle value[ON]                      |
|                                                                       |
| bf780:18795732:Current state of toggle value[ON]                      |
|                                                                       |
| bf780:18895789:Current state of toggle value[ON]                      |
|                                                                       |
| bf780:18995846:Current state of toggle value[ON]                      |
|                                                                       |
| bf780:19095903:Current state of toggle value[ON]                      |
|                                                                       |
| bf780:19195960:Current state of toggle value[ON]                      |
|                                                                       |
| bf780:19296017:Current state of toggle value[ON]                      |
|                                                                       |
| bf780:19396074:Current state of toggle value[ON]                      |
|                                                                       |
| bf780:19496131:Current state of toggle value[ON]                      |
|                                                                       |
| bf780:19596188:Current state of toggle value[ON]                      |
|                                                                       |
| bf780:19696245:Current state of toggle value[ON]                      |
|                                                                       |
| bf780:19796302:Current state of toggle value[ON]                      |
|                                                                       |
| bf780:19896359:Current state of toggle value[ON]                      |
|                                                                       |
| bf780:19996416:Current state of toggle value[ON]                      |
|                                                                       |
| Callout example completed                                             |
|                                                                       |
| bf780:20096472:Current state of toggle value[ON]                      |
+=======================================================================+
+-----------------------------------------------------------------------+
