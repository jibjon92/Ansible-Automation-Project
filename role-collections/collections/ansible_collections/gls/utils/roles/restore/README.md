restore
=======

This role restores a backup previously created using the `gls.utils.backup` role.
The backup to restore is identified by the name (`backup_id`) that was used during backup.


Requirements
------------

The backup to restore must have been created using the `gls.utils.backup` role.


Role Variables
--------------

The role accepts the following variables:

* `backup_id`: The name (or ID) for the backup to restore. This is the name you used when you ran the `gls.utils.backup` role.
  By default, `backup_id` is set to `test`.
* `restore_remove_after`: This tells whether the backup must be removed after a successful restore or not.
  By default, `restore_remove_after` is true (the backup is removed after restore)


Dependencies
------------

None


Example Playbook
----------------

```yaml
---
- name: Restoring configuration files and the home directory of devops
  hosts: nodes
  become: true
  gather_facts: false

  tasks:
    - include_role:
        name: gls.utils.restore
      vars:
        backup_id: ge01
...
```

The `tests/` directory provides an additional example.


License
-------

GPL 3.0 or later.
