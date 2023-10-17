Introduction
============

This application note provides a brief about Threads and Semaphore APIs
available in the SDK. Accompanying sample application describes the use
of these APIs.

Threads and Semaphores
======================

Threads
-------

A thread is represented by the struct os_thread. This object contains
all information needed by the kernel to manage the execution of the
thread.

Each thread is created with a stack and an entry point. The entry point
is a function that the threads begin to execute when started by the
kernel. The thread will continue to run until it returns from this
function.

The threads are scheduled on a strict priority-based scheme, with eight
different priority levels 0-7, 7 having the highest priority. The
scheduler will preempt the currently running thread at any point if a
thread with a higher priority becomes ready to execute.

Semaphores
----------

A semaphore provides a synchronized counter for a shared resource for
use in a thread context. Each semaphore has a value (a non-negative
number) representing *how much* of the resource is available. If the
value is only ever zero or one, it can be used as a sleeping lock. Since
waiting for a semaphore depends on the ability to sleep, it must not be
done in an interrupt context.

Threads and Semaphores APIs
===========================

Thread handling APIs
--------------------

os_create_thread()
~~~~~~~~~~~~~~~~~~

Creates a new thread with priority specified in flags.

+-----------------------------------------------------------------------+
| struct os_thread \* os_create_thread(const char \*name,               |
| os_entrypoint_t entry, os_threadarg_t arg, uint32_t flags, size_t     |
| stacksz)                                                              |
+=======================================================================+
+-----------------------------------------------------------------------+

Though the thread is placed in the run queue, there is no immediate
reschedule.

Parameters passed to the API are:

1. Name of the thread

2. Entry point for the thread

3. Argument passed to entry point - specifies attributes like a priority
   for the new thread

4. Requested stack size in bytes.

The thread continues to run until the entry point returns, at which
point return value (a pointer) can be obtained with os_join_thread().

Returns pointer to struct os_thread if successful, NULL otherwise.

os_join_thread ()
~~~~~~~~~~~~~~~~~

Waits for a thread to terminate and destroy the thread.

+-----------------------------------------------------------------------+
| void \* os_join_thread(struct os_thread \*thread)                     |
+=======================================================================+
+-----------------------------------------------------------------------+

Calling this function will suspend the execution of the calling thread
until the target thread exits. The memory used to hold the threads stack
and control block is freed.

The function returns the value returned by the terminating thread.

If the return value is of no consequence, OS_CRTHREAD_DETACHED can be
passed in flags. This causes the OS to reap the thread.

os_self()
~~~~~~~~~

Return reference to the calling thread.

+-----------------------------------------------------------------------+
| struct os_thread \* os_self(void)                                     |
+=======================================================================+
+-----------------------------------------------------------------------+

This function returns the reference to the calling thread. This is the
same value that was returned from the os_create_thread() call used to
create this thread.

Semaphore handling APIs
-----------------------

os_sem_init()
~~~~~~~~~~~~~

Initializes a semaphore when passed a pointer to the semaphore where the
initial value is to be assigned to the semaphore.

+-----------------------------------------------------------------------+
| void os_sem_init(struct os_semaphore \*sem, int value)                |
+=======================================================================+
+-----------------------------------------------------------------------+

os_sem_wait()
~~~~~~~~~~~~~

Locks a semaphore. If the value of the semaphore is greater than zero,
it decrements the counter. If the value is zero, it puts the current
thread to sleep until the value becomes positive.

+-----------------------------------------------------------------------+
| void os_sem_wait(struct os_semaphore \*sem)                           |
+=======================================================================+
+-----------------------------------------------------------------------+

os_sem_wait_timeout()
~~~~~~~~~~~~~~~~~~~~~

Locks a semaphore with timeout passed as parameter tmo in microseconds.

+-----------------------------------------------------------------------+
| int os_sem_wait_timeout(struct os_semaphore \*sem, uint32_t tmo)      |
+=======================================================================+
+-----------------------------------------------------------------------+

If the value is zero, it puts the current thread to sleep for at most
tmo microseconds. If the semaphore is unlocked before the timeout
expires, it locks the semaphore and returns zero. If a timeout occurs,
-1 is returned (and the semaphore is unlocked).

