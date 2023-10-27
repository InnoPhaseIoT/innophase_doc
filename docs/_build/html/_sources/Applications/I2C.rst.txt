Introduction 
=============

This application note describes the usage of I2C on Talaria TWO using
sensors integrated in the EVB board.

I2C
===

Talaria TWO modules include I2C bus interface that can serve as an I2C
master or slave. The SCL and SDA lines can be individually programmed
for use on any GPIO. Internal pull-up resistors are available for
SCL/SDA on all GPIOs except for GPIO18.

**Note**: GPIO18 only has internal pull-down resistors.

.. table:: Table 1: I2C specifications

   +-----------------------------------+----------------------------------+
   | **I2C Specification**             | **Details**                      |
   +===================================+==================================+
   | Data Rates                        | 100Kbps, 400Kbps, 1Mbps          |
   +-----------------------------------+----------------------------------+
   | Address Modes                     | 7-bit, 10-bit                    |
   +-----------------------------------+----------------------------------+
   | Other Features                    | Send STOP at End                 |
   |                                   |                                  |
   |                                   | NOSTART Before Msg               |
   |                                   |                                  |
   |                                   | IGNORE NAK From Slave            |
   +-----------------------------------+----------------------------------+

I2C Sensors 
============

The INP301x board has the following sensors available on board for quick
prototyping/testing:

1. Temperature/Humidity (Sensirion SHTC3)

2. Pressure (Bosch BMP388)

3. Light (TI OPT3002)

|A picture containing text, electronics, circuit Description
automatically generated|

Figure : On-board I2C sensors

**Note :** To use the sensors on I2C bus the jumpers J7, J8 and pins 1 &
2 of J1 should be connected as shown in the picture below. This enables
the I2C clock, I2C data and power connection to the sensors on board.

|image1|

Figure 2: I2C sensor jumper connection

This application enables I2C supported sensors available on the EVB. It
measures and displays the real-time values of pressure, temperature,
humidity and light using the on-board sensors.

Source Code Walk-through
========================

Directory structure
-------------------

Figure 3: File directory tree

1. **i2c_sensor**: The i2c_sensor.c file present in this directory
   contains the logic to configure the i2c bus, read and display the
   readings from the sensors periodically.

2. **include**: contains header files with the structure variables,
   unions, and prototypes of the functions to initialize, read and write
   corresponding each of the sensors.

3. **sensor**:

   a. **bmp388**

..

   The bmp388.c file in this directory contains the function definitions
   to initialize, configure and read the data from bmp388 pressure
   sensor.

b. **callout_delay**

..

   It contains routines to generate delay in microsecond and milli
   seconds.

c. **dtoa**

..

   The dtoa.c file in this directory Contains functions for printing
   floating-point primitives.

d. **opt3002**

..

   The opt3002.c file in this directory contains function definitions to
   initialize, configure and read opt3002 Light to Digital Sensor.

e. **sensor.h**

..

   This header file contains structure definitions required to
   initialize and read the sensor readings.

f. **shtc1-4.1.0**

..

   The shtc1-4.1.0.c file in this directory contains function
   definitions for i2c abstraction layer and commonly shared code.

Application flow
----------------

In this application, Talaria TWO is programmed to enable I2C
communication with the sensors integrated in the EVB board. This
application read the on-board sensor readings and print it to the
console.

Following are the steps to achieve this as per the i2c_sensor.c:

1. This application creates a thread to initializes i2c bus.

2. Initializes the sensors available in EVB.

3. Reads the sensor ids from the sensors.

4. Starts fetching the readings from sensors.

5. Prints the sensor readings in console.

I2C APIs
--------

1. i2c_bus_init - Return a handle for the specified bus.

..

   This function is the first one to call when working with I2C devices.
   This call will initialize the bus driver and returns a handle for the
   new bus. The Talaria TWO device provides a single I2C interface,
   therefor the bus no must be set to 0.

2. i2c_acquire_bus() - Take ownership of the bus.

..

   Called to claim ownership of the I2C bus. If another thread is
   currently operating the bus, the function will block until the bus
   becomes available.

3. i2c_release_bus() - Release ownership of the bus.

..

   Not normally used since the i2c_transfer() function handles this. See
   rationale in i2c_acquire_bus().

4. i2c_create_device() - Create a new I2 C device on the specified bus.

..

   This function will create an object representing an I2C device
   attached to the specified bus. The device is specified using its
   address on this bus. The maximum frequency this device can handle is
   also specified in this call.

5. i2c_destroy_device() - Free an I2 C device.

..

   This function will release and free the resources claimed by a
   previously initialized i2c_device.

6. i2c_set_address() - Change the I2 C address for an i2c_device.

..

   Some devices require certain messages to be address to a different
   address (For example: while performing a device reset). This function
   will assist in temporarily changing the device address.

7. i2c_transfer()- Perform one I2 C transfer.

..

   An I2C transfer consists of several messages. Each message has a
   direction, READ (from slave to master) or WRITE (from master to
   slave). The msg parameter is a pointer to an array of messages and
   the len parameter specifies the number of messages that make up the
   transfer.

