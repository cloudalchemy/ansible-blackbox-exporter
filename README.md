Ansible role for Blackbox Exporter 
=========================================

This role installs Blackbox exporter that allows blackbox probing of endpoints over HTTP, HTTPS, DNS, TCP and ICMP.
Blackbox source: https://github.com/prometheus/blackbox_exporter

Role Variables
--------------

Below are the roles variables with the respective default values. Usually you'd only change the blackbox_version.

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

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: ansible-blackbox-exporter, blackbox_version: 0.2.0 }

Test
----


