.. _fl design:

Factory Loader Design
======================

The factory loader application is designed to be used with a companion
script that implements the factory loader HIO commands over UART. 

Command Reference
-----------------

.. table:: Table 2: Commands with description, input, and output

   +----------+------------------------------+------------+--------------+
   | **C      | **Description**              | **Input**  | **Output**   |
   | ommand** |                              |            |              |
   +==========+==============================+============+==============+
   | fla      | Writes image file to target  | f          | N/A          |
   | sh_write | address in flash             | ile_image, |              |
   |          |                              | flash_addr |              |
   +----------+------------------------------+------------+--------------+
   | enroll   | Enrolls key contents in      | keyfile    | N/A          |
   |          | flash                        |            |              |
   +----------+------------------------------+------------+--------------+
   | f        | Programs partition table     | Partition  | N/A          |
   | rom_json | into flash                   | JSON       |              |
   |          |                              | con        |              |
   |          |                              | figuration |              |
   |          |                              | file       |              |
   +----------+------------------------------+------------+--------------+
   | to_json  | Reads partition table from   |            | Partition    |
   |          | flash into a json file       |            | information  |
   |          |                              |            | in JSON      |
   |          |                              |            | format       |
   +----------+------------------------------+------------+--------------+
   | ge       | Returns the status of        |            | Returns 0 if |
   | t_status | *factory loader* application |            | fa           |
   |          |                              |            | ctory_loader |
   |          |                              |            | application  |
   |          |                              |            | is loaded    |
   +----------+------------------------------+------------+--------------+
   | prov     | Provisions AP parameters and | ssid,      | Returns 0 on |
   | ision_ap | connects to AP               | passphrase | successful   |
   |          |                              |            | connection   |
   +----------+------------------------------+------------+--------------+
   | get_     | Downloads and flashes any    | url, port, | Returns 0 on |
   | http_bin | binary file to target flash  | filename,  | success      |
   |          | addr                         | flash_addr |              |
   +----------+------------------------------+------------+--------------+
   | get_h    | Downloads file and writes it | url, port, | Returns 0 on |
   | ttp_file | into target file system      | filename,  | success      |
   |          |                              | m          |              |
   |          |                              | ount_point |              |
   +----------+------------------------------+------------+--------------+
   | wr       | Writes a file to target file | mo         | Returns 0 on |
   | ite_file | system                       | unt_point, | success      |
   |          |                              | filename   |              |
   +----------+------------------------------+------------+--------------+
   | file_enc | Encrypts existing file in    | mo         | Returns 0 on |
   |          | the file system. Requires    | unt_point, | success      |
   |          | that a keyfile has been      | filename   |              |
   |          | previously enrolled          |            |              |
   +----------+------------------------------+------------+--------------+
   | mount_fs | Mounts a file system         | m          | Returns 0 on |
   |          |                              | ount_addr, | success      |
   |          |                              | img_size,  |              |
   |          |                              | m          |              |
   |          |                              | ount_point |              |
   +----------+------------------------------+------------+--------------+
