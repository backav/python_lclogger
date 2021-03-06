#!/usr/bin/env python
# -*- coding: utf-8 -*-


from setuptools import setup

__author__ = 'bac'

setup(
    name='py_lclogger',
    version='0.4',
    keywords=('LogCentral', 'log','logger'),
    description=u'Save log to server',
    license='Apache License',
    install_requires=['requests','futures'],

    url="http://xiangyang.li/project/python_lclogger",

    author='bac',
    author_email='wo@xiangyang.li',

    packages=['py_lclogger'],
    platforms='any',
)
