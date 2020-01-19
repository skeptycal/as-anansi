# AutoSys - Anansi

>as-anansi.py - Tricky and fun ansi text utilities for python programs. The obligatory ANSI CLI module from the Python system utilities package [AutoSys](https://pypi.org/project/autosys/)

---

[![Build Status](https://travis-ci.com/skeptycal/autosys.svg?branch=master)](https://travis-ci.com/skeptycal/autosys) ![https://pypi.python.org/pypi/autosys](http://img.shields.io/pypi/v/autosys.svg?style=flat) ![https://pypi.python.org/pypi/autosys](https://img.shields.io/pypi/wheel/autosys.svg)

![https://pypi.python.org/pypi/autosys](https://img.shields.io/badge/test_coverage-100%25-6600CC.svg) ![https://pypi.python.org/pypi/autosys](https://img.shields.io/badge/branch_coverage-100%25-6600CC.svg)

## Getting Started

### Documentation

[Using GNU Fortran (pdf)](https://gcc.gnu.org/onlinedocs/gcc-9.2.0/gfortran.pdf)

### Prerequisites

Autosys requires the following:

- macOS 10.12+ (most likely any modern macOS or Linux distro)
- Python 3.8+ (or 3.6+ with fstrings library)
_No external libraries are required for basic functionality._

| Optional Features                           | Requirements                                                     |
| ------------------------------------------- | ---------------------------------------------------------------- |
| Web scraping / url parsing                  | [Requests: HTTP for Humans™](https://pypi.org/project/requests/) |
| YAML serialization                          | [PyYAML](https://pypi.org/project/PyYAML/)                       |
| ultra fast JSON                             | [ujson](https://pypi.org/project/ujson/)                         |
| data wrangling; array computing with Python | [numpy](https://pypi.org/project/numpy/)                         |
| Fortran Interoperability & Paralellization  | numpy, [GNU Fortran 7+](http://hpc.sourceforge.net/#fortran)     |
| GO Interoperability                         | go1.12                                                           |
| database support                            | PostgreSQL, MySQL, ODBC driver                                   |

_macOS specific information:_

- many optional features require Apple's XCode Tools (installed from the Mac App Store)
- On 10.9 Mavericks or higher, you can get the command-line tools by simply typing xcode-select --install.
- And on Catalina, you may have to specifify the following additional include path for the compiler to find the system headers.

```sh
-I/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include
```

## Installing

```sh
# installing GNU computation tools: gcc, c++, and gfortran

# Homebrew install (macOS)
brew cask install gcc gfortran

# direct install (macOS / linux)
curl -o gcc-9.2-bin.tar.gz http://prdownloads.sourceforge.net/hpc/gcc-9.2-bin.tar.gz
gunzip gcc-9.2-bin.tar.gz
sudo tar -xvf gcc-9.2-bin.tar -C /
```

For Windows support, check [here](https://gcc.gnu.org/install/specific.html#windows).

## Running the tests

## Break down into end to end tests

## Coding style tests

Pylint and Autopep8 are used to enforce coding conventions.

## Deployment

```sh
python3 -m pip install autosys
```

## Built With

![python on vscode](src/vscode_python.png)


## Contributing

Please read CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use SemVer for versioning. For the versions available, see the tags on this repository.

## Contributors
- [Michael Treanor](https://www.twitter.com/skeptycal) - Initial work, updates, maintainer
- [Sarah Treanor](https://www.streanor.com/) - art and design inspiration
- [Sarah Drasner](https://sarahdrasnerdesign.com/) - advice and motivation

See also the list of contributors who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## System utilities for Python on macOS

Setup and maintain python repos automatically
### Example Usage

### More Examples

### Utility Functions

### License

AutoSys is licensed under the MIT <https://opensource.org/licenses/MIT>.
