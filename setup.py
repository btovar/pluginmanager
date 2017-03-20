#!/usr/bin/env python
#
# Setup prog for infoservice

import commands
import os
import re
import sys

from pluginmanager import plugin
release_version=plugin.__version__

from distutils.core import setup
from distutils.command.install import install as install_org
from distutils.command.install_data import install_data as install_data_org

setup(
    name="pluginmanager",
    version=release_version,
    description='plugin load and config',
    long_description='''plugin load and config''',
    license='GPL',
    author='John Hover',
    author_email='jhover@bnl.gov',
    maintainer='John Hover',
    maintainer_email='jhover@bnl.gov',
    url='https://github.com/vc3-project',
    packages=['pluginmanager'],

)
