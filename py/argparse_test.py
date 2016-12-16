#!/bin/usr/python
# coding: utf-8

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("echo", help="显示你在这里输入的字符串")
args = parser.parse_args()
print args.echo
