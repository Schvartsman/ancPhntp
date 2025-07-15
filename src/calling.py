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

def cigar(a):
    x=0
    y=0
    n=''
    l=''
    for i in range(len(a)):
        if a[i] != 'M' and a[i] != 'I' and a[i] != 'D' and a[i] != 'N' and a[i] != 'S' and a[i] != 'H' and a[i] != 'P' and a[i] != '=' and a[i] != 'X':
            n = n + a[i]
        else:
            l = a[i]
            if l == 'M':
                x = x + int(n)
                y = y + int(n)
            if l == 'I':
                x = x + int(n)
            if l == 'D':
                y = y + int(n)
            if l == 'N':
                y = y + int(n)
            if l == 'S':
                x = x + int(n)
            if l == '=':
                x = x + int(n)
                y = y + int(n)
            if l == 'X':
                x = x + int(n)
                y = y + int(n)
            l = ''
            n = ''
    return x,y


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
y = times[k].split('\t')
for s in f:
    if s[0] == '@':
        continue
    else:
        x = s.split('\t')
        if x[2] == y[1]:
#            print(int(y[2]), '  ', int(x[3]), '  ', cigar(x[5])[1]+int(x[3]))
            if cigar(x[5])[1]+int(x[3]) >= int(y[2]) and int(x[3]) <= int(y[2]):
                print(x[0])
            while int(x[3]) > int(y[2]):
                if x[2] == y[1]:
                    if k < 40:
                        k = k + 1
                        y = times[k].split('\t')
                        if cigar(x[5])[1]+int(x[3]) >= int(y[2]) and int(x[3]) <= int(y[2]):
                            print(x[0])
                    else:
                        break
                else:
                    break
            if k == 40:
                break
#print(x)
#print(y)
#print(x[5])
#print(cigar(x[5]))
f.close()
