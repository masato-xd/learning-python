#!/usr/bin/python
#-*- coding: UTF-8 -*-

def printMax(x, y):
    '''首字母是大写, 句号结尾, 这一行是简单描述.
        这一行是空行
        这一行是具体描述.'''
    x = int(x) # convert to integers, if possible
    y = int(y)

    if x > y:
        print x, 'is maximum'
    else:
        print y, 'is maximum'

printMax(3, 5)

# 通过调用__doc__来调用, 上面的文档字符串内容
print printMax.__doc__
