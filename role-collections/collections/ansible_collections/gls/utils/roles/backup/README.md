backup
======

This role backups up the files and directories provided using the `backup_files` variable.
The backup is identified with a given name (`backup_id`) and can be restored using the `gls.utils.restore` role.

If a backup with the same name already exists, then the role immediately returns.


Requirements
------------

None


Role Variables
--------------

The role accepts the following variables:

* `backup_id`: The name (or ID) for the backup. This can be any string you want (without spaces). This name is used to identify the backup when you call the `restore` role.
  By default, `backup_id` is set to `test`.
* `backup_files`: The list of files and directories to backup. You can use globs (`*`) in those path names. Files and directories that do not exist on the system are silently skipped.
  `/etc` by default.


Dependencies
------------

None


Example Playbook
----------------

```yaml
---
- name: Backing up configuration files and the home directory of devops
  hosts: nodes
  become: true
  gather_facts: false

  tasks:
    - include_role:
        name: gls.utils.backup
      vars:
        backup_id: ge01
        backup_files:
          - /etc/hosts
          - /etc/resolv.conf
          - /etc/fstab
          - /home/devops
...
```

The `tests/` directory provides an additional example.


License
-------

GPL 3.0 or later.
