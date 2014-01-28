# -*- coding: utf-8 -*-
from os.path import join, dirname
from setuptools import setup, find_packages


def read(fname):
    return open(join(dirname(__file__), fname)).read()

setup(
    name = "correcthorse",
    description = "XKCD-style multiword password generator",
    packages = find_packages(),
    long_description = read("README.mkd"),
    include_package_data = True,
    package_data = {
        "": ["*.txt"],
    },
)
