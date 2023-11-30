.. _porting guide:

Porting Guide
=============

InnoOS to FreeRTOS
``````````````

This porting guide describes the procedure to port FreeRTOS code to InnoOS for multiple generic scenarios.

**Create tasks (threads)**

**Note**: Argument order differs between os_create_thread() and xTaskCreate().

.. table:: Table 1: Creating tasks - FreeRTOS and InnoOS

    +---------------------------------------------+---------------------------------------------+
    | **FreeRTOS**                                | **InnoOS**                                  |
    +=============================================+=============================================+
    |  BaseType_t                                 | struct os_thread *os_create_thread (const   |
    |  xTaskCreate(TaskFunction_t pvTaskCode,     | char *name, os_entrypoint_t entry,          |
    |  const char * const pcName,                 | os_threadarg_t arg, uint32_t flags,         |
    |  configSTACK_DEPTH_TYPE usStackDepth, void  | size_t stacksz);                            |
    |  *pvParameters, UBaseType_t uxPriority,     |                                             |
    |   TaskHandle_t *pxCreatedTask);             |                                             |
    +---------------------------------------------+---------------------------------------------+
    | .. code:: shell                             | .. code:: shell                             |
    |                                             |                                             |
    | static void task(void *arg)                 | static void * task(void *arg)               |
    | {                                           | {                                           |
    |   int cnt = 0;                              |   int cnt = 0;                              |
    |   for(;;) {                                 |   for (;;) {                                |
    |     printf("Count %d\\n", cnt++);           |     os_printf("Count %d\\n", cnt++);        |
    |     vTaskDelay(1000, portTICK_PERIOD_MS);   |     os_sleep_us(SYSTIME_SEC(1),             |
    |  }                                          |     OS_TIMEOUT_WAKEUP);                     |
    | }                                           |  }                                          |
    | int main(void)                              |   return NULL;                              |
    | {                                           | }                                           |
    |  xTaskCreate(task,"task",1024,NULL,1,NULL); | int main(void)                              |
    |  return 0;                                  | {                                           |
    |  }                                          |   os_create_thread("task",task,NULL,1,1024);|
    |                                             |   return 0;                                 |
    |                                             | }                                           |
    +---------------------------------------------+---------------------------------------------+

Note: The stack size is represented as number of words (4 byte) in FreeRTOS and number of bytes in InnOS.

**Message Queues**


In InnoOS, every thread gets a message queue at os_create_thread(). Hence, the message queues are not created separately. The message queues have no maximum number of items, and the items can be of different sizes.
Message type is used to differentiate between messages. The sender specifies to which thread the message should be sent. The receiver does not specify the queue, as it receives from its own thread queue. The receiver has no reception timeout, but there is a flag which decides if the call should wait or return immediately if there is no message in the reception queue for the moment.
It is also possible to use os_recvmsg_type to wait for a specific message type.
Following is an example with a Tx task sending messages to an Rx task:


**InnoOS**

.. code:: shell

   #define MSG_TYPE 100
   struct os_thread *thread_rx;
   struct os_thread *thread_tx;
   struct my_msg {
      struct os_msg msg;
      int data;
   };
   static void * tx(void *arg)
   {
      for (;;) {
         struct my_msg *msg = (struct my_msg *)os_msg_alloc(MSG_TYPE, sizeof *msg);
         msg->data = 0xaddababe;
         os_sendmsg(thread_rx, &msg->msg);
         os_sleep_us(SYSTIME_SEC(1), OS_TIMEOUT_WAKEUP);
      }
      return NULL;
   }
   static void * rx(void *arg)
   {
      for (;;) {
         struct my_msg *rec = (struct my_msg *)os_recvmsg(false);
         os_printf("Received %x from %s\\n", rec->data,
         os_thread_name(rec->msg.msg_sender));
         os_msg_release((struct os_msg *)rec);
      }
      return NULL;
   }
   int main(void)
   {
      thread_tx = os_create_thread("tx", tx, NULL, 1, 1024);
      thread_rx = os_create_thread("rx", rx, NULL, 1, 1024);
      return 0;
   }


In FreeRTOS, the message queue is created separately and has a maximum
size and an element size. xQueueSend and xQueueReceive specify the
message queue, with specific timeouts on the duration for block in case
of failure.

**FreeRTOS**

