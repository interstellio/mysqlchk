# -*- coding: utf-8 -*-
# Copyright (c) 2021 Interstellio (PTY) LTD - All Rights Reserved.
# Unauthorized copying of this file, via any medium is strictly prohibited.
# Proprietary and confidential.
import os
import sys
from importlib.machinery import SourceFileLoader

try:
    from setuptools import setup, find_packages
except ImportError:
    print('Requires `setuptools` to be installed')
    print('`pip install setuptools`')
    exit()

# DEFINE ROOT PACKAGE NAME
PACKAGE = 'mysqlchk'

###############################################################################
# DO NOT EDIT CODE BELOW THIS POINT ###########################################
###############################################################################

MYDIR = os.path.abspath(os.path.dirname(__file__))
CODE_DIRECTORY = os.path.join(MYDIR, PACKAGE)
TESTS_DIRECTORY = os.path.join(MYDIR, 'tests')
sys.path.insert(0, MYDIR)
os.chdir(MYDIR)

# Load Metadata from package.
metadata = SourceFileLoader(
    'metadata', os.path.join(MYDIR, CODE_DIRECTORY,
                             'metadata.py')).load_module()


def requirements(path):
    dependency = []
    if os.path.exists(os.path.join(os.path.dirname(__file__), path)):
        with open(os.path.join(os.path.dirname(__file__), path)) as req:
            dependency = req.read().splitlines()

    return dependency


def read(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as f:
        return f.read()


python_version_specific_requires = []
install_requires = requirements('install-requires.txt')
dependency_links = requirements('dependency-links.txt')

# See here for more options:
# <http://pythonhosted.org/setuptools/setuptools.html>
setup_dict = dict(
    name=metadata.package,
    version=metadata.version,
    author=metadata.author,
    author_email=metadata.email,
    maintainer=metadata.author,
    maintainer_email=metadata.email,
    url=metadata.url,
    description=metadata.description,
    long_description=read('README.rst'),
    include_package_data=True,
    classifiers=metadata.classifiers,
    packages=find_packages(exclude=(TESTS_DIRECTORY,)),
    install_requires=[] + python_version_specific_requires + install_requires,
    dependency_links=dependency_links,
    zip_safe=False,  # don't use eggs
    entry_points={
        'console_scripts': [
            'mysqlchk = mysqlchk.main:entry_point'
        ],
    },
    python_requires='>=3.6',
)


def main():
    setup(**setup_dict)


if __name__ == '__main__':
    main()
