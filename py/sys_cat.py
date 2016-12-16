#!/usr/bin/python
#coding: utf-8

import sys

def readfile(filename):
    '''print a file to the standard output.\
        将文件打印到标准输出'''


    f = file(filename)
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print line,


    f.close()


# 脚本从这开始运行

if len(sys.argv) < 2:
    print "No action specified.未指定操作"
    sys.exit()

# 参数是以 -- 开始
if sys.argv[1].startswith('--'):
    option = sys.argv[1][2:]

    if option == 'version':
        print 'version 1.2'

    elif option == 'help':
        print '''\
This program prints files to the standard output.
Any number of files can be specified.
Options include:
  --version : Prints the version number
  --help    : Display this help'''

 
    else: 

        print 'Unknow option'
    sys.exit()

else:
    for filename in sys.argv[1:]:
        readfile(filename)

# print readfile.__doc__
