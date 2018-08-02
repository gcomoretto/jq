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


def read(filename):
    """Convenience function for includes"""
    full_filename = os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        filename)
    return codecs.open(full_filename, 'r', 'utf-8').read()


long_description = read('README.md')  # pylint:disable=invalid-name


setup(
    name=PACKAGENAME,
    description=DESCRIPTION,
    long_description=long_description,
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
    use_scm_version=True,
    packages=find_packages(exclude=['docs', 'tests*']),
    install_requires=[
        'requests>=2.8.1,<3.0.0',
    ],
    setup_requires=[
        'setuptools_scm',
    ],
    # package_data={},
    entry_points={
        'console_scripts': [
            'testspecgen = jq.cli.testspecgen:main',
        ]
    }
)
