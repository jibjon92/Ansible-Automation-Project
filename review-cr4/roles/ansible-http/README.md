ansible-httpd
=========
Example ansible-httpd role from "Red Hat Enterprise Linux Automation with Ansible" (RH294)

Role Variables
--------------

* `web_package`: the RPM package
* `web_service`: the systemd service
* `web_config_file`: the path to the main configuration file
* `web_root`: the path to an index.html file
* `web_fw_service`: the name of a firewalld service

Dependencies
------------

None.

Example Playbook
----------------

    - hosts: servers
      roles:
        - ansible-httpd

License
-------

BSD

Author Information
------------------

Red Hat (training@redhat.com)
