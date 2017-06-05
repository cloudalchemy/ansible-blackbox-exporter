<p><img src="http://jacobsmedia.com/wp-content/uploads/2015/08/black-box-edit.png" alt="blackbox logo" title="blackbox" align="right" height="60" /></p>

Ansible Role: Blackbox Exporter
===============================

[![Build Status](https://ci.devops.sosoftware.pl/buildStatus/icon?job=SoInteractive/blackbox-exporter/master)](https://ci.devops.sosoftware.pl/blue/organizations/jenkins/SoInteractive%2Fblackbox-exporter/activity) [![License](https://img.shields.io/badge/license-MIT%20License-brightgreen.svg)](https://opensource.org/licenses/MIT) [![Ansible Role](https://img.shields.io/ansible/role/18268.svg)](https://galaxy.ansible.com/SoInteractive/blackbox-exporter/) [![Twitter URL](https://img.shields.io/twitter/follow/sointeractive.svg?style=social&label=Follow%20%40SoInteractive)](https://twitter.com/sointeractive)

Deploy Blackbox exporter which allows blackbox probing of endpoints over HTTP, HTTPS, DNS, TCP and ICMP.
Blackbox exporter source: https://github.com/prometheus/blackbox_exporter

Role Variables
--------------

Below are the roles variables with the respective default values. Usually you'd only change the blackbox_version.

```
blackbox_version: 0.5.0
blackbox_url: https://github.com/prometheus/blackbox_exporter/releases/download/v{{ blackbox_version }}/blackbox_exporter-{{ blackbox_version }}.linux-amd64.tar.gz
blackbox_install_dir: /opt/blackbox_exporter
blackbox_config_file: /etc/blackbox.yml
blackbox_pid_file: /var/run/blackbox.pid
blackbox_log_file: /var/log/blackbox.log
blackbox_log_level: info
blackbox_log_format: ''
blackbox_user: prometheus
blackbox_group: prometheus
blackbox_service_name: blackbox
blackbox_web_listen_address: "0.0.0.0:9115"
```

Example usage
-------------

Use it in a playbook as follows:
```yaml
- hosts: all
  become: true
  roles:
    - SoInteractive.blackbox-exporter
```

Have a look at the [defaults/main.yml](defaults/main.yml) for role variables
that can be overridden.
