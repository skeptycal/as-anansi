#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# pylint: disable=missing-docstring
# Note: To use the 'upload' functionality of this file, you must:
#   $ pipenv install twine --dev

import io
import os
import sys
from enum import Enum
from shutil import rmtree
from typing import Dict, List, Set, Tuple

from setuptools import Command, find_packages, setup


# !----------------------------------------- Package meta-data.
__version__: str = '1.0.1'

NAME: str = 'as_anansi'
# Create 'Pypi-safe' project name by replaceing ['-',' '] with '_'
NAME = NAME.lower().replace("-", "_").replace(" ", "_")

DESCRIPTION: str = 'Tricky and fun ansi text utilities for python programs.'
URL: str = f'https://github.com/skeptycal/{NAME}'
EMAIL: str = 'skeptycal@gmail.com'
AUTHOR: str = 'Michael Treanor'
LICENSE: str = 'MIT'
REQUIRES_PYTHON: str = '>=3.8.0'
VERSION: Tuple = tuple(map(int, __version__.split('.')))

# !----------------------------------------- Package README.md
# Set directory of this script to <here>
here: str = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
# Note: this will only work if 'README.md' is present in your MANIFEST.in file!
with io.open(
    os.path.join(here, 'README.md'),
    mode='r',
    encoding='utf-8'
) as f:
    try:
        long_description = '\n' + f.read()
    except FileNotFoundError:
        long_description = DESCRIPTION

# UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS: Set[str] = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

# What packages are required for this module to be executed?
REQUIRED: List[str] = [
    'typing', 'requests',  # 'maya', 'records',
]

# What packages are optional?
EXTRAS: Dict[str, List[str]] = {
    'CLI options': ['docopt'],
    # 'fancy feature': ['django'],
}

# The rest you shouldn't have to touch too much :)
# ------------------------------------------------
# Except, perhaps the License and Trove Classifiers!
# If you do change the License, remember to change the
#   Trove Classifier for that!


class UploadCommand(Command):
    """Support setup.py upload."""

    description: str = 'Build and publish the package.'
    user_options: List[str] = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status('Removing previous builds…')
            rmtree(os.path.join(here, 'dist'))
        except OSError:
            pass

        self.status('Building Source and Wheel (universal) distribution…')
        os.system('{0} setup.py sdist bdist_wheel --universal'.format(
            sys.executable))

        self.status('Uploading the package to PyPI via Twine…')
        os.system('twine upload dist/*')

        self.status('Pushing git tags…')
        os.system('git tag v{0}'.format(about['__version__']))
        os.system('git push --tags')

        sys.exit()


setup(  # Where the magic happens:
    name=NAME,
    version=__version__,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    license=LICENSE,
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    project_urls={
        "Documentation": f"https://{NAME}.github.io",
        "Source": f"https://github.com/skeptycal/{NAME}",
        "Funding": "https://www.patreon.com/skeptycal",
    },
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: MIT License',
        "Development Status:: 4 - Beta",
        "Environment:: Console",
        "Environment:: MacOS X",
        "Natural Language:: English",
        "Operating System:: MacOS",
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        "Topic :: Multimedia :: Graphics",
        "Topic :: Multimedia :: Graphics :: Capture :: Digital Camera",
        "Topic :: Multimedia :: Graphics :: Capture :: Screen Capture",
        "Topic :: Multimedia :: Graphics :: Graphics Conversion",
        "Topic :: Multimedia :: Graphics :: Viewers",
    ],
    package_dir={'include': f"{NAME.lower()}"},
    packages=find_packages(
        exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    # If your package is a single module, use this instead of 'packages':
    #   py_modules=['mypackage'],

    #   entry_points={
    #       'console_scripts': ['mycli=mymodule:cli'],
    #  },
    install_requires=REQUIRED,
    extras_require=EXTRAS,
    include_package_data=True,
    keywords=["CLI", "macOS", "ANSI", "Color", "Console", "Utility"],
    #   setup_requires=pytest_runner,
    tests_require=["pytest"],
    #   ext_modules=[Extension(f"{NAME}._some_method", [f"_{NAME}.c"])],
    #   zip_safe=not (debug_build() or PLATFORM_MINGW),
    # $ setup.py publish support.
    cmdclass={
        'upload': UploadCommand,
    },
)
