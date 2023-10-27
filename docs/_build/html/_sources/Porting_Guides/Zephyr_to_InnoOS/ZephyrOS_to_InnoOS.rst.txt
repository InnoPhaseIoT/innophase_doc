.. _Porting_Guides/Zephyr_to_InnoOS/ZephyrOS_to_InnoOS:

This porting guide describes porting of the ZephyrOS code to InnoOS for
a few common scenarios.

ZephyrOS to InnoOS
------------------

Create Threads
~~~~~~~~~~~~~~

In InnoOS, a thread is created using the function os_create_thread(..).
The function os_create_thread, takes five input parameters:

1. Name of the thread to create

2. Entry function of the thread task

3. Argument(s) of the entry function

4. Priority of the thread

5. Stack size of the thread

Following is the prototype of the function os_create_thread:

.. table:: Table 1: Create a thread

   +-----------------------------------------------------------------------+
   | struct os_thread \*os_create_thread(const char \*name,                |
   | os_entrypoint_t entry, os_threadarg_t arg, uint32_t flags, size_t     |
   | stacksz);                                                             |
   +=======================================================================+
   +-----------------------------------------------------------------------+

Contrary to ZephyrOS, in InnoOS the entry function always returns NULL.
It is not possible to pass more than one argument to the entry function.
An alternative is to use a pointer to a struct to pass more than one
argument.

The following example provides a comparison between Zephyr and InnoOS,
on how a thread is created:

