<p><img src="http://jacobsmedia.com/wp-content/uploads/2015/08/black-box-edit.png" alt="blackbox logo" title="blackbox" align="right" height="60" /></p>

# Ansible Role: Blackbox Exporter

[![Build Status](https://travis-ci.org/cloudalchemy/ansible-blackbox-exporter.svg?branch=master)](https://travis-ci.org/cloudalchemy/ansible-blackbox-exporter)
[![License](https://img.shields.io/badge/license-MIT%20License-brightgreen.svg)](https://opensource.org/licenses/MIT)
[![Ansible Role](https://img.shields.io/badge/ansible%20role-cloudalchemy.blackbox_exporter-blue.svg)](https://galaxy.ansible.com/cloudalchemy/blackbox-exporter/)
[![GitHub tag](https://img.shields.io/github/tag/cloudalchemy/ansible-blackbox-exporter.svg)](https://github.com/cloudalchemy/ansible-blackbox-exporter/tags)
[![IRC](https://img.shields.io/badge/irc.freenode.net-%23cloudalchemy-yellow.svg)](https://kiwiirc.com/nextclient/#ircs://irc.freenode.net/#cloudalchemy)

# Description

Deploy and manage [blackbox exporter](https://github.com/prometheus/blackbox_exporter) which allows blackbox probing of endpoints over HTTP, HTTPS, DNS, TCP and ICMP.

## Requirements

- Ansible >= 2.5 (It might work on previous versions, but we cannot guarantee it)
- gnu-tar on Mac deployer host (`brew install gnu-tar`)

## Role Variables

All variables which can be overridden are stored in [defaults/main.yml](defaults/main.yml) file as well as in table below.

| Name           | Default Value | Description                        |
| -------------- | ------------- | -----------------------------------|
| `blackbox_exporter_version` | 0.13.0 | Blackbox exporter package version |
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

The preferred way of locally testing the role is to use Docker and [molecule](https://github.com/metacloud/molecule) (v2.x). You will have to install Docker on your system. See "Get started" for a Docker package suitable to for your system.
We are using tox to simplify process of testing on multiple ansible versions. To install tox execute:
```sh
pip install tox
```
To run tests on all ansible versions (WARNING: this can take some time)
```sh
tox
```
To run a custom molecule command on custom environment with only default test scenario:
```sh
tox -e py27-ansible25 -- molecule test -s default
```
For more information about molecule go to their [docs](http://molecule.readthedocs.io/en/latest/).

If you would like to run tests on remote docker host just specify `DOCKER_HOST` variable before running tox tests.

## Travis CI

Combining molecule and travis CI allows us to test how new PRs will behave when used with multiple ansible versions and multiple operating systems. This also allows use to create test scenarios for different role configurations. As a result we have a quite large test matrix (42 parallel role executions in case of [ansible-prometheus](https://github.com/cloudalchemy/ansible-prometheus)) which will take more time than local testing, so please be patient.

## Contributing

See [contributor guideline](CONTRIBUTING.md).

## License

This project is licensed under MIT License. See [LICENSE](/LICENSE) for more details.
