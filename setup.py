#!/usr/bin/env python
# -*- coding: utf-8 -*-
version = "0.1.0"

try:
    import fastentrypoints
except ImportError:
    from setuptools.command import easy_install
    import pkg_resources
    easy_install.main(['fastentrypoints'])
    pkg_resources.require('fastentrypoints')
    import fastentrypoints

import sys
from setuptools import setup, find_packages


if sys.version_info[0] == 2:
    jsonrpclib = "jsonrpclib"
    ep = {"console_scripts": ["zerophone_api_daemon = zerophone_api_daemon.zerophone_api_daemon:main"]}
elif sys.version_info[0] == 3:
    jsonrpclib = "jsonrpclib-pelix"
    ep = {}


setup(
    name='zerophone_api_daemon',
    packages=find_packages(),
    version=version,
    description='ZeroPhone API daemon',
    author='CRImier',
    author_email='crimier@yandex.ru',
    install_requires=[
        jsonrpclib,
        "PyRIC",
        "zerophone_hw >= 0.4.0"
    ],
    url = 'https://github.com/ZeroPhone/Zerophone-API-Daemon',
    download_url = 'https://github.com/ZeroPhone/Zerophone-API-Daemon/archive/{}.tar.gz'.format(version),
    entry_points=ep
)
import sys


