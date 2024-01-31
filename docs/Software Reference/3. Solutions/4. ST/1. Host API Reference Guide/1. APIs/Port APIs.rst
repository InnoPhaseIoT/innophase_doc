Port APIs
~~~~~~~~~

These APIs provides basic read/write over the hardware interface
(SPI/UART) between the host and Talaria TWO where each API must be
defined for each port.

hapi_serial_open
^^^^^^^^^^^^^^^^

Initializes HAPI serial interface. This function initializes the serial
device and creates the HAPI interface. This is specific to each
platform. This function also registers the platform specific
read/write/close APIs to the HAPI interface.

+-----------------------------------------------------------------------+
| struct hapi \* hapi_serial_open(const char \*devname,int baudrate)    |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. devname: Pointer to HAPI serial device context.

2. Baudrate: SPI clock speed.

Return: HAPI context.

hapi_serial_write
^^^^^^^^^^^^^^^^^

Writes data to Talaria TWO over HAPI interface.

+-----------------------------------------------------------------------+
| ssize_t hapi_serial_write(void \*dev, const void \*data, size_t       |
| length)                                                               |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. dev: Pointer to interface device.

2. data: Source buffer address.

3. length: Number of bytes to be written.

Return: number of bytes written on Success else Error.

hapi_serial_read
^^^^^^^^^^^^^^^^

Reads data from Talaria TWO over HAPI interface.

+-----------------------------------------------------------------------+
| ssize_t hapi_serial_read(void \*dev, void \*data, size_t length)      |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. dev: Pointer to interface device.

2. data: Source buffer address.

3. length: Number of bytes to be read.

Return: number of bytes read. -1 on Error.

hapi_serial_close
^^^^^^^^^^^^^^^^^

Closes HAPI interface.

+-----------------------------------------------------------------------+
| void hapi_serial_close(void\* dev)                                    |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. dev: Pointer to the interface device.

Return: None.

hapi_serial_break
^^^^^^^^^^^^^^^^^

Used to wakeup Talaria TWO. Sends break to Talaria TWO.

+-----------------------------------------------------------------------+
| void hapi_serial_break(void \*dev, bool on)                           |
+=======================================================================+
+-----------------------------------------------------------------------+

Arguments:

1. dev: Pointer to the interface device.

2. on: Send break to Talaria TWO is this set to TRUE.

Return: None.
