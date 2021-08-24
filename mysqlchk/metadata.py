# -*- coding: utf-8 -*-
"""Project metadata

Information describing the project.
"""
from datetime import datetime

# The package name, which is also the "UNIX name" for the project.
package = 'mysqlchk'
project = "NebularStack " + package.title()
project_no_spaces = project.replace(' ', '')
# Please follow https://www.python.org/dev/peps/pep-0440/
version = '0.0'
description = project
author = 'Interstellio IO (PTY) LTD'
email = 'project@nebularstack.com'
license = 'Proprietary and Confidential'
copyright = '2021-%s %s' % (datetime.now().year, author,)
url = 'https://www.nebularstack.com'
identity = project + ' v' + version

# Classifiers
# <http://pypi.python.org/pypi?%3Aaction=list_classifiers>
classifiers = [
    'Development Status :: 1 - Planning',
    'Environment :: Other Environment',
    'Intended Audience :: Developers',
    'Intended Audience :: Information Technology',
    'Intended Audience :: System Administrators',
    'License :: OSI Approved :: BSD License',
    'Natural Language :: English',
    'Operating System :: POSIX :: Linux',
    'Programming Language :: Python :: 3.8',
    'Topic :: Internet :: WWW/HTTP',
    'Topic :: Internet :: WWW/HTTP :: WSGI',
    'Topic :: Internet :: WWW/HTTP :: WSGI :: Application'
    ]
