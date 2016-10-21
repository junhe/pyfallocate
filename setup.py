#!/usr/bin/env python

import os
import sys

from setuptools import setup, find_packages

os.chdir(os.path.dirname(sys.argv[0]) or ".")

setup (
    name = "pyfallocate",
    version = "0.1",
    description = "A python wrapper around libc fallocate",
    long_description = open("README.md", "rt").read(),
    url = "https://github.com/junhe/pyfallocate",
    author = "",
    install_requires=["cffi>=1.0.0"],
    setup_requires=["cffi>=1.0.0"],
    packages=find_packages(),
    cffi_modules=["./pyfallocate/fallocate_build.py:ffi"]
)
