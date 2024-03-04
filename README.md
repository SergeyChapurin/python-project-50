### Hexlet tests and linter status:
[![Actions Status](https://github.com/SergeyChapurin/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/SergeyChapurin/python-project-50/actions)
### Github Actions status:
[![Python CI](https://github.com/SergeyChapurin/python-project-50/actions/workflows/python_CI.yml/badge.svg)](https://github.com/SergeyChapurin/python-project-50/actions/workflows/python_CI.yml)
### CodeClimate status:
[![Maintainability](https://api.codeclimate.com/v1/badges/5e504c73f64e4289bef5/maintainability)](https://codeclimate.com/github/SergeyChapurin/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/5e504c73f64e4289bef5/test_coverage)](https://codeclimate.com/github/SergeyChapurin/python-project-50/test_coverage)

# Difference Generator

### Description
This project allows you to compare two configuration files in json format and yaml(yml) shows the difference

### Minimum requirements
python3.10

### Installation guide

To install the package for an end-user

Execute:

python3 -m pip install --user dist/*.whl

If you would like to install it as a developer
To install all dependencies execute:

make install

To build a package execute:

make build

To install the package execute:

make package-install

## Optional arguments

1. **-h, --help**  `gendiff -h` - launch help
2. **-f, --format** `gendiff -f` - set format of output. **Available formats:**
* `-f stylish` - default format
* `-f plain`
* `-f json`

### An example of the gendiff package (json files):
[![asciicast](https://asciinema.org/a/nOL2VUocXaWlPAX9XJY7S4dS9.svg)](https://asciinema.org/a/nOL2VUocXaWlPAX9XJY7S4dS9)
### An example of the gendiff package (yaml files):
[![asciicast](https://asciinema.org/a/eDQv9TAkIGVxE88p1JmdTjuNO.svg)](https://asciinema.org/a/eDQv9TAkIGVxE88p1JmdTjuNO)
### An example of the gendiff package (yml files with nesting in the stylish format):
[![asciicast](https://asciinema.org/a/N8yGP9Pz5nLjhlDugBtY0y4Pj.svg)](https://asciinema.org/a/N8yGP9Pz5nLjhlDugBtY0y4Pj)
### An example of the gendiff package (json files with nesting in the stylish format):
[![asciicast](https://asciinema.org/a/fh38d5CZyGkxse0USNBdD2zLc.svg)](https://asciinema.org/a/fh38d5CZyGkxse0USNBdD2zLc)
### An example of the gendiff package (plain format):
[![asciicast](https://asciinema.org/a/sREk8fTZWBcXM4Dkj84KXYhUN.svg)](https://asciinema.org/a/sREk8fTZWBcXM4Dkj84KXYhUN)
### An example of the gendiff package (json format):
[![asciicast](https://asciinema.org/a/yNTTEGSlaiQld4jjWs7wBzX2q.svg)](https://asciinema.org/a/yNTTEGSlaiQld4jjWs7wBzX2q)