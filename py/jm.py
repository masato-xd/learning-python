#!/usr/bin/python
#-*- coding: UTF-8 -*-

#def printMax(a, b):
#    if a > b:
#        print a, 'is max'
#
#    else :
#        print b, 'is max'
#
#
#
#printMax(3,4)
#
#x = 1
#y = 11
#
#printMax(x,y)


def func(x):

    print "x is", x
    x = 2
    #局部变量不会影响外部变量
    print 'change local x to', x

x = 50
func(x)
print 'x is still', x


def fund():
    
    #global 定义全局变量
    global x
    print 'x is', x
    x = 2
    print 'change local x to', x

x = 50
fund()
print 'x is', x

