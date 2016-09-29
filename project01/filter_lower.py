#!/usr/bin/env python

"""
A filter that transfer the upper case to lower case..
"""

import fileinput


def process(line):
    """For each line of input, transfer the upper case to lower case."""
    print(line[:-1].lower())


for line in fileinput.input():
    process(line)
