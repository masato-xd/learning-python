#!/usr/bin/python
#coding: utf-8

import re

old_file = '/tmp/dev/release/bin/config25.json'

fopen = open(old_file,'r')

w_str = ""
for line in fopen:
    print line
    if re.search('1.1.1.1', line):
        line = re.sub('1.1.1.1','a.a.a.a',line)
        w_str+=line
    else:
        w_str+=line

wopen = open(old_file, 'w')

wopen.write(w_str)
fopen.close()
wopen.close()
