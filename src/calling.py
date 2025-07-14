#!/usr/bin/env python3

import os
import argparse

def argument():
    parser=argparse.ArgumentParser(description="Calling of ancient DNA",
                                   formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--sam", type=str,
                        help="Input sam-file for calling")
    parser.add_argument("--ref", type=str,
                        help="Number of reference genome (19 or 38), which was applied in alignment")
    args=parser.parse_args()
    return args

args = argument()
sam = args.sam
ref = args.ref
f = open(sam, 'r')
for s in f:
    if s[0] == '@':
        continue
    else:
        x = s.split('\t')
        break
print(x)
f.close()
