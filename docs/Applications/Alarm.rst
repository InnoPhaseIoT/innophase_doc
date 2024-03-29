Introduction
============

Alarm provides the mechanism to schedule activities for the future which
occur periodically or are executed at once. This application note
demonstrates the alarm functionality in Talaria TWO.

Relevant APIs
=============

alarm_init()
------------

Initializes the alarm.

+-----------------------------------------------------------------------+
| alarm_init();                                                         |
+=======================================================================+
+-----------------------------------------------------------------------+

alarm_set_time ()
-----------------

Sets the system time.

+-----------------------------------------------------------------------+
| alarm_set_time ();                                                    |
+=======================================================================+
+-----------------------------------------------------------------------+

sntp_setservername ()
---------------------

Initializes one of the NTP servers via the IP address of the Talaria TWO
module.

+-----------------------------------------------------------------------+
| sntp_setservername ();                                                |
+=======================================================================+
+-----------------------------------------------------------------------+

sntp_init() 
------------

Initializes the SNTP of the Talaria TWO module. It sends out a request
instantly or after sntp_startup_delay(func).

+-----------------------------------------------------------------------+
| sntp_init ();                                                         |
+=======================================================================+
+-----------------------------------------------------------------------+

sntp_stop ()
------------

Stops the Talaria TWO module.

+-----------------------------------------------------------------------+
| sntp_stop ();                                                         |
+=======================================================================+
+-----------------------------------------------------------------------+

uart_puts ()
------------

Writes a string to the serial port.

+-----------------------------------------------------------------------+
| uart_puts ();                                                         |
+=======================================================================+
+-----------------------------------------------------------------------+

uart_flush()
------------

Flushes the output buffer.

+-----------------------------------------------------------------------+
| uart_flush();                                                         |
+=======================================================================+
+-----------------------------------------------------------------------+

uart_close()
------------

Closes the serial port.

+-----------------------------------------------------------------------+
| uart_close();                                                         |
+=======================================================================+
+-----------------------------------------------------------------------+

uart_getchar()
--------------

Reads one character from the serial port.

+-----------------------------------------------------------------------+
| uart_getchar ();                                                      |
+=======================================================================+
+-----------------------------------------------------------------------+

uart_putchar()
--------------

Writes one character to the serial port.

+-----------------------------------------------------------------------+
| uart_putchar();                                                       |
+=======================================================================+
+-----------------------------------------------------------------------+

uart_set_event_callback()
-------------------------

Sets event callback.

+-----------------------------------------------------------------------+
| uart_set_event_callback();                                            |
+=======================================================================+
+-----------------------------------------------------------------------+

Code Walkthrough
================

Connecting to a Wi-Fi network
-----------------------------

To connect to a Wi-Fi network, wcm_create()API from the Wi-Fi Connection
Manager are used. Initially, the Wi-Fi network interface is created
using wcm_create().

+-----------------------------------------------------------------------+
| h = wcm_create(NULL);                                                 |
+=======================================================================+
+-----------------------------------------------------------------------+

..

   wcm_connect_to_network()reads the configurations and connects to
   network.

+-----------------------------------------------------------------------+
| rval = wifi_connect_to_network(&h, WCM_CONN_WAIT_INFINITE,            |
| &wcm_connect_success);                                                |
|                                                                       |
| if(rval < 0) {                                                        |
|                                                                       |
| os_printf("\\nError: Unable to connect to network\\n");               |
|                                                                       |
| return 0;                                                             |
|                                                                       |
| }                                                                     |
+=======================================================================+
+-----------------------------------------------------------------------+

Validating Date
---------------

validdate_date() validates the date in month, year, and date, and
returns informing whether the parameters which are set are valid or not.

