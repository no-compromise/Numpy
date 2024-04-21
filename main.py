#!/usr/bin/env python3

from ast import arg
import numpy as np
import argparse

parser = argparse.ArgumentParser()

parser.add_argument(
    "-r",
    "--rows",
    type=int,
    help="Numbers of rows to generate",
    metavar="<int>",
    required=True,
)

args = parser.parse_args()

print(args)
print(args.rows)
