#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = '''
---
module: newping
version_added: historical
short_description: Try to connect to host, verify a usable python and return C(pong) on success
description:
   - A trivial test module, this module always returns C(pong) on successful
     contact. It does not make sense in playbooks, but it is useful from
     C(/usr/bin/ansible) to verify the ability to login and that a usable Python is configured.
   - This is NOT ICMP ping, this is just a trivial test module that requires Python on the remote-node.
   - For Windows targets, use the M(ansible.windows.win_ping) module instead.
   - For Network targets, use the M(ansible.netcommon.net_ping) module instead.
options:
  data:
    description:
      - Data to return for the C(ping) return value.
      - If this parameter is set to C(crash), the module will cause an exception.
    type: str
    default: pong
seealso:
- module: ansible.netcommon.net_ping
- module: ansible.windows.win_ping
author:
    - Ansible Core Team
'''

EXAMPLES = '''
# Test we can logon to 'webservers' and execute python with json lib.
# ansible webservers -m newping
- name: Example from an Ansible Playbook
  newping:
- name: Induce an exception to see what happens
  newping:
    data: crash
'''

RETURN = '''
newping:
    description: value provided with the data parameter
    returned: success
    type: str
    sample: pong
'''

from ansible.module_utils.basic import AnsibleModule


def main():
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='Hello'),
        ),
        supports_check_mode=True
    )

    if module.params['data'] == 'crash':
        raise Exception("boom")

    result = dict(
        newping=module.params['data'],
    )

    module.exit_json(**result)


if __name__ == '__main__':
    main()