+-----------------------------------------------------------------------+
| void sntp_setservername(u8_t idx, char \*server);                     |
|                                                                       |
| uint8_t validdate_date(uint32_t yy,uint32_t mm,uint32_t dd)           |
|                                                                       |
| {                                                                     |
|                                                                       |
| //check year                                                          |
|                                                                       |
| if(yy>=1900 && yy<=9999)                                              |
|                                                                       |
| {                                                                     |
|                                                                       |
| //check month                                                         |
|                                                                       |
| if(mm>=1 && mm<=12)                                                   |
|                                                                       |
| {                                                                     |
|                                                                       |
| //check days                                                          |
|                                                                       |
| if((dd>=1 && dd<=31) && (mm==1 \|\| mm==3 \|\| mm==5 \|\| mm==7 \|\|  |
| mm==8 \|\| mm==10 \|\| mm==12))                                       |
|                                                                       |
| os_printf("Date is valid.\\n");                                       |
|                                                                       |
| else if((dd>=1 && dd<=30) && (mm==4 \|\| mm==6 \|\| mm==9 \|\|        |
| mm==11))                                                              |
|                                                                       |
| os_printf("Date is valid.\\n");                                       |
|                                                                       |
| else if((dd>=1 && dd<=28) && (mm==2))                                 |
|                                                                       |
| os_printf("Date is valid.\\n");                                       |
|                                                                       |
| else if(dd==29 && mm==2 && (yy%400==0 \||(yy%4==0 && yy%100!=0)))     |
|                                                                       |
| os_printf("Date is valid.\\n");                                       |
|                                                                       |
| else                                                                  |
|                                                                       |
| {                                                                     |
|                                                                       |
| os_printf("Day is invalid.\\n");                                      |
|                                                                       |
| return 1;                                                             |
|                                                                       |
| }                                                                     |
|                                                                       |
| }                                                                     |
|                                                                       |
| else                                                                  |
|                                                                       |
| {                                                                     |
|                                                                       |
| printf("Month is not valid.\\n");                                     |
|                                                                       |
| return 1;                                                             |
|                                                                       |
| }                                                                     |
|                                                                       |
| }                                                                     |
|                                                                       |
| else                                                                  |
|                                                                       |
| {                                                                     |
|                                                                       |
| return 1;                                                             |
|                                                                       |
| }                                                                     |
|                                                                       |
| return 0;                                                             |
|                                                                       |
| }                                                                     |
+=======================================================================+
+-----------------------------------------------------------------------+

Validating Time
---------------

validdate_time() validates the time in hour, minute, and seconds.

+-----------------------------------------------------------------------+
| uint8_t validdate_time(int32_t hh, int32_t mi, int32_t se)            |
|                                                                       |
| {                                                                     |
|                                                                       |
| if((hh < 0 \|\| hh >23 ) \|\| (mi < 0 \|\| mi > 59) \||(se < 0 \|\|   |
| se > 59)) {                                                           |
|                                                                       |
| os_printf("Time is Not valid.\\n");                                   |
|                                                                       |
| return 1;                                                             |
|                                                                       |
| }                                                                     |
|                                                                       |
| else {                                                                |
|                                                                       |
| os_printf("Time is valid.\\n");                                       |
|                                                                       |
| return 0;                                                             |
|                                                                       |
| }                                                                     |
|                                                                       |
| }                                                                     |
+=======================================================================+
+-----------------------------------------------------------------------+

Get NTP time
------------

ntp_time_get()is used to get the NTP time. Here, sntp_setservername()
initializes one of the NTP servers via the IP address of the Talaria TWO
module and then sntp_init() initializes the SNTP of the Talaria TWO
module.

+-----------------------------------------------------------------------+
| unsigned int ntp_time_get()                                           |
|                                                                       |
| {                                                                     |
|                                                                       |
| int times = 0;                                                        |
|                                                                       |
| unsigned int time_now;                                                |
|                                                                       |
| if(NULL != ntp_srv_name)                                              |
|                                                                       |
| sntp_setservername(0, (char \*)ntp_srv_name);                         |
|                                                                       |
| sntp_init();                                                          |
|                                                                       |
| do {                                                                  |
|                                                                       |
| os_printf("waiting for sntp, times=%d\\n", times++);                  |
|                                                                       |
| time_now = sntp_time();                                               |
|                                                                       |
| if(time_now == 0 && times < 16) {                                     |
|                                                                       |
| os_sleep_us(2000000, OS_TIMEOUT_NO_WAKEUP);                           |
|                                                                       |
| continue;                                                             |
|                                                                       |
| }                                                                     |
|                                                                       |
| else                                                                  |
|                                                                       |
| break;                                                                |
|                                                                       |
| } while(time_now == 0 && times < 10);                                 |
|                                                                       |
| sntp_stop();                                                          |
|                                                                       |
| return time_now;                                                      |
|                                                                       |
| }                                                                     |
+=======================================================================+
+-----------------------------------------------------------------------+

Read Input String from UART
---------------------------

uart_getchar() and uart_putchar()reads and writes one character from
serial port.

