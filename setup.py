# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='practice_circleci',
    version='0.1.0',
    long_description=readme,
    author='kentaro ishii',
    author_email='kentaro.ishii0407@gmail.com',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

