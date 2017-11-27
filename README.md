<p><img src="http://jacobsmedia.com/wp-content/uploads/2015/08/black-box-edit.png" alt="blackbox logo" title="blackbox" align="right" height="60" /></p>

Ansible Role: Blackbox Exporter
===============================

[![Build Status](https://travis-ci.org/cloudalchemy/ansible-blackbox-exporter.svg?branch=master)](https://travis-ci.org/cloudalchemy/ansible-blackbox-exporter) [![License](https://img.shields.io/badge/license-MIT%20License-brightgreen.svg)](https://opensource.org/licenses/MIT) [![Ansible Role](https://img.shields.io/badge/ansible%20role-cloudalchemy.blackboxexporter-blue.svg)](https://galaxy.ansible.com/cloudalchemy/blackbox-exporter/) [![GitHub tag](https://img.shields.io/github/tag/cloudalchemy/ansible-blackbox-exporter.svg)](https://github.com/cloudalchemy/ansible-blackbox-exporter/tags)

Deploy Blackbox exporter which allows blackbox probing of endpoints over HTTP, HTTPS, DNS, TCP and ICMP.
Blackbox exporter source: https://github.com/prometheus/blackbox_exporter

Example usage
-------------

Use it in a playbook as follows:
```yaml
- hosts: all
  become: true
  roles:
    - cloudalchemy.blackbox-exporter
```

Have a look at the [defaults/main.yml](defaults/main.yml) for role variables
that can be overridden.
