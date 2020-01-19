# AutoSys - Anansi

Tricky and fun ansi text utilities for python programs. The obligatory ANSI CLI module from the Python system utilities package [AutoSys](https://pypi.org/project/autosys/)

---

[![netlify badge](https://api.netlify.com/api/v1/badges/416b8ca3-82db-470f-9adf-a6d06264ca75/deploy-status)](https://app.netlify.com/sites/mystifying-keller-ab5658/deploys) [![Build Status](https://travis-ci.com/skeptycal/autosys.svg?branch=master)](https://travis-ci.com/skeptycal/autosys)

![https://pypi.python.org/pypi/autosys](http://img.shields.io/pypi/v/autosys.svg?color=Yellow&style=popout) ![https://pypi.python.org/pypi/autosys](https://img.shields.io/pypi/wheel/autosys.svg) ![PyPI - Status](https://img.shields.io/pypi/status/autosys.svg)

![https://pypi.python.org/pypi/autosys](https://img.shields.io/badge/test_coverage-100%25-6600CC.svg) ![https://pypi.python.org/pypi/autosys](https://img.shields.io/badge/branch_coverage-100%25-6600CC.svg)

[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-v1.4%20adopted-ff69b4.svg)](code-of-conduct.md) [![code style: prettier](https://img.shields.io/badge/code_style-prettier-ff69b4.svg?style=flat-square)](https://github.com/prettier/prettier)

![Twitter Follow](https://img.shields.io/twitter/follow/skeptycal.svg?label=%40skeptycal&style=social) ![GitHub followers](https://img.shields.io/github/followers/skeptycal.svg?style=social)


## Getting Started

### AutoSys - System utilities for Python on macOS

- Setup and maintain python repos automatically
- Automate web access, blog updates, social media
- Collect and analyze data sets efficiently
- Create vivid and descriptive visualizations of data
- Use Python to interact with compiled languages and devops tools

### Documentation

[Using GNU Fortran (pdf)](https://gcc.gnu.org/onlinedocs/gcc-9.2.0/gfortran.pdf)

### Prerequisites

Autosys requires the following:

- macOS 10.12+ (most likely any modern macOS or Linux distro)
- Python 3.8+ (or 3.6+ with fstrings library)
_No external libraries are required for basic functionality._

| Optional Features          | Requirements                                                     |
| -------------------------- | ---------------------------------------------------------------- |
| Web scraping / url parsing | [Requests: HTTP for Humans™](https://pypi.org/project/requests/) |
| YAML serialization         | [PyYAML](https://pypi.org/project/PyYAML/)                       |
| ultra fast JSON            | [ujson](https://pypi.org/project/ujson/)                         |
| data wrangling; vectors    | [numpy](https://pypi.org/project/numpy/)                         |
| data visualization         | D3, Seaborn, Bokeh, Vegas                                        |
| framework interaction      | Flask, Vue / Nuxt                                                |
| Fortran Interoperability   | numpy, [GNU Fortran 7+](http://hpc.sourceforge.net/#fortran)     |
| GO Interoperability        | go1.12                                                           |
| database support           | drivers for MySQL, MongoDB, etc                                  |

_macOS specific information:_

- *many optional features require Apple's XCode Tools (installed from the Mac App Store)*
- *On 10.9 Mavericks or higher, you can get the command-line tools by simply typing xcode-select --install.*
- _And on Catalina, you may have to specifify the following additional include path for the compiler to find the system headers:_


        -I/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include

## Installing


        # installing GNU computation tools: gcc, c++, and gfortran

        # Homebrew install (macOS)
        brew cask install gcc gfortran

        # direct install (macOS / linux)
        curl -o gcc-9.2-bin.tar.gz http://prdownloads.sourceforge.net/hpc/gcc-9.2-bin.tar.gz
        gunzip gcc-9.2-bin.tar.gz
        sudo tar -xvf gcc-9.2-bin.tar -C /


For Windows support, check [here](https://gcc.gnu.org/install/specific.html#windows).

## Running the tests

## Break down into end to end tests

## Coding style tests

Pylint and Autopep8 are used to enforce coding conventions.

## Deployment

        python3 -m pip install autosys

## Built With

![python on vscode](images/vscode_python.png)


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

AutoSys is licensed under the MIT <https://opensource.org/licenses/MIT> - see the [LICENSE](LICENSE) file for details.



### Example Usage

### More Examples

### Utility Functions

### License