8. 

Source files
------------

i2c_sensor.c
~~~~~~~~~~~~

This section describes the sample application used to read the sensor
values over I2C. The sensor_app_init() creates a thread called
sensor_app_main that initializes the I2C bus. Sensors fetch the sensor
IDs, reads and prints the sensor data.

+-----------------------------------------------------------------------+
| app_thread = os_create_thread("app_thread", (void \*)                 |
| sensor_app_main,                                                      |
|                                                                       |
| NULL, APP_THREAD_PRIO, APP_THREAD_STACK_SIZE);                        |
|                                                                       |
| if( app_thread == NULL ){                                             |
|                                                                       |
| os_printf(" thread creation failed\\n");                              |
|                                                                       |
| return;                                                               |
|                                                                       |
| }                                                                     |
|                                                                       |
| os_join_thread(app_thread);                                           |
+=======================================================================+
+-----------------------------------------------------------------------+

osCreateThread routine initializes the given thread pointed to the
argument and puts the thread on an active queue. This app thread allows
the user to implement concurrent functions at the same time.

The sensor_app_main thread initiates the I2C bus by calling the init_i2c
thread post which it starts fetching the sensor ID and prints the
readings to the console.

init_i2c will initialize the bus driver after enabling the internal
pull-ups on SCL and SDA pins of Talaria TWO module. It routes the SCL
and SDA pins to the corresponding GPIOs.

+-----------------------------------------------------------------------+
| os_gpio_set_pull(GPIO_PIN(SCL_PIN) \| GPIO_PIN(SDA_PIN));             |
|                                                                       |
| os_gpio_mux_sel(GPIO_MUX_SEL_SCL, SCL_PIN);                           |
|                                                                       |
| os_gpio_mux_sel(GPIO_MUX_SEL_SDA, SDA_PIN);                           |
|                                                                       |
| return i2c_bus_init(0);                                               |
+=======================================================================+
+-----------------------------------------------------------------------+

It then begins to initialize the I2C bus with corresponding GPIO pins
after which it initiates the sensors by init_sensors().

+-----------------------------------------------------------------------+
| int rc;                                                               |
|                                                                       |
| struct i2c_bus \*bus = NULL;                                          |
|                                                                       |
| sensor_id_t ids = {};                                                 |
|                                                                       |
| bus = init_i2c();                                                     |
|                                                                       |
| init_sensors(bus);                                                    |
|                                                                       |
| get_sensor_ids(&ids);                                                 |
|                                                                       |
| print_sensor_ids(&ids);                                               |
|                                                                       |
| os_printf("\\n");                                                     |
|                                                                       |
| sensor_reading_t \*readings = NULL;                                   |
|                                                                       |
| readings = os_zalloc(sizeof(\*readings));                             |
+=======================================================================+
+-----------------------------------------------------------------------+

Sensor readings are read using the poll_sensors() function and is
printed on the console for every 2 seconds.

+-----------------------------------------------------------------------+
| poll_sensors(readings);                                               |
|                                                                       |
| print_sensor_readings(readings, 1);                                   |
|                                                                       |
| poll_sensors(readings);                                               |
|                                                                       |
| os_msleep(2000);                                                      |
+=======================================================================+
+-----------------------------------------------------------------------+

sensor.c 
~~~~~~~~~

init_sensors() contains all three sensors initialization part. All the
sensors are initiated from here by the following functions:

BMP388 (Pressure sensor) - bmp388_init() initiates the pressure sensor.

+-----------------------------------------------------------------------+
| bmp388_init(&pres_sen,&dev,bus,0x76);                                 |
+=======================================================================+
+-----------------------------------------------------------------------+

Opt3002 (Light sensor) - opt3002_init() initiates the light sensor.

+-----------------------------------------------------------------------+
| opt3002_init(&opt_sen, bus, 0x44);                                    |
+=======================================================================+
+-----------------------------------------------------------------------+

shtc3 (Temperature / Humidity sensor) - sensirion_i2c_init() initializes
the temp/hum sensor.

+-----------------------------------------------------------------------+
| sensirion_i2c_init(bus);                                              |
|                                                                       |
| shtc1_probe();                                                        |
|                                                                       |
| shtc1_enable_low_power_mode(1);                                       |
|                                                                       |
| #else                                                                 |
|                                                                       |
| sensirion_i2c_init(bus);                                              |
|                                                                       |
| shtc1_probe();                                                        |
|                                                                       |
| sensirion_i2c_release();                                              |
|                                                                       |
| #endif                                                                |
+=======================================================================+
+-----------------------------------------------------------------------+

In the humidity sensor also there is a need to implement the mode of
operation. shtc1_probe() enables or disables sleep in the driver based
on product code and will put the device in sleep mode if supported.

The get_sensor_ids() function reads the sensor IDs from each of the
sensor.

BMP388 (Pressure sensor) - The bmp3_get_device_ID () API reads the
device ID of bmp388 pressure sensor. The mode is set using
set_normal_mode().

