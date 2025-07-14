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
tsv19 = '/home/flower/prj_1/data/19.tsv'
tsv38 = '/home/flower/prj_1/data/38.tsv'
if ref == '19':
    t = open(tsv19, 'r')
if ref == '38':
    t = open(tsv38, 'r')
times = t.readlines()
t.close()
f = open(sam, 'r')
k = 0
for s in f:
    y = times[k].split('\t')
    if s[0] == '@':
        continue
    else:
        x = s.split('\t')
        break
print(x)
print(y)
f.close()
