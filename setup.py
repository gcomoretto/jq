#!/usr/bin/env python3
"""Setup Tools Script"""
import os
import codecs
from setuptools import setup, find_packages

PACKAGENAME = 'jq'
DESCRIPTION = 'jira quering tool'
AUTHOR = 'Gabriele Comoretto'
AUTHOR_EMAIL = 'gcomoretto@lsst.org'
URL = 'https://github.com/gcomoretto/jq'
LICENSE = 'MIT'

requires = [
    'requests',
    'pyandoc',
    'arrow',
    'jinja2',
    'click',
    'BeautifulSoup4'
]


setup(
    name=PACKAGENAME,
    description=DESCRIPTION,
    url=URL,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license=LICENSE,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License',
    ],
    keywords='lsst',
    use_scm_version=False,
    packages=find_packages(exclude=['docs', 'tests*']),
    entry_points={
        'console_scripts': [
            'jq = jq:main',
        ]
    }
)