+-----------------------------------------------------------------------+
| ids->bmp388_id = bmp3_get_device_ID(&dev);                            |
|                                                                       |
| set_normal_mode(&dev);                                                |
+=======================================================================+
+-----------------------------------------------------------------------+

Opt3002 (Light sensor) - The opt3002_readManufacturerID() reads the
manufacturing ID of light sensor.

+-----------------------------------------------------------------------+
| ids->opt3002_id = opt3002_readManufacturerID(&opt_sen);               |
+=======================================================================+
+-----------------------------------------------------------------------+

shtc3 (Temperature / Humidity sensor) - The shtc1_read_serial() API
reads the sensor id of shtc3 sensor.

+-----------------------------------------------------------------------+
| ids->shtc3_serial = 0;                                                |
|                                                                       |
| shtc1_read_serial(&ids->shtc3_serial);                                |
+=======================================================================+
+-----------------------------------------------------------------------+

Poll_sensor() function reads the sensor readings of all three sensors.

The get_sensor_data()reads the sensor data. The temperature and pressure
value of sensors are assigned to temp_bmp and pressure variables of this
structure sensor_reading_t readings.

+-----------------------------------------------------------------------+
| reading->pressure = 0;                                                |
|                                                                       |
| reading->temp_bmp = 0;                                                |
|                                                                       |
| /\* Read pressure and temperature recorded by bmp388 \*/              |
|                                                                       |
| float \*sensor_data;                                                  |
|                                                                       |
| sensor_data = get_sensor_data(&dev);                                  |
|                                                                       |
| reading->temp_bmp = (sensor_data[0]/100);                             |
|                                                                       |
| reading->pressure = (sensor_data[1]/100);                             |
+=======================================================================+
+-----------------------------------------------------------------------+

The opt_config_trigger assigns the sensor mode, conversion time and
latch operation. The opt3002_config_t opt_config_read() function reads
the raw data. The Memset() function stores the light sensor data in a
memory.

+-----------------------------------------------------------------------+
| opt3002_config_t opt_config_trigger = {                               |
|                                                                       |
| .RangeNumber = 0xC, // Automatic full-scale mode                      |
|                                                                       |
| .ConversionTime = 0, // 100 ms conversion time                        |
|                                                                       |
| .ModeOfConversionOperation = 0x1, // Single-shot mode                 |
|                                                                       |
| .Latch = 0x1 // Latched operation                                     |
|                                                                       |
| };                                                                    |
|                                                                       |
| opt3002_config_t opt_config_read = {.rawData = 0};                    |
|                                                                       |
| memset(&reading->light, 0, sizeof(reading->light));                   |
|                                                                       |
| opt3002_writeConfig(&opt_sen, opt_config_trigger);                    |
|                                                                       |
| callout_delay_ms(100);                                                |
|                                                                       |
| do                                                                    |
|                                                                       |
| { opt_config_read = opt3002_readConfig(&opt_sen);                     |
|                                                                       |
| }                                                                     |
|                                                                       |
| while(!opt_config_read.ConversionReady);                              |
|                                                                       |
| reading->light = opt3002_readResult(&opt_sen);                        |
+=======================================================================+
+-----------------------------------------------------------------------+

Opt3002_write_config() triggers the reading of sensor data. The sensor
reading is assigned to the light member.

The function initiates the humidity and temperature of shtc3 sensor and
shtc1_measure_blocking_read reads the sensor temperature and humidity
readings. The sensor readings are assigned to the humidity and temp_shtc
members.

+-----------------------------------------------------------------------+
| int32_t humidity_x1000 = 0, temp_shtc_x1000 = 0;                      |
|                                                                       |
| shtc1_measure_blocking_read(&temp_shtc_x1000, &humidity_x1000);       |
|                                                                       |
| reading->humidity = humidity_x1000 / 1000.0;                          |
|                                                                       |
| reading->temp_shtc = temp_shtc_x1000 / 1000.0;                        |
+=======================================================================+
+-----------------------------------------------------------------------+

Also, the printing functions are here to print the readings of the
sensors to the console.

callout_delay.c
~~~~~~~~~~~~~~~

The callout_delay.c file contains the routines to generate the delay in
milliseconds and microseconds.

bmp388.c (Pressure sensor)
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Configuring the sensor**

To configure the pressure sensor, select the power mode and sensor
setting. In addition to this, output data rate and oversampling settings
for pressure and temperature are selected using the following function:

**Note**: Here, BMP3_NO_OVERSAMPLING is selected, and the mode of
operation is chosen to be normal.

+-----------------------------------------------------------------------+
| int8_t set_normal_mode(struct bmp3_dev \*dev)                         |
+=======================================================================+
+-----------------------------------------------------------------------+

Enable the pressure and temperature sensor:

+-----------------------------------------------------------------------+
| dev->settings.press_en = BMP3_ENABLE;                                 |
|                                                                       |
| dev->settings.temp_en = BMP3_ENABLE;                                  |
+=======================================================================+
+-----------------------------------------------------------------------+