.. table:: Table 2: Message queues

   +----------------------------------+-----------------------------------+
   | **ZephyrOS**                     | **InnoOS**                        |
   +==================================+===================================+
   | static void task(void)           | static void \* task(void \*arg)   |
   |                                  |                                   |
   | {                                | {                                 |
   |                                  |                                   |
   | int cnt = 0;                     | int cnt = 0;                      |
   |                                  |                                   |
   | for (;;){                        | for (;;) {                        |
   |                                  |                                   |
   | printk(“Count %d\\n”,cnt++);     | os_printf("Count %d\\n", cnt++);  |
   |                                  |                                   |
   | k_sleep(K_SECONDS(1));           | os_sleep_us(SYSTIME_SEC(1),       |
   |                                  |                                   |
   | }                                | }                                 |
   |                                  |                                   |
   | }                                | return NULL; }                    |
   |                                  |                                   |
   | int main(void)                   | int main(void)                    |
   |                                  |                                   |
   | {                                | {                                 |
   |                                  |                                   |
   | K_                               | os_create_thread(                 |
   | THREAD_STACK_DEFINE(stack,1024); |                                   |
   |                                  | "task",                           |
   | static struct k_thread           |                                   |
   | my_thread;                       | task,                             |
   |                                  |                                   |
   | k_thread_create(                 | NULL,                             |
   |                                  |                                   |
   | &my_thread,                      | 1,                                |
   |                                  |                                   |
   | stack,                           | 1024);                            |
   |                                  |                                   |
   | K_THREAD_STACK_SIZEOF(stack),    | return 0;                         |
   |                                  |                                   |
   | (k_thread_entry_t) task,         | }                                 |
   |                                  |                                   |
   | NULL,                            |                                   |
   |                                  |                                   |
   | NULL,                            |                                   |
   |                                  |                                   |
   | NULL,                            |                                   |
   |                                  |                                   |
   | 1,                               |                                   |
   |                                  |                                   |
   | 0,                               |                                   |
   |                                  |                                   |
   | K_NO_WAIT) ;                     |                                   |
   |                                  |                                   |
   | return 0;                        |                                   |
   |                                  |                                   |
   | }                                |                                   |
   +----------------------------------+-----------------------------------+

Message Queues 
~~~~~~~~~~~~~~~

In ZephyrOS, the message queue must be initiated separately. To do so,
it is required to allocate a message buffer that is aligned. In addition
to this, in ZephyrOS, the receiver is required to specify the message
queue from which it wants to get the message from.

There is also an option to peek a message from the queue, without
removing it from the queue.

In InnoOS, every thread gets a message queue when a thread is created
(i.e., after calling os_create_thread()). Hence, the message queues are
not created separately.

In InnoOS, message queues have no maximum number of items, and each
message on the queue can be of different sizes. InnoOS uses the message
type (field) to differentiate between messages. The sender specifies to
which thread the message should be sent. The receiver does not specify
the queue, as it receives it from its own thread queue. The receiver has
no reception timeout, but there is a flag which tells if the call should
wait or return immediately if there is no message in the reception queue
for the moment.

Additionally, in InnoOS, it is also possible to use an os_recvmsg_type
to wait for a specific message type.

.. table:: Table 3: Soft timers

   +----------------------------------+-----------------------------------+
   | **ZephyrOS**                     | **InnoOS**                        |
   +==================================+===================================+
   | struct k_msgq msgq;              | #define MSG_TYPE 100              |
   |                                  |                                   |
   | K_THREAD_STACK_DEFINE(stack1,    | struct os_thread \*thread_rx;     |
   | 1024);                           |                                   |
   |                                  | struct os_thread \*thread_tx;     |
   | K_THREAD_STACK_DEFINE(stack2,    |                                   |
   | 1024);                           | struct my_msg {                   |
   |                                  |                                   |
   | static void tx()                 | struct os_msg msg;                |
   |                                  |                                   |
   | {                                | int data;                         |
   |                                  |                                   |
   | int item = 0xaddababe;           | };                                |
   |                                  |                                   |
   | for(;;) {                        | static void \* tx(void \*arg)     |
   |                                  |                                   |
   | if (k_msgq_put(&msgq, &item,     | {                                 |
   |                                  |                                   |
   | K_SECONDS(0.5))==0)              | for (;;) {                        |
   |                                  |                                   |
   | printk("Send ok\\n");            | struct my_msg \*msg = (struct     |
   |                                  | my_msg\*)                         |
   | else                             |                                   |
   |                                  | os_msg_alloc(MSG_TYPE, sizeof     |
   | printk("Send failed\\n");        | \*msg);                           |
   |                                  |                                   |
   | k_sleep(K_SECONDS(1));           | msg->data = 0xaddababe;           |
   |                                  |                                   |
   | }                                | os_sendmsg(thread_rx, &msg->msg); |
   |                                  |                                   |
   | }                                | os_sleep_us(SYSTIME_SEC(1),       |
   |                                  |                                   |
   | static void rx()                 | OS_TIMEOUT_WAKEUP);               |
   |                                  |                                   |
   | {                                | }                                 |
   |                                  |                                   |
   | int item;                        | return NULL;                      |
   |                                  |                                   |
   | for(;;) {                        | }                                 |
   |                                  |                                   |
   | if (k_msgq_get(&msgq, &item,     | static void \* rx(void \*arg)     |
   |                                  |                                   |
   | K_SECONDS(0.5))==0)              | {                                 |
   |                                  |                                   |
   | printk("Received %x\\n",item);   | for (;;) {                        |
   |                                  |                                   |
   | else                             | struct my_msg \*rec = (struct     |
   |                                  | my_msg\*)os_recvmsg(false);       |
   | printk("Reception failed\\n");   |                                   |
   |                                  | os_printf("Received %x from       |
   | k_sleep(K_SECONDS(1));           | %s\\n", rec->data,                |
   |                                  |                                   |
   | }                                | os_t                              |
   |                                  | hread_name(rec->msg.msg_sender)); |
   | }                                |                                   |
   |                                  | os_msg_release((struct os_msg     |
   | int main()                       | \*)rec);                          |
   |                                  |                                   |
   | {                                | }                                 |
   |                                  |                                   |
   | char \__aligned(4)               | return NULL;                      |
   | msg_buffer[5*sizeof(void\*)];    |                                   |
   |                                  | }                                 |
   | k_msgq_init(&msgq, msg_buffer,   |                                   |
   | sizeof(void\*), 5);              | int main(void)                    |
   |                                  |                                   |
   | static struct k_thread           | {                                 |
   | thread_rx;                       |                                   |
   |                                  | thread_tx =                       |
   | static struct k_thread           | os_create_thread("tx", tx, NULL,  |
   | thread_tx;                       | 1, 1024);                         |
   |                                  |                                   |
   | k_thread_create(&thread_tx,      | thread_rx =                       |
   | stack1,                          | os_create_thread("rx", rx, NULL,  |
   |                                  | 1, 1024);                         |
   | K_THREAD_STACK_SIZEOF(stack1),   |                                   |
   |                                  | return 0;                         |
   | (k_thread_entry_t) tx, NULL,     |                                   |
   | NULL, NULL,                      | }                                 |
   |                                  |                                   |
   | 1, 0, K_NO_WAIT) ;               |                                   |
   |                                  |                                   |
   | k_thread_create(&thread_rx,      |                                   |
   | stack2,                          |                                   |
   |                                  |                                   |
   | K_THREAD_STACK_SIZEOF(stack2),   |                                   |
   |                                  |                                   |
   | (k_thread_entry_t) rx, NULL,     |                                   |
   | NULL, NULL,                      |                                   |
   |                                  |                                   |
   | 1, 0, K_NO_WAIT) ;               |                                   |
   |                                  |                                   |
   | return 0;                        |                                   |
   |                                  |                                   |
   | }                                |                                   |
   +----------------------------------+-----------------------------------+

Soft Timers 
~~~~~~~~~~~~

Table 3 depicts an example where the timer is run multiple times.
ZephyrOS does not have a callback which counts the number of times the
timer has elapsed in total. It only has a status function which checks
the number of times it has elapsed since the status was last read and
then resets it to zero. Because of this, there is a need to have a
global count which will keep track of the number of times the timer has
elapsed in total.

In InnoOS, the timers are called callouts, and the APIs are prefixed
with callout\_. The preferred coding style is to use a struct including
the timer (callout) and the parameters needed.

For example: cnt in this example.

In the callback function, the pointer to the struct is returned via the
container_of macro. This will lead to a lot of different coding
opportunities with InnoOS.

In InnoOS, there is an additional function called
callout_scedule_at(struct callout \*co, uint32_t time)which offers the
possibility to schedule the callout to start after a few microseconds.

.. table:: Table 4: Semaphores

   +----------------------------------+-----------------------------------+
   | **ZephyrOS**                     | **InnoOS**                        |
   +==================================+===================================+
   | uint32_t cnt=0;                  | #include <kernel/os.h>            |
   |                                  |                                   |
   | struct k_timer timer;            | #include <kernel/callout.h>       |
   |                                  |                                   |
   | static void                      | struct my_state {                 |
   |                                  |                                   |
   | timer_callback()                 | struct callout timer;             |
   |                                  |                                   |
   | {                                | uint32_t cnt;                     |
   |                                  |                                   |
   | cnt+=k_timer_status_get(&timer); | } state;                          |
   |                                  |                                   |
   | printk("cnt: %u\\n", cnt);       | static void \__irq                |
   |                                  |                                   |
   | if (cnt<10)                      | timer_callback(struct callout     |
   |                                  | \*co)                             |
   | /\* timer is auto-reloaded \*/   |                                   |
   |                                  | {                                 |
   | k_timer_start(&timer,            |                                   |
   | K_SECONDS(1),                    | struct my_state \*state =         |
   |                                  | container_of(co, struct my_state, |
   | K_NO_WAIT);                      | timer);                           |
   |                                  |                                   |
   | else {                           | state->cnt++;                     |
   |                                  |                                   |
   | k_timer_stop(&timer);            | os_printf("cnt: %u\\n",           |
   |                                  | state->cnt);                      |
   | printk("Ready!\\n");             |                                   |
   |                                  | if (state->cnt < 10)              |
   | }                                |                                   |
   |                                  | /\* Reschedule the timer \*/      |
   | }                                |                                   |
   |                                  | callout_schedule(&state->timer,   |
   | int                              | SYSTIME_SEC(1));                  |
   |                                  |                                   |
   | main(void)                       | else                              |
   |                                  |                                   |
   | {                                | os_printf("Ready\\n");            |
   |                                  |                                   |
   | k_timer_init(&timer,             | }                                 |
   | timer_callback, NULL);           |                                   |
   |                                  | int                               |
   | k_timer_start(&timer,            |                                   |
   | K_SECONDS(1),                    | main(void)                        |
   |                                  |                                   |
   | K_NO_WAIT);                      | {                                 |
   |                                  |                                   |
   | return 0;                        | callout_init(&state.timer,        |
   |                                  | timer_callback);                  |
   | }                                |                                   |
   |                                  | callout_schedule(&state.timer,    |
   |                                  | SYSTIME_SEC(1));                  |
   |                                  |                                   |
   |                                  | return 0;                         |
   |                                  |                                   |
   |                                  | }                                 |
   +----------------------------------+-----------------------------------+

Semaphores 
~~~~~~~~~~~

The differences between ZephyrOS and InnoOS are minor when it comes to
semaphores. Table 4 depicts the different functions.

.. table:: Table 5: Work queue

   +----------------------------------+-----------------------------------+
   | **ZephyrOS**                     | **InnoOS**                        |
   +==================================+===================================+
   | struct k_sem semaphore;          | struct os_semaphore semaphore;    |
   |                                  |                                   |
   | k_sem_init(&semaphore, 1,        | os_sem_init(&semaphore, 1);       |
   | MAX_VALUE);                      | os_sem_wait_timeout(&semaphore,   |
   |                                  | timeout);                         |
   | k_sem_take(&semaphore, timeout); |                                   |
   |                                  | os_sem_post(&semaphore);          |
   | k_sem_give(&semaphore);          |                                   |
   +----------------------------------+-----------------------------------+

InnoOS has the API os_sem_wait(&semaphore), which is without a timeout
and blocks until the semaphore is taken. The same behavior can be
achieved in ZephyrOS using k_sem_take, if the timeout argument is set to
K_MAX_FOREVER.

Work Queue
~~~~~~~~~~

ZephyrOS and InnoOS work queues are similar. They can write to the
systems work queue and create new work queues. Following is an example
of both writing to the systems work queue:

+----------------------------------+-----------------------------------+
| **ZephyrOS**                     | **InnoOS**                        |
+==================================+===================================+
| struct my_state{                 | struct my_state {                 |
|                                  |                                   |
| struct k_work mining;            | struct os_work mining;            |
|                                  |                                   |
| };                               | };                                |
|                                  |                                   |
| static void                      | static void                       |
|                                  |                                   |
| working_in_a_coalmine(struct     | working_in_a_coalmine(struct      |
| k_work \*work)                   | os_work \*work)                   |
|                                  |                                   |
| {                                | {                                 |
|                                  |                                   |
| struct my_state \*state =        | struct my_state \*state =         |
| CONTAINER_OF(work,               | container_of(work, struct         |
|                                  | my_state,                         |
| struct my_state, mining);        |                                   |
|                                  | mining);                          |
| // do some work...               |                                   |
|                                  | // do some work...                |
| }                                |                                   |
|                                  | }                                 |
| static void                      |                                   |
|                                  | static void                       |
| interrupt_service_receive(struct |                                   |
| my_state \*state)                | interrupt_service_receive(struct  |
|                                  | my_state \*state)                 |
| {                                |                                   |
|                                  | {                                 |
| k_work_submit(&state->mining);   |                                   |
|                                  | os_q                              |
| }                                | ueue_system_work(&state->mining); |
|                                  |                                   |
| static void                      | }                                 |
|                                  |                                   |
| init_mining(struct my_state      | static void                       |
| \*state)                         |                                   |
|                                  | init_mining(struct my_state       |
| {                                | \*state)                          |
|                                  |                                   |
| //Associate the work function    | {                                 |
| with the struct k_work object    |                                   |
|                                  | //Associate the work function     |
| k_work_init(&state->mining,      | with the struct os_work object    |
| working_in_a_coalmine);          |                                   |
|                                  | os_init_work(&state->mining,      |
| }                                | working_in_a_coalmine);           |
|                                  |                                   |
|                                  | }                                 |
+----------------------------------+-----------------------------------+