+-----------------------------------------------------------------------+
| void get_string(uint8_t \*buffer, uint32_t len)                       |
|                                                                       |
| {                                                                     |
|                                                                       |
| int ch;                                                               |
|                                                                       |
| int chindex = 0;                                                      |
|                                                                       |
| uint8_t \*ptr = buffer;                                               |
|                                                                       |
| while(chindex < len) {                                                |
|                                                                       |
| ch = uart_getchar(uarthandle);                                        |
|                                                                       |
| if(ch == '\\r' \|\| ch == '\\n') {                                    |
|                                                                       |
| ptr[chindex++] = '\\0';                                               |
|                                                                       |
| return;                                                               |
|                                                                       |
| }                                                                     |
|                                                                       |
| else if(ch == '\\b')                                                  |
|                                                                       |
| {                                                                     |
|                                                                       |
| uart_putchar(uarthandle, ch);                                         |
|                                                                       |
| uart_putchar(uarthandle, ' ');                                        |
|                                                                       |
| uart_putchar(uarthandle, ch);                                         |
|                                                                       |
| chindex--;                                                            |
|                                                                       |
| }                                                                     |
|                                                                       |
| else {                                                                |
|                                                                       |
| uart_putchar(uarthandle, ch);                                         |
|                                                                       |
| ptr[chindex++] = ch;                                                  |
|                                                                       |
| }                                                                     |
|                                                                       |
| }                                                                     |
|                                                                       |
| }                                                                     |
+=======================================================================+
+-----------------------------------------------------------------------+

Alarm Callback
--------------

User defined function alarm_user_cb()is used to set the alarm ID and the
argument. It prints the alarm ID and name, once the alarm is set.