Select the output data rate and oversampling settings for pressure and
temperature:

+-----------------------------------------------------------------------+
| dev->settings.odr_filter.press_os = BMP3_NO_OVERSAMPLING;             |
|                                                                       |
| dev->settings.odr_filter.temp_os = BMP3_NO_OVERSAMPLING;              |
|                                                                       |
| dev->settings.odr_filter.odr = BMP3_ODR_200_HZ;                       |
+=======================================================================+
+-----------------------------------------------------------------------+

Set the power mode to normal:

+-----------------------------------------------------------------------+
| ev->settings.op_mode = BMP3_NORMAL_MODE;                              |
|                                                                       |
| rslt = bmp3_set_op_mode(dev);                                         |
+=======================================================================+
+-----------------------------------------------------------------------+

**Initialize the sensor**

To initiate the sensor, select the digital interface as I2C and instance
is created of the structure bpm388 by bmp388_init(). Read and write
instances are also created inside this function.

+-----------------------------------------------------------------------+
| bmp388->dev = i2c_create_device(bus, address, I2C_CLK_400K);          |
|                                                                       |
| dev->dev_id = bmp388->dev;                                            |
|                                                                       |
| dev->intf = BMP3_I2C_INTF;                                            |
|                                                                       |
| dev->read = bmp3_read_data;                                           |
|                                                                       |
| dev->write = bmp3_write_data;                                         |
|                                                                       |
| dev->delay_ms = callout_delay_ms;                                     |
|                                                                       |
| bmp3_init(dev);                                                       |
+=======================================================================+
+-----------------------------------------------------------------------+

**Reading sensor data**

To read the sensor data, create a readData()function. This defines the
length, flag, and data fields of the sensor. This function read sensor
data and store it in a buffer.

+-----------------------------------------------------------------------+
| uint8_t buf[1];                                                       |
|                                                                       |
| int ret = 0;                                                          |
|                                                                       |
| uint16_t length = 0;                                                  |
|                                                                       |
| while(length < len){                                                  |
|                                                                       |
| if((ret = read_reg(dev_id, buf, 1))){                                 |
|                                                                       |
| os_printf("I2C read error");                                          |
|                                                                       |
| return ret;                                                           |
|                                                                       |
| }                                                                     |
|                                                                       |
| data[length] = \*buf;                                                 |
|                                                                       |
| length++;                                                             |
|                                                                       |
| }                                                                     |
|                                                                       |
| return ret;                                                           |
+=======================================================================+
+-----------------------------------------------------------------------+

This executes read transaction on the I2C. The function reads I2C data
and stores it in buffer. It reads a given number of bytes. If the device
does not acknowledge the read command, an error will be returned. To
read I2C data, initialize read_reg()function. This permits reading of
the I2C data and storing it in msg. This function will be reading the
I2C data.

+-----------------------------------------------------------------------+
| struct i2c_msg msg;                                                   |
|                                                                       |
| int i2c_result = 0;                                                   |
|                                                                       |
| if( !dev_id){                                                         |
|                                                                       |
| os_printf("no device\\n");                                            |
|                                                                       |
| return -ENODEV;                                                       |
|                                                                       |
| }                                                                     |
|                                                                       |
| msg.im_len = count;                                                   |
|                                                                       |
| msg.im_flags = I2C_M_RD \| I2C_M_STOP;                                |
|                                                                       |
| msg.im_buf = data;                                                    |
|                                                                       |
| if ((i2c_result = i2c_transfer(dev_id, &msg, 1))){                    |
|                                                                       |
| os_printf("bmp388 i2c read error %d: %s\\n", i2c_result,              |
| strerror(-i2c_result));                                               |
|                                                                       |
| }                                                                     |
|                                                                       |
| return i2c_result;                                                    |
+=======================================================================+
+-----------------------------------------------------------------------+

**Writing sensor data**

To write the sensor data, create writeData()instance. This defines the
length, flag, and data fields of the sensor. This function writes the
command data on a register.

+-----------------------------------------------------------------------+
| uint8_t command_byte = command;                                       |
|                                                                       |
| write_reg( dev_id,&command_byte, 1);                                  |
|                                                                       |
| return 0;                                                             |
+=======================================================================+
+-----------------------------------------------------------------------+

This permits writing of I2C data in msg buffer. The write_reg()function
reads the I2C data and stores it in msg buffer. This executes write
transaction on the I2C bus, which sends a given number of bytes. The
bytes in the supplied buffer must be sent to the given address. If the
slave device does not acknowledge any of the bytes, an error will be
returned.

