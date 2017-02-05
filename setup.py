#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='wcld',
    version='0.0.2',
    description='wc clone in Python, plus support directory as arguments',
    author='Viet Hung Nguyen',
    author_email='hvn@familug.org',
    url='https://github.com/hvnsweeting/wcld',
    entry_points='''[console_scripts]
        wcld=wcld:cli
    '''
)
