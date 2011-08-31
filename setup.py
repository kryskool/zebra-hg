#!/usr/bin/env python
import sys
from distutils.core import setup

try:
    from distutils.command.build_py import build_py_2to3 as build_py
except ImportError:
    from distutils.command.build_py import build_py

classifiers = ['Development Status :: 3 - Alpha',
               'Operating System :: Microsoft :: Windows',
               'Operating System :: Unix',
               "Operating System :: MacOS :: MacOS X",
               'License :: OSI Approved :: MIT License',
               'Intended Audience :: Developers',
               'Programming Language :: Python :: 2.7',
               'Programming Language :: Python :: 3',
               'Topic :: Printing']

long_description = open('README').read()

if sys.platform.lower().startswith('win'):
    requires = ['win32print']
    try:
        import win32print
    except:
        raise Exception('Requires the win32print module from the pywin32 package.\nDownload from http://pypi.python.org/pypi/pywin32/')
else:
    requires = []

setup(name             = 'zebra',
      version          = '0.0.3a',
      py_modules       = ['zebra'],
      author           = 'Ben Croston',
      author_email     = 'ben@croston.org',
      maintainer       = 'Ben Croston',
      maintainer_email = 'ben@croston.org',
      url              = 'http://www.wyre-it.co.uk/zebra/',
      description      = 'A package to communicate with (Zebra) label printers using EPL2',
      long_description = long_description,
      platforms        = 'Windows, Unix, MacOSX',
      classifiers      = classifiers,
      license          = 'MIT',
      cmdclass         = {'build_py': build_py},
      requires         = requires,
      )