+-----------------------------------------------------------------------+
| struct i2c_msg msg;                                                   |
|                                                                       |
| int i2c_result = 0;                                                   |
|                                                                       |
| if( !dev_id){                                                         |
|                                                                       |
| os_printf("no device\\n");                                            |
|                                                                       |
| return -ENODEV;                                                       |
|                                                                       |
| }                                                                     |
|                                                                       |
| msg.im_len = count;                                                   |
|                                                                       |
| msg.im_flags = I2C_M_STOP;                                            |
|                                                                       |
| msg.im_buf = data;                                                    |
|                                                                       |
| if ((i2c_result = i2c_transfer(dev_id, &msg, 1))){                    |
|                                                                       |
| os_printf("bmp388 i2c write error in write reg %d: %s\\n",            |
| i2c_result, strerror(-i2c_result));                                   |
|                                                                       |
| }                                                                     |
|                                                                       |
| return i2c_result;                                                    |
+=======================================================================+
+-----------------------------------------------------------------------+

 Opt3002.c (Optical sensor)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Initializing the sensor**

To initialize the sensor, select the digital interface as I2C and create
an instance of structure:

opt3002_init() function enables the I2C device, clock signals with
frequency of 400khz.

+-----------------------------------------------------------------------+
| opt3002->dev = i2c_create_device(bus, address, I2C_CLK_400K).         |
+=======================================================================+
+-----------------------------------------------------------------------+

The function readManufacturerID()reads the manufacturing ID of the
device. This reads the manufacturing ID. If sensor is detected, the
opt3002_write data exports the manufacturing ID.

+-----------------------------------------------------------------------+
| uint16_t result = 0;                                                  |
|                                                                       |
| int error = opt3002_writeData(opt3002, MANUFACTURER_ID);              |
|                                                                       |
| if (!error)                                                           |
|                                                                       |
| error = opt3002_readData(opt3002, &result);                           |
|                                                                       |
| return result;                                                        |
+=======================================================================+
+-----------------------------------------------------------------------+

This enables the configuration of the read and write functions of
optical sensor opt3002. The function pt3002_readConfig()defines the
configuration of reading.

+-----------------------------------------------------------------------+
| opt3002_config_t config = {.rawData = 0};                             |
|                                                                       |
| int error = opt3002_writeData(opt3002, CONFIG);                       |
|                                                                       |
| if (!error)                                                           |
|                                                                       |
| error = opt3002_readData(opt3002, &config.rawData);                   |
|                                                                       |
| return config;                                                        |
+=======================================================================+
+-----------------------------------------------------------------------+

The opt3001_i2c_write writes the configuration of opt3002 sensor.

+-----------------------------------------------------------------------+
| uint8_t buf[3] = {CONFIG, config.rawData >> 8, config.rawData &       |
| 0x00FF};                                                              |
|                                                                       |
| return opt3002_i2c_write(opt3002, buf, ARRAY_SIZE(buf));              |
+=======================================================================+
+-----------------------------------------------------------------------+

Post initiating, read and write instances are created to read sensor
data stored in buffer and sent to the I2C bus. The following function
reads data from opt3002 to the I2C bus. The function opt3002_light_t
opt3002_readRegister()reads data from sensor in a raw format and makes
the required calculations by using formula:

+-----------------------------------------------------------------------+
| (lux = (1.2)*(powr(2, er.Exponent)*er.Result))                        |
+=======================================================================+
+-----------------------------------------------------------------------+

The calculated data value will be stored lux variable.

+-----------------------------------------------------------------------+
| int error = opt3002_writeData(opt3002, command);                      |
|                                                                       |
| if (!error) {                                                         |
|                                                                       |
| opt3002_light_t result;                                               |
|                                                                       |
| result.lux = 0;                                                       |
|                                                                       |
| result.raw.rawData = 0;                                               |
|                                                                       |
| result.error = 0;                                                     |
|                                                                       |
| opt3002_ER_t er;                                                      |
|                                                                       |
| error = opt3002_readData(opt3002, &er.rawData);                       |
|                                                                       |
| if (!error) {                                                         |
|                                                                       |
| result.raw = er;                                                      |
|                                                                       |
| if(!raw){                                                             |
|                                                                       |
| result.lux = (1.2)*(powr(2, er.Exponent)*er.Result);                  |
|                                                                       |
| }                                                                     |
|                                                                       |
| }                                                                     |
|                                                                       |
| else {                                                                |
|                                                                       |
| result.error = error;                                                 |
|                                                                       |
| }                                                                     |
|                                                                       |
| return result;                                                        |
|                                                                       |
| }                                                                     |
|                                                                       |
| else {                                                                |
|                                                                       |
| return opt3002_returnError(error);}                                   |
+=======================================================================+
+-----------------------------------------------------------------------+

**Reading sensor data**

The opt3002_i2c_readData()function executes the read transaction on the
I2C bus, reads data from the sensor through I2C and stores it in buffer.
If the device does not acknowledge the read command, an error will be
returned.

+-----------------------------------------------------------------------+
| struct i2c_msg msg;                                                   |
|                                                                       |
| int i2c_result = 0;                                                   |
|                                                                       |
| if(!opt3002 \|\| !opt3002->dev)                                       |
|                                                                       |
| return -ENODEV;                                                       |
|                                                                       |
| msg.im_len = count;                                                   |
|                                                                       |
| msg.im_flags = I2C_M_RD \| I2C_M_STOP;                                |
|                                                                       |
| msg.im_buf = data;                                                    |
|                                                                       |
| if((i2c_result = i2c_transfer(opt3002->dev, &msg, 1)))                |
|                                                                       |
| os_printf("opt3002 i2c read error %d: %s\\n", i2c_result,             |
| strerror(-i2c_result));                                               |
|                                                                       |
| return i2c_result;                                                    |
+=======================================================================+
+-----------------------------------------------------------------------+