.. code:: shell

   #define Q_SIZE 5 /* number of items in queue */
   #define I_SIZE sizeof(int) /* size of each item */
   #define Q_TX_TO 500 /* timeout for send if queue is full */
   #define Q_RX_TO 500 /* timeout for reception if queue is empty */
   xQueueHandle msg_queue;
   static void tx(void *arg)
   {
       int item = 0xaddababe;
       for(;;) {
           if (xQueueSend(msg_queue, &item, Q_TX_TO))
               printf("Send ok\n");
           else
               printf("Send failed\n");
           vTaskDelay(1000, portTICK_PERIOD_MS);
       }
   }

   static void rx(void *arg)
   {
       int item;
       for(;;) {
           if (xQueueReceive(msg_queue, &item, Q_RX_TO))
               printf("Received %x\n", item);
           else
               printf("Reception failed\n");
       }
   }

   int main(void)
   {
       msg_queue = xQueueCreate(Q_SIZE, I_SIZE);
       xTaskCreate(rx, "Rx", 1024, NULL, 1, NULL);
       xTaskCreate(tx, "Tx", 1024, NULL, 1, NULL);
       vTaskStartScheduler();
       return 0;
   }


**Soft Timers**

In InnoOS, the timers are called callouts, and the APIs are prefixed
with callout\_.

The preferred coding style is to use a struct including the timer
(callout) and the parameters needed. For example: cnt. In the callback
function, the pointer to the struct is captured via the container_of
macro.

**InnoOS**

.. code-block:: c

    #include <kernel/os.h>
    #include <kernel/callout.h>

    struct my_state {
        struct callout timer;
        uint32_t cnt;
    } state;

    static void __irq timer_callback(struct callout *co)
    {
        struct my_state *state = container_of(co, struct my_state, timer);
        state->cnt++;
        os_printf("cnt: %u\n", state->cnt);
        if (state->cnt < 10)
        {
            /* Reschedule the timer */
            callout_schedule(&state->timer, SYSTIME_SEC(1));
        }
        else
        {
            os_printf("Ready\n");
        }
    }

    int main(void)
    {
        callout_init(&state.timer, timer_callback);
        callout_schedule(&state.timer, SYSTIME_SEC(1));

        return 0;
    }

In FreeRTOS, there is a built-in counter that determines the number of
times the counter has elapsed. There is also an auto-reload option where
the timer is automatically restarted. In this example we use it to
illustrate a difference between FreeRTOS and InnoOS.

For both FreeRTOS and InnoOS, the timer callback function will execute
in the timer service context, and no blocking calls must be used.
Preferably the work is handed over to another task/thread.

**FreeRTOS**

.. code-block:: c

    #include <stdio.h>
    #include "FreeRTOS.h"
    #include "timers.h"
    static void timer_callback(TimerHandle_t timer)
    {
        uint32_t cnt = (uint32_t)pvTimerGetTimerID(timer);
        cnt++;
        printf("cnt: %u\n", cnt);
        if (cnt < 10)
        {
            /* timer is auto-reloaded */
            vTimerSetTimerID(timer, (void*)cnt);
        }
        else
        {
            xTimerStop(timer, 0);
            printf("Ready\n");
        }
    }

    int main(void)
    {
        TimerHandle_t timer;
        timer = xTimerCreate("timer", 1000/portTICK_PERIOD_MS, pdTRUE, (void*)0, timer_callback);
        xTimerStart(timer, 0);
    }


**Semaphores**

The differences between FreeRTOS and InnoOS when it comes to semaphores
are very small. lists the functions required.


+-----------------------------------+----------------------------------+
| **FreeRTOS**                      | **InnoOS**                       |
+===================================+==================================+
| xSemaphoreHandle semaphore;       | struct os_semaphore semaphore;   |
+-----------------------------------+----------------------------------+
| semaphore =                       | os_sem_init(&semaphore, 1);      |
| xSemaphoreCreateMutex();          |                                  |
+-----------------------------------+----------------------------------+
| xSemaphoreTake(semaphore,         | os_sem_wait_timeout(&semaphore,  |
| timeout);                         | timeout);                        |
+-----------------------------------+----------------------------------+
| xSemaphoreGive(semaphore);        | os_sem_post(&semaphore);         |
+-----------------------------------+----------------------------------+

InnoOS has the API os_sem_wait (&semaphore), which is without timeout, and which blocks until the semaphore is taken. This is the same behavior as is achieved in FreeRTOS if:

    - INCLUDE_vTaskSuspend is set to '1'
    - Setting the timeout in xSemaphoreTake to portMAX_DELAY.

xSemaphoreTake() as well as os_sem_wait() and os_sem_wait_timeout() must not be used in interrupt context.


**Work Queue**

Work queues are used to schedule functions to run in a specific thread context. Most commonly used to defer work from an interrupt handler that needs to run quickly to another function that may do the more heavy processing involved in serving the interrupt.
But FreeRTOS doesn’t have built support for Work Queue. However, this can be easily implemented using a thread and a message queue.

**Wait Queue**

Wait queue is used for a task/thread to wait for an event.
But FreeRTOS doesn’t have built-in support for wait queue. However, this can be easily implemented using semaphores and message queue.
