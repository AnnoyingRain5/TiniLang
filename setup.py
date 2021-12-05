#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""TiniLang setup script."""

from setuptools import setup

__VERSION__ = "0.0.1"

if __name__ == "__main__":
    setup(
        name="TiniLang",
        version=__VERSION__,
        description="A brainfuck derivative based off the vocabulary of Victini.",
        license="MIT",
        keywords="esoteric programming language brainfuck",
        author="AnnoyingRains",
        author_email="annoyingrain5@gmail.com",
        url="https://github.com/annoyingrain5/tinilang",
        py_modules=["TiniLang", "TiniLang.cli", "TiniLang.interpreter", "setup"],
        install_requires=["ply"],
        entry_points={"console_scripts": ["TiniLang = TiniLang.cli:main"]},
        classifiers=[
            "Development Status :: 4 - Beta",
            "Environment :: Console",
            "Intended Audience :: Developers",
            "Intended Audience :: Science/Research",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
            "Programming Language :: Python",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 2.6",
            "Programming Language :: Python :: 2.7",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.4",
            "Programming Language :: Python :: 3.5",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: Implementation :: PyPy",
        ],
    )
