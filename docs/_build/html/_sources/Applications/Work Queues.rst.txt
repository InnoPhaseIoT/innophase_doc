Introduction
============

This application note describes the concept and usage of Work Queues.
Accompanying sample application provides a brief on how to use Work
Queue APIs available with the SDK.

Work Queue
==========

Work Queues are used to defer a set of work by scheduling functions
doing that work to run by a dedicated thread. For example, a set of work
can be differed from interrupt context to thread context using this
mechanism.

These deferred function calls are managed by an abstraction called work,
defined by the struct os_work, which is initialized with a work function
by calling os_init_work().

A work queue is a list of os_work objects which are initialized using
os_init_workqueue().

Once the work queue is created and initialized, a set of Work objects
can be Queued to this queue.

A dedicated thread called Worker Thread is created to service the work
queue. This thread simply calls the function os_run_work() with a
pointer to an initialized work queue as a single argument. Then the
functions in the queued set of work are called from this thread’s
context when the Worker Thread is given time to run by the scheduler.

More information on the APIs in the consecutive sections.

The system automatically creates a work queue on start-up that is used
internally for executing system type work. For example, cleaning up
after the threads have terminated. It is called a system work queue and
can be used by applications having simple work functions, not requiring
a dedicated thread context.

Alternatively, application defined threads can be used to service a work
queue. This gives more control to the application to create many threads
and manage their properties (stack size and priorities) as per the
needs.

Two examples accompanying this application note showcase the system
threads approach and application created threads approach for servicing
the work queue.

Work Queue APIs
===============

os_init_work()
--------------

Initializes a struct os_work with a work function. Pointers to both the
work functions are passed as input.

+-----------------------------------------------------------------------+
| static inline void os_init_work(struct os_work \*work, os_workfn_t    |
| func)                                                                 |
+=======================================================================+
+-----------------------------------------------------------------------+

os_init_workqueue()
-------------------

Initializes os_workqueue struct.

+-----------------------------------------------------------------------+
| void os_init_workqueue(struct os_workqueue \*wq)                      |
+=======================================================================+
+-----------------------------------------------------------------------+

os_run_work()
-------------

This function is called to service a work queue.

+-----------------------------------------------------------------------+
| void os_run_work(struct os_workqueue \*wq)                            |
+=======================================================================+
+-----------------------------------------------------------------------+

The function will not return until the work queue is flushed via a call
to os_flush_workqueue().

os_flush_workqueue()
--------------------

Called to flush a work queue.

+-----------------------------------------------------------------------+
| void os_flush_workqueue(struct os_workqueue \*wq)                     |
+=======================================================================+
+-----------------------------------------------------------------------+

Flushing a work queue stops any new work from being queued and signals
the os_run_work() function to exit when the previously queued work has
been completed.

os_queue_work()
---------------

Used to queue work on a specified work queue. Pointers to both are
passed as input.

+-----------------------------------------------------------------------+
| int os_queue_work(struct os_workqueue \*wq, struct os_work \*work)    |
+=======================================================================+
+-----------------------------------------------------------------------+

Returns true if work is added to the work queue, false if the work is
not (for example, if work is already queued or work queue is destroyed).
The work struct must have been initialized before passing it to this
function.

The work will be queued on the specified work queue and handled when the
associated worker thread is given time to run by the scheduler.

os_cancel_work()
----------------

Removes work from the specified work queue.

+-----------------------------------------------------------------------+
| int os_cancel_work(struct os_work \*work)                             |
+=======================================================================+
+-----------------------------------------------------------------------+

Work that has been queued on a work queue may be removed while it is
waiting to be carried out. This function will remove such work if it has
not yet reached the head of the service queue.

Returns true if the work was pending on the work queue, false otherwise.

os_queue_system_work()
----------------------

Queues work on the system work queue.

+-----------------------------------------------------------------------+
| int os_queue_system_work(struct os_work \*work)                       |
+=======================================================================+
+-----------------------------------------------------------------------+

