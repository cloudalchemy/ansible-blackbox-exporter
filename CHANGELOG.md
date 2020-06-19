# Change Log

## [0.9.2](https://galaxy.ansible.com/cloudalchemy/blackbox-exporter) (2020-06-19)
**Merged pull requests:**

- New prometheus/blackbox\_exporter upstream release! [\#69](https://github.com/cloudalchemy/ansible-blackbox-exporter/pull/69) ([cloudalchemybot](https://github.com/cloudalchemybot))
- \[REPO SYNC\] Add passlib as a test requirement [\#67](https://github.com/cloudalchemy/ansible-blackbox-exporter/pull/67) ([cloudalchemybot](https://github.com/cloudalchemybot))

## [0.9.1](https://galaxy.ansible.com/cloudalchemy/blackbox-exporter) (2020-04-20)
**Fixed bugs:**

- ICMP probes fails on older systemd  [\#64](https://github.com/cloudalchemy/ansible-blackbox-exporter/issues/64)

**Merged pull requests:**

- \[REPO SYNC\] lock molecule to v2 [\#66](https://github.com/cloudalchemy/ansible-blackbox-exporter/pull/66) ([cloudalchemybot](https://github.com/cloudalchemybot))
- Set AmbientCapabilities=CAP\_NET\_RAW outside of the systemd\_version conditional [\#65](https://github.com/cloudalchemy/ansible-blackbox-exporter/pull/65) ([elcomtik](https://github.com/elcomtik))
- \[REPO SYNC\] Merge pull request \#4 from cloudalchemy/travis\_fix [\#62](https://github.com/cloudalchemy/ansible-blackbox-exporter/pull/62) ([cloudalchemybot](https://github.com/cloudalchemybot))

## [0.9.0](https://galaxy.ansible.com/cloudalchemy/blackbox-exporter) (2020-01-11)
**Fixed bugs:**

- systemd version fails to parse correctly on Debian 10 [\#57](https://github.com/cloudalchemy/ansible-blackbox-exporter/issues/57)

**Merged pull requests:**

- Switch user login shell to /usr/sbin/nologin [\#61](https://github.com/cloudalchemy/ansible-blackbox-exporter/pull/61) ([paulfantom](https://github.com/paulfantom))
- \[REPO SYNC\] use latest available python [\#60](https://github.com/cloudalchemy/ansible-blackbox-exporter/pull/60) ([cloudalchemybot](https://github.com/cloudalchemybot))
- preflight: Fix detection of systemd version for systemd 240+ [\#58](https://github.com/cloudalchemy/ansible-blackbox-exporter/pull/58) ([lae](https://github.com/lae))
- \[REPO SYNC\] remove IRC link [\#56](https://github.com/cloudalchemy/ansible-blackbox-exporter/pull/56) ([cloudalchemybot](https://github.com/cloudalchemybot))
- \[REPO SYNC\] add declarative label sync; add autolabelling PRs [\#55](https://github.com/cloudalchemy/ansible-blackbox-exporter/pull/55) ([cloudalchemybot](https://github.com/cloudalchemybot))
- molecule: add alternative test scenario; fix default test scenario [\#53](https://github.com/cloudalchemy/ansible-blackbox-exporter/pull/53) ([paulfantom](https://github.com/paulfantom))
- \[REPO SYNC\] molecule: use CI images from quay.io instead of dockerhub [\#52](https://github.com/cloudalchemy/ansible-blackbox-exporter/pull/52) ([cloudalchemybot](https://github.com/cloudalchemybot))
- New prometheus/blackbox\_exporter upstream release! [\#51](https://github.com/cloudalchemy/ansible-blackbox-exporter/pull/51) ([cloudalchemybot](https://github.com/cloudalchemybot))
- \[REPO SYNC\] Update releaser.sh [\#50](https://github.com/cloudalchemy/ansible-blackbox-exporter/pull/50) ([cloudalchemybot](https://github.com/cloudalchemybot))
- tasks/preflight.yml: fixed systemd version fact parsing [\#49](https://github.com/cloudalchemy/ansible-blackbox-exporter/pull/49) ([elcomtik](https://github.com/elcomtik))

## [0.8.0](https://galaxy.ansible.com/cloudalchemy/blackbox-exporter) (2019-10-24)
**Closed issues:**

- Default module configuration missing status codes [\#32](https://github.com/cloudalchemy/ansible-blackbox-exporter/issues/32)

**Merged pull requests:**

- \[REPO SYNC\] add support for CentOS8 [\#47](https://github.com/cloudalchemy/ansible-blackbox-exporter/pull/47) ([cloudalchemybot](https://github.com/cloudalchemybot))
- New prometheus/blackbox\_exporter upstream release! [\#46](https://github.com/cloudalchemy/ansible-blackbox-exporter/pull/46) ([cloudalchemybot](https://github.com/cloudalchemybot))
- templates/blackbox\_exporter.service.j2: allow icmp probe [\#45](https://github.com/cloudalchemy/ansible-blackbox-exporter/pull/45) ([lborguetti](https://github.com/lborguetti))
- New prometheus/blackbox\_exporter upstream release! [\#44](https://github.com/cloudalchemy/ansible-blackbox-exporter/pull/44) ([cloudalchemybot](https://github.com/cloudalchemybot))
- Synchronize files from cloudalchemy/skeleton [\#43](https://github.com/cloudalchemy/ansible-blackbox-exporter/pull/43) ([cloudalchemybot](https://github.com/cloudalchemybot))
- increase systemd service security [\#42](https://github.com/cloudalchemy/ansible-blackbox-exporter/pull/42) ([paulfantom](https://github.com/paulfantom))
- Synchronize files from cloudalchemy/skeleton [\#41](https://github.com/cloudalchemy/ansible-blackbox-exporter/pull/41) ([cloudalchemybot](https://github.com/cloudalchemybot))
- Update minimum required ansible version [\#40](https://github.com/cloudalchemy/ansible-blackbox-exporter/pull/40) ([cloudalchemybot](https://github.com/cloudalchemybot))
- Moving to python 3 and dropping support for python 2.x \(on deployer host\) [\#39](https://github.com/cloudalchemy/ansible-blackbox-exporter/pull/39) ([cloudalchemybot](https://github.com/cloudalchemybot))
- Synchronize files from cloudalchemy/skeleton [\#37](https://github.com/cloudalchemy/ansible-blackbox-exporter/pull/37) ([cloudalchemybot](https://github.com/cloudalchemybot))
- added restartsec and startlimitinterval configurations [\#36](https://github.com/cloudalchemy/ansible-blackbox-exporter/pull/36) ([oguzhaninan](https://github.com/oguzhaninan))
- add simple preflight checks [\#35](https://github.com/cloudalchemy/ansible-blackbox-exporter/pull/35) ([paulfantom](https://github.com/paulfantom))
- Added default module options to exporter [\#33](https://github.com/cloudalchemy/ansible-blackbox-exporter/pull/33) ([brokoli18](https://github.com/brokoli18))
- Synchronize files from cloudalchemy/skeleton [\#31](https://github.com/cloudalchemy/ansible-blackbox-exporter/pull/31) ([cloudalchemybot](https://github.com/cloudalchemybot))
- Wait for network to be online [\#30](https://github.com/cloudalchemy/ansible-blackbox-exporter/pull/30) ([paulfantom](https://github.com/paulfantom))

## [0.7.1](https://galaxy.ansible.com/cloudalchemy/blackbox-exporter) (2019-03-23)
**Merged pull requests:**

- New blackbox\_exporter upstream release! [\#29](https://github.com/cloudalchemy/ansible-blackbox-exporter/pull/29) ([cloudalchemybot](https://github.com/cloudalchemybot))

## [0.7.0](https://galaxy.ansible.com/cloudalchemy/blackbox-exporter) (2018-12-05)
**Merged pull requests:**

- Always install in /usr/local/bin & role cleanup [\#28](https://github.com/cloudalchemy/ansible-blackbox-exporter/pull/28) ([paulfantom](https://github.com/paulfantom))
- New blackbox\_exporter upstream release! [\#27](https://github.com/cloudalchemy/ansible-blackbox-exporter/pull/27) ([cloudalchemybot](https://github.com/cloudalchemybot))
- Mention gnu-tar requirement [\#26](https://github.com/cloudalchemy/ansible-blackbox-exporter/pull/26) ([jstaffans](https://github.com/jstaffans))

## [0.6.2](https://galaxy.ansible.com/cloudalchemy/blackbox-exporter) (2018-10-08)
**Merged pull requests:**

- move to ansible 2.7 [\#25](https://github.com/cloudalchemy/ansible-blackbox-exporter/pull/25) ([paulfantom](https://github.com/paulfantom))

## [0.6.1](https://galaxy.ansible.com/cloudalchemy/blackbox-exporter) (2018-09-06)
## [0.6.0](https://galaxy.ansible.com/cloudalchemy/blackbox-exporter) (2018-07-01)
**Merged pull requests:**

- use tox, ansible 2.6, and allow using remote docker host [\#23](https://github.com/cloudalchemy/ansible-blackbox-exporter/pull/23) ([paulfantom](https://github.com/paulfantom))

## [0.5.11](https://galaxy.ansible.com/cloudalchemy/blackbox-exporter) (2018-05-27)
**Fixed bugs:**

- fix architecture var parsing [\#22](https://github.com/cloudalchemy/ansible-blackbox-exporter/pull/22) ([paulfantom](https://github.com/paulfantom))

**Merged pull requests:**

- upgrade to molecule 2.x [\#21](https://github.com/cloudalchemy/ansible-blackbox-exporter/pull/21) ([paulfantom](https://github.com/paulfantom))
- Use newer test filter schema to get rid of some deprecation warnings. [\#20](https://github.com/cloudalchemy/ansible-blackbox-exporter/pull/20) ([swesterveld](https://github.com/swesterveld))

## [0.5.10](https://galaxy.ansible.com/cloudalchemy/blackbox-exporter) (2018-04-17)
**Merged pull requests:**

- python 2 and 3 compatibility [\#19](https://github.com/cloudalchemy/ansible-blackbox-exporter/pull/19) ([paulfantom](https://github.com/paulfantom))

## [0.5.9](https://galaxy.ansible.com/cloudalchemy/blackbox-exporter) (2018-04-05)
**Merged pull requests:**

- Retry when connecting to external services [\#17](https://github.com/cloudalchemy/ansible-blackbox-exporter/pull/17) ([paulfantom](https://github.com/paulfantom))

## [0.5.8](https://galaxy.ansible.com/cloudalchemy/blackbox-exporter) (2018-03-26)
**Merged pull requests:**

- Ubuntu bionic \(18.04\) support [\#15](https://github.com/cloudalchemy/ansible-blackbox-exporter/pull/15) ([paulfantom](https://github.com/paulfantom))

## [0.5.7](https://galaxy.ansible.com/cloudalchemy/blackbox-exporter) (2018-03-24)
**Merged pull requests:**

- ansible 2.5 [\#16](https://github.com/cloudalchemy/ansible-blackbox-exporter/pull/16) ([paulfantom](https://github.com/paulfantom))

## [0.5.6](https://galaxy.ansible.com/cloudalchemy/blackbox-exporter) (2018-03-02)
**Merged pull requests:**

- Upgrade default blackbox\_exporter version [\#14](https://github.com/cloudalchemy/ansible-blackbox-exporter/pull/14) ([paulfantom](https://github.com/paulfantom))

## [0.5.5](https://galaxy.ansible.com/cloudalchemy/blackbox-exporter) (2018-02-14)
**Merged pull requests:**

- Make Prometheus blackbox exporter restart/reload with sudo privileges. [\#13](https://github.com/cloudalchemy/ansible-blackbox-exporter/pull/13) ([swesterveld](https://github.com/swesterveld))

## [0.5.4](https://galaxy.ansible.com/cloudalchemy/blackbox-exporter) (2018-02-01)
**Merged pull requests:**

- move to systemd logs [\#12](https://github.com/cloudalchemy/ansible-blackbox-exporter/pull/12) ([paulfantom](https://github.com/paulfantom))

## [0.5.3](https://galaxy.ansible.com/cloudalchemy/blackbox-exporter) (2018-01-14)
**Fixed bugs:**

- Include package for setcap [\#9](https://github.com/cloudalchemy/ansible-blackbox-exporter/issues/9)

**Merged pull requests:**

- support more OSes; move to custom docker images; refactor tests [\#11](https://github.com/cloudalchemy/ansible-blackbox-exporter/pull/11) ([paulfantom](https://github.com/paulfantom))

## [0.5.2](https://galaxy.ansible.com/cloudalchemy/blackbox-exporter) (2018-01-11)
**Merged pull requests:**

- Debian support; better tests; fixed capabilities [\#10](https://github.com/cloudalchemy/ansible-blackbox-exporter/pull/10) ([paulfantom](https://github.com/paulfantom))

## [0.5.1](https://galaxy.ansible.com/cloudalchemy/blackbox-exporter) (2018-01-07)
**Merged pull requests:**

- added i386 arch [\#8](https://github.com/cloudalchemy/ansible-blackbox-exporter/pull/8) ([rdemachkovych](https://github.com/rdemachkovych))
- docs [\#7](https://github.com/cloudalchemy/ansible-blackbox-exporter/pull/7) ([paulfantom](https://github.com/paulfantom))

## [0.5.0](https://galaxy.ansible.com/cloudalchemy/blackbox-exporter) (2018-01-02)
**Merged pull requests:**

- Update generatetag.sh [\#6](https://github.com/cloudalchemy/ansible-blackbox-exporter/pull/6) ([paulfantom](https://github.com/paulfantom))
- support older raspberry pi [\#5](https://github.com/cloudalchemy/ansible-blackbox-exporter/pull/5) ([paulfantom](https://github.com/paulfantom))

## [0.4.7](https://galaxy.ansible.com/cloudalchemy/blackbox-exporter) (2017-12-27)
**Merged pull requests:**

- Fix ARMv7 auto detection [\#4](https://github.com/cloudalchemy/ansible-blackbox-exporter/pull/4) ([paulfantom](https://github.com/paulfantom))

## [0.4.6](https://galaxy.ansible.com/cloudalchemy/blackbox-exporter) (2017-12-15)
**Merged pull requests:**

- auto set go architecture [\#2](https://github.com/cloudalchemy/ansible-blackbox-exporter/pull/2) ([paulfantom](https://github.com/paulfantom))

## [0.4.5](https://galaxy.ansible.com/cloudalchemy/blackbox-exporter) (2017-12-15)
**Merged pull requests:**

- bump version; better systemd service file [\#3](https://github.com/cloudalchemy/ansible-blackbox-exporter/pull/3) ([paulfantom](https://github.com/paulfantom))

## [0.4.4](https://galaxy.ansible.com/cloudalchemy/blackbox-exporter) (2017-12-04)
## [0.4.3](https://galaxy.ansible.com/cloudalchemy/blackbox-exporter) (2017-11-30)
## [0.4.2](https://galaxy.ansible.com/cloudalchemy/blackbox-exporter) (2017-11-30)
## [0.4.1](https://galaxy.ansible.com/cloudalchemy/blackbox-exporter) (2017-11-28)
**Merged pull requests:**

- fix CI; remove company from role description [\#1](https://github.com/cloudalchemy/ansible-blackbox-exporter/pull/1) ([paulfantom](https://github.com/paulfantom))

## [0.4.0](https://galaxy.ansible.com/cloudalchemy/blackbox-exporter) (2017-10-16)
## [0.3.1](https://galaxy.ansible.com/cloudalchemy/blackbox-exporter) (2017-10-05)
## [0.3.0](https://galaxy.ansible.com/cloudalchemy/blackbox-exporter) (2017-07-21)
## [0.2.0](https://galaxy.ansible.com/cloudalchemy/blackbox-exporter) (2017-07-21)
## [0.1.3](https://galaxy.ansible.com/cloudalchemy/blackbox-exporter) (2017-07-19)
## [0.1.4](https://galaxy.ansible.com/cloudalchemy/blackbox-exporter) (2017-07-19)
## [0.1.1](https://galaxy.ansible.com/cloudalchemy/blackbox-exporter) (2017-06-14)
## [0.1.2](https://galaxy.ansible.com/cloudalchemy/blackbox-exporter) (2017-06-14)
## [0.1.0](https://galaxy.ansible.com/cloudalchemy/blackbox-exporter) (2017-06-05)
## [0.0.1](https://galaxy.ansible.com/cloudalchemy/blackbox-exporter) (2017-05-16)


\* *This Change Log was automatically generated by [github_changelog_generator](https://github.com/skywinder/Github-Changelog-Generator)*