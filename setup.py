from __future__ import print_function, division, unicode_literals

import re
import ast

from setuptools import setup


_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('pendulumify/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

setup(
    name='pendulumify',
    version=version,
    description='Recursively replace Python standard datetime objects with Pendulum instances',
    url='https://github.com/SpotOnInc/pendulumify',
    download_url='https://github.com/SpotOnInc/pendulumify/archive/v{0}.tar.gz'.format(version),
    license='MIT',
    author='SpotOn',
    author_email='josh@spoton.com',
    keywords=['pendulum', 'time', 'date', 'datetime'],
    packages=[str('pendulumify')],
    platforms='any',
    tests_require=['pytest', 'pytest-cov'],
)