The opt3002_readData() reads the sensor data and OPT3002 transmits data
in Big-Endian format.

+-----------------------------------------------------------------------+
| uint8_t buf[2];                                                       |
|                                                                       |
| int ret = 0;                                                          |
|                                                                       |
| if((ret = opt3002_i2c_read(opt3002, buf, 2)))                         |
|                                                                       |
| return ret;                                                           |
|                                                                       |
| \*data = (buf[0] << 8) \| buf[1];                                     |
|                                                                       |
| return ret;                                                           |
+=======================================================================+
+-----------------------------------------------------------------------+

**Writing sensor data**

The opt3002_writeData() writes the command data to the I2C.

+-----------------------------------------------------------------------+
| return opt3002_i2c_write(opt3002, &command_byte, 1);                  |
+=======================================================================+
+-----------------------------------------------------------------------+

The int opt3002_i2c_write() executes write transaction on the I2C bus
and sends a given number of bytes. The bytes in the supplied buffer must
be sent to the given address. If the slave device does not acknowledge
any of the bytes, an error will be returned.

+-----------------------------------------------------------------------+
| struct i2c_msg msg;                                                   |
|                                                                       |
| int i2c_result = 0;                                                   |
|                                                                       |
| if(!opt3002 \|\| !opt3002->dev)                                       |
|                                                                       |
| return -ENODEV;                                                       |
|                                                                       |
| msg.im_len = count;                                                   |
|                                                                       |
| msg.im_flags = I2C_M_STOP;                                            |
|                                                                       |
| msg.im_buf = data;                                                    |
|                                                                       |
| if((i2c_result = i2c_transfer(opt3002->dev, &msg, 1)))                |
|                                                                       |
| os_printf("opt3002 i2c write error %d: %s\\n", i2c_result,            |
| strerror(-i2c_result));                                               |
|                                                                       |
| return i2c_result;                                                    |
+=======================================================================+
+-----------------------------------------------------------------------+

sensirion_hw_i2c_implementation.c (Temperature/Humidity)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The sensirion_hw_i2c_implementation.c contains the routines required to
perform the I2C initialization, read and write operations of Sensirion
temperature/humidity sensor.

The i2c_create_device() function creates the I2C device with the clock
frequency of 400KHz. The sensirion_i2c_init()initializes all hardware
and software components of the Sensirion for I2C.

+-----------------------------------------------------------------------+
| dev = i2c_create_device(bus, SHTC1_ADDRESS, I2C_CLK_400K);            |
+=======================================================================+
+-----------------------------------------------------------------------+

It executes one read transaction on the I2C bus through the function
sensirion_i2c_read(), which reads a given number of bytes. If the device
does not acknowledge the read command, an error will be returned.

+-----------------------------------------------------------------------+
| struct i2c_msg msg;                                                   |
|                                                                       |
| int i2c_result = 0;                                                   |
|                                                                       |
| if(!dev)                                                              |
|                                                                       |
| return -ENODEV;                                                       |
|                                                                       |
| msg.im_len = count;                                                   |
|                                                                       |
| msg.im_flags = I2C_M_RD \| I2C_M_STOP;                                |
|                                                                       |
| msg.im_buf = data;                                                    |
|                                                                       |
| i2c_set_address(dev, address);                                        |
|                                                                       |
| if((i2c_result = i2c_transfer(dev, &msg, 1)))                         |
|                                                                       |
| os_printf("shtc3 i2c read error %d: %s\\n", i2c_result,               |
| strerror(-i2c_result));                                               |
|                                                                       |
| return i2c_result;                                                    |
+=======================================================================+
+-----------------------------------------------------------------------+

The sensirion_i2c_write()executes one write transaction on the I2C bus
which sends a given number of bytes. The bytes in the supplied buffer
must be sent to the given address. If the slave device does not
acknowledge any of the bytes, an error will be returned.

+-----------------------------------------------------------------------+
| struct i2c_msg msg;                                                   |
|                                                                       |
| int i2c_result = 0;                                                   |
|                                                                       |
| if(!dev)                                                              |
|                                                                       |
| return -ENODEV;                                                       |
|                                                                       |
| msg.im_len = count;                                                   |
|                                                                       |
| msg.im_flags = I2C_M_STOP;                                            |
|                                                                       |
| msg.im_buf = (uint8_t\*)data; /\* Data pointed to won't be modified   |
| \*/                                                                   |
|                                                                       |
| i2c_set_address(dev, address);                                        |
|                                                                       |
| if((i2c_result = i2c_transfer(dev, &msg, 1)))                         |
|                                                                       |
| os_printf("shtc3 i2c write error %d: %s\\n", i2c_result,              |
| strerror(-i2c_result));                                               |
|                                                                       |
| return i2c_result;                                                    |
+=======================================================================+
+-----------------------------------------------------------------------+

