#!/usr/bin/env python

"""
A filter that remove the stop words.
"""

import fileinput

stopwords = ['and','the','to','of','her','in','it','for','you','was','she','as','with','that']

def process(line):
    """For each line of input, remove the stop words."""
    line = line[:-1]
    while line not in stopwords:
        print(line)
        break

for line in fileinput.input():
    process(line)
