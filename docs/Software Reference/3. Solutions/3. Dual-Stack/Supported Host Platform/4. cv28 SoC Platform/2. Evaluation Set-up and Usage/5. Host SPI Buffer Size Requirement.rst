Host SPI Buffer Size Requirement
--------------------------------

The minimum Host SPI buffer size required is 16KB. Verify the buffer
size on the Host by issuing the following command:

+-----------------------------------------------------------------------+
| cat /sys/module/spidev/parameters/bufsiz                              |
+=======================================================================+
+-----------------------------------------------------------------------+

If the buffer size is less than 16384, it can be increased using the
following procedure:

1. Create a spidef.conf file:

+-----------------------------------------------------------------------+
| vi /etc/modprobe.d/spidev.conf                                        |
+=======================================================================+
+-----------------------------------------------------------------------+

2. Add this to the spidef.conf file:

+-----------------------------------------------------------------------+
| options spidev bufsiz=16384                                           |
+=======================================================================+
+-----------------------------------------------------------------------+

3. Reboot the Host.
