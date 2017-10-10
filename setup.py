#! /usr/bin/env python

# This file is part of neulang

# neulang - A language sitting on top of Python that executes pseudocode that's very close to natural language.

# @author Andrew Phillips
# @copyright 2017 Andrew Phillips <skeledrew@gmail.com>

# neulang is free software; you can redistribute it and/or
# modify it under the terms of the GNU AFFERO GENERAL PUBLIC LICENSE
# License as published by the Free Software Foundation; either
# version 3 of the License, or any later version.

# neulang is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU AFFERO GENERAL PUBLIC LICENSE for more details.

# You should have received a copy of the GNU Affero General Public
# License along with neulang.  If not, see <http://www.gnu.org/licenses/>.

import sys
from os.path import join, dirname

from setuptools import setup

from neulang.cerebrum import meta, __version__

setup(
    name=meta.get('name', 'neu'),
    version=__version__,
    entry_points={
        'console_scripts': [
            'neu = neulang.cerebrum:neu_main',
        ],
    },
    author='Andrew Phillips',
    author_email='skeledrew@gmail.com',
    description='Coding for humans.',
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    url='https://github.com/skeledrew/neulang',
    packages=['neulang'],
    platforms=['any'],
    license='AGPLv3',
    classifiers=[
        'License :: AGPLv3', 'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6'
    ])
