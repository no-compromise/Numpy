#!/usr/bin/env python3

import numpy as np
import argparse
import json
import sys

# ---- Argument parsing section ----

parser = argparse.ArgumentParser()

parser.add_argument(
    "-r",
    "--rows",
    type=int,
    help="Numbers of rows to generate",
    metavar="<int>",
    required=True,
)
parser.add_argument("-d", "--debug", action="store_true", help="Turns on debug info")

args = parser.parse_args()

# -----------------------------------

# import data.json
try:
    f = open("./data.json", "r")
except FileNotFoundError:
    print("Data file not found!")
    sys.exit(1)
else:
    with f:
        data = json.load(f)


if args.debug:
    print("*** DEBUG INFO: ***\n")
    print(args)
    print(args.rows)
    print(args.debug)
    print(type(data))
    print("*** END DEBUG INFO ***")