The system work queue can be used by applications that have simple work
functions that do not require a dedicated thread context. The work
functions that are scheduled on the system work queue should be
relatively simple to avoid starving others out.

os_init_delayed_work()
----------------------

Initializes struct os_delayed_work with a work function.

+-----------------------------------------------------------------------+
| void os_init_delayed_work(struct os_delayed_work \*dw, os_workfn_t    |
| func)                                                                 |
+=======================================================================+
+-----------------------------------------------------------------------+

os_queue_delayed_work()
-----------------------

Queues work that is to be run at the specified absolute time passed as
parameter expire in the future on the specified work queue.

+-----------------------------------------------------------------------+
| int os_queue_delayed_work (struct os_delayed_work \*dw,               |
|                                                                       |
| struct os_workqueue \*wq, uint32_t expire)                            |
+=======================================================================+
+-----------------------------------------------------------------------+

The delayed work struct must have been initialized before passing it to
this function. The work will be queued on the specified work queue when
the system time passes the expiration value. Returns true if the delayed
work was previously pending, false otherwise.

os_cancel_delayed_work()
------------------------

Cancels a pending delayed work from expiring.

+-----------------------------------------------------------------------+
| int os_cancel_delayed_work(struct os_delayed_work \*dw)               |
+=======================================================================+
+-----------------------------------------------------------------------+

Delayed work that has been scheduled to run on a work queue may be
removed while waiting for its timer to expire. Returns true if the
delayed work was still pending to be put on the work queue, false
otherwise.

Code Walkthrough
================

Sample Application 1 – Work Queue using System Thread
-----------------------------------------------------

Overview
~~~~~~~~

In the sample code in the path /examples/innoos_work_q/src/workq1.c, a
work is initialized and added to the system work queue. The work is to
convert the received data structure into a specific json format and
print it to console output.

Sample Code Walkthrough
~~~~~~~~~~~~~~~~~~~~~~~

Define a data structure for the data which is to be handled in the work:

+-----------------------------------------------------------------------+
| /\*define the data for the work*/                                     |
|                                                                       |
| typedef struct my_wq_data_tag                                         |
|                                                                       |
| {                                                                     |
|                                                                       |
| struct os_work work; /\*first member should be of type struct         |
| os_work*/                                                             |
|                                                                       |
| char deviceid[64];                                                    |
|                                                                       |
| int current_reading;                                                  |
|                                                                       |
| struct os_thread \*generated_by;                                      |
|                                                                       |
| }my_wq_data;                                                          |
+=======================================================================+
+-----------------------------------------------------------------------+

As shown in the code, apart from struct os_work, this structure has a
character array to hold the device ID, an integer current reading, and
an os_thread structure pointer to keep the reference of the thread which
will be generating and populating this structure.

Worker function is defined as shown in the following code snippet. This
is the thread function for the work and forms a simple payload (json)
from the input and prints it to the console.

The work function takes a pointer to a work object, struct os_work
\*work, as input. A pointer to the full data structure defined for work
can be retrieved using macro container_of() on this pointer \*work
provided to the worker function.

The macro container_of(ptr, type,member)takes three arguments:

1. A pointer

2. Type of the container

3. Name of the member the pointer refers to.

..

   The macro will then expand to a new address pointing to the container
   which accommodates the respective member.

+-----------------------------------------------------------------------+
| static void prepare_and_dispatch_device_reading_json(struct os_work   |
| \*work)                                                               |
|                                                                       |
| {                                                                     |
|                                                                       |
| my_wq_data \*my_data;                                                 |
|                                                                       |
| /\*extracting the app data*/                                          |
|                                                                       |
| my_data = container_of(work, my_wq_data, work);                       |
|                                                                       |
| os_printf                                                             |
| ("\\n{\\n\\t\\"device_id\\":\\"%s\\",\\n\\t\\"r                       |
| eading\\":%u,\\n\\t\\"generated_by\\":%x,\\n\\t\\"send_by\\":%x\\n}", |
|                                                                       |
| my_data->deviceid,                                                    |
|                                                                       |
| my_data->current_reading,(unsignedint)my_data->generated_by,          |
|                                                                       |
| (unsignedint)os_self());                                              |
|                                                                       |
| os_msleep(25);                                                        |
|                                                                       |
| os_free (my_data);                                                    |
|                                                                       |
| }                                                                     |
+=======================================================================+
+-----------------------------------------------------------------------+

