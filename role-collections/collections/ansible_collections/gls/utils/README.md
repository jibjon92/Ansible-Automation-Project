GLS Toolbox Collection
======================


## Included Content

### Roles

* [backup](roles/backup/README.md): Backup files and directories on the targeted hosts.
* [restore](roles/restore/README.md): Restore files and directories previously saved by the `backup` role.

### Modules

* `newping`: Test connection to the targeted hosts.


## Building the Collection

Before you can use the collection, you must build it:

```
cd gls/utils
ansible-galaxy collection build
```

That command creates a tar archive that you can use to install the collection.


## Using the Collection

Before using the collection, you must install it with the `ansible-galaxy` command.
In your Ansible working directory (this is usually the directory where you store the `ansible.cfg`, `inventory`, and playbook files), run the following command:

```
ansible-galaxy collection install gls-utils-0.0.1.tar.gz
```

That command installs the collection in the default path, `~/.ansible/collections` by default.
If you want to install it in a different location, in your working directory for example, add the `-p` option to the `ansible-galaxy` command:

```
ansible-galaxy collection install gls-utils-0.0.1.tar.gz -p ./collections
```

You also need to add that path to the `collections_paths` variable under the `[defaults]` section of your `ansible.cfg` file.

```
[defaults]
inventory=inventory
remote_user=devops
collections_paths=collections
```

See [Ansible Using collections](https://docs.ansible.com/ansible/latest/user_guide/collections_using.html) for more details.


## Licensing

GNU General Public License v3.0 or later.
