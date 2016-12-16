#!/usr/bin/python
#-*- coding: UTF-8 -*-

# 关键参数值(关键字参数, 命名参数)
def say(a, b=10, c=55):
    print 'a is', a
    print 'b is', b
    print 'c is', c


say(100)
say(c=20, a=101)
say(a=111, b=222, c=333)