Data for the work is prepared by the application main thread.

+-----------------------------------------------------------------------+
| /\*preparing the data for the work*/                                  |
|                                                                       |
| my_wq_data \*data ;                                                   |
|                                                                       |
| data = os_alloc(sizeof(my_wq_data));                                  |
|                                                                       |
| snprintf (data->deviceid,sizeof(data->deviceid),"this is exe by       |
| system thread\_%u", rand());                                          |
|                                                                       |
| data->current_reading =1;                                             |
|                                                                       |
| data->generated_by = os_self();                                       |
+=======================================================================+
+-----------------------------------------------------------------------+

To initialize a work and to associate a function with it, we use
os_init_work().

Here, the member work of my_wq_data \*data is initialized and associated
with worker function prepare_and_dispatch_device_reading_json().

+-----------------------------------------------------------------------+
| /\*initialize the work, associating work, and work function*/         |
|                                                                       |
| os_init_work(&data->work, prepare_and_dispatch_device_reading_json);  |
+=======================================================================+
+-----------------------------------------------------------------------+

To add a work to the work queue, we use os_queue_system_work().

+-----------------------------------------------------------------------+
| /\*inserting to system work q*/                                       |
|                                                                       |
| os_queue_system_work(&data->work);                                    |
+=======================================================================+
+-----------------------------------------------------------------------+

Please note that the system work queue does not need to be separately
created or initialized, as it is created and initialized at the time of
system start-up itself.

When the system work queue is serviced by the system thread, it will
call the worker function with parameter \*work, which will eventually
retrieve the full data structure associated with my_wq_data \*my_data,
and will perform the defined work on that data from the context of the
system thread.

The work defined here is printing the data and the reference to the
thread which generated the data to the console in a json format, as
shown in section 5.1.4.

Running the Application 
~~~~~~~~~~~~~~~~~~~~~~~~

Program workq1.elf(sdk_x.y\\examples\\innoos_work_q\\bin) using the
Download tool:

1. Launch the Download tool provided with InnoPhase Talaria TWO SDK.

2. In the GUI window:

   a. Boot Target: Select the appropriate EVK from the drop-down.

   b. ELF Input: Load the workq1.elf by clicking on Select ELF File.

   c. Programming: Prog RAM or Prog Flash as per requirement.

For more details on using the Download tool, refer to the document:
UG_Download_Tool.pdf (path: *sdk_x.y/pc_tools/Download_Tool/doc*).

**Note**: x and y refer to the SDK release version. For example:
sdk_2.4/doc.

Expected Output
~~~~~~~~~~~~~~~

workq1.elf is created when compiling this code and gives the following
console output when programmed to Talaria TWO.

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
| Workqueue Demo App 1                                                  |
|                                                                       |
| {                                                                     |
|                                                                       |
| "device_id":"this is exe by system thread_0",                         |
|                                                                       |
| "reading":1,                                                          |
|                                                                       |
| "generated_by":b2de0,                                                 |
|                                                                       |
| "send_by":bede8                                                       |
|                                                                       |
| }                                                                     |
|                                                                       |
| all done                                                              |
+=======================================================================+
+-----------------------------------------------------------------------+

Sample Application 2 – Work Queue using Application defined Thread
------------------------------------------------------------------

.. _overview-1:

Overview
~~~~~~~~

In the sample code in the path /examples/innoos_work_q/src/workq2.c, two
threads are created to generate requests to the work queue and two
threads for handling the requests.

.. _sample-code-walkthrough-1:

Sample Code Walkthrough
~~~~~~~~~~~~~~~~~~~~~~~

Define a data structure for the data which is to be handled in the work:

+-----------------------------------------------------------------------+
| /\*define the data structure for the workqueue*/                      |
|                                                                       |
| typedef struct my_wq_data_tag                                         |
|                                                                       |
| {                                                                     |
|                                                                       |
| Struct os_work work;                                                  |
|                                                                       |
| char deviceid[64];                                                    |
|                                                                       |
| int current_reading;                                                  |
|                                                                       |
| struct os_thread \*generated_by;                                      |
|                                                                       |
| }my_wq_data;                                                          |
+=======================================================================+
+-----------------------------------------------------------------------+

As shown in the code, apart from struct os_work, this structure has a
character array to hold the device ID, an integer current reading, and
an os_thread structure pointer to keep the reference of the thread which
will be generating and populating this structure.

In this sample, two different work functions are defined.

First work function, prepare_and_dispatch_device_reading_json() forms
the json message from the input data.

Second work function prepare_and_dispatch_device_reading_xml()prints to
the console in XML format.

Both the work functions take the pointer to a work object, struct
os_work \*work, as input. A pointer to the full data structure defined
for work can be retrieved using macro container_of() on this pointer
\*work, which is provided to the worker function, as explained in the
code sample in section 5.1.

Work 1:

+-----------------------------------------------------------------------+
| static void prepare_and_dispatch_device_reading_json(struct os_work   |
| \*work)                                                               |
|                                                                       |
| {                                                                     |
|                                                                       |
| my_wq_data \*my_data;                                                 |
|                                                                       |
| /\*extracting the app data*/                                          |
|                                                                       |
| my_data = container_of(work, my_wq_data, work);                       |
|                                                                       |
| os_printf                                                             |
| ("\\n{\\n\\t\\"device_id\\":\\"%s\\",\\n\\t\\"r                       |
| eading\\":%u,\\n\\t\\"generated_by\\":%x,\\n\\t\\"send_by\\":%x\\n}", |
|                                                                       |
| my_data->deviceid,                                                    |
|                                                                       |
| my_data->curren                                                       |
| t_reading,(unsignedint)my_data->generated_by,(unsignedint)os_self()); |
|                                                                       |
| os_msleep(25);                                                        |
|                                                                       |
| os_free (my_data);}                                                   |
+=======================================================================+
+-----------------------------------------------------------------------+

Work2:

+-----------------------------------------------------------------------+
| static void prepare_and_dispatch_device_reading_xml(struct os_work    |
| \*work)                                                               |
|                                                                       |
| {                                                                     |
|                                                                       |
| my_wq_data \*my_data;                                                 |
|                                                                       |
| /\*extracting the app data*/                                          |
|                                                                       |
| my_data = container_of(work, my_wq_data, work);                       |
|                                                                       |
| os_printf                                                             |
| ("\\n{\\n\\t\\"device_id\\":\\"%s\\",\\n\\t\\"reading\\":%u, \\       |
|                                                                       |
| \\n\\t\\"generated_by\\":%x,\\n\\t\\"send_by\\":%x\\n}",              |
|                                                                       |
| my_data->deviceid,                                                    |
|                                                                       |
| my_data->current_reading, (unsigned int)my_data-                      |
| >generated_by,(unsigned int)os_self());                               |
|                                                                       |
| os_msleep(25);                                                        |
|                                                                       |
| os_free (my_data);                                                    |
|                                                                       |
| }                                                                     |
+=======================================================================+
+-----------------------------------------------------------------------+