os_sem_post()
~~~~~~~~~~~~~

Unlocks a semaphore. Increments the value of a semaphore and wakes the
first thread waiting for this semaphore.

+-----------------------------------------------------------------------+
| void os_sem_post(struct os_semaphore \*sem)                           |
+=======================================================================+
+-----------------------------------------------------------------------+

os_sem_waiting()
~~~~~~~~~~~~~~~~

Return true if there are any threads waiting for this semaphore.

+-----------------------------------------------------------------------+
| bool os_sem_waiting(struct os_semaphore \*sem)                        |
+=======================================================================+
+-----------------------------------------------------------------------+

Code Walkthrough
================

Sample Application 1 – Thread Creation
--------------------------------------

**Note**: All the applicable ELFs are available in the following
location of the SDK release package:
sdk_x.y\\examples\\innoos_threads_semaphores\\bin).

x and y in sdk_x.y refer to the SDK release version. For example:
*sdk_2.4\\examples\\innoos_threads_semaphores\\bin*.

Overview
~~~~~~~~

The sample code in the path /examples/innoos_threads_semaphores
/src/threads_sample1.c provides more details on how to create a thread
and execute it.

Sample Code Walkthrough
~~~~~~~~~~~~~~~~~~~~~~~

We assign the priority and stack size of the thread using the
preprocessing directives as follows:

+-----------------------------------------------------------------------+
| #define MY_APP_THREAD_PRIO 1 /\* thread priority*/                    |
|                                                                       |
| #define MY_APP_THREAD_STACK_SIZE 512 /\* thread stack size*/          |
+=======================================================================+
+-----------------------------------------------------------------------+

After thread creation, we check if the creation of a thread was
successful or not. If the call to os_create_thread() is successful, the
OS schedules the thread to run where the function my_app_thread_func()
will be called. It prints the string output to the console and returns.

+-----------------------------------------------------------------------+
| /\* creates a thread \*/                                              |
|                                                                       |
| my_app_thread = os_create_thread("my_app_thread",                     |
| my_app_thread_func,NULL, MY_APP_THREAD_PRIO,                          |
| MY_APP_THREAD_STACK_SIZE);                                            |
+=======================================================================+
+-----------------------------------------------------------------------+

While the thread function is still running, the API os_join_thread()will
suspend the main thread (calling thread) until the thread to be joined
(i.e.. the ‘my_app_thread’ in this example) terminates.

+-----------------------------------------------------------------------+
| if( my_app_thread ==NULL)                                             |
|                                                                       |
| {                                                                     |
|                                                                       |
| os_printf(" thread creation failed\\n");                              |
|                                                                       |
| return-1;                                                             |
|                                                                       |
| }                                                                     |
|                                                                       |
| /\* waits for thread function to finish \*/                           |
|                                                                       |
| os_join_thread(my_app_thread);                                        |
+=======================================================================+
+-----------------------------------------------------------------------+

Using of Delays in Threads
~~~~~~~~~~~~~~~~~~~~~~~~~~

Delays are mainly used when we want to stop the execution flow of a
program for t units of time. The libkernel.a library provides many
function calls with different delay precision.

We can use the functions such as os_msleep() for milliseconds, and
os_usleep() for microseconds.

i.e., os_msleep(1000) will provide a 1000 millisecond delay. Consider
the example where a delay function is used:

+-----------------------------------------------------------------------+
| static void\* my_app_thread_func(void\* arg)                          |
|                                                                       |
| {                                                                     |
|                                                                       |
| os_printf("1. hello world from a thread function\\n");                |
|                                                                       |
| os_msleep(1000);                                                      |
|                                                                       |
| os_printf("2. hello world after 1000ms\\n");                          |
|                                                                       |
| returnNULL;                                                           |
|                                                                       |
| }                                                                     |
+=======================================================================+
+-----------------------------------------------------------------------+

When the thread function is called, it outputs the first string. Then
the thread suspends for 1000 milliseconds and when it resumes execution
and then prints the second string.

Running the Application 
~~~~~~~~~~~~~~~~~~~~~~~~

Program threads_sample1.elf using the Download tool:

1. Launch the Download tool provided with InnoPhase Talaria TWO SDK.

