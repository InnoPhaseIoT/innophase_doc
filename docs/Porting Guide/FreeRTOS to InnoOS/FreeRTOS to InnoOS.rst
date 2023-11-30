

Work Queue
``````````

Work queues are used to schedule functions to run in a specific thread context. Most commonly used to defer work from an interrupt handler that needs to run quickly to another function that may do the more heavy processing involved in serving the interrupt.
But FreeRTOS doesn’t have built support for Work Queue. However, this can be easily implemented using a thread and a message queue.

Wait Queue
``````````

Wait queue is used for a task/thread to wait for an event.
But FreeRTOS doesn’t have built-in support for wait queue. However, this can be easily implemented using semaphores and message queue.