In this example, a separate thread is created to service the work queue
where a work queue is to be initialized. To achieve this we use
os_init_workqueue().

+-----------------------------------------------------------------------+
| /\*work q handle*/                                                    |
|                                                                       |
| struct os_workqueue hwq;                                              |
|                                                                       |
| /\*initializing work q*/                                              |
|                                                                       |
| os_init_workqueue(&hwq);                                              |
+=======================================================================+
+-----------------------------------------------------------------------+

Two worker threads (worker1 and worker2) are created and associated with
the same work queue previously initialized.

To achieve this, os_create_thread()is used to create these two worker
threads and a function is associated with them:

+-----------------------------------------------------------------------+
| /\*thread 1*/                                                         |
|                                                                       |
| os_create_thread("worker1", my_work_thread,&hwq,1, WORKQ_STACK_SIZE); |
|                                                                       |
| /\*thread 2*/                                                         |
|                                                                       |
| os_create_thread("worker2", my_work_thread,&hwq,1, WORKQ_STACK_SIZE); |
+=======================================================================+
+-----------------------------------------------------------------------+

The function my_work_thread()is associated with both the worker threads.

The work queue handle is passed as an argument to this thread function
while creating both the worker threads.

The application can set the required stack size and priority for the
threads based on the type of work it intends to defer to these threads.

