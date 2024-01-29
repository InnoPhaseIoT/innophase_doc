.. _ex watchdog timer:

Watchlog Timer
------------------------

This application note describes managing the Talaria TWO watchdog timer
using the functions provided by the watchdog driver.

Watchdog Timer 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The sample application provides functions for managing the Talaria TWO
watchdog timer.

**wdreset.c**

The callout_init()function initiates the callout object. wakeup callout
is used to schedule a wakeup from suspend state.
xSemaphoreCreateCounting(1, 0) initiates the semaphore with a default
value of 0. watchdog_init initializes the watchdog with the specified
timeout in microseconds and the watchdog expire_cb is passed as NULL,
resulting in a system reset at timer expiration. The watchdog_start()
function starts the watchdog counter.

.. code:: shell

      callout_init(&wakeup, wakeup_callback);
      wakeup_event = xSemaphoreCreateCounting(1, 0);
      watchdog_init(WATCHDOG_TIMEOUT, NULL);
      watchdog_start();


callout_init_soft()initializes callout object with a soft deadline.
kicker callout is used to kick the watchdog to reload the counter to its
initial value to avoid the counter value reaching zero. A soft callout
timeout accepts the timeout to be invoked later than requested if this
could lead to savings in power consumption. The
callout_schedule()schedules the callback function to be invoked after
the specified number of microseconds. Application needs to kick the
watchdog before it expires, hence the timeout is given as
WATCHDOG_TIMEOUT \* 9 / 10.

.. code:: shell

      callout_init_soft(&kicker, kick_the_dog);
      callout_schedule(&kicker, WATCHDOG_TIMEOUT * 9 / 10);



Talaria TWO is put to suspend mode to demonstrate that the watchdog
works fine both in suspend mode and awake mode. After enabling the
suspend mode, wakeup callout is scheduled after two seconds. Then the
thread suspends on a wakeup_event semaphore. Since there is no other
activity scheduled at this point, the system enters suspend mode.

.. code:: shell

      os_suspend_enable();
      callout_schedule(&wakeup, SYSTIME_SEC(2));
      os_printf("Sleeping\n");
      if (xSemaphoreTake(wakeup_event, portMAX_DELAY) == pdFAIL) {
          os_printf("Unable to wait on semaphore...!!\n");
          return -1;
      }
      os_printf("Awake\n");
      os_suspend_disable();
      vTaskDelay(4000);


This callback function of wakeup callout wakes the system up from
suspend state and posts the semaphore for which the main thread was
waiting before going to suspend mode.

**Note**: wakeup_callback is executed from ISR context, hence the
SemaphoreGiveFromISR() is used.

.. code:: shell

      static void
      wakeup_callback(struct callout *c)
      {     xSemaphoreGiveFromISR(wakeup_event, NULL); }


This callback function of kicker callout kicks the watchdog.

.. code:: shell

      static void
      kick_the_dog(struct callout *c)
      {
          static uint32_t num_kicks;
          os_printf("Kick\n");
          watchdog_kick();
          if (++num_kicks < 30)
              callout_schedule(c, WATCHDOG_TIMEOUT * 9 / 10);
          else
          os_printf("Last kick\n");
      }


Here, kick_the_dog()function calls watchdog_kick()before the watchdog
timer expires.

Every time watchdog_kick() is called, it resets the watchdog timer which
is set using watchdog_init(). After the 30th call of watchdog_kick(),
this callback is not scheduled and thus the watchdog timer expires,
resulting in system reset.

System reset occurs because the watchdog_init() was called with
expire_cb passed as NULL.

.. code:: shell

       watchdog_init(WATCHDOG_TIMEOUT, NULL);   


Running the Application 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Program wdreset.elf (*freertos_sdk_x.y\\examples\\watchdog_timer\\bin*)
using the Download tool:

1. Launch the Download tool provided with InnoPhase Talaria TWO SDK.

2. In the GUI window:

   a. Boot Target: Select the appropriate EVK from the drop-down.

   b. ELF Input: Load the wdreset.elf by clicking on Select ELF File.

   c. Programming: Prog RAM or Prog Flash as per requirement.

**Note**: Post 30\ :sup:`th` call of the watchdog_kick()function, the
watchdog timer expires

a. Prog RAM: After reset, wdreset.elf halts

b. Prog Flash: After reset, wdreset.elf runs in a loop

Expected Output
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: shell

      Build $Id: git-df9b9ef $
      Flash detected. flash.hw.uuid: 39483937-3207-0051-002a-ffffffffffff
      $App:git-6818774
      SDK Ver: FREERTOS_SDK_1.0
      Watchdog Reset Demo App
      Starting watchdog
      Sleeping
      Kick
      Kick
      Awake
      Kick
      Kick
      Kick
      Kick
      Sleeping
      Kick
      Awake
      Kick
      Kick
      Kick
      Kick
      Sleeping
      Kick
      Awake
      Kick
      Kick
      Kick
      Kick
      Sleeping
      Kick
      Awake
      Kick
      Kick
      Kick
      Kick
      Sleeping
      Kick
      Awake
      Kick
      Kick
      Kick
      Kick
      Sleeping
      Kick
      Awake
      Kick
      Kick
      Kick
      Last kick
