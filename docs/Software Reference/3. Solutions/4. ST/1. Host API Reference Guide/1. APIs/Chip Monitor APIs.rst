.. _st api chip-monitor:

Chip Monitor APIs
~~~~~~~~~~~~~~~~~

hapi_chip_mon_power_init
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: shell

      bool hapi_chip_mon_power_init(struct hapi *hapi)

Arguments:

1. hapi: HAPI instance pointer.

Return: True=Success, False=Failure.

hapi_chip_mon_start
^^^^^^^^^^^^^^^^^^^

.. code:: shell

      bool hapi_chip_mon_start(struct hapi *hapi ,uint32_t source ,uint32_t interval ,uint32_t last_sample ,uint32_t threshold)


Arguments:

1. hapi: HAPI instance pointer.

2. source: Select chip monitor services

   a. 0: CoreTemp

   b. 1: VBAT, 2:ADC

   c. 3:power(uA)

3. interval: Time interval in seconds for measuring the value of the
   subscribed chip.

4. last_sample: Last sample value measured. This value gets updated
   every time the measurement is made.

5. threshold: Threshold value to trigger the registered callback for a
   subscribed service.

Return: True=Success, False=Failure.

hapi_chip_mon_stop
^^^^^^^^^^^^^^^^^^

.. code:: shell

      bool hapi_chip_mon_stop(struct hapi *hapi ,uint32_t source)


Arguments:

1. hapi: HAPI instance pointer.

2. source: Select chip monitor services

   a. 0: CoreTemp

   b. 1: VBAT, 2:ADC

   c. 3:power(uA)

Return: True=Success, False=Failure.

hapi_chip_mon_trig
^^^^^^^^^^^^^^^^^^

.. code:: shell

      bool hapi_chip_mon_trig(struct hapi *hapi ,uint32_t source)


Arguments:

1. hapi: HAPI instance pointer.

2. source: Select chip monitor services

   a. 0: CoreTemp

   b. 1: VBAT, 2:ADC

   c. 3:power(uA)

Return: True=Success, False=Failure.
