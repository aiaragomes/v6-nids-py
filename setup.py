# -*- coding: utf-8 -*-

from os import path
from codecs import open
from setuptools import setup, find_packages

# Get current directory
here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Setup the package
setup(
    name='v6-nids-py',
    version='1.0.0',
    description='Vantage6 algorithm to count number of unique ids',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/aiaragomes/v6-nids-py',
    packages=find_packages(),
    python_requires='>=3.10',
    install_requires=[
        'vantage6-client'
    ]
)