The thread function takes the pointer to the work queue handle passed as
input and calls os_run_work()with this work queue handle.
os_run_work()is a blocking call and it will exit on
os_flush_workqueue().

+-----------------------------------------------------------------------+
| static void \*my_work_thread(void*p)                                  |
|                                                                       |
| {                                                                     |
|                                                                       |
| struct os_workqueue \*wq = p;                                         |
|                                                                       |
| os_printf ("\\n%x:started worker thread",(unsignedint)os_self());     |
|                                                                       |
| os_run_work(wq);                                                      |
|                                                                       |
| /\* the above function will return when the workqueue is destroyed*/  |
|                                                                       |
| os_printf ("\\n%x:exitng worker thread",(unsignedint)os_self());      |
|                                                                       |
| returnNULL;}                                                          |
+=======================================================================+
+-----------------------------------------------------------------------+

Two more threads (producer1 and producer2) are created in this example
and are associated with the same work queue initialized previously.
These producer threads will produce the work for the worker threads
previously created.

To achieve this, os_create_thread()is used to create these two producer
threads and a function is associated with them:

+-----------------------------------------------------------------------+
| int main()                                                            |
|                                                                       |
| {                                                                     |
|                                                                       |
| ...                                                                   |
|                                                                       |
| ...                                                                   |
|                                                                       |
| producer_thread_1 = os_create_thread("producer1",                     |
| workq_load_producer, &hwq, 1, WORKQ_STACK_SIZE);                      |
|                                                                       |
| producer_thread_2 = os_create_thread("producer2",                     |
| workq_load_producer, &hwq, 1, WORKQ_STACK_SIZE);                      |
|                                                                       |
| os_join_thread(producer_thread_1);                                    |
|                                                                       |
| os_join_thread(producer_thread_2);                                    |
|                                                                       |
| ...                                                                   |
|                                                                       |
| ...                                                                   |
|                                                                       |
| }                                                                     |
+=======================================================================+
+-----------------------------------------------------------------------+

The function workq_load_producer()is associated with both of these
producer threads. The work queue handle is passed as an argument to this
thread function while creating both the producer threads.

The data for the work is prepared by these producer threads inside the
thread function workq_load_producer(), and os_init_work() is used to
associate the work with the two work functions in a way that alternate
data goes to xml and json works.

The work is then added to the work queue using os_queue_work()which
returns true if succeeds in adding or false if the work is already
queued.

