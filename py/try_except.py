#!/usr/bin/python
#coding: utf-8

import sys
'''处理错误异常'''

try:
    s = raw_input('输入一些东西--->')

# 异常的名称(这是具体存在的)
except EOF:
    print '\nwhy did you do an EOF on me?'
    sys.exit()

# 这会处理所有的错误和异常
except:
    print '\nsome error/exception occurred.'

print 'Done'
