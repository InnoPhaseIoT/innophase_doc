HAPI Configuration APIs 
~~~~~~~~~~~~~~~~~~~~~~~~

hapi_malloc 
^^^^^^^^^^^^

Allocates memory on HAPI.

+-----------------------------------------------------------------------+
| static inline void \* hapi_malloc(size_t size)                        |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. size: Specified memory size.

Return: Pointer to the allocated memory or NULL if the request fails.

hapi_sem_init 
^^^^^^^^^^^^^^

Initializes the mentioned semaphore.

+-----------------------------------------------------------------------+
| static inline void hapi_sem_init(hapi_sem_t \*sem, int value)         |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. sem: Initialized semaphore.

2. value: Value of the initialized semaphore.

Return: NULL.

hapi_sem_wait 
^^^^^^^^^^^^^^

Holds the referenced semaphore by performing the semaphore lock
operation.

+-----------------------------------------------------------------------+
| static inline void hapi_sem_wait(hapi_sem_t \*sem)                    |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. sem: Initialized semaphore.

Return: NULL.

hapi_sem_wait_timeout 
^^^^^^^^^^^^^^^^^^^^^^

Holds the referenced semaphore by performing the semaphore lock
operation. This wait is terminated when the specified timeout expires.

+-----------------------------------------------------------------------+
| static inline void hapi_sem_wait_timeout(hapi_sem_t \*sem,uint32_t    |
| timeout_msec))                                                        |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. sem: Initialized semaphore.

2. timeout_msec: Time specified for timeout.

Return: NULL.

hapi_sem_post 
^^^^^^^^^^^^^^

Unlocks the specified semaphore.

+-----------------------------------------------------------------------+
| static inline void hapi_sem_post(hapi_sem_t \*sem)                    |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. sem: Initialized semaphore.

Return: NULL.
