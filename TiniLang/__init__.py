#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""TiniLang module.

A brainfuck derivative based off the vocabulary of Victini from Pokemon.

Copyright (c) 2019 Blake Grotewold
"""

from __future__ import print_function

import sys
import os

from TiniLang.interpreter import TiniLangProgram


def load_source(file):
    if os.path.isfile(file):
        if os.path.splitext(file)[1] == ".pokeball":
            with open(file, "r") as TiniLang_file:
                TiniLang_data = TiniLang_file.read()

            return TiniLang_data

        else:
            print("TiniLang: file is not a pokeball", file=sys.stderr)
            return False

    else:
        print("TiniLang: file does not exist", file=sys.stderr)
        return False


def evaluate(source):
    """Run TiniLang system."""

    program = TiniLangProgram(source)
    program.run()