+-----------------------------------------------------------------------+
| static void \*workq_load_producer(void*p)                             |
|                                                                       |
| {                                                                     |
|                                                                       |
| struct os_workqueue \*wq = p;                                         |
|                                                                       |
| int msg_counter = 0;                                                  |
|                                                                       |
| ...                                                                   |
|                                                                       |
| ...                                                                   |
|                                                                       |
| while ( (msg_counter <= MAX_MESSAGES_PER_THREAD))                     |
|                                                                       |
| {                                                                     |
|                                                                       |
| my_wq_data \*data ;                                                   |
|                                                                       |
| data = os_alloc(sizeof(my_wq_data));                                  |
|                                                                       |
| snprintf (data->deviceid, sizeof(data->deviceid), "abcd_xyz\_%u",     |
| rand());                                                              |
|                                                                       |
| data->current_reading = msg_counter;                                  |
|                                                                       |
| data->generated_by = os_self();                                       |
|                                                                       |
| ...                                                                   |
|                                                                       |
| ...                                                                   |
|                                                                       |
| ...                                                                   |
|                                                                       |
| if(0==(msg_counter%2))                                                |
|                                                                       |
| {                                                                     |
|                                                                       |
| os_init_work(&data->work, prepare_and_dispatch_device_reading_json);  |
|                                                                       |
| }                                                                     |
|                                                                       |
| else                                                                  |
|                                                                       |
| {                                                                     |
|                                                                       |
| os_init_work(&data->work, prepare_and_dispatch_device_reading_xml);   |
|                                                                       |
| }                                                                     |
|                                                                       |
| /\*inserting to the workq*/                                           |
|                                                                       |
| ret = os_queue_work(wq, &data->work);                                 |
|                                                                       |
| if (!ret)                                                             |
|                                                                       |
| {                                                                     |
|                                                                       |
| os_printf("\\nrequest is in q. ret:%d", ret);                         |
|                                                                       |
| }                                                                     |
|                                                                       |
| os_msleep(10);                                                        |
|                                                                       |
| ++msg_counter;                                                        |
|                                                                       |
| }                                                                     |
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

Each of the two producer threads adds work1 and work2 alternatively to
the work queue until a while loop counter finishes.

os_flush_workqueue() is used to send a signal to the
os_run_work()function to exit when all the previously queued work has
been completed.

+-----------------------------------------------------------------------+
| /\*for worker thread 1*/                                              |
|                                                                       |
| os_flush_workqueue(&hwq);                                             |
|                                                                       |
| /\*for worker thread 2*/                                              |
|                                                                       |
| os_flush_workqueue(&hwq);                                             |
+=======================================================================+
+-----------------------------------------------------------------------+

.. _running-the-application-1:

Running the Application 
~~~~~~~~~~~~~~~~~~~~~~~~

Program workq2.elf(sdk_x.y\\examples\\innoos_work_q\\bin) using the
Download tool:

1. Launch the Download tool provided with InnoPhase Talaria TWO SDK.

2. In the GUI window:

   a. Boot Target: Select the appropriate EVK from the drop-down.

   b. ELF Input: Load the workq2.elf by clicking on Select ELF File.

   c. Programming: Prog RAM or Prog Flash as per requirement.

For more details on using the Download tool, refer to the document:
UG_Download_Tool.pdf (path: *sdk_x.y/pc_tools/Download_Tool/doc*).

**Note**: x and y refer to the SDK release version. For example:
sdk_2.4/doc.

.. _expected-output-1:

Expected Output
~~~~~~~~~~~~~~~

workq2.elf is created when compiling this code and gives the following
console output when programmed to Talaria TWO.

Note that when the two worker threads are started, send by field in each
message refers to either of these worker threads, whichever serviced the
message. Based on scheduling, the messages serviced by the worker
threads are random.

Each reading is generated twice, once per producer thread, and is shown
in generated by the field. All the even readings by both the producers
are dispatched as json and all the odd ones as xml.

This is provided as an output to the console till reading 50 is
generated by both the producers. Post this, the work queue is flushed,
and the worker threads exit as shown in the following snippet.

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
| Workqueue Demo App 2                                                  |
|                                                                       |
| bf968:started worker thread                                           |
|                                                                       |
| b35e8:started worker thread                                           |
|                                                                       |
| b3ae8:started worker thread                                           |
|                                                                       |
| {                                                                     |
|                                                                       |
| "device_id":"abcd_xyz_0",                                             |
|                                                                       |
| "reading":0,                                                          |
|                                                                       |
| "generated_by":b3fe8,                                                 |
|                                                                       |
| "send_by":bf968                                                       |
|                                                                       |
| }                                                                     |
|                                                                       |
| <payload>                                                             |
|                                                                       |
| <device_id>                                                           |
|                                                                       |
| abcd_xyz_1774527498                                                   |
|                                                                       |
| </device_id>                                                          |
|                                                                       |
| <reading>                                                             |
|                                                                       |
| 1                                                                     |
|                                                                       |
| </reading>                                                            |
|                                                                       |
| <generated_by>                                                        |
|                                                                       |
| b3fe8                                                                 |
|                                                                       |
| </generated_by>                                                       |
|                                                                       |
| <send_by>                                                             |
|                                                                       |
| b3ae8                                                                 |
|                                                                       |
| </send_by>                                                            |
|                                                                       |
| </payload>                                                            |
|                                                                       |
| {                                                                     |
|                                                                       |
| "device_id":"abcd_xyz_2099690603",                                    |
|                                                                       |
| "reading":2,                                                          |
|                                                                       |
| "generated_by":b3fe8,                                                 |
|                                                                       |
| "send_by":b35e8                                                       |
|                                                                       |
| }                                                                     |
|                                                                       |
| {                                                                     |
|                                                                       |
| "device_id":"abcd_xyz_1452469787",                                    |
|                                                                       |
| "reading":0,                                                          |
|                                                                       |
| "generated_by":b44e8,                                                 |
|                                                                       |
| "send_by":bf968                                                       |
|                                                                       |
| }                                                                     |
|                                                                       |
| .                                                                     |
|                                                                       |
| .                                                                     |
|                                                                       |
| .                                                                     |
|                                                                       |
| .                                                                     |
|                                                                       |
| .                                                                     |
|                                                                       |
| .                                                                     |
|                                                                       |
| <payload>                                                             |
|                                                                       |
| <device_id>                                                           |
|                                                                       |
| abcd_xyz_790790538                                                    |
|                                                                       |
| </device_id>                                                          |
|                                                                       |
| <reading>                                                             |
|                                                                       |
| 49                                                                    |
|                                                                       |
| </reading>                                                            |
|                                                                       |
| <generated_by>                                                        |
|                                                                       |
| b3fe8                                                                 |
|                                                                       |
| </generated_by>                                                       |
|                                                                       |
| <send_by>                                                             |
|                                                                       |
| b3ae8                                                                 |
|                                                                       |
| </send_by>                                                            |
|                                                                       |
| </payload>                                                            |
|                                                                       |
| {                                                                     |
|                                                                       |
| "device_id":"abcd_xyz_2035955618",                                    |
|                                                                       |
| "reading":40,                                                         |
|                                                                       |
| "generated_by":b44e8,                                                 |
|                                                                       |
| "send_by":bf968                                                       |
|                                                                       |
| }                                                                     |
|                                                                       |
| <payload>                                                             |
|                                                                       |
| <device_id>                                                           |
|                                                                       |
| abcd_xyz_657584690                                                    |
|                                                                       |
| </device_id>                                                          |
|                                                                       |
| <reading>                                                             |
|                                                                       |
| 49                                                                    |
|                                                                       |
| </reading>                                                            |
|                                                                       |
| <generated_by>                                                        |
|                                                                       |
| b44e8                                                                 |
|                                                                       |
| </generated_by>                                                       |
|                                                                       |
| <send_by>                                                             |
|                                                                       |
| b3ae8                                                                 |
|                                                                       |
| </send_by>                                                            |
|                                                                       |
| </payload>                                                            |
|                                                                       |
| b35e8:exiting worker thread                                           |
|                                                                       |
| b3ae8:exiting worker thread                                           |
|                                                                       |
| all done                                                              |
+=======================================================================+
+-----------------------------------------------------------------------+
