#!/usr/bin/python
# coding: utf-8

import sys
import getopt

try:                            # 过滤第1个参数(从0开始), cb: b后面需要接参数, 所以加:
    opts, args = getopt.getopt(sys.argv[1:], "a:dec", ["file="])

except getopt.GetoptError as e:
    print 'Error:', e.msg
    sys.exit()


def catfile(filename):
    '''查看文件内容'''
    with open(filename) as f:
        for line in f.readlines():
            print line,

for op, value in opts:
    print op, value
    print '---------'
    if op in ('--file'):
        #        print '选项--file'
        filename = value

    if op in ('-a'):
        action = value

#    if op in ('-d'):
#        print '选项-del'
#
#    if op in ('-e'):
#        print '选项-edit'

#    if op in ('-c'):
#        print '选项-cat'


if 'action' in dir():
    print '正常运行'
else:
    print '无参数, 值'
    sys.exit()


if action == 'del':
    print '删除文件内容'

elif action == 'edit':
    print '编辑文件内容'

elif action == 'cat':
    catfile(filename)
