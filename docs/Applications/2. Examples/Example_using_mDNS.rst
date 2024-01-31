.. _ex using mdns:

mDNS
----------------

This document describes using the mDNS APIs provided by the mDNS module
in: freertos_sdk_x.y/components/mdns. This application demonstrates
using these APIs to advertise and discover the services on the local
network.

For more details regarding the features and limitations of mDNS
implementation and APIs, refer mdns_apiref.pdf.

Code Walkthrough for mDNS
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Application Flow
~~~~~~~~~~~~~~~~~~~~~~~~~~~

mDNS is a protocol that provides DNS like facility to advertise and
discover services in a local area network.

Following are the steps:

1. Connects to a Wi-fi network.

2. Registers to the hostname and services.

3. Acts as a mDNS announce or discovery according to the boot arguments
   passed.

Sample Code Walkthrough 
~~~~~~~~~~~~~~~~~~~~~~~~~~~

A user-defined data struct is created to store the data of the mDNS:

.. code:: shell

      #define APP_NAME "mDNS application"
      #define APP_VERSION "2.0"
      
      OS_APPINFO {.stack_size = 4096};
      
      #define INPUT_PARAMETER_SSID "ssid"
      #define INPUT_PARAMETER_PASSPHRASE "passphrase"
      #define INPUT_PARAMETER_HOST "host"
      #define INPUT_PARAMETER_URL "url"
      #define INPUT_PARAMETER_PATH "path"
      #define INPUT_PARAMETER_PORT "port"
      #define INPUT_PARAMETER_SECURED "secured"
      #define INPUT_PARAMETER_METHOD "method"
      #define INPUT_PARAMETER_CA "ca_cert"
      #define INPUT_PARAMETER_POST_LEN "post_len"
      #define INPUT_PARAMETER_CLIENT_CERT "client_cert"
      #define INPUT_PARAMETER_CLIENT_KEY "client_key"
      #define INPUT_PARAMETER_TEST_ITER "test_iterations"
      #define INPUT_PARAMETER_USE_CA_BUNDLE "use_ca_bundle"
      
      #define NULL_STR ""
      
      struct param_t {
      const char *ssid;
         const char *passphrase;
         /* parameters for advertise */
         const char *servicename;
         const char *service_type;
         const char *proto; /* 0 - UDP, 1- TCP */
         const char *port;
         const char *txt_key;
         const char *txt_val;
         const char *hostname;
         /* Parameters for Service Discovery */
         const char *sd_srvc_type;
         const char *sd_srvc_proto;
         const char *action;
      };
      bool wcm_connected = false;
      struct param_t param;
      char default_port[8];
      
      char keyVal[256];
      const char *txt_key_val[10];


The following boot arguments are passed in this application:

1. SSID and passphrase to connect to the Wi-Fi network.

2. Hostname, service name, service type, proto, port, text key and
   value.

3. SD service type and proto, and action.

