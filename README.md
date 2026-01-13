This repository contains my solutions, playbooks, and configuration files for the Red Hat Enterprise Linux Automation with Ansible course. It serves as a practical guide and portfolio demonstrating proficiency in automating Linux administration using Ansible.

📌 Project Overview
The goal of this project is to automate standard system administration tasks on RHEL systems. The repository is structured to follow the official Red Hat curriculum, progressing from basic installation to complex role-based orchestration and system-wide automation.

🛠️ Curriculum & Key Topics
Section	Topic	Core Properties & Modules Covered
01	Ansible Intro & Install	ansible-core installation, Control Node vs. Managed Hosts.
02	Core Mechanics	Static/Dynamic Inventories, ansible.cfg, YAML syntax, ansible-playbook.
03	Data Management	Variable precedence, ansible-vault (secrets), ansible_facts.
04	Task Control	loop, when conditionals, handlers, block/rescue/always.
05	File Manipulation	copy, fetch, lineinfile, blockinfile, Jinja2 Templates.
06	Large Projects	Host patterns (regex), import_playbook, include_tasks.
07	Ansible Roles	ansible-galaxy, Role directory structure, Content Collections.
08	Troubleshooting	debug module, --check mode, ansible-lint, log analysis.
09	System Automation	yum/dnf, user, parted, nmcli, firewalld, systemd.
10	Comprehensive Review	End-to-end deployment of multi-tier applications.

🚀 Key Features Demonstrated

1. Advanced Playbook Logic: Implementation of complex workflows using conditional execution and error handling to ensure idempotent system states.
2.  Secret Management: Securely managing sensitive data (passwords, SSH keys) using Ansible Vault to ensure security best practices in DevOps pipelines.
3. Modularization with Roles: Organizing automation into reusable roles.Includes usage of RHEL System Roles to leverage Red Hat-supported automation for networking, storage, and kernel settings.
4. Dynamic Infrastructure Configuration: Using Jinja2 templates to dynamically generate configuration files (like /etc/hosts or Apache Vhosts) based on host-specific variables.


📂 Repository Structure:

.
├── group_vars/             # Global and group-specific variables
├── host_vars/              # Host-specific variables
├── inventory/              # Static inventory files
├── roles/                  # Custom Ansible Roles
│   └── my_custom_role/     # Example: Webserver or DB setup
├── playbooks/              # Individual lab solutions
│   ├── install_ansible.yml
│   ├── manage_storage.yml
│   └── network_config.yml
├── ansible.cfg             # Local Ansible configuration
└── README.md

💻 Environment Prerequisites

1. Control Node: RHEL 8 or 9
2. Managed Hosts: RHEL-based systems
3. Ansible Version: 2.11+
4. Python: 3.9+



    Securely manage user accounts and system subscriptions.

    Standardize software deployments across different host groups.