Shtc1.c (Temperature/Humidity)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The SHTC3 Humidity and Temperature Sensor from Sensirion is a highly
accurate digital humidity and temperature sensor that communicates using
the I2C protocol.

**Note**: SHTC1 compatible sensors: SHTW1, SHTW2, SHTC3.

**Configuring mode of operation**

The SHTC3 provides a low power measurement mode with a specific set of
commands. Using the low power mode significantly shortens the
measurement duration and thus minimizes the energy consumption per
measurement. The following functions define the power mode of the shtc3.
Low power mode is being implemented here.

To initiate the measurement, the following function is created:

+-----------------------------------------------------------------------+
| shtc1_measure(void)                                                   |
+=======================================================================+
+-----------------------------------------------------------------------+

This is meant to awaken the sensor from sleep mode, begin measuring the
sensor data and write the data through I2C.

Function shtc1_measure() starts a measurement in high precision mode.
Use shtc1_read() to read out the values once the measurement is done.
The duration of the measurement depends on the sensor in use. Refer
datasheet for more details.

+-----------------------------------------------------------------------+
| int16_t ret;                                                          |
|                                                                       |
| return PM_WAKE(ret,sensirion_i2c_write_cmd(SHTC1_ADDRESS,             |
| shtc1_cmd_measure));                                                  |
+=======================================================================+
+-----------------------------------------------------------------------+

Function shtc1_probe()detects if a sensor is connected by reading out
the ID register. If the sensor does not answer or if the answer is not
the expected value, the function returns error. If the sensor is
detected, 0 is returned.

+-----------------------------------------------------------------------+
| uint16_t id;                                                          |
|                                                                       |
| int16_t ret;                                                          |
|                                                                       |
| supports_sleep = 1;                                                   |
|                                                                       |
| sleep_enabled = 1;                                                    |
|                                                                       |
| (void)shtc1_wakeup();                                                 |
|                                                                       |
| ret= sensirion_i2c_delayed_read_cmd(SHTC1_ADDRESS,                    |
| SHTC1_CMD_READ_ID_REG,                                                |
|                                                                       |
| SHTC1_CMD_DURATION_USEC, &id, 1);                                     |
|                                                                       |
| if (ret)                                                              |
|                                                                       |
| return ret;                                                           |
|                                                                       |
| if ((id & SHTC3_PRODUCT_CODE_MASK) == SHTC3_PRODUCT_CODE)             |
|                                                                       |
| return shtc1_sleep();                                                 |
|                                                                       |
| if ((id & SHTC1_PRODUCT_CODE_MASK) == SHTC1_PRODUCT_CODE) {           |
|                                                                       |
| supports_sleep = 0;                                                   |
|                                                                       |
| return STATUS_OK;                                                     |
|                                                                       |
| }                                                                     |
|                                                                       |
| return STATUS_UNKNOWN_DEVICE;                                         |
+=======================================================================+
+-----------------------------------------------------------------------+

Function shtc1_measure_blocking_read() starts reading the sensor data.
This function blocks while the measurement is in progress. Temperature
is returned in [°C], multiplied by 1000 and relative humidity in
[percent relative humidity], multiplied by 1000.

+-----------------------------------------------------------------------+
| int16_t ret;                                                          |
|                                                                       |
| PM_WAKE(ret, shtc1_measure());                                        |
|                                                                       |
| #if !defined(USE_SENSIRION_CLOCK_STRETCHING) \|\|                     |
| !USE_SENSIRION_CLOCK_STRETCHING                                       |
|                                                                       |
| sensirion_sleep_usec(SHTC1_MEASUREMENT_DURATION_USEC);                |
|                                                                       |
| #endif                                                                |
|                                                                       |
| /\* USE_SENSIRION_CLOCK_STRETCHING \*/                                |
|                                                                       |
| ret = shtc1_read(temperature, humidity);                              |
|                                                                       |
| return PM_SLEEP(ret);                                                 |
+=======================================================================+
+-----------------------------------------------------------------------+

**Reading the sensor data**

To read the sensor data, the function shtc1_read() is used . It reads
the sensor data and calculates temperature (Temperature = 175 \* S_T /
2^16 – 45), humidity (Relative Humidity = 100 \* S_RH / 2^16) using the
formulae. It reads out the results of a measurement that was previously
started by shtc1_measure(). If the measurement is still in progress,
this function returns an error. Temperature is returned in [°C],
multiplied by 1000, and relative humidity [in percent relative
humidity], multiplied by 1000.

+-----------------------------------------------------------------------+
| uint16_t words[2];                                                    |
|                                                                       |
| int16_t ret = sensirion_i2c_read_words(SHTC1_ADDRESS, words,          |
|                                                                       |
| SENSIRION_NUM_WORDS(words));                                          |
|                                                                       |
| \*temperature = ((21875 \* (int32_t)words[0]) >> 13) - 45000;         |
|                                                                       |
| \*humidity = ((12500 \* (int32_t)words[1]) >> 13);                    |
|                                                                       |
| return PM_SLEEP(ret);                                                 |
+=======================================================================+
+-----------------------------------------------------------------------+