.. code:: shell

      static int
      parse_boot_args(void)
      {
          int ret = 0;
      
          param.ssid= os_get_boot_arg_str(INPUT_PARAMETER_SSID);
          param.passphrase= os_get_boot_arg_str(INPUT_PARAMETER_PASSPH);
      
          param.hostname= os_get_boot_arg_str(INPUT_PARAMETER_HOST_NAME);
          param.servicename= os_get_boot_arg_str(INPUT_PARAMETER_SRVC_NAME);
          param.service_type= os_get_boot_arg_str(INPUT_PARAMETER_SRVC_TYPE);
          param.proto= os_get_boot_arg_str(INPUT_PARAMETER_PROTO);
          param.port = os_get_boot_arg_str(INPUT_PARAMETER_PORT);
          param.txt_key = os_get_boot_arg_str(INPUT_PARAMETER_TXT_KEY);
          param.txt_val = os_get_boot_arg_str(INPUT_PARAMETER_TXT_VAL);
      
          param.sd_srvc_type = os_get_boot_arg_str(INPUT_PARAMETER_SD_SRVC_TYPE);
          param.sd_srvc_proto = os_get_boot_arg_str(INPUT_PARAMETER_SD_SRVC_PROTO);
          param.action = os_get_boot_arg_str(INPUT_PARAMETER_ACTION);



To connect to a Wi-Fi network, wcm_create()API from the Wi-Fi Connection
Manager is used. Initially, the Wi-Fi network interface is created using
wcm_create().

.. code:: shell

      h = wcm_create(NULL);   

..

   wifi_connect_to_network()API, from components library, connects to
   the Wi-Fi network using the AP credentials provided.

.. code:: shell

      rval = wifi_connect_to_network(&h, WCM_CONN_WAIT_INFINITE, &wcm_connect_success);
          if(rval < 0) {
              os_printf("\nError: Unable to connect to network\n");
              return 0;
          }


Here, the data structure mdns_srvc_info_t is used to pass information
about the discovered service such as service instance, protocol, type,
port and IP address. Information is passed through the callback function
provided while calling the mdns_service_discover API from main function.

.. code:: shell

      void app_dns_sd_cb(void *data_ptr,
                                       const mdns_srvc_info_t *srvinfo,
                                       uint32_t status)
      {
          os_printf("\n------------------------------------------------------------");
          os_printf("\n[APP]%s:Discovered service info:", __FUNCTION__);
          os_printf("\n\tInstance = %s \n\tservice type = %s \n\tprotocol = %s\n\t"
                    "txt info = %s \n\tport = %d \n\tipaddr = %x\n",
                    srvinfo->instance, srvinfo->srvc_type, srvinfo->protocol,
                    srvinfo->txtInfo, srvinfo->port, srvinfo->ipaddr);
          os_printf("\n");
          os_printf("\n------------------------------------------------------------");


If the action parameter is set to 0, mDNS will register and advertise
the service.

The data structure mdns_hnreg_param_t is used to pass parameters while
registering the Host Name. Set a unique host name for a device by using
mac address. Add domain name as MDNS_LOCAL_DOMAIN and IP address in
little endian format.

.. code:: shell

      mdns_hnreg_param_t hn_reg_prm = {0};
              hn_reg_prm.hostname = (!param.hostname)?
                                (uint8_t *)"InnophaseDev" : (uint8_t *)param.hostname;
              hn_reg_prm.domain = (uint8_t *)MDNS_LOCAL_DOMAIN;
              hn_reg_prm.ipaddr = ntohl(ipaddr);


The function mdns_hostname_reg is used for registering the host name of
the interface.

.. code:: shell

      mdns_hostname_reg(mc, &hn_reg_prm);
              os_printf("\n[APP]Host name Reg done");


The data structure mdns_srvreg_param_t is used to pass the parameters
while registering a service.

.. code:: shell

      mdns_srvreg_param_t srv_reg = {0};
      
              srv_reg.srvc_name = (uint8_t *)param.servicename;
              srv_reg.srvc_type = (uint8_t *)param.service_type;
              srv_reg.srvc_proto = (!param.proto) ?
                                  (uint8_t *)"_tcp": (uint8_t *)param.proto;
              srv_reg.port = (!param.port)? 80 : atoi(param.port);
              srv_reg.domain = (uint8_t *)MDNS_LOCAL_DOMAIN;


The function mdns_service_register is used for registering the service.
Once registered, response for any matching query will be given
internally.

.. code:: shell

      mdns_service_register(mc, &srv_reg);
              os_printf("\n[APP]Service Reg done");


The following section provides information on how the discovery of the
service happens when the action parameter is not set to 0.

The data structure mdns_srvcdisc_param_t is used for passing the
parameters while discovering for service of specific type.

.. code:: shell

      os_printf("\n[APP]Discovering Service");
              mdns_srvcdisc_param_t sd_param = {0};
              sd_param.srvc_sub_type = NULL;
              sd_param.srvc_type = (!param.sd_srvc_type)?
                                  (uint8_t *)"_http": (uint8_t *)param.sd_srvc_type;
              sd_param.srvc_proto =(!param.sd_srvc_proto)?
                                  (uint8_t *)"_tcp": (uint8_t *)param.sd_srvc_proto;
              sd_param.domain = (uint8_t *)MDNS_LOCAL_DOMAIN;
              sd_param.scope = MDNS_SCOPE_IPV4_LOCAL;
              sd_param.cb = app_dns_sd_cb;
              mdns_service_discover(mc, &sd_param);


Running the Application 
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Programming Talaria TWO board with ELF
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Program mdns.elf *(freertos_sdk_x.y/examples/mdns/bin)* using the
Download tool:

1. Launch the Download tool provided with InnoPhase Talaria TWO SDK.

2. In the GUI window:

   a. Boot Target: Select the appropriate EVK from the drop-down.

   b. ELF Input: Load the mdns.elf by clicking on Select ELF File.

   c. AP Options: Pass the SSID and Passphrase to connect to an Access
      Point.

   d. Boot Arguments: Pass the appropriate boot arguments.

   e. Programming: Prog RAM or Prog Flash as per requirement.

Using the Application
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Following are the list of boot arguments:

1.  ssid: SSID of the Wi-Fi network to connect to.

2.  passphrase: Passphrase of the network.

3.  hostname: Hostname of the device. For example: “InnoDev”.

4.  service_name: Service name. For example: “Prov”.

5.  service_type: Type of service. For example: "\_http".

6.  proto: Protocol type. For example: "\_tcp" / "\_udp".

7.  port: Get/Post.

8.  txt_key: “key” part of the one key-val pair of txt data.

9.  txt_val: “val” part of the one key-val pair of txt data. Only one
    Key-val pair can be set.

10. sd_srvc_type: Type of service to discover.

11. sd_srvc_proto: Type of protocol to discover.

12. action:

    a. 0 – Register and Advertise a service.

    b. 1 – Discover a service. The combination of sd_srvc_type and
       sd_srvc_proto are used for discovering the service. Providing
       both the parameters is a must for discovering a service.

Example Bootargs for mDNS Service Register and Announce
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: shell

      ssid=<ssid>,passphrase=<passphrase>,host=Innodev, service_name =Prov, service_type=_http,proto=_tcp,port=80,txt_key=path,txt_val=/data,action=0


Console output:

.. code:: shell

      Y-BOOT 208ef13 2019-07-22 12:26:54 -0500 790da1-b-7
      ROM yoda-h0-rom-16-0-gd5a8e586
      FLASH:PWWWWWWAE
      Build $Id: git-e52d93e $
      Flash detected. flash.hw.uuid: 39483937-3207-0080-0055-ffffffffffff
      Bootargs: ssid=innotest_AP passphrase=inno@1234 sd_srvc_type=_http, sd_srvc_proto=_tcp, action=1
      $App:git-8b301e9
      SDK Ver: FREERTOS_SDK_1.0
      MDNS Demo App
      Application Information:
      ------------------------
      Name       : MDNS  application
      Version    : 1.0
      Build Date : Aug 24 2023
      Build Time : 15:26:32
      Heap Available: 311 KB (318968 Bytes)
      
      [APP]Bootparams:
      
      hostname=<null>
      port = <null>
      servicename = <null>
      service_type = <null>
      proto = <null>
      key = <null>
      val = <null>
      sd_service_type = _http,
      sd_service_proto = _tcp,
      [APP]Bootparams check done....ret = 0
      addr e0:69:3a:00:08:38
      network profile created for ssid: innotest_AP
      
      Connecting to added network : innotest_AP
      [1.330,481] DEAUTHENTICATED: reason 1
      [1.740,583] CONNECT:0e:70:6c:d6:3a:62 Channel:6 rssi:-49 dBm
      wcm_notify_cb to App Layer - WCM_NOTIFY_MSG_LINK_UP
      wcm_notify_cb to App Layer - WCM_NOTIFY_MSG_ADDRESS
      [1.786,814] MYIP 192.168.99.195
      [1.786,978] IPv6 [fe80::e269:3aff:fe00:838]-link
      wcm_notify_cb to App Layer - WCM_NOTIFY_MSG_CONNECTED
      
      Connected to added network : innotest_AP
      
      [APP]Starting Mdns
      [APP]Mdns init done
      [APP]Discovering Service


Once mDNS Service Register and Announce is started, start any of the
discovery apps and scan for the services that are announced by Talaria
TWO. Following are some of the options for the user for the service
discovery:

**Option 1:** Mobile application: mDNS Discovery

1. Install and launch the mDNS Discovery app on the mobile.

..

|image163|

Figure 1: mDNS Discovery app

2. Add the service type i.e., HTTP in the search option, enable TCP
   which is the proto and click on Search.

|image164|

Figure 2: Add service type

3. Now the announced service from Talaria TWO can be found as shown in
   Figure 3.

..

|image165|

Figure 3: Discovered service

**Option 2**: Command line on Windows OS

Prerequisite: Install the Bonjour Browser from the following link to run
the command line on Windows OS:
https://hobbyistsoftware.com/bonjourbrowser.

1. Service discovery can be done from a Windows command line, using the
   dns-sd command to browse for services that are being broadcast on the
   local network by Talaria TWO.

..

|image166|

Figure 4: Service discovery from Windows command line

**Option 3**: User can also use two Talaria TWO modules: One for service
register and announce from section 6.1 and one more for service
discovery from section 6.2 to load the application. On the service
discovery console, the announced service can be observed.

Example Bootargs for mDNS Service Discovery
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: shell

      ssid=<ssid>,passphrase=<passphrase>, sd_srvc_type=_http, sd_srvc_proto=_tcp, action=1


Console output:

.. code:: shell

      Y-BOOT 208ef13 2019-07-22 12:26:54 -0500 790da1-b-7
      ROM yoda-h0-rom-16-0-gd5a8e586
      FLASH:PWWWWWWAE
      Build $Id: git-e52d93e $
      Flash detected. flash.hw.uuid: 39483937-3207-0080-0055-ffffffffffff
      Bootargs: ssid=innotest_AP passphrase=inno@1234 host=Innodev service_name=Prov service_type=_http proto=_tcp port=80 txt_key=path txt_val=/data action=0
      $App:git-8b301e9
      SDK Ver: FREERTOS_SDK_1.0
      MDNS Demo App
      Application Information:
      ------------------------
      Name       : MDNS  application
      Version    : 1.0
      Build Date : Aug 24 2023
      Build Time : 15:26:32
      Heap Available: 311 KB (318968 Bytes)
      [APP]Bootparams:
      
      hostname=<null>
      port = 80
      servicename = Prov
      service_type = _http
      proto = _tcp
      key = path
      val = /data
      sd_service_type = <null>
      sd_service_proto = <null>
      [APP]Bootparams check done....ret = 0
      addr e0:69:3a:00:08:38
      network profile created for ssid: innotest_AP
      
      Connecting to added network : innotest_AP
      [0.746,137] CONNECT:0e:70:6c:d6:3a:62 Channel:6 rssi:-34 dBm
      wcm_notify_cb to App Layer - WCM_NOTIFY_MSG_LINK_UP
      wcm_notify_cb to App Layer - WCM_NOTIFY_MSG_ADDRESS
      [0.823,237] MYIP 192.168.99.195
      [0.823,400] IPv6 [fe80::e269:3aff:fe00:838]-link
      wcm_notify_cb to App Layer - WCM_NOTIFY_MSG_CONNECTED
      
      Connected to added network : innotest_AP
      
      [APP]Starting Mdns
      [APP]Mdns init done
      [APP]Advertising Service
      [APP]WCM interface ip addr = c363a8c0
      [APP]Host name Reg done
      [APP]Service Reg done
      [APP]Hostname and Service Announce done
      [APP]Service is Now discoverable by other devices in the N/w


.. |image163| image:: media/image163.png
   :width: 3.14961in
   :height: 6.39128in
.. |image164| image:: media/image164.png
   :width: 3.14961in
   :height: 6.54135in
.. |image165| image:: media/image165.png
   :width: 3.14961in
   :height: 6.0702in
.. |image166| image:: media/image166.png
   :width: 5.90551in
   :height: 1.65893in
