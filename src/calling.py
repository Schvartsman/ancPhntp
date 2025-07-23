#!/usr/bin/env python3

import os
import argparse
import numpy as np
import aspose.words as aw

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

def regain(z,k,coor_o):
    if coor_o == 'A':
        z[k][0] = z[k][0] + 1
    if coor_o == 'C':
        z[k][1] = z[k][1] + 1
    if coor_o == 'G':
        z[k][2] = z[k][2] + 1
    if coor_o == 'T':
        z[k][3] = z[k][3] + 1
    return z

def coor(a,b,c,d):
    nuc=''
    x=-1
    y=-1
    n=''
    l=''
    for i in range(len(a)):
        if a[i] != 'M' and a[i] != 'I' and a[i] != 'D' and a[i] != 'N' and a[i] != 'S' and a[i] != 'H' and a[i] != 'P' and a[i] != '=' and a[i] != 'X':
            n = n + a[i]
        else:
            l = a[i]
            if l == 'M':
                if b+y+int(n) > c:
                    for j in range(int(n)):
                        y = y + 1
                        x = x + 1
                        if b+y == c:
                            nuc = d[x]
                    break
                if b+y+int(n) == c:
                    x = x + int(n)
                    y = y + int(n)
                    nuc = d[x]
                    break
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
                if b+y+int(n) > c:
                    for j in range(int(n)):
                        y = y + 1
                        x = x + 1
                        if b+y == c:
                            nuc = d[x]
                    break
                if b+y+int(n) == c:
                    x = x + int(n)
                    y = y + int(n)
                    nuc = d[x]
                    break
                x = x + int(n)
                y = y + int(n)
            if l == 'X':
                if b+y+int(n) > c:
                    for j in range(int(n)):
                        y = y + 1
                        x = x + 1
                        if b+y == c:
                            nuc = d[x]
                    break
                if b+y+int(n) == c:
                    x = x + int(n)
                    y = y + int(n)
                    nuc = d[x]
                    break
                x = x + int(n)
                y = y + int(n)
            l = ''
            n = ''
    return nuc

def code(a,b,c):
    res1 = ''
    res2 = ''
    for i in range(len(c)):
        y = c[i].split('\t')
        if y[0] == a:
            if b[i][0] != 0:
                res1 = res1 + 'A'
                res2 = res2 + str(b[i][0])[:-2]
            if b[i][1] != 0:
                res1, res2 = slash(res1,res2)
                res1 = res1 + 'C'
                res2 = res2 + str(b[i][1])[:-2]
            if b[i][2] != 0:
                res1, res2 = slash(res1,res2)
                res1 = res1 + 'G'
                res2 = res2 + str(b[i][2])[:-2]
            if b[i][3] != 0:
                res1, res2 = slash(res1,res2)
                res1 = res1 + 'T'
                res2 = res2 + str(b[i][3])[:-2]
            break
    return res1+':'+res2

def slash(a,b):
    if len(a) != 0:
        a = a + '|'
        b = b + '|'
    return a,b


args = argument()
sam = args.sam
ref = args.ref
tsv19 = '/home/flower/prj_1/data/19.tsv'
tsv38 = '/home/flower/prj_1/data/38.tsv'
tsvw = '/home/flower/prj_1/data/specimen.tsv'
if ref == '19':
    t = open(tsv19, 'r')
if ref == '38':
    t = open(tsv38, 'r')
times = t.readlines()
t.close()
f = open(sam, 'r')
k = 0
z = np.zeros([41,4])
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
                coor_o = coor(x[5],int(x[3]),int(y[2]),x[9])
                print(coor_o, '  ', int(y[2]), '  ', y[1])
                z = regain(z,k,coor_o)
            while int(x[3]) > int(y[2]):
                if x[2] == y[1]:
                    if k < 40:
                        k = k + 1
                        y = times[k].split('\t')
                        if cigar(x[5])[1]+int(x[3]) >= int(y[2]) and int(x[3]) <= int(y[2]):
                            print(x[0])
                            coor_o = coor(x[5],int(x[3]),int(y[2]),x[9])
                            print(coor_o, '  ', int(y[2]), '  ', y[1])
                            z = regain(z,k,coor_o)
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
w = open(tsvw, 'r')
wines = w.readlines()
print(z)
doc = aw.Document()
builder = aw.DocumentBuilder(doc)
font = builder.font
font.size = 8
font.name = "TimesNewRoman"
#paragraphFormat = builder.paragraph_format
#paragraphFormat.first_line_indent = 14
#paragraphFormat.alignment = aw.ParagraphAlignment.JUSTIFY
#paragraphFormat.keep_together=True


table = builder.start_table()
print(len(wines))
for i in range(len(wines)):
    wew = wines[i].split('\t')
    if i == 0:
        for j in range(len(wew)):
            builder.insert_cell()
            builder.write(wew[j])
    if i != 0:
        for j in range(len(wew)+2):
            if j < 6:
                builder.insert_cell()
                builder.write(wew[j])
            if j == 6:
                builder.insert_cell()
                builder.write(code(wew[1],z,times))
            if j == 7:
                builder.insert_cell()
    builder.end_row()
builder.end_table()
doc.save('/home/flower/Desktop/phen.docx')
