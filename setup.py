#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='dwc',
    version='0.0.4',
    description='wc clone in Python, plus support directory as arguments',
    author='Viet Hung Nguyen',
    author_email='hvn@familug.org',
    py_modules=['dwc'],
    url='https://github.com/hvnsweeting/dwc',
    entry_points='''[console_scripts]
        dwc=dwc:cli
    '''
)
