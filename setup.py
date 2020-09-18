# -*- coding: utf-8 -*-

import os
import sys
import re

try:
    from setuptools import setup
    setup
except ImportError:
    from distutils.coding import setup
    setup

# Use UTF-8 if Python 3.
major, minor1, minor2, release, serial = sys.version_info
def read(filename):
    kwargs = {'encoding': 'utf-8'} if major >= 3 else {}
    with open(filename, **kwargs) as f:
        return f.read()

name = 'ptemceeg'

# Get current version.
pattern = re.compile('__version__\s*=\s*(\'|")(.*?)(\'|")')
initPath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ptemceeg/__init__.py')
version = pattern.findall(read(initPath))[0][1]

setup(
    name=name,
    version=version,
    author='Will Vousden and Quentin Baghi',
    author_email='will@vousden.me.uk',
    packages=['ptemceeg'],
    url='https://github.com/willvousden/ptemcee',
    download_url='https://github.com/willvousden/ptemcee/tarball/' + version,
    license='MIT',
    description='Parallel-tempered emcee within Gibbs.',
    long_description=read('README.rst'),
    package_data={'': ['LICENSE']},
    include_package_data=True,
    install_requires=['numpy'],
    tests_require=['pytest'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    zip_safe=True,
)