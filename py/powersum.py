#!/usr/bin/python
#coding: utf-8

#def powersum(power, *args):
#    '''计算指定数的power次方'''
#
#    total = 0
#    for i in args:
#
#        total += pow(i, power)
#
#    return total

def powersum(power, *args):

    total = 0
    for i in args:
        total = total + i * power

    return total

nlist = [2, 3, 4]

#  nlist 的所有元素作为可变参数传入函数
print powersum(2, *nlist)


def printinfo(arg, **kw):
    
    for key, value in kw.items():
        print "key : %s, value : %s" % (key, value)



d = {"name":'bali', "age":20, "city":'shanghai'}

printinfo(1, **d)