The function shtc1_disable_sleep()enables or disables the SHT's sleep
mode between measurements, if supported. Sleep mode is enabled by
default if supported.

+-----------------------------------------------------------------------+
| if (!supports_sleep)                                                  |
|                                                                       |
| return STATUS_FAIL;                                                   |
|                                                                       |
| sleep_enabled = !disable_sleep;                                       |
|                                                                       |
| if (disable_sleep)                                                    |
|                                                                       |
| return shtc1_wakeup();                                                |
|                                                                       |
| return shtc1_sleep();                                                 |
+=======================================================================+
+-----------------------------------------------------------------------+

Enable or disable the SHT's low power mode.

+-----------------------------------------------------------------------+
| shtc1_cmd_measure =enable_low_power_mode ? SHTC1_CMD_MEASURE_LPM :    |
| SHTC1_CMD_MEASURE_HPM;                                                |
+=======================================================================+
+-----------------------------------------------------------------------+

The function shtc1_read_serial() is implemented to read out the serial
number.

+-----------------------------------------------------------------------+
| int16_t shtc1_read_serial(uint32_t \*serial)                          |
+=======================================================================+
+-----------------------------------------------------------------------+

Building 
=========

To build the sample application, execute the following commands:

+-----------------------------------------------------------------------+
| cd examples/i2c                                                       |
|                                                                       |
| make                                                                  |
+=======================================================================+
+-----------------------------------------------------------------------+

The make command generates the i2c_sensor.elf in the out directory.

Running the Application 
========================

Programming Talaria TWO device using the Download tool 
-------------------------------------------------------

Program i2c_sensor.elf (sdk_x.y\\examples\\i2c\\bin) using the Download
tool:

1. Launch the Download tool provided with InnoPhase Talaria TWO SDK.

2. In the GUI window:

   a. Boot Target: Select the appropriate EVK from the drop-down.

   b. ELF Input: Load the i2c_sensor.elf by clicking on Select ELF File.

   c. Programming: Prog RAM or Prog Flash as per requirement.

For more details on using the Download tool, refer to the document:
UG_Download_Tool.pdf (path: *sdk_x.y/pc_tools/Download_Tool/doc*).

**Note**: x and y refer to the SDK release version. For example:
sdk_2.4/doc.

Expected Output
---------------

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
| FLASH:PNWWWAEBuild $Id: git-58a17ea8a $                               |
|                                                                       |
| Initializing bmp388...                                                |
|                                                                       |
| Initializing opt3002...                                               |
|                                                                       |
| Initializing shtc3...                                                 |
|                                                                       |
| bmp388 ID: 0x50                                                       |
|                                                                       |
| opt3002 ID: 0x5449                                                    |
|                                                                       |
| shtc3 ID: 0x5CDE0125                                                  |
|                                                                       |
| -----Timestamp: 112061 uS-----                                        |
|                                                                       |
| Pressure: 90905.2 Pa                                                  |
|                                                                       |
| Temperature (bmp): 33.6 C                                             |
|                                                                       |
| Optical power: 25152.0 nW/cm2                                         |
|                                                                       |
| Humidity: 22.9 %                                                      |
|                                                                       |
| Temperature (shtc): 34.2 C                                            |
|                                                                       |
| -----Timestamp: 2375522 uS-----                                       |
|                                                                       |
| Pressure: 90907.5 Pa                                                  |
|                                                                       |
| Temperature (bmp): 33.8 C                                             |
|                                                                       |
| Optical power: 25344.0 nW/cm2                                         |
|                                                                       |
| Humidity: 23.0 %                                                      |
|                                                                       |
| Temperature (shtc): 34.2 C                                            |
|                                                                       |
| -----Timestamp: 4636257 uS-----                                       |
|                                                                       |
| Pressure: 90906.5 Pa                                                  |
|                                                                       |
| Temperature (bmp): 33.8 C                                             |
|                                                                       |
| Optical power: 25382.4 nW/cm2                                         |
|                                                                       |
| Humidity: 22.9 %                                                      |
|                                                                       |
| Temperature (shtc): 34.2 C                                            |
|                                                                       |
| -----Timestamp: 6896980 uS-----                                       |
|                                                                       |
| Pressure: 90909.3 Pa                                                  |
|                                                                       |
| Temperature (bmp): 33.8 C                                             |
|                                                                       |
| Optical power: 25267.2 nW/cm2                                         |
|                                                                       |
| Humidity: 22.8 %                                                      |
|                                                                       |
| Temperature (shtc): 34.4 C                                            |
+=======================================================================+
+-----------------------------------------------------------------------+

.. |A picture containing text, electronics, circuit Description automatically generated| image:: media/image1.jpeg
   :width: 5.90551in
   :height: 4.24709in
.. |image1| image:: media/image2.jpeg
   :width: 3.93661in
   :height: 5.46339in
