#!/usr/bin/env python

import os
import sys

foo = sys.argv

for i in foo:
    print(i)

try:
    dot = sys.argv[2]
except:
    print('Not enough arg')
    sys.exit()

if dot == '.':
    print('It is a dot')
    print(os.getcwd())
else:
    print('Not a dot')
