# Change Log

## [**Next release**](https://galaxy.ansible.com/Roman Demachkovych, Pawel Krupa/null)

## [1.0.0] - 2021-04-25
**Merged pull requests:**

- Merge pull request [#80](https://github.com/cloudalchemy/ansible-blackbox-exporter/issues/80) from cloudalchemy/skeleton
- :robot: sync with cloudalchemy/skeleton (SHA: 5ca88c27): Merge pull request [#9](https://github.com/cloudalchemy/ansible-blackbox-exporter/issues/9) from cloudalchemy/superq/more_updates
- Merge pull request [#77](https://github.com/cloudalchemy/ansible-blackbox-exporter/issues/77) from kmille/master
- Remove PIDfile from systemd unit file [#76](https://github.com/cloudalchemy/ansible-blackbox-exporter/issues/76)


## [0.9.3] - 2020-10-12
**Merged pull requests:**

- Only run capabilities module in apply mode. ([#73](https://github.com/cloudalchemy/ansible-blackbox-exporter/issues/73))
- [REPO SYNC] add troubleshooting doc skeleton ([#71](https://github.com/cloudalchemy/ansible-blackbox-exporter/issues/71))


## [0.9.2] - 2020-06-19
**Merged pull requests:**

- [REPO SYNC] Add passlib as a test requirement ([#67](https://github.com/cloudalchemy/ansible-blackbox-exporter/issues/67))


## [0.9.1] - 2020-04-20
**Merged pull requests:**

- :robot: sync with cloudalchemy/skeleton (SHA: 40e7ce18): lock molecule to v2 ([#66](https://github.com/cloudalchemy/ansible-blackbox-exporter/issues/66))
- Set AmbientCapabilities=CAP_NET_RAW outside of the systemd_versio… ([#65](https://github.com/cloudalchemy/ansible-blackbox-exporter/issues/65))
- :robot: sync with cloudalchemy/skeleton (SHA: 69fc5be8): Merge pull request [#4](https://github.com/cloudalchemy/ansible-blackbox-exporter/issues/4) from cloudalchemy/travis_fix ([#62](https://github.com/cloudalchemy/ansible-blackbox-exporter/issues/62))


## [0.9.0] - 2020-01-11
**Merged pull requests:**

- Switch user login shell to /usr/sbin/nologin ([#61](https://github.com/cloudalchemy/ansible-blackbox-exporter/issues/61))
- :robot: sync with cloudalchemy/skeleton (SHA: f4521f6a): use latest available python ([#60](https://github.com/cloudalchemy/ansible-blackbox-exporter/issues/60))
- preflight: Fix detection of systemd version for systemd 240+ ([#58](https://github.com/cloudalchemy/ansible-blackbox-exporter/issues/58))
- :robot: sync with cloudalchemy/skeleton (SHA: bb0f0949): remove IRC link ([#56](https://github.com/cloudalchemy/ansible-blackbox-exporter/issues/56))
- molecule: add alternative test scenario; fix default test scenario ([#53](https://github.com/cloudalchemy/ansible-blackbox-exporter/issues/53))
- [REPO SYNC] add declarative label sync; add autolabelling PRs ([#55](https://github.com/cloudalchemy/ansible-blackbox-exporter/issues/55))
- [REPO SYNC] molecule: use CI images from quay.io instead of docke… ([#52](https://github.com/cloudalchemy/ansible-blackbox-exporter/issues/52))
- :tada: automated upstream release update ([#51](https://github.com/cloudalchemy/ansible-blackbox-exporter/issues/51))
- [REPO SYNC] Update releaser.sh ([#50](https://github.com/cloudalchemy/ansible-blackbox-exporter/issues/50))
- tasks/preflight.yml: fixed systemd version fact parsing ([#49](https://github.com/cloudalchemy/ansible-blackbox-exporter/issues/49))


## [0.8.0] - 2019-10-24
**Merged pull requests:**

- :robot: sync with cloudalchemy/skeleton (SHA: 8cf4d397): add support for CentOS8 ([#47](https://github.com/cloudalchemy/ansible-blackbox-exporter/issues/47))
- New prometheus/blackbox_exporter upstream release! ([#46](https://github.com/cloudalchemy/ansible-blackbox-exporter/issues/46))
- New prometheus/blackbox_exporter upstream release! ([#44](https://github.com/cloudalchemy/ansible-blackbox-exporter/issues/44))
- templates/blackbox_exporter.service.j2: allow icmp probe ([#45](https://github.com/cloudalchemy/ansible-blackbox-exporter/issues/45))
- Synchronize files from cloudalchemy/skeleton ([#43](https://github.com/cloudalchemy/ansible-blackbox-exporter/issues/43))
- Synchronize files from cloudalchemy/skeleton ([#41](https://github.com/cloudalchemy/ansible-blackbox-exporter/issues/41))
- increase systemd service security ([#42](https://github.com/cloudalchemy/ansible-blackbox-exporter/issues/42))
- :robot: synchronize with last commit in cloudalchemy/skeleton (SHA: 1f68dc21) ([#40](https://github.com/cloudalchemy/ansible-blackbox-exporter/issues/40))
- Moving to python 3 and dropping support for python 2.x (on deploy… ([#39](https://github.com/cloudalchemy/ansible-blackbox-exporter/issues/39))
- :robot: synchronize files from cloudalchemy/skeleton ([#37](https://github.com/cloudalchemy/ansible-blackbox-exporter/issues/37))
- added restartsec and startlimitinterval configurations ([#36](https://github.com/cloudalchemy/ansible-blackbox-exporter/issues/36))
- add simple preflight checks ([#35](https://github.com/cloudalchemy/ansible-blackbox-exporter/issues/35))
- Added default module options to exporter ([#33](https://github.com/cloudalchemy/ansible-blackbox-exporter/issues/33))
- Wait for network to be online ([#30](https://github.com/cloudalchemy/ansible-blackbox-exporter/issues/30))
- Synchronize files from cloudalchemy/skeleton ([#31](https://github.com/cloudalchemy/ansible-blackbox-exporter/issues/31))


## [0.7.1] - 2019-03-23
**Merged pull requests:**

- New blackbox_exporter upstream release! ([#29](https://github.com/cloudalchemy/ansible-blackbox-exporter/issues/29))


## [0.7.0] - 2018-12-05
**Merged pull requests:**

- Always install in /usr/local/bin & role cleanup ([#28](https://github.com/cloudalchemy/ansible-blackbox-exporter/issues/28))
- New blackbox_exporter upstream release! ([#27](https://github.com/cloudalchemy/ansible-blackbox-exporter/issues/27))
- Mention gnu-tar requirement ([#26](https://github.com/cloudalchemy/ansible-blackbox-exporter/issues/26))


## [0.6.2] - 2018-10-08
**Merged pull requests:**

- move to ansible 2.7 ([#25](https://github.com/cloudalchemy/ansible-blackbox-exporter/issues/25))


## [0.6.1] - 2018-09-06

## [0.6.0] - 2018-07-01
**Merged pull requests:**

- use tox, ansible 2.6, and allow using remote docker host ([#23](https://github.com/cloudalchemy/ansible-blackbox-exporter/issues/23))


## [0.5.11] - 2018-05-27
**Merged pull requests:**

- fix architecture var parsing ([#22](https://github.com/cloudalchemy/ansible-blackbox-exporter/issues/22))
- upgrade to molecule 2.x ([#21](https://github.com/cloudalchemy/ansible-blackbox-exporter/issues/21))
- Merge pull request [#20](https://github.com/cloudalchemy/ansible-blackbox-exporter/issues/20) from swesterveld/fix-deprecation-warnings


## [0.5.10] - 2018-04-17
**Merged pull requests:**

- Merge pull request [#19](https://github.com/cloudalchemy/ansible-blackbox-exporter/issues/19) from cloudalchemy/python3


## [0.5.9] - 2018-04-05
**Merged pull requests:**

- Merge pull request [#17](https://github.com/cloudalchemy/ansible-blackbox-exporter/issues/17) from cloudalchemy/paulfantom-patch-1


## [0.5.8] - 2018-03-26
**Merged pull requests:**

- Merge pull request [#15](https://github.com/cloudalchemy/ansible-blackbox-exporter/issues/15) from cloudalchemy/bionic


## [0.5.7] - 2018-03-24
**Merged pull requests:**

- Merge pull request [#16](https://github.com/cloudalchemy/ansible-blackbox-exporter/issues/16) from cloudalchemy/new_ansible


## [0.5.6] - 2018-03-02
**Merged pull requests:**

- Merge pull request [#14](https://github.com/cloudalchemy/ansible-blackbox-exporter/issues/14) from cloudalchemy/version_0.12.0


## [0.5.5] - 2018-02-14
**Merged pull requests:**

- Merge pull request [#13](https://github.com/cloudalchemy/ansible-blackbox-exporter/issues/13) from swesterveld/fix_daemon_reload_for_role_include


## [0.5.4] - 2018-02-01
**Merged pull requests:**

- Merge pull request [#12](https://github.com/cloudalchemy/ansible-blackbox-exporter/issues/12) from cloudalchemy/systemd_logs


## [0.5.3] - 2018-01-14
**Merged pull requests:**

- Merge pull request [#11](https://github.com/cloudalchemy/ansible-blackbox-exporter/issues/11) from cloudalchemy/dockerfiles


## [0.5.2] - 2018-01-11
**Merged pull requests:**

- Merge pull request [#10](https://github.com/cloudalchemy/ansible-blackbox-exporter/issues/10) from cloudalchemy/issue9


## [0.5.1] - 2018-01-07
**Merged pull requests:**

- Merge pull request [#8](https://github.com/cloudalchemy/ansible-blackbox-exporter/issues/8) from cloudalchemy/add_arch
- Merge pull request [#7](https://github.com/cloudalchemy/ansible-blackbox-exporter/issues/7) from cloudalchemy/docs


## [0.5.0] - 2018-01-02
**Merged pull requests:**

- Merge pull request [#6](https://github.com/cloudalchemy/ansible-blackbox-exporter/issues/6) from cloudalchemy/paulfantom-patch-1
- Merge pull request [#5](https://github.com/cloudalchemy/ansible-blackbox-exporter/issues/5) from cloudalchemy/raspberrypi


## [0.4.7] - 2017-12-27
**Merged pull requests:**

- Merge pull request [#4](https://github.com/cloudalchemy/ansible-blackbox-exporter/issues/4) from cloudalchemy/paulfantom-patch-1


## [0.4.6] - 2017-12-15
**Merged pull requests:**

- Merge pull request [#2](https://github.com/cloudalchemy/ansible-blackbox-exporter/issues/2) from cloudalchemy/go_arch


## [0.4.5] - 2017-12-15
**Merged pull requests:**

- Merge pull request [#3](https://github.com/cloudalchemy/ansible-blackbox-exporter/issues/3) from cloudalchemy/service


## [0.4.4] - 2017-12-04

## [0.4.3] - 2017-11-30

## [0.4.2] - 2017-11-30

## [0.4.1] - 2017-11-29
**Merged pull requests:**

- Merge pull request [#1](https://github.com/cloudalchemy/ansible-blackbox-exporter/issues/1) from cloudalchemy/ci


## [0.4.0] - 2017-10-16
**Merged pull requests:**

- Merge pull request [#7](https://github.com/cloudalchemy/ansible-blackbox-exporter/issues/7) from SoInteractive/feature_travis


## [0.3.1] - 2017-10-05
**Merged pull requests:**

- Merge pull request [#6](https://github.com/cloudalchemy/ansible-blackbox-exporter/issues/6) from SoInteractive/systemd
- Merge pull request [#5](https://github.com/cloudalchemy/ansible-blackbox-exporter/issues/5) from paulfantom/feature_install


## [0.2.0] - 2017-07-21

## [0.3.0] - 2017-07-21
**Merged pull requests:**

- Merge pull request [#4](https://github.com/cloudalchemy/ansible-blackbox-exporter/issues/4) from SoInteractive/feature_autoupdate_minor


## [0.1.3] - 2017-07-19

## [0.1.4] - 2017-07-19
**Merged pull requests:**

- Merge pull request [#2](https://github.com/cloudalchemy/ansible-blackbox-exporter/issues/2) from SoInteractive/update


## [0.1.1] - 2017-06-14

## [0.1.2] - 2017-06-14
**Merged pull requests:**

- Merge pull request [#1](https://github.com/cloudalchemy/ansible-blackbox-exporter/issues/1) from SoInteractive/tgrzesik-patch-1


## [0.1.0] - 2017-06-05

## 0.0.1 - 2017-05-30

[Unreleased]: https://github.com/cloudalchemy/ansible-blackbox-exporter/compare/1.0.0...HEAD
[1.0.0]: https://github.com/cloudalchemy/ansible-blackbox-exporter/compare/0.9.3...1.0.0
[0.9.3]: https://github.com/cloudalchemy/ansible-blackbox-exporter/compare/0.9.2...0.9.3
[0.9.2]: https://github.com/cloudalchemy/ansible-blackbox-exporter/compare/0.9.1...0.9.2
[0.9.1]: https://github.com/cloudalchemy/ansible-blackbox-exporter/compare/0.9.0...0.9.1
[0.9.0]: https://github.com/cloudalchemy/ansible-blackbox-exporter/compare/0.8.0...0.9.0
[0.8.0]: https://github.com/cloudalchemy/ansible-blackbox-exporter/compare/0.7.1...0.8.0
[0.7.1]: https://github.com/cloudalchemy/ansible-blackbox-exporter/compare/0.7.0...0.7.1
[0.7.0]: https://github.com/cloudalchemy/ansible-blackbox-exporter/compare/0.6.2...0.7.0
[0.6.2]: https://github.com/cloudalchemy/ansible-blackbox-exporter/compare/0.6.1...0.6.2
[0.6.1]: https://github.com/cloudalchemy/ansible-blackbox-exporter/compare/0.6.0...0.6.1
[0.6.0]: https://github.com/cloudalchemy/ansible-blackbox-exporter/compare/0.5.11...0.6.0
[0.5.11]: https://github.com/cloudalchemy/ansible-blackbox-exporter/compare/0.5.10...0.5.11
[0.5.10]: https://github.com/cloudalchemy/ansible-blackbox-exporter/compare/0.5.9...0.5.10
[0.5.9]: https://github.com/cloudalchemy/ansible-blackbox-exporter/compare/0.5.8...0.5.9
[0.5.8]: https://github.com/cloudalchemy/ansible-blackbox-exporter/compare/0.5.7...0.5.8
[0.5.7]: https://github.com/cloudalchemy/ansible-blackbox-exporter/compare/0.5.6...0.5.7
[0.5.6]: https://github.com/cloudalchemy/ansible-blackbox-exporter/compare/0.5.5...0.5.6
[0.5.5]: https://github.com/cloudalchemy/ansible-blackbox-exporter/compare/0.5.4...0.5.5
[0.5.4]: https://github.com/cloudalchemy/ansible-blackbox-exporter/compare/0.5.3...0.5.4
[0.5.3]: https://github.com/cloudalchemy/ansible-blackbox-exporter/compare/0.5.2...0.5.3
[0.5.2]: https://github.com/cloudalchemy/ansible-blackbox-exporter/compare/0.5.1...0.5.2
[0.5.1]: https://github.com/cloudalchemy/ansible-blackbox-exporter/compare/0.5.0...0.5.1
[0.5.0]: https://github.com/cloudalchemy/ansible-blackbox-exporter/compare/0.4.7...0.5.0
[0.4.7]: https://github.com/cloudalchemy/ansible-blackbox-exporter/compare/0.4.6...0.4.7
[0.4.6]: https://github.com/cloudalchemy/ansible-blackbox-exporter/compare/0.4.5...0.4.6
[0.4.5]: https://github.com/cloudalchemy/ansible-blackbox-exporter/compare/0.4.4...0.4.5
[0.4.4]: https://github.com/cloudalchemy/ansible-blackbox-exporter/compare/0.4.3...0.4.4
[0.4.3]: https://github.com/cloudalchemy/ansible-blackbox-exporter/compare/0.4.2...0.4.3
[0.4.2]: https://github.com/cloudalchemy/ansible-blackbox-exporter/compare/0.4.1...0.4.2
[0.4.1]: https://github.com/cloudalchemy/ansible-blackbox-exporter/compare/0.4.0...0.4.1
[0.4.0]: https://github.com/cloudalchemy/ansible-blackbox-exporter/compare/0.3.1...0.4.0
[0.3.1]: https://github.com/cloudalchemy/ansible-blackbox-exporter/compare/0.2.0...0.3.1
[0.2.0]: https://github.com/cloudalchemy/ansible-blackbox-exporter/compare/0.3.0...0.2.0
[0.3.0]: https://github.com/cloudalchemy/ansible-blackbox-exporter/compare/0.1.3...0.3.0
[0.1.3]: https://github.com/cloudalchemy/ansible-blackbox-exporter/compare/0.1.4...0.1.3
[0.1.4]: https://github.com/cloudalchemy/ansible-blackbox-exporter/compare/0.1.1...0.1.4
[0.1.1]: https://github.com/cloudalchemy/ansible-blackbox-exporter/compare/0.1.2...0.1.1
[0.1.2]: https://github.com/cloudalchemy/ansible-blackbox-exporter/compare/0.1.0...0.1.2
[0.1.0]: https://github.com/cloudalchemy/ansible-blackbox-exporter/compare/0.0.1...0.1.0