2. In the GUI window:

   a. Boot Target: Select the appropriate EVK from the drop-down.

   b. ELF Input: Load the threads_sample1.elf by clicking on Select ELF
      File.

   c. Programming: Prog RAM or Prog Flash as per requirement.

For more details on using the Download tool, refer to the document:
UG_Download_Tool.pdf (path: *sdk_x.y/pc_tools/Download_Tool/doc*).

**Note**: x and y refer to the SDK release version. For example:
sdk_2.4/doc.

Expected Output
~~~~~~~~~~~~~~~

threads_sample1.elf is created when compiling this code which gives the
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
| Threads Demo App 1                                                    |
|                                                                       |
| 1. hello world from a thread function                                 |
|                                                                       |
| 2. hello world after 1000ms                                           |
+=======================================================================+
+-----------------------------------------------------------------------+

Sample Application 2 – Thread Priorities
----------------------------------------

.. _overview-1:

Overview
~~~~~~~~

The sample code in the path:
/examples/innoos_threads_semaphores/src/threads_sample2.c describes the
creation of two threads with different priority levels.

.. _sample-code-walkthrough-1:

Sample Code Walkthrough
~~~~~~~~~~~~~~~~~~~~~~~

Priorities are assigned for each thread as follows:

+-----------------------------------------------------------------------+
| #define MY_APP_THREAD_PRIO 2 /\* thread priority ie, the first        |
| executing thread*/                                                    |
|                                                                       |
| #define MY_APP_THREAD_STACK_SIZE 512 /\* thread stack size*/          |
|                                                                       |
| #define MY_APP_THREAD_2_PRIO 1 /\* thread priority ie, the second     |
| executing thread*/                                                    |
|                                                                       |
| #define MY_APP_THREAD_2_STACK_SIZE 512 /\* thread stack size*/        |
+=======================================================================+
+-----------------------------------------------------------------------+

Here, two thread variables are declared:

+-----------------------------------------------------------------------+
| /\* declare os_thread variables \*/                                   |
|                                                                       |
| static struct os_thread \*my_app_thread;                              |
|                                                                       |
| static struct os_thread \*my_app_thread_2;                            |
+=======================================================================+
+-----------------------------------------------------------------------+

Post which, os_create_thread() API is called with the following boot
arguments: name of the thread, entry point for the thread, argument for
the entry point, thread priority flag and the stack size in bytes.

+-----------------------------------------------------------------------+
| /\* create threads \*/                                                |
|                                                                       |
| my_app_thread =os_create_thread("my_app_thread",                      |
| my_app_thread_func,NULL, MY_APP_THREAD_PRIO,                          |
| MY_APP_THREAD_STACK_SIZE);                                            |
|                                                                       |
| if(NULL== my_app_thread)                                              |
|                                                                       |
| {                                                                     |
|                                                                       |
| os_printf(" thread creation failed\\n");                              |
|                                                                       |
| return-1;                                                             |
|                                                                       |
| }                                                                     |
|                                                                       |
| my_app_thread_2 =os_create_thread("my_app_thread_2",                  |
| my_app_thread_func_2,NULL, MY_APP_THREAD_2_PRIO,                      |
| MY_APP_THREAD_2_STACK_SIZE);                                          |
|                                                                       |
| if(NULL== my_app_thread_2 )                                           |
|                                                                       |
| {                                                                     |
|                                                                       |
| os_printf(" thread creation failed\\n");                              |
|                                                                       |
| return-1;                                                             |
|                                                                       |
| }                                                                     |
+=======================================================================+
+-----------------------------------------------------------------------+

Any type of variable can be passed as an argument to the threads. Here,
the thread takes a string argument which is received as an output inside
the thread function itself.

