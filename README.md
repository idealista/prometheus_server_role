![Logo](https://raw.githubusercontent.com/idealista/prometheus_server_role/master/logo.gif)

[![Build Status](https://travis-ci.org/idealista/prometheus_server_role.png)](https://travis-ci.org/idealista/prometheus_server_role)

# Prometheus Server Ansible role

This ansible role installs a Prometheus server in a debian environment. The server is installed using the sources.

- [Getting Started](#getting-started)
	- [Prerequisities](#prerequisities)
	- [Installing](#installing)
- [Usage](#usage)
- [Testing](#testing)
- [Built With](#built-with)
- [Versioning](#versioning)
- [Authors](#authors)
- [License](#license)
- [Contributing](#contributing)

## Getting Started

These instructions will get you a copy of the role for your ansible playbook. Once launched, it will install an [Prometheus](https://prometheus.io/) server in a Debian system.

### Prerequisities

Ansible 2.8.x.x version installed.
Inventory destination should be a Debian environment.

For testing purposes, [Molecule](https://molecule.readthedocs.io/) with [Docker](https://www.docker.com/) as driver. Pipenv 2018.11.26 and Python 3 recommended.

### Installing

Create or add to your roles dependency file (e.g requirements.yml):

```
- src: idealista.prometheus_server_role
  version: 1.5.0
  name: prometheus
```

Install the role with ansible-galaxy command:

```
ansible-galaxy install -p roles -r requirements.yml -f
```

Use in a playbook:

```
---
- hosts: someserver
  roles:
    - role: prometheus
```

## Usage

Look to the [defaults](defaults/main.yml) properties file to see the possible configuration properties.

## Testing

```
pipenv shell
pipenv sync
molecule test
```

See [molecule.yml](https://github.com/idealista/prometheus_server_role/blob/master/molecule.yml) to check possible testing platforms

## Built With

![Ansible](https://img.shields.io/badge/ansible-2.8.6.0-green.svg)
![Molecule](https://img.shields.io/badge/molecule-2.22.0-green.svg)

## Versioning

For the versions available, see the [tags on this repository](https://github.com/idealista/prometheus_server_role/tags).

Additionaly you can see what change in each version in the [CHANGELOG.md](CHANGELOG.md) file.

## Authors

* **Idealista** - *Work with* - [idealista](https://github.com/idealista)

See also the list of [contributors](https://github.com/idealista/prometheus_server_role/contributors) who participated in this project.

## License

![Apache 2.0 License](https://img.shields.io/hexpm/l/plug.svg)

This project is licensed under the [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) license - see the [LICENSE](LICENSE) file for details.

## Contributing

Please read [CONTRIBUTING.md](.github/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.
