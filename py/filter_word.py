#!/usr/bin/python
#coding: utf-8

import sys

finput = []
finput = finput.append(raw_input("请输入内容:"))

f = open("words.txt")

files = f.readlines()

f.close()

if finput in files:
    print "Freedom";
    finput = []

else:
    print "Human Rights"
    finput = []

