#!/usr/bin/env python3

import os
import argparse

def argument():
    parser=argparse.ArgumentParser(description="Calling of ancient DNA",
                                   formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--sam", type=str,
                        help="Input sam-file for calling")
    args=parser.parse_args()
    return args

args = argument()
sam = args.sam
print(sam)
