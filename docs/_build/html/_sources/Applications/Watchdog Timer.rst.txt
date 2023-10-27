Introduction 
=============

This application note describes managing the Talaria TWO watchdog timer
using the functions provided by the watchdog driver.

Watchdog Timer 
===============

The watchdog driver provides functions for managing the Talaria TWO
watchdog timer.

It is a down-counting timer that generates a system reset (or an
interrupt) when the counter reaches zero. The timer is started with an
application specific timeout via the watchdog_init() and
watchdog_start() functions. The client application uses the
watchdog_kick() function to periodically reload the counter to its
initial value to avoid it counting to zero.

Depending on what the application wants to supervise using this
watchdog, the watchdog_kick() may be performed from contexts. If the
goal is to make sure that a certain real-time response time is required
on a particular thread priority level, a dedicated thread on this
priority level should kick the watchdog. Failure to meet the real-time
response will then lead to a system reset. Another use case is to
supervise on interrupt level. In this case, the watchdog should be
kicked from an interrupt service handler on a timer interrupt that is
scheduled at an interval slightly lower than the watchdog timeout.

Sample Code Walkthrough
=======================

The sample application watchdog driver provides functions for managing
the Talaria TWO watchdog timer.

**wdreset.c**

The callout_init()function initiates the callout object. os_sem_init
initiates the semaphore with a default value of 0. Watchdog_init
initializes the watchdog with the specified timeout in microseconds and
the watchdog timer NULL called for system reset. The watchdog_start()
function will start the watchdog counter.

+-----------------------------------------------------------------------+
| callout_init(&wakeup, wakeup_callback);                               |
|                                                                       |
| os_sem_init(&wakeup_event, 0);                                        |
|                                                                       |
| watchdog_init(WATCHDOG_TIMEOUT, NULL);                                |
|                                                                       |
| watchdog_start();                                                     |
+=======================================================================+
+-----------------------------------------------------------------------+

callout_init_soft()initializes callout object with a soft deadline. A
soft callout timeout accepts the timeout to be invoked later than
requested if this could lead to savings in power consumption. The
callout_schedule()schedules the callback function to be invoked after
the specified number of microseconds. Application needs to kick the
watchdog before it expires, hence the timeout is given as
WATCHDOG_TIMEOUT \* 9 / 10.

+-----------------------------------------------------------------------+
| callout_init_soft(&kicker, kick_the_dog);                             |
|                                                                       |
| callout_schedule(&kicker, WATCHDOG_TIMEOUT \* 9 / 10);                |
+=======================================================================+
+-----------------------------------------------------------------------+

Talaria TWO is put to suspend mode to demonstrate that the watchdog
works fine both in suspend mode and awake mode.

+-----------------------------------------------------------------------+
| os_suspend_enable();                                                  |
|                                                                       |
| callout_schedule(&wakeup, SYSTIME_SEC(2));                            |
|                                                                       |
| os_printf("Sleeping\\n");                                             |
|                                                                       |
| os_sem_wait(&wakeup_event);                                           |
|                                                                       |
| os_printf("Awake\\n");                                                |
|                                                                       |
| os_suspend_disable();                                                 |
|                                                                       |
| os_usleep(SYSTIME_SEC(4));                                            |
+=======================================================================+
+-----------------------------------------------------------------------+

This call back function is to wake up when the semaphore returns.

+-----------------------------------------------------------------------+
| static void                                                           |
|                                                                       |
| wakeup_callback(struct callout \*c)                                   |
|                                                                       |
| {                                                                     |
|                                                                       |
| os_sem_post(&wakeup_event);                                           |
|                                                                       |
| }                                                                     |
+=======================================================================+
+-----------------------------------------------------------------------+

This callback function is to trigger the watchdog.

+-----------------------------------------------------------------------+
| static void                                                           |
|                                                                       |
| kick_the_dog(struct callout \*c)                                      |
|                                                                       |
| {                                                                     |
|                                                                       |
| static uint32_t num_kicks;                                            |
|                                                                       |
| os_printf("Kick\\n");                                                 |
|                                                                       |
| watchdog_kick();                                                      |
|                                                                       |
| if (++num_kicks < 30)                                                 |
|                                                                       |
| callout_schedule(c, WATCHDOG_TIMEOUT \* 9 / 10);                      |
|                                                                       |
| else                                                                  |
|                                                                       |
| os_printf("Last kick\\n");                                            |
|                                                                       |
| }                                                                     |
+=======================================================================+
+-----------------------------------------------------------------------+