+-----------------------------------------------------------------------+
| static void\* my_app_thread_func_2(void\* arg)                        |
|                                                                       |
| {                                                                     |
|                                                                       |
| do                                                                    |
|                                                                       |
| {                                                                     |
|                                                                       |
| flag++;                                                               |
|                                                                       |
| os_printf("Message from Second Thread. Thread                         |
| id[%x]\\n",(unsignedint)os_self());                                   |
|                                                                       |
| }while(flag<3);                                                       |
|                                                                       |
| returnNULL;                                                           |
|                                                                       |
| }                                                                     |
+=======================================================================+
+-----------------------------------------------------------------------+

To join threads, os_join_thread()API is used as shown in the following
code block:

+-----------------------------------------------------------------------+
| /\* waits for thread function to finish \*/                           |
|                                                                       |
| os_join_thread(my_app_thread);                                        |
|                                                                       |
| os_join_thread(my_app_thread_2);                                      |
+=======================================================================+
+-----------------------------------------------------------------------+

.. _running-the-application-1:

Running the Application 
~~~~~~~~~~~~~~~~~~~~~~~~

Program threads_sample2.elf using the Download tool:

1. Launch the Download tool provided with InnoPhase Talaria TWO SDK.

2. In the GUI window:

   a. Boot Target: Select the appropriate EVK from the drop-down.

   b. ELF Input: Load the threads_sample2.elf by clicking on Select ELF
      File.

   c. Programming: Prog RAM or Prog Flash as per requirement.

For more details on using the Download tool, refer to the document:
UG_Download_Tool.pdf (path: *sdk_x.y/pc_tools/Download_Tool/doc*).

**Note**: x and y refer to the SDK release version. For example:
sdk_2.4/doc.

.. _expected-output-1:

Expected Output
~~~~~~~~~~~~~~~

threads_sample2.elf is created when compiling this code which gives the
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
| Threads Demo App 2                                                    |
|                                                                       |
| Message from First Thread. Thread id[bf780]                           |
|                                                                       |
| Message from First Thread. Thread id[bf780]                           |
|                                                                       |
| Message from First Thread. Thread id[bf780]                           |
|                                                                       |
| Message from Second Thread. Thread id[bfa00]                          |
|                                                                       |
| Message from Second Thread. Thread id[bfa00]                          |
|                                                                       |
| Message from Second Thread. Thread id[bfa00]                          |
+=======================================================================+
+-----------------------------------------------------------------------+

Sample Application 3 – Thread & Stack Size
------------------------------------------

.. _overview-2:

Overview
~~~~~~~~

In the sample code in the path:
/examples/innoos_threads_semaphores/src/threads_sample3.c, threads are
created with a given stack size in a loop. After creating a few threads,
further thread creation fails due to the stack size. If the stack size
for each thread is lowered, then multiple threads can co-exist.

.. _sample-code-walkthrough-2:

Sample Code Walkthrough
~~~~~~~~~~~~~~~~~~~~~~~

Thread stack sized defined as a macro:

+-----------------------------------------------------------------------+
| #define THREAD_BASICS_STACK_SIZE 1024 /\* thread stack size*/         |
+=======================================================================+
+-----------------------------------------------------------------------+

Here, threads are created in a loop until failure occurs. If thread
creation fails, os_create_thread() returns a NULL pointer:

+-----------------------------------------------------------------------+
| /\* creates a threads, until creation of thread fails \*/             |
|                                                                       |
| while(1)                                                              |
|                                                                       |
| { thread_id =                                                         |
| os_create_thread("THREAD_BASICS",thread_sample_thread_func,           |
|                                                                       |
| NULL, OS_CRTHREAD_DETACHED|THREAD_BASICS_PRIO,                        |
| THREAD_BASICS_STACK_SIZE);                                            |
|                                                                       |
| if(NULL== thread_id)                                                  |
|                                                                       |
| {                                                                     |
|                                                                       |
| os_printf("resource not available. thread creation failed.\\n");      |
|                                                                       |
| os_error(OS_ERR_INTERNAL_ERROR);                                      |
|                                                                       |
| }                                                                     |
|                                                                       |
| os_sleep_us(10*1000, OS_TIMEOUT_NO_WAKEUP);                           |
|                                                                       |
| }                                                                     |
+=======================================================================+
+-----------------------------------------------------------------------+

Each thread prints a text, and sleeps inside a while loop. If the thread
is not sleeping, then thread creation might not fail. This is because,
resources allocated for the earlier threads were on exit and are
available for new threads.

+-----------------------------------------------------------------------+
| /\* the thread function \*/                                           |
|                                                                       |
| static void\* thread_sample_thread_func(void\* arg)                   |
|                                                                       |
| {                                                                     |
|                                                                       |
| os_printf("%03d:thread created\\n",++thread_count);                   |
|                                                                       |
| while(1)                                                              |
|                                                                       |
| {                                                                     |
|                                                                       |
| os_sleep_us(1000*1000, OS_TIMEOUT_NO_WAKEUP);                         |
|                                                                       |
| }                                                                     |
|                                                                       |
| return NULL;                                                          |
|                                                                       |
| }                                                                     |
+=======================================================================+
+-----------------------------------------------------------------------+

Changing the stack size and the number of threads created before failure
increases is as defined in the following code:

+-----------------------------------------------------------------------+
| #define THREAD_BASICS_STACK_SIZE 512 /\* thread stack size*/          |
+=======================================================================+
+-----------------------------------------------------------------------+

.. _running-the-application-2:

Running the Application 
~~~~~~~~~~~~~~~~~~~~~~~~

Program threads_sample3.elf using the Download tool:

1. Launch the Download tool provided with InnoPhase Talaria TWO SDK.

2. In the GUI window:

   a. Boot Target: Select the appropriate EVK from the drop-down.

   b. ELF Input: Load the threads_sample3.elf by clicking on Select ELF
      File.

   c. Programming: Prog RAM or Prog Flash as per requirement.

For more details on using the Download tool, refer to the document:
UG_Download_Tool.pdf (path: *sdk_x.y/pc_tools/Download_Tool/doc*).

**Note**: x and y refer to the SDK release version. For example:
sdk_2.4/doc.

.. _expected-output-2:

Expected Output
~~~~~~~~~~~~~~~

threads_sample3.elf is created when compiling this code which gives the
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
| Threads Demo App 3                                                    |
|                                                                       |
| 001:thread created                                                    |
|                                                                       |
| 002:thread created                                                    |
|                                                                       |
| 003:thread created                                                    |
|                                                                       |
| 004:thread created                                                    |
|                                                                       |
| 005:thread created                                                    |
|                                                                       |
| 006:thread created                                                    |
|                                                                       |
| 007:thread created                                                    |
|                                                                       |
| 008:thread created                                                    |
|                                                                       |
| 009:thread created                                                    |
|                                                                       |
| 010:thread created                                                    |
|                                                                       |
| 011:thread created                                                    |
|                                                                       |
| 012:thread created                                                    |
|                                                                       |
| 013:thread created                                                    |
|                                                                       |
| 014:thread created                                                    |
|                                                                       |
| 015:thread created                                                    |
|                                                                       |
| 016:thread created                                                    |
|                                                                       |
| 017:thread created                                                    |
|                                                                       |
| 018:thread created                                                    |
|                                                                       |
| 019:thread created                                                    |
|                                                                       |
| 020:thread created                                                    |
|                                                                       |
| 021:thread created                                                    |
|                                                                       |
| 022:thread created                                                    |
|                                                                       |
| 023:thread created                                                    |
|                                                                       |
| 024:thread created                                                    |
|                                                                       |
| 025:thread created                                                    |
|                                                                       |
| 026:thread created                                                    |
|                                                                       |
| 027:thread created.                                                   |
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
| .                                                                     |
|                                                                       |
| 697:thread created                                                    |
|                                                                       |
| 698:thread created                                                    |
|                                                                       |
| resource not available. thread creation failed.                       |
|                                                                       |
| OS_ERROR 0xfc                                                         |
|                                                                       |
| OS_UNEXPECTED_EXCEPTION 0x6                                           |
|                                                                       |
| R0=00000030 R1=0004b6d4 R2=00fc0d00 R3=00000000                       |
|                                                                       |
| R4=00000200 R5=001049cd R6=00104a47 R7=07777777                       |
|                                                                       |
| R8=08888888 R9=09999999 R10=0aaaaaaa R11=0bbbbbbb                     |
|                                                                       |
| R12=000b2be3 SP=000b2c84 LR=00104a1b PC=00104a1a                      |
|                                                                       |
| xPSR=21000000 CONTROL=00000000 CFSR=00010000 BFAR=e000ed38            |
|                                                                       |
| STACK:                                                                |
|                                                                       |
| 0x000b2cc8: 00000200 01111111 04444444 05555555                       |
|                                                                       |
| 0x000b2cd8: 06666666 00044e81 6e69616d 2988fa00                       |
|                                                                       |
| 0x000b2ce8: 001049f1 07f83201 00000002 000b2c84                       |
|                                                                       |
| 0x000b2cf8: 000b24e8 a5631209 000b2d00 000b2d00                       |
|                                                                       |
| 0x000b2d08: 000b2d08 000b2d08 0004000c 0004000c                       |
|                                                                       |
| 0x000b2d18: 000bf5e0 000bed20 000b2d20 000b2d20                       |
|                                                                       |
| 0x000b2d28: 00000000 00000000 2df339e6 7349fc7f                       |
|                                                                       |
| 0x000b2d38: 9ae964cd 00b1164b 345d406c 39c04a4e                       |
|                                                                       |
| 0x000b2d48: ffc8daa2 abfbaff5 8fb90474 1b15e267                       |
|                                                                       |
| 0x000b2d58: 7e319424 5ba8eb37 77759125 fdb7ba53                       |
|                                                                       |
| 0x000b2d68: ebadcc99 201b8df4 0b444886 67873273                       |
|                                                                       |
| 0x000b2d78: 297324ac 11501758 e51c63cf 036a56b6                       |
|                                                                       |
| 0x000b2d88: 70db1ab6 040913ed aa791662 5dd9b7f3                       |
|                                                                       |
| 0x000b2d98: e309dfe6 83476ca2 cd864e0a 33f21c84                       |
|                                                                       |
| 0x000b2da8: 6c98c51e dcf15390 84ece867 1518ef2a                       |
|                                                                       |
| 0x000b2db8: e50d55a8 b8202166 b3b87b4e 9974b048                       |
+=======================================================================+
+-----------------------------------------------------------------------+

Sample Application 4 – Thread & Semaphores
------------------------------------------

.. _overview-3:

Overview
~~~~~~~~

In the sample code in the path:
/examples/innoos_threads_semaphores/src/threads_semaphores.c, three
threads are created, each with separate thread functions. By using a
semaphore, the threads will execute according to the value used for the
initialization of the semaphore variable.

In this application, Thread1 initially takes the semaphore while Thread2
and Thread3 wait until Thread1 completes its task and releases the
semaphore. Thread2 and Thread3 are both waiting for the semaphore but in
two different ways.

.. _sample-code-walkthrough-3:

Sample Code Walkthrough
~~~~~~~~~~~~~~~~~~~~~~~

Here we are using three threads as shown below:

+-----------------------------------------------------------------------+
| my_app_thread_1 =os_create_thread("my_app_thread_1",                  |
| my_app_thread_func_1, NULL, SEMAPHORE_SAMPLE_THREAD_PRIORITY,         |
| SEMAPHORE_SAMPLE_THREAD_STACK_SIZE);                                  |
|                                                                       |
| /\* creating thread 1 \*/                                             |
|                                                                       |
| my_app_thread_2                                                       |
| =os_create_thread("my_app_thread_2",my_app_thread_func_2, NULL,       |
| SEMAPHORE_SAMPLE_THREAD_PRIORITY,                                     |
| SEMAPHORE_SAMPLE_THREAD_STACK_SIZE);                                  |
|                                                                       |
| /\* creating thread 2 \*/                                             |
|                                                                       |
| my_app_thread_3 =os_create_thread("my_app_thread_3",                  |
| my_app_thread_func_3,NULL, SEMAPHORE_SAMPLE_THREAD_PRIORITY,          |
| SEMAPHORE_SAMPLE_THREAD_STACK_SIZE);                                  |
|                                                                       |
| /\* creating thread 2 \*/                                             |
+=======================================================================+
+-----------------------------------------------------------------------+

Before thread creation, there is a need to declare and initialize the
semaphore variable by using the following statements:

+-----------------------------------------------------------------------+
| static struct os_semaphore my_sem;                                    |
|                                                                       |
| …                                                                     |
|                                                                       |
| …                                                                     |
|                                                                       |
| …                                                                     |
|                                                                       |
| /\* initializes a semaphore. this has to be called before using       |
| my_sem.                                                               |
|                                                                       |
| init with 0                                                           |
|                                                                       |
| \*/                                                                   |
|                                                                       |
| os_sem_init(&my_sem,0);                                               |
+=======================================================================+
+-----------------------------------------------------------------------+

It is required to initialize the semaphore variable using
os_sem_init()before using the semaphore variable. In the code, the
semaphore is initialized to 0.

Consider the thread functions defined for our created threads:

my_app_thread_func_1() for Thread1:

+-----------------------------------------------------------------------+
| static void\* my_app_thread_func_1(void\* arg)                        |
|                                                                       |
| {                                                                     |
|                                                                       |
| os_printf("\\n%x:%u:from thread 1. doing initial tasks",              |
|                                                                       |
| SEMAPHORE_SAMPLE_CURRENT_THREAD_ID,os_systime());                     |
|                                                                       |
| /\*sleeping for some time, still other threads waiting*/              |
|                                                                       |
| os_msleep(1000);                                                      |
|                                                                       |
| /\*checking is there any one waiting on the thread*/                  |
|                                                                       |
| os_printf("\\n%x:%u:from thread 1. Is any one waiting for sem:%s",    |
|                                                                       |
| SEMAPHORE_SAMPLE_CURRENT_THREAD_ID,os_systime(),                      |
|                                                                       |
| os_sem_waiting(&my_sem)==1?"Yes":"No");                               |
|                                                                       |
| os_printf("\\n%x:%u:from thread 1. initial jobs done. now thread 2/3  |
| can start."                                                           |
|                                                                       |
| " going to release the semaphore",                                    |
|                                                                       |
| SEMAPHORE_SAMPLE_CURRENT_THREAD_ID,os_systime());                     |
|                                                                       |
| /\*releasing the semaphore*/                                          |
|                                                                       |
| os_sem_post(&my_sem );                                                |
|                                                                       |
| /\*checking is there any one waiting on the thread*/                  |
|                                                                       |
| return NULL;                                                          |
|                                                                       |
| }                                                                     |
+=======================================================================+
+-----------------------------------------------------------------------+

my_app_thread_func_2() for Thread2.

Thread 2 is waiting to acquire the semaphore. Once it does, it waits for
3000 milliseconds post which it releases the semaphore.

+-----------------------------------------------------------------------+
| static void\* my_app_thread_func_2(void\* arg)                        |
|                                                                       |
| {                                                                     |
|                                                                       |
| os_printf("\\n%x:%u:from thread 2. waiting for semaphore",            |
|                                                                       |
| SEMAPHORE_SAMPLE_CURRENT_THREAD_ID,os_systime());                     |
|                                                                       |
| /\*waiting on the semaphore*/                                         |
|                                                                       |
| os_sem_wait(&my_sem );                                                |
|                                                                       |
| os_printf("\\n%x:%u:from thread 2. got semaphore",                    |
|                                                                       |
| SEMAPHORE_SAMPLE_CURRENT_THREAD_ID,os_systime());                     |
|                                                                       |
| /\*thread 2 business logic here*/                                     |
|                                                                       |
| os_printf("\\n%x:%u:from thread 2. releasing semaphore\\n",           |
|                                                                       |
| SEMAPHORE_SAMPLE_CURRENT_THREAD_ID,os_systime());                     |
|                                                                       |
| /\*releasing the semaphore*/                                          |
|                                                                       |
| os_sem_post(&my_sem );                                                |
|                                                                       |
| return NULL;                                                          |
|                                                                       |
| }                                                                     |
+=======================================================================+
+-----------------------------------------------------------------------+

my_app_thread_func_3() for Thread3.

Thread 3 is waiting to acquire the semaphore until it times out. If it
times out, it will loop back and once again try to acquire the
semaphore.

Once it does, it will complete its task and releases the semaphore:

+-----------------------------------------------------------------------+
| static void\* my_app_thread_func_3(void\* arg)                        |
|                                                                       |
| {                                                                     |
|                                                                       |
| int ret;                                                              |
|                                                                       |
| os_printf("\\n%x:%u:from thread 3. waiting for semaphore",            |
|                                                                       |
| SEMAPHORE_SAMPLE_CURRENT_THREAD_ID,os_systime());                     |
|                                                                       |
| while(1)                                                              |
|                                                                       |
| {                                                                     |
|                                                                       |
| /\*If the value of the semaphore is greater than zero,                |
|                                                                       |
| decrement the counter and return zero; here the value of the          |
| semaphore is 1*/                                                      |
|                                                                       |
| ret = os_sem_wait_timeout(&my_sem,1000000);                           |
|                                                                       |
| if(ret)                                                               |
|                                                                       |
| {                                                                     |
|                                                                       |
| os_printf("\\n%x:%u:from thread 3. timedout. still waiting for        |
| semaphore. ret:%d",                                                   |
|                                                                       |
| SEMAPHORE_SAMPLE_CURRENT_THREAD_ID,os_systime(), ret);                |
|                                                                       |
| /\*based on the application requirement, application can decide       |
|                                                                       |
| whether to wait more or continue with 'could not lock' logic*/        |
|                                                                       |
| }                                                                     |
|                                                                       |
| else                                                                  |
|                                                                       |
| {                                                                     |
|                                                                       |
| os_printf("\\n%x:%u:from thread 3. got semaphore. ret:%d",            |
|                                                                       |
| SEMAPHORE_SAMPLE_CURRENT_THREAD_ID,os_systime(), ret);                |
|                                                                       |
| break;                                                                |
|                                                                       |
| }                                                                     |
|                                                                       |
| }                                                                     |
|                                                                       |
| os_printf("\\n%x:%u:from thread 3. releasing semaphore\\n",           |
|                                                                       |
| SEMAPHORE_SAMPLE_CURRENT_THREAD_ID,os_systime());                     |
|                                                                       |
| /\*releasing the semaphore*/                                          |
|                                                                       |
| os_sem_post(&my_sem );                                                |
|                                                                       |
| returnNULL; }                                                         |
+=======================================================================+
+-----------------------------------------------------------------------+

.. _running-the-application-3:

Running the Application 
~~~~~~~~~~~~~~~~~~~~~~~~

Program threads_semaphores.elf using the Download tool:

1. Launch the Download tool provided with InnoPhase Talaria TWO SDK.

2. In the GUI window:

   a. Boot Target: Select the appropriate EVK from the drop-down.

   b. ELF Input: Load the threads_semaphores.elf by clicking on Select
      ELF File.

   c. Programming: Prog RAM or Prog Flash as per requirement.

For more details on using the Download tool, refer to the document:
UG_Download_Tool.pdf (path: *sdk_x.y/pc_tools/Download_Tool/doc*).

**Note**: x and y refer to the SDK release version. For example:
sdk_2.4/doc.

.. _expected-output-3:

Expected Output
~~~~~~~~~~~~~~~

threads_semaphores.elf is created when compiling this code which gives
the following console output when programmed to Talaria TWO.

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
| Threads Semaphores Demo App                                           |
|                                                                       |
| bfb80:95336:from thread 1. doing initial tasks                        |
|                                                                       |
| b35e8:95382:from thread 2. waiting for semaphore                      |
|                                                                       |
| b3868:95543:from thread 3. waiting for semaphore                      |
|                                                                       |
| bfb80:1095384:from thread 1. Is any one waiting for sem:Yes           |
|                                                                       |
| bfb80:1095434:from thread 1. initial jobs done. now thread 2/3 can    |
| start. going to release the semaphore                                 |
|                                                                       |
| b35e8:1095504:from thread 2. got semaphore                            |
|                                                                       |
| b3868:1095593:from thread 3. timedout. still waiting for semaphore.   |
| ret:-1                                                                |
|                                                                       |
| b3868:2095658:from thread 3. timedout. still waiting for semaphore.   |
| ret:-1                                                                |
|                                                                       |
| b3868:3095723:from thread 3. timedout. still waiting for semaphore.   |
| ret:-1                                                                |
|                                                                       |
| b35e8:4095550:from thread 2. releasing semaphore                      |
|                                                                       |
| b3868:4095601:from thread 3. got semaphore. ret:0                     |
|                                                                       |
| b3868:4095647:from thread 3. releasing semaphore                      |
+=======================================================================+
+-----------------------------------------------------------------------+
