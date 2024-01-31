.. _3201 ex apps:


Dual-Stack solution is a hosted solution with Talaria TWO Wi-Fi module
which replaces normal Wi-Fi driver concept of Linux stack. This solution
is suitable for power consuming high performance host processor with
Linux as the operating system.

​This document includes custom application walkthroughs. Each application
uses a unique group ID to communicate with Talaria TWO and each
functionality within this group is identified by a unique message ID.

Following are the range for group IDs:

.. table:: Table 1: Group ID – range

   +-------------------------------------+--------------------------------+
   | **Group IDs**                       | **Usage**                      |
   +=====================================+================================+
   | 0-63                                | Firmware HIO groups            |
   +-------------------------------------+--------------------------------+
   | 65-127                              | Talaria TWO apps               |
   +-------------------------------------+--------------------------------+
   | 128-255                             | Custom                         |
   +-------------------------------------+--------------------------------+

This section contains example applications intended to demonstrate
Dual-Stack solution functionality. These applications can also be
customized using the source code available at:
*\\talaria_two_dual_stack\\talaria_two_dual_stack_vx.y\\host\\<host_platform>\\dual-stack\\dualstack_examples\\src\\*.

Following are the list of custom applications currently supported in the
Dual-Stack solution:

1. Custom GPIO Monitor

2. Custom Echo

3. Custom MQTT

4. Heartbeat Monitor

5. Custom FOS

6. Custom Network Test

7. Custom Wi-Fi Connection

8. PIR Monitor

Compilation of Dual-Stack Example Applications
----------------------------------------------

Prebuilt binaries for custom applications are available at:
*talaria_two_dual_stack_vx.y\\host\\<host_platform>\\dual-stack\\bins*.

**Note**: x and y in *vx.y* refers to the package release version.

In case any changes are made to the custom application, the binaries can
be clean compiled for a specific platform.

For example:

1. Browse the path
   *\\talaria_two_dual_stack\\talaria_two_dual_stack_vx.y\\host\\<host_platform>\\dual-stack\\*.

2. Refer build.mak file to get the correct platform name.

3. Build the application using make command.

.. code:: shell

      $ cd <PACKAGE>/host/<platform>/dual-stack/    
      $ make clean
      $ make platform=<host>_SDIO

Copy the compiled binaries to host using TFTP/SD card depending on
availability of the ethernet interface or SD card slot on host platform.

**Note:** Following are the prerequisites to execute the Dual-Stack
example application:

1. tunadapter should be running (. /tunadapter &)

2. Talaria TWO side ELF must support the custom groups

3. Serial terminal application such as GTKTerm can be used on the host
   to run the example application


Example applications
---------------------
.. toctree::
   :maxdepth: 2

   Custom Echo Application.rst
   Custom FOS Application.rst
   Custom GPIO Application.rst
   Custom MQTT Application.rst
   Custom Network Test Application.rst
   Heartbeat Monitor Application.rst
