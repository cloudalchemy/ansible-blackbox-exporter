<p><img src="http://jacobsmedia.com/wp-content/uploads/2015/08/black-box-edit.png" alt="blackbox logo" title="blackbox" align="right" height="60" /></p>

# Ansible Role: Blackbox Exporter

[![Build Status](https://travis-ci.org/cloudalchemy/ansible-blackbox-exporter.svg?branch=master)](https://travis-ci.org/cloudalchemy/ansible-blackbox-exporter)
[![License](https://img.shields.io/badge/license-MIT%20License-brightgreen.svg)](https://opensource.org/licenses/MIT)
[![Ansible Role](https://img.shields.io/badge/ansible%20role-cloudalchemy.blackboxexporter-blue.svg)](https://galaxy.ansible.com/cloudalchemy/blackbox-exporter/)
[![GitHub tag](https://img.shields.io/github/tag/cloudalchemy/ansible-blackbox-exporter.svg)](https://github.com/cloudalchemy/ansible-blackbox-exporter/tags)
[![IRC](https://img.shields.io/badge/chat-on%20freenode-blue.svg)](http://webchat.freenode.net/?channels=cloudalchemy)

# Description

Deploy and manage [blackbox exporter](https://github.com/prometheus/blackbox_exporter) which allows blackbox probing of endpoints over HTTP, HTTPS, DNS, TCP and ICMP.

## Requirements

- Ansible >= 2.3
- go-lang installed on deployer machine (same one where ansible is installed)

## Role Variables

All variables which can be overridden are stored in [defaults/main.yml](defaults/main.yml) file as well as in table below.

| Name           | Default Value | Description                        |
| -------------- | ------------- | -----------------------------------|
| `blackbox_exporter_version` | 0.11.0 | Blackbox exporter package version |
| `blackbox_exporter_root_dir` | /opt/blackbox_exporter | Path to directory with blackbox exporter binary file |
| `blackbox_exporter_web_listen_address` | 0.0.0.0:9115 | Address on which blackbox exporter will be listening |
| `blackbox_exporter_cli_flags` | {} | Additional configuration flags passed to blackbox exporter binary at startup |
| `blackbox_exporter_configuration_modules` | http_2xx: { prober: http, timeout: 5s, http: '' } | |

## Example

### Playbook

```yaml
- hosts: all
  become: true
  roles:
    - cloudalchemy.blackbox-exporter
```

### Demo site

We provide demo site for full monitoring solution based on prometheus and grafana. Repository with code and links to running instances is [available on github](https://github.com/cloudalchemy/demo-site) and site is hosted on [DigitalOcean](https://digitalocean.com).

## Local Testing

The preferred way of locally testing the role is to use Docker and [molecule](https://github.com/metacloud/molecule) (v1.25). You will have to install Docker on your system. See Get started for a Docker package suitable to for your system.
All packages you need to can be specified in one line:
```sh
pip install ansible ansible-lint>=3.4.15 molecule==1.25.0 docker testinfra>=1.7.0
```
This should be similiar to one listed in `.travis.yml` file in `install` section. 
After installing test suit you can run test by running
```sh
molecule test
```
For more information about molecule go to their [docs](http://molecule.readthedocs.io/en/stable-1.25/).

## Contributing

See [contributor guideline](CONTRIBUTING.md).

## License

This project is licensed under MIT License. See [LICENSE](/LICENSE) for more details.
