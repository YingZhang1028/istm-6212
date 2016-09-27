#!/usr/bin/env python

"""
A filter that split lines of text into one word per line.
"""

import fileinput
import re

def process(line):
    """For each line of input, split the line into words."""      
    word = re.compile('\w{2,}')
    line = word.findall(line)
    
    for i in line:
        print (i)

for line in fileinput.input():
    process(line)



    
