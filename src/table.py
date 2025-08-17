#!/usr/bin/env python3

import os
import argparse
import aspose.words as aw

def argument():
    parser=argparse.ArgumentParser(description="Creation file with table of phenotype results.",
            formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--input', type=str,
            help="Input file 'Result.csv'")
    parser.add_argument('--id', type=str,
            help="ID of specimen")
    args = parser.parse_args()
    return args

def roun(a):
    b = a*1000
    b = float(int(b))/1000
    return b

def line(a, adress):
    P = 'P'
    L = 'AUC_Loss_'
    word1 = ''
    word2 = ''
    name = ''
    count = ''
    f = open(adress, 'r')
    for s in f:
        name = ''
        count = ''
        n = 0
        for i in range(len(s)):
            if s[i] == '\t' or s[i] == ' ':
                n = n + 1
            if n == 0 and s[i] != '\t' and s[i] != '\n' and s[i] != ' ':
                name = name + s[i]
            if n > 0  and s[i] != '\t' and s[i] != '\n' and s[i] != ' ':
                count = count + s[i]
#        print(name, '  ', count)
        if name == P+a:
            word1 = count
        if name == L+a:
            word2 = count
    if word2 == '':
        word2 = '0'
    line = a+'\t'+word1+'\t'+word2+'\n'
    return line

args = argument()
inp = args.input
idd = args.id
f = open(inp, 'r')
fines = f.readlines()
f.close()
n = 0
m = 0
for i in range(len(fines[0])):
    if fines[0][i] == ',':
        n = n + 1
for i in range(len(fines[1])):
    if fines[1][i] == ',':
        m = m + 1
i = 0
j = 0
n = 0
m = 0
string = ''
word1 = ''
word2 = ''
while(fines[0][n] != '\n'):
    if m == len(fines[1]):
        j = j + 1
    if m < len(fines[1]):
        if fines[1][m] == ',':
            m = m + 1
            j = j + 1
    if n < len(fines[0]):
        if fines[0][n] == ',':
            n = n + 1
            i = i + 1
            string = string + word1 + '\t' + word2 + '\n'
            word1 = ''
            word2 = ''
    if j == i:
        word2 = word2 + fines[1][m]
        m = m + 1
    if j > i:
        word1 = word1 + fines[0][n]
        n = n + 1
f = open('/home/daniils/table.txt', 'w')
out = '/home/daniils'
f.write(string)
f.close()
e = 'Eye'
h = 'Hair'
s = 'Skin'
w1 = 'Blue'
w2 = 'Intermediate'
w3 = 'Brown'
w4 = 'Blond'
w5 = 'Red'
w6 = 'Black'
w7 = 'VeryPale'
w8 = 'Pale'
w9 = 'Dark'
w10 = 'DarktoBlack'
w11 = 'Light'
res = ''
res = res + line(w1+e, out+'/table.txt') + line(w2+e, out+'/table.txt') + line(w3+e, out+'/table.txt') + line(w4+h, out+'/table.txt') + line(w3+h, out+'/table.txt') + line(w5+h, out+'/table.txt') + line(w6+h, out+'/table.txt') + line(w11+h, out+'/table.txt') + line(w9+h, out+'/table.txt') + line(w7+s, out+'/table.txt') + line(w8+s, out+'/table.txt') + line(w2+s, out+'/table.txt') + line(w9+s, out+'/table.txt') + line(w10+s, out+'/table.txt')
print(res)
f = open('/home/daniils/res.txt', 'w')
f.write(res)
f.close()
doc = aw.Document()
builder = aw.DocumentBuilder(doc)
font = builder.font
font.size = 16
font.name = "TimesNewRoman"
f = open('/home/daniils/res.txt', 'r')
paragraphFormat = builder.paragraph_format
paragraphFormat.first_line_indent = 15
paragraphFormat.alignment = aw.ParagraphAlignment.JUSTIFY
paragraphFormat.keep_together=True

table = builder.start_table()
builder.insert_cell()
builder.write("Name of phenotype")
builder.insert_cell()
builder.write("p-value")
builder.insert_cell()
builder.write("AUC-Loss")
builder.end_row()
for s in f:
    name = ''
    p = ''
    dec = ''
    n = 0
    for i in range(len(s)):
        if s[i] == '\t':
            n = n + 1
        if n == 0 and s[i] != '\t':
            name = name + s[i]
        if n == 1 and s[i] != '\t':
            p = p + s[i]
        if n == 2 and s[i] != '\t' and s[i] != '\n':
            dec = dec + s[i]
    builder.insert_cell()
    builder.write(name)
    builder.insert_cell()
    if p == 'NA':
        builder.write("NA")
    else:
        builder.write(str(roun(float(p))))
    builder.insert_cell()
    if dec == 'NA':
        builder.write("NA")
    else:
        builder.write(str(roun(float(dec))))
    builder.end_row()
builder.end_table()
f.close()
paragraphFormat = builder.paragraph_format
paragraphFormat.first_line_indent = 15
paragraphFormat.alignment = aw.ParagraphAlignment.CENTER
paragraphFormat.keep_together=True
font = builder.font
font.size = 16
font.bold = True    
font.name = "TimesNewRoman"
font.bold = False
doc.save(out+"/"+idd+".phen.docx")
#os.system('rm /home/flower/Desktop/res.txt')
#os.system('rm /home/flower/Desktop/table.txt')