+-----------------------------------------------------------------------+
| void                                                                  |
|                                                                       |
| alarm_user_cb(uint32_t id , uint8_t \*arg)                            |
|                                                                       |
| {                                                                     |
|                                                                       |
| char buffer[128];                                                     |
|                                                                       |
| os_printf("alarm_user_cb");                                           |
|                                                                       |
| snprintf(buffer, 256, "\\r\\n \*****Alarm:Id-%d:Name=%s \****\*", id, |
| arg);                                                                 |
|                                                                       |
| uart_puts(uarthandle, buffer);                                        |
+=======================================================================+
+-----------------------------------------------------------------------+

Alarm Display Callback
----------------------

User defined function alarm_display_cd() is used to display the alarm
information by printing the following:

1. Alarm ID

2. Name

3. Time

4. Type

5. If it is a repeating alarm or not.

+-----------------------------------------------------------------------+
| void                                                                  |
|                                                                       |
| alarm_display_cb(struct alarm_info \*ainfo)                           |
|                                                                       |
| {                                                                     |
|                                                                       |
| os_printf("alarm_display_cb");                                        |
|                                                                       |
| snprintf((char \*)buffer, 256," \\r\\nAlarm ID:%d                     |
| \\r\\nnName:%s\\r\\nAlarm Time:%s\\r\\nAlarm                          |
| Type:%s\\r\\nRepeat:%s\\r\\n",                                        |
|                                                                       |
| ainfo->alarm_id, ainfo->alarm_name, time_tostr((time_t                |
| \*)&ainfo->alarm_timesec),                                            |
|                                                                       |
| (ainfo->alarm_type == ALARM_TYPE_DAILY) ?"DAILY":"WEEKLY",            |
|                                                                       |
| (ainfo->alarm_repeat == 1) ? "Yes":"No");                             |
|                                                                       |
| uart_puts(uarthandle, buffer);                                        |
|                                                                       |
| }                                                                     |
+=======================================================================+
+-----------------------------------------------------------------------+

Suspend the System
------------------

uart_suspend_enable()enables suspend and waits for the system to wakeup,
where os_sleep_us() suspends execution for the specified number of
microseconds and uart_flush() flushes the output buffer.

+-----------------------------------------------------------------------+
| static void                                                           |
|                                                                       |
| uart_suspend_wait(struct uart \*u)                                    |
|                                                                       |
| {                                                                     |
|                                                                       |
| suspend=1;                                                            |
|                                                                       |
| uart_suspend_enable(uarthandle);                                      |
|                                                                       |
| while(suspend)                                                        |
|                                                                       |
| {                                                                     |
|                                                                       |
| os_sem_wait(&suspend_lock);                                           |
|                                                                       |
| if(suspend)                                                           |
|                                                                       |
| uart_suspend_enable(uarthandle);                                      |
|                                                                       |
| };                                                                    |
|                                                                       |
| os_sleep_us(100000, OS_TIMEOUT_NO_WAKEUP);                            |
|                                                                       |
| uart_flush(uarthandle);                                               |
|                                                                       |
| uart_close(uarthandle);                                               |
|                                                                       |
| uarthandle = uart_open(115200);                                       |
|                                                                       |
| uart_puts(uarthandle, "Out of Sleep !!\\r\\n");                       |
|                                                                       |
| }                                                                     |
+=======================================================================+
+-----------------------------------------------------------------------+

Cases Supporting the Alarm Menu
===============================

Case 0: Sleep Mode
------------------

Puts Talaria TWO in sleep mode.

+-----------------------------------------------------------------------+
| case 0: /\*Sleep*/                                                    |
|                                                                       |
| {                                                                     |
|                                                                       |
| uart_flush(uarthandle);                                               |
|                                                                       |
| uart_set_event_callback(uarthandle, handle_event, NULL);              |
|                                                                       |
| uart_suspend_wait(uarthandle);                                        |
|                                                                       |
| break;                                                                |
|                                                                       |
| }                                                                     |
+=======================================================================+
+-----------------------------------------------------------------------+

Case 1: Wi-Fi Connection Status
-------------------------------

Checks for Wi-Fi connection status. If the link is up, then by using
ntp_time_get() NTP time in seconds will be printed. However, if the
Wi-Fi link is down, ntp_time_get() fails.

+-----------------------------------------------------------------------+
| case 1: /\*Get NTP time*/                                             |
|                                                                       |
| {                                                                     |
|                                                                       |
| /\*check wifi connection status*/                                     |
|                                                                       |
| wcm_get_status(alarm_wcm_handle, &wcmstat);                           |
|                                                                       |
| if(wcmstat.link_up) {                                                 |
|                                                                       |
| tim_now = ntp_time_get();                                             |
|                                                                       |
| os_printf("\\r\\n Ntp time:%d Sec", tim_now);                         |
|                                                                       |
| snprintf(buffer, 256, "\\r\\n NTP Time:%d sec\\r\\n", tim_now);       |
|                                                                       |
| uart_puts(uarthandle, buffer);                                        |
|                                                                       |
| }                                                                     |
|                                                                       |
| else {                                                                |
|                                                                       |
| snprintf(buffer, 256, "\\r\\n WIFI link down: Ntp time get failed");  |
|                                                                       |
| os_printf("%s", buffer);                                              |
|                                                                       |
| uart_puts(uarthandle, buffer);                                        |
|                                                                       |
| }                                                                     |
|                                                                       |
| break;                                                                |
|                                                                       |
| }                                                                     |
+=======================================================================+
+-----------------------------------------------------------------------+

Case 2: System Time
-------------------

gettimeofday()gets system time in seconds.

+-----------------------------------------------------------------------+
| case 2: /\*Get System time Seconds*/                                  |
|                                                                       |
| gettimeofday(&now, NULL);                                             |
|                                                                       |
| os_printf("\\r\\n time:%lld", now.tv_sec);                            |
|                                                                       |
| snprintf(buffer, 256, "\\r\\n System Time:%lld sec\\r\\n",            |
| now.tv_sec);                                                          |
|                                                                       |
| uart_puts(uarthandle, buffer);                                        |
|                                                                       |
| break;                                                                |
+=======================================================================+
+-----------------------------------------------------------------------+

Case 3: System Date and Time
----------------------------

gettimeofday() gets system date and time, prints the date, day, time in
hour minute and seconds as per local time.

+-----------------------------------------------------------------------+
| case 3: /\*Get System Date and time*/                                 |
|                                                                       |
| {                                                                     |
|                                                                       |
| struct tm \*tm;                                                       |
|                                                                       |
| gettimeofday(&now, NULL);                                             |
|                                                                       |
| os_printf("\\r\\n time:%lld", now.tv_sec);                            |
|                                                                       |
| tm = localtime(&now.tv_sec);                                          |
|                                                                       |
| os_printf("\\r\\n timew:%d", tm->tm_hour);                            |
|                                                                       |
| strftime(buffer, 64, "%a %b %e %T %Y\\n", tm);                        |
|                                                                       |
| uart_puts(uarthandle, buffer);                                        |
|                                                                       |
| os_printf("\\r\\n Date:%s",time_tostr(&now.tv_sec));                  |
|                                                                       |
| break;                                                                |
|                                                                       |
| }                                                                     |
+=======================================================================+
+-----------------------------------------------------------------------+

Case 4: Set System Time
-----------------------

Here, wcm_get_status()checks the Wi-Fi connection status. If the link is
up, ntp_time_get() gets the NTP time. If the link is down,
ntp_time_get()fails to get the NTP time.

Only if the NTP time is captured, the alarm can be set using
alarm_init(), after which alarm_set_time() will replace the system time
with the NTP time. This helps set the alarm for present date and time.

+-----------------------------------------------------------------------+
| case 4: /\*Set Sytem time with NTP time*/                             |
|                                                                       |
| {                                                                     |
|                                                                       |
| /\*check wifi connection status*/                                     |
|                                                                       |
| wcm_get_status(alarm_wcm_handle, &wcmstat);                           |
|                                                                       |
| if(wcmstat.link_up) {                                                 |
|                                                                       |
| tim_now = ntp_time_get();                                             |
|                                                                       |
| /\*initilaise the alarm only after setting the time*/                 |
|                                                                       |
| if(0 != tim_now) {                                                    |
|                                                                       |
| alarm_init();                                                         |
|                                                                       |
| alarm_set_time((uint64_t)tim_now);                                    |
|                                                                       |
| }                                                                     |
|                                                                       |
| }                                                                     |
|                                                                       |
| else {                                                                |
|                                                                       |
| snprintf(buffer, 256, "\\r\\n WIFI link down: Ntp time get failed");  |
|                                                                       |
| os_printf("%s", buffer);                                              |
|                                                                       |
| uart_puts(uarthandle, buffer);                                        |
|                                                                       |
| }                                                                     |
|                                                                       |
| break;                                                                |
|                                                                       |
| }                                                                     |
+=======================================================================+
+-----------------------------------------------------------------------+

Case 5: Set System Time in Seconds
----------------------------------

Sets system time in seconds. alarm_init() initializes the alarm and
alarm time is set using alarm_set_time().

+-----------------------------------------------------------------------+
| case 5: /\*Set Sytem time in seconds*/                                |
|                                                                       |
| {                                                                     |
|                                                                       |
| snprintf(buffer, 256, "\\r\\n Time(seconds):");                       |
|                                                                       |
| uart_puts(uarthandle, buffer);                                        |
|                                                                       |
| tim_now= get_num((uint8_t \*)buffer, 256, &status);                   |
|                                                                       |
| if(status < 0)                                                        |
|                                                                       |
| break;                                                                |
|                                                                       |
| /\*Initiliase alarm*/                                                 |
|                                                                       |
| alarm_init();                                                         |
|                                                                       |
| /\*Set Time*/                                                         |
|                                                                       |
| alarm_set_time((uint64_t)tim_now);                                    |
|                                                                       |
| break;                                                                |
|                                                                       |
| }                                                                     |
+=======================================================================+
+-----------------------------------------------------------------------+

Case 6: Set the Alarm
---------------------

Sets the alarm with an option to add the following:

1. alarm_time.tm_year – Year

2. alarm_time.tm_mon – Month (1-12)

3. alarm_time.tm_mday – Day (1-31)

4. alarm_time.tm_hour – Hour (0-23)

5. alarm_time.tm_min – Minute (0-59)

6. alarm_time.tm_sec – Second (0-59)

7. alarm_type – Can be set for:

   a. DAILY (0) or WEEKLY (1)

..

   If the alarm is set for daily, on the configured time, the alarm will
   be notified to the user on the serial console with a string
   containing the alarm ID and name, every day at the same time.

   If the alarm is set for weekly, on the configured time, the alarm
   will be notified to the user on the serial console with a string
   containing the alarm ID and name, every week at the same time.

b. Shot (0) or Repeat (1)

..

   If the alarm should be notified to the user only once on a DAILY or
   WEEKLY basis, then the “Shot” option should be selected.

   If the alarm should be periodically notified to the user on a DAILY
   or WEEKLY basis, then the “Repeat” option should be selected.

If the user enters a wrong value for the prompted options, an ‘Invalid’
followed by the option is printed on the terminal.

For example: ‘Invalid date, time’ is printed on the terminal.

If configuring of the alarm is not successful, ‘Alarm set failed’ is
printed. Else, the alarm ID is printed on the terminal.

+-----------------------------------------------------------------------+
| case 6: /\*Set Alarm*/                                                |
|                                                                       |
| { struct alarm_tm alarm_time;                                         |
|                                                                       |
| uint8_t alarm_type;                                                   |
|                                                                       |
| uint8_t periodic;                                                     |
|                                                                       |
| snprintf(buffer, 256, "\\r\\n Year:");                                |
|                                                                       |
| uart_puts(uarthandle, buffer);                                        |
|                                                                       |
| alarm_time.tm_year = get_num((uint8_t \*)buffer, 256, &status);       |
|                                                                       |
| if(status < 0)                                                        |
|                                                                       |
| break;                                                                |
|                                                                       |
| snprintf(buffer, 256, "\\r\\n Month(1-12):");                         |
|                                                                       |
| uart_puts(uarthandle, buffer);                                        |
|                                                                       |
| alarm_time.tm_mon = get_num((uint8_t \*)buffer,256, &status);         |
|                                                                       |
| if(status < 0)                                                        |
|                                                                       |
| break;                                                                |
|                                                                       |
| snprintf(buffer, 256, "\\r\\n Day(1-31):");                           |
|                                                                       |
| uart_puts(uarthandle, buffer);                                        |
|                                                                       |
| alarm_time.tm_mday = get_num((uint8_t \*)buffer, 256, &status);       |
|                                                                       |
| if(status < 0)                                                        |
|                                                                       |
| break;                                                                |
|                                                                       |
| if(validdate_date(alarm_time.tm_year, alarm_time.tm_mon,              |
| alarm_time.tm_mday))                                                  |
|                                                                       |
| {                                                                     |
|                                                                       |
| snprintf(buffer, 256, "\\r\\n Invalid Date");                         |
|                                                                       |
| uart_puts(uarthandle, buffer);                                        |
|                                                                       |
| break;                                                                |
|                                                                       |
| }                                                                     |
|                                                                       |
| snprintf(buffer, 256, "\\r\\n Hour(0-23):");                          |
|                                                                       |
| uart_puts(uarthandle, buffer);                                        |
|                                                                       |
| alarm_time.tm_hour = get_num((uint8_t \*)buffer, 256, &status);       |
|                                                                       |
| if(status < 0)                                                        |
|                                                                       |
| break;                                                                |
|                                                                       |
| snprintf(buffer, 256, "\\r\\n Min(0-59):");                           |
|                                                                       |
| uart_puts(uarthandle, buffer);                                        |
|                                                                       |
| alarm_time.tm_min = get_num((uint8_t \*)buffer, 256, &status);        |
|                                                                       |
| if(status < 0)                                                        |
|                                                                       |
| break;                                                                |
|                                                                       |
| snprintf(buffer, 256, "\\r\\n Sec(0-59):");                           |
|                                                                       |
| uart_puts(uarthandle, buffer);                                        |
|                                                                       |
| alarm_time.tm_sec = get_num((uint8_t \*)buffer, 256, &status);        |
|                                                                       |
| if(status < 0)                                                        |
|                                                                       |
| break;                                                                |
|                                                                       |
| if(validdate_time((int32_t)alarm_time.tm_hour,                        |
| (int32_t)alarm_time.tm_min, (int32_t)alarm_time.tm_sec))              |
|                                                                       |
| {                                                                     |
|                                                                       |
| snprintf(buffer, 256, "\\r\\n Invalid Time");                         |
|                                                                       |
| uart_puts(uarthandle, buffer);                                        |
|                                                                       |
| break;                                                                |
|                                                                       |
| }                                                                     |
|                                                                       |
| snprintf(buffer, 256, "\\r\\n Alarm Type(DAILY(0)/WEEKLY(1):");       |
|                                                                       |
| uart_puts(uarthandle, buffer);                                        |
|                                                                       |
| alarm_type = get_num((uint8_t \*)buffer, 256, &status);               |
|                                                                       |
| if((status < 0 ) \|\| (alarm_type < 0 \|\| alarm_type > 1))           |
|                                                                       |
| {                                                                     |
|                                                                       |
| status =-1;                                                           |
|                                                                       |
| break;                                                                |
|                                                                       |
| }                                                                     |
|                                                                       |
| snprintf(buffer, 256, "\\r\\n Repeat(One shot(0)/Repeat(1):");        |
|                                                                       |
| uart_puts(uarthandle, buffer);                                        |
|                                                                       |
| periodic = get_num((uint8_t \*)buffer, 256, &status);                 |
|                                                                       |
| if((status < 0)|\| (periodic < 0 \|\| periodic > 1) )                 |
|                                                                       |
| {                                                                     |
|                                                                       |
| status =-1;                                                           |
|                                                                       |
| break;                                                                |
|                                                                       |
| }                                                                     |
|                                                                       |
| snprintf(buffer, 256, "\\r\\n Name:");                                |
|                                                                       |
| uart_puts(uarthandle, buffer);                                        |
|                                                                       |
| get_string((uint8_t \*)buffer, 256);                                  |
|                                                                       |
| os_printf("\\r\\n alarm:%d:%d:%d:%d:%d:%d",alarm_time.tm_year,        |
| alarm_time.tm_mon, alarm_time.tm_mday,                                |
|                                                                       |
| alarm_time.tm_hour, alarm_time.tm_min, alarm_time.tm_sec);            |
|                                                                       |
| alarm_id = alarm_set(&alarm_time, alarm_type, periodic,               |
| (uint32_t)alarm_user_cb,                                              |
|                                                                       |
| (uint8_t \*)buffer);                                                  |
|                                                                       |
| if(alarm_id < 0) {                                                    |
|                                                                       |
| snprintf(buffer, 256, "\\r\\n Alarm set failed:%d\\r\\n", alarm_id);  |
|                                                                       |
| }                                                                     |
|                                                                       |
| else {                                                                |
|                                                                       |
| snprintf(buffer, 256, "\\r\\n Alarm ID:%d\\r\\n", alarm_id);          |
|                                                                       |
| }                                                                     |
|                                                                       |
| uart_puts(uarthandle, buffer);                                        |
|                                                                       |
| break;                                                                |
|                                                                       |
| }                                                                     |
+=======================================================================+
+-----------------------------------------------------------------------+

Case 7: Delete the Alarm
------------------------

Deletes the alarm. On checking the alarm ID, if it is more than 0, alarm
is deleted. However, if the alarm ID is less than 0, alarm deletion
fails.

+-----------------------------------------------------------------------+
| case 7: /\*Delete Alarm*/                                             |
|                                                                       |
| { snprintf(buffer, 256, "\\r\\n Alarm ID to Delete:");                |
|                                                                       |
| uart_puts(uarthandle, buffer);                                        |
|                                                                       |
| alarm_id = get_num((uint8_t \*)buffer, 256, &status);                 |
|                                                                       |
| if(status < 0)                                                        |
|                                                                       |
| break;                                                                |
|                                                                       |
| if(alarm_delete(alarm_id) < 0) {                                      |
|                                                                       |
| snprintf(buffer, 256, "\\r\\n Alarm Delete failed:%d\\r\\n",          |
| alarm_id);                                                            |
|                                                                       |
| }                                                                     |
|                                                                       |
| else {                                                                |
|                                                                       |
| snprintf(buffer, 256, "\\r\\n Alarm Deleted\\r\\n");                  |
|                                                                       |
| }                                                                     |
|                                                                       |
| uart_puts(uarthandle, buffer);                                        |
|                                                                       |
| break; }                                                              |
+=======================================================================+
+-----------------------------------------------------------------------+

Case 8: Display Configured Alarm
--------------------------------

Displays the configured alarm.

+-----------------------------------------------------------------------+
| case 8: /\*Display Alarm*/                                            |
|                                                                       |
| { alram_display((uint32_t)alarm_display_cb);                          |
|                                                                       |
| break; }                                                              |
|                                                                       |
| default:                                                              |
|                                                                       |
| break;                                                                |
+=======================================================================+
+-----------------------------------------------------------------------+

Running the Application
=======================

Programming Talaria TWO 
------------------------

Program alarm.elf (*sdk_x.y\\apps\\alarm\\bin*) using the Download tool:

1. Launch the Download tool provided with InnoPhase Talaria TWO SDK.

2. In the GUI window:

   a. Boot Target: Select the appropriate EVK from the drop-down

   b. ELF Input: Load the alarm.elf by clicking on Select ELF File.

   c. AP Options: Provide the SSID and Passphrase under AP Options to
      connect to an Access Point.

   d. Programming: Prog RAM or Prog Flash as per requirement.

For more details on using the Download tool, refer to the document:
UG_Download_Tool.pdf (path: *sdk_x.y\\pc_tools\\Download_Tool\\doc*).

**Note**: x and y refer to the SDK release version. For example:
*sdk_2.5\\doc*.

Expected Output
---------------

+-----------------------------------------------------------------------+
| Y-BOOT 208ef13 2019-07-22 12:26:54 -0500 790da1-b-7                   |
|                                                                       |
| ROM yoda-h0-rom-16-0-gd5a8e586                                        |
|                                                                       |
| FLASH:PNWWWWWAEBuild $Id: git-34e3eddb8 $                             |
|                                                                       |
| np_conf_path=/data/nprofile.json ssid=InnoPhase_AE                    |
| passphrase=Inno@1234                                                  |
|                                                                       |
| $App:git-fc1c5cb4                                                     |
|                                                                       |
| SDK Ver: sdk_2.5                                                      |
|                                                                       |
| Alarm Demo App                                                        |
|                                                                       |
| addr e0:69:3a:00:2c:3c                                                |
|                                                                       |
| Adding network: ssid = InnoPhase_AE : passphrase = Inno@1234          |
|                                                                       |
| Connecting to added network : InnoPhase_AE[0.961,039]                 |
| CONNECT:98:da:c4:73:b7:76 Channel:11 rssi:-32 dBm                     |
|                                                                       |
| wcm_notify_cb to App Layer - WCM_NOTIFY_MSG_LINK_UP                   |
|                                                                       |
| wcm_notify_cb to App Layer - WCM_NOTIFY_MSG_ADDRESS                   |
|                                                                       |
| [1.102,314] MYIP 192.168.0.130                                        |
|                                                                       |
| [1.102,479] IPv6 [fe80::e269:3aff:fe00:2c3c]-link                     |
|                                                                       |
| Connected to < InnoPhase_AE > network                                 |
+=======================================================================+
+-----------------------------------------------------------------------+

Evaluating the Application
==========================

For this menu-driven application, UART is used as the interface to input
the menu options. Launch any of the serial terminal for example GTK term
or minicom with the following configurations:

**Note**: This application is supported on both Windows and Linux.

1. Baud Rate: 115200bps

2. Select the required port.

+-----------------------------------------------------------------------+
| /dev/ttyUSB\*                                                         |
+=======================================================================+
+-----------------------------------------------------------------------+

|image1|

Figure : Configuring the serial terminal

Once the application is flashed, reset the board, and observe the
following outputs on the console:

|image2|

Figure : Menu options - UART terminal

Subsequent sections show the different menu option configurations.

Put System in Sleep Mode 
-------------------------

To put the system in sleep mode, set the option to 0. To wake Talaria
TWO up from sleep, send break(Clt+Shift+b).

|image3|

Figure : Put system in sleep mode

.. _get-ntp-time-1:

Get NTP Time
------------

To get NTP time in seconds, set the option to 1.

|image4|

Figure : Get NTP time

Get System Time
---------------

To get system time in seconds, set the option to 2.

|image5|

Figure : Get system time

Get System Date and Time
------------------------

To get system date and time, set option to 3.

|image6|

Figure : Get system date and time

Set System Time with NTP Time
-----------------------------

To set system time with NTP time, set the option to 4. Use option 3 to
check if the time is set correctly.

|image7|

Figure : Set system time with NTP time

Set System Time (Seconds)
-------------------------

To set system time in seconds, set the option to 5.

**Note**: If the user needs to get back to the default system time, then
set the Time(seconds): to 0.

|image8|

Figure : Set system time in seconds

Set Alarm
---------

To set the alarm, set the option to 6. Once the alarm is successfully
set, the Alarm ID is generated. Multiple alarms can be set using this
option.

For more information on setting the alarm, refer section 6.7.

|image9|

Figure : Set alarm

Delete Alarm
------------

To delete the alarm, set the option to 7.

|image10|

Figure : Delete the alarm

Display All Alarms
------------------

To display all the configured alarms, set the option to 8.

|image11|

Figure : Display all alarms

Alarm Expiry
------------

Once the alarm expires , the alarm ID and name is displayed on the
terminal, depending upon the configured time added in section 8.7.

|image12|

Figure : Alarm expiry

.. |image1| image:: media/image1.png
   :width: 4.72441in
   :height: 1.98766in
.. |image2| image:: media/image2.png
   :width: 5.51181in
   :height: 2.84442in
.. |image3| image:: media/image3.png
   :width: 5.51181in
   :height: 1.83991in
.. |image4| image:: media/image4.png
   :width: 5.51181in
   :height: 1.95in
.. |image5| image:: media/image5.png
   :width: 5.51181in
   :height: 1.91937in
.. |image6| image:: media/image6.png
   :width: 5.51181in
   :height: 1.9265in
.. |image7| image:: media/image7.png
   :width: 5.51181in
   :height: 3.55704in
.. |image8| image:: media/image8.png
   :width: 5.51181in
   :height: 1.93677in
.. |image9| image:: media/image9.png
   :width: 5.51181in
   :height: 3.22292in
.. |image10| image:: media/image10.png
   :width: 5.51181in
   :height: 2.29625in
.. |image11| image:: media/image11.png
   :width: 5.51181in
   :height: 3.06389in
.. |image12| image:: media/image12.png
   :width: 5.51181in
   :height: 1.9833in
