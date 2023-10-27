VM versus Non VM based application
==================================

There are two types of application that could be generated based on the
virtual memory usage for executing the application on Talaria TWO:

1. **VM based application:**

In case of a VM based application, a portion of the flash memory is
allocated to be used as virtual memory. The application stored in
Talaria TWO’s FLASH/ROM is loaded into virtual memory for execution by
the MCU.

2. **Non-VM based application:**

In case of a Non-VM image, no virtual memory is allocated and the MCU
executes the application by directly fetching it from Talaria TWO’s
ROM/Flash.
