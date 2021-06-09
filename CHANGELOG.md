# Change Log
All notable changes to this project will be documented in this file.
This project adheres to [Semantic Versioning](http://semver.org/) and [Keep a changelog](https://github.com/olivierlacan/keep-a-changelog).

## [Unreleased](https://github.com/idealista/prometheus_server_role/tree/develop)
### Fixed
### Added
### Changed
### Removed

### Added
- [#53](https://github.com/idealista/prometheus_server_role/issues/53) *[BUG] Change prometheus user shell path in /etc/passwd* @marcelogalmor

## [1.10.0](https://github.com/idealista/prometheus_server_role/tree/1.10.0)
## [Full Changelog](https://github.com/idealista/prometheus_server_role/compare/1.9.0...1.10.0)
### Added
- *[#49](https://github.com/idealista/prometheus_server_role/issues/49) Promtool testing before deploying* @blalop

## [1.9.0](https://github.com/idealista/prometheus_server_role/tree/1.9.0)
## [Full Changelog](https://github.com/idealista/prometheus_server_role/compare/1.8.0...1.9.0)
### Changed
- *Upgraded to molecule 3 and more tests* @blalop
- *Optional logrotate config* @blalop

## [1.8.0](https://github.com/idealista/prometheus_server_role/tree/1.8.0)
## [Full Changelog](https://github.com/idealista/prometheus_server_role/compare/1.7.0...1.8.0)
### Added
- *[#40](https://github.com/idealista/prometheus_server_role/issues/40) [FEATURE] Remote write tuning support* @emepege

## [1.7.0](https://github.com/idealista/prometheus_server_role/tree/1.7.0) (2021-02-09)
## [Full Changelog](https://github.com/idealista/prometheus_server_role/compare/1.0.6...1.0.7)
### Added
- *[#37](https://github.com/idealista/prometheus_server_role/issues/37) Replace copy with template with custom delimiters for rules* @caldito

## [1.6.0](https://github.com/idealista/prometheus_server_role/tree/1.6.0)
[Full Changelog](https://github.com/idealista/prometheus_server_role/compare/1.5.0...1.6.0)
### Added
- *[#34](https://github.com/idealista/prometheus_server_role/issues/34) Support remote read and write features* @vicsufer

## [1.5.0](https://github.com/idealista/prometheus_server_role/tree/1.5.0)
[Full Changelog](https://github.com/idealista/prometheus_server_role/compare/1.4.2...1.5.0)
### Fixed
- *[#28](https://github.com/idealista/prometheus_server_role/issues/28) Updated molecule tests; replaced vagrant by docker and testinfra by goss* @frantsao
- *[#28](https://github.com/idealista/prometheus_server_role/issues/28) Renamed role* @frantsao


## [1.4.2](https://github.com/idealista/prometheus_server_role/tree/1.4.2)
[Full Changelog](https://github.com/idealista/prometheus_server_role/compare/1.4.1...1.4.2)
### Fixed
- *[#24](https://github.com/idealista/prometheus_server_role/issues/24) Rise & parametrize timeout for `reload prometheus` handler to 60 seconds* @jnogol

## [1.4.1](https://github.com/idealista/prometheus_server_role/tree/1.4.1)
[Full Changelog](https://github.com/idealista/prometheus_server_role/compare/1.4.0...1.4.1)
### Fixed
- *Prevent configuration verification from deleting config files* @edwinkortman
- *[#21](https://github.com/idealista/prometheus_server_role/issues/21) Don't overwrite log file after (re)start* @jnogol
- *Add Restart on-failure policy on service file* @jnogol

## [1.4.0](https://github.com/idealista/prometheus_server_role/tree/1.4.0)
[Full Changelog](https://github.com/idealista/prometheus_server_role/compare/1.3.1...1.4.0)
### Added
- *Ability to provide configuration templates via playbook* @jnogol

## [1.3.1](https://github.com/idealista/prometheus_server_role/tree/1.3.1)
[Full Changelog](https://github.com/idealista/prometheus_server_role/compare/1.3.0...1.3.1)
### Fixed
- *[#11](https://github.com/idealista/prometheus_server_role/issues/11) Fix reload handler failure due to Prometheus restart* @jnogol

## [1.3.0](https://github.com/idealista/prometheus_server_role/tree/1.3.0)
[Full Changelog](https://github.com/idealista/prometheus_server_role/compare/1.2.0...1.3.0)
### Added
- *[#7](https://github.com/idealista/prometheus_server_role/issues/7) Support prometheus version 2* @jmonterrubio

## [1.2.0](https://github.com/idealista/prometheus_server_role/tree/1.2.0)
[Full Changelog](https://github.com/idealista/prometheus_server_role/compare/1.1.0...1.2.0)
### Added
- *[#3](https://github.com/idealista/prometheus_server_role/issues/3) Include CI and contribution files* @jmonterrubio
- *[#2](https://github.com/idealista/prometheus_server_role/issues/2) Enable command-line flags by configuration file* @jmonterrubio

## [1.1.0](https://github.com/idealista/prometheus_server_role/tree/1.1.0)
[Full Changelog](https://github.com/idealista/prometheus_server_role/compare/1.0.0...1.1.0)
### Added
- *Add scrapes unitary* @jmonterrubio

### Fixed
- *Fix logrotate* @jmonterrubio

## [1.0.0](https://github.com/idealista/prometheus_server_role/tree/1.0.0) (2017-03-03)
### Added
- *First release*