Here, kick_the_dog()function calls watchdog_kick()before the watchdog
timer expires. Every time watchdog_kick() is called, it resets the
watchdog timer which is set using watchdog_init(). After the 30th call
of watchdog_kick(), it is no longer seen and thus the watchdog timer
expires.

+-----------------------------------------------------------------------+
| watchdog_init(WATCHDOG_TIMEOUT, NULL);                                |
+=======================================================================+
+-----------------------------------------------------------------------+

Running the Application 
------------------------

Program wdreset.elf(sdk_x.y\\examples\\watchdog_timer\\bin) using the
Download tool:

1. Launch the Download tool provided with InnoPhase Talaria TWO SDK.

2. In the GUI window:

   a. Boot Target: Select the appropriate EVK from the drop-down.

   b. ELF Input: Load the wdreset.elf by clicking on Select ELF File.

   c. Programming: Prog RAM or Prog Flash as per requirement.

For more details on using the Download tool, refer to the document:
UG_Download_Tool.pdf (path: *sdk_x.y/pc_tools/Download_Tool/doc*).

**Note**:

1. x and y refer to the SDK release version. For example: sdk_2.4/doc.

2. Post 30\ :sup:`th` call of the watchdog_kick()function:

   a. Prog RAM: watchdog timer expires

   b. Prog Flash: watchdog timer runs in an infinite loop

For details on using the Download tool, refer to the document:
UG_Download_Tool.pdf.

Expected Output
---------------

+-----------------------------------------------------------------------+
| UART:NWWWWAE                                                          |
|                                                                       |
| 4 DWT comparators, range 0x8000                                       |
|                                                                       |
| Build $Id: git-7e2fd6a94 $                                            |
|                                                                       |
| hio.baudrate=115200                                                   |
|                                                                       |
| flash: Gordon ready!                                                  |
|                                                                       |
| UART:NWWWAEBuild $Id: git-65f6c1f46 $                                 |
|                                                                       |
| $App:git-e3ccdc7a                                                     |
|                                                                       |
| SDK Ver: sdk_2.4                                                      |
|                                                                       |
| Watchdog Reset Demo App                                               |
|                                                                       |
| Starting watchdog                                                     |
|                                                                       |
| Sleeping                                                              |
|                                                                       |
| Kick                                                                  |
|                                                                       |
| Kick                                                                  |
|                                                                       |
| Awake                                                                 |
|                                                                       |
| Kick                                                                  |
|                                                                       |
| Kick                                                                  |
|                                                                       |
| Kick                                                                  |
|                                                                       |
| Kick                                                                  |
|                                                                       |
| Sleeping                                                              |
|                                                                       |
| Kick                                                                  |
|                                                                       |
| Awake                                                                 |
|                                                                       |
| Kick                                                                  |
|                                                                       |
| Kick                                                                  |
|                                                                       |
| Kick                                                                  |
|                                                                       |
| Kick                                                                  |
|                                                                       |
| Sleeping                                                              |
|                                                                       |
| Kick                                                                  |
|                                                                       |
| Awake                                                                 |
|                                                                       |
| Kick                                                                  |
|                                                                       |
| Kick                                                                  |
|                                                                       |
| Kick                                                                  |
|                                                                       |
| Kick                                                                  |
|                                                                       |
| Sleeping                                                              |
|                                                                       |
| Kick                                                                  |
|                                                                       |
| Awake                                                                 |
|                                                                       |
| Kick                                                                  |
|                                                                       |
| Kick                                                                  |
|                                                                       |
| Kick                                                                  |
|                                                                       |
| Kick                                                                  |
|                                                                       |
| Sleeping                                                              |
|                                                                       |
| Kick                                                                  |
|                                                                       |
| Awake                                                                 |
|                                                                       |
| Kick                                                                  |
|                                                                       |
| Kick                                                                  |
|                                                                       |
| Kick                                                                  |
|                                                                       |
| Kick                                                                  |
|                                                                       |
| Sleeping                                                              |
|                                                                       |
| Kick                                                                  |
|                                                                       |
| Awake                                                                 |
|                                                                       |
| Kick                                                                  |
|                                                                       |
| Kick                                                                  |
|                                                                       |
| Kick                                                                  |
|                                                                       |
| Last kick                                                             |
+=======================================================================+
+-----------------------------------------------------------------------+
