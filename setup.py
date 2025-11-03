#!/usr/bin/env python3

from setuptools import setup

setup(
    name='dev_aberto_caiorp',
    version='0.1',
    packages=['dev_aberto'],
    author='Caio',
    python_requires='>=3.6',
    install_requires=[
        'requests>=2.25.0'
    ],
    # scripts=['scripts/hello.py'],
    entry_points={
        'console_scripts': [
            'hello=dev_aberto.dev_aberto:main'
        ],
    },
)