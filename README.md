<p><img src="http://jacobsmedia.com/wp-content/uploads/2015/08/black-box-edit.png" alt="blackbox logo" title="blackbox" align="right" height="60" /></p>

Ansible Role: Blackbox Exporter
===============================

[![Build Status](https://travis-ci.org/SoInteractive/ansible-blackbox-exporter.svg?branch=master)](https://travis-ci.org/SoInteractive/ansible-blackbox-exporter) [![License](https://img.shields.io/badge/license-MIT%20License-brightgreen.svg)](https://opensource.org/licenses/MIT) [![Ansible Role](https://img.shields.io/badge/ansible%20role-SoInteractive.blackboxexporter-blue.svg)](https://galaxy.ansible.com/SoInteractive/blackbox-exporter/) [![GitHub tag](https://img.shields.io/github/tag/sointeractive/ansible-blackbox-exporter.svg)](https://github.com/SoInteractive/ansible-blackbox-exporter/tags)  [![Twitter URL](https://img.shields.io/twitter/follow/sointeractive.svg?style=social&label=Follow%20%40SoInteractive)](https://twitter.com/sointeractive)

Deploy Blackbox exporter which allows blackbox probing of endpoints over HTTP, HTTPS, DNS, TCP and ICMP.
Blackbox exporter source: https://github.com/prometheus/blackbox_exporter

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
