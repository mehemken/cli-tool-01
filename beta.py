#!/usr/bin/env python
# Tutorial:
# https://docs.python.org/3.6/howto/argparse.html#introducing-optional-arguments

import logging
logger = logging.getLogger()
logging.basicConfig(level=logging.DEBUG)


import argparse
parser = argparse.ArgumentParser()
# parser.add_argument('echo', help='echo the string you use here')
parser.add_argument('square', type=int, help='display a square of a given number')
args = parser.parse_args()
print(args.square**2)
