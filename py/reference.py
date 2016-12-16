#!/usr/bin/python
#coding: utf-8

shoplist = ['a', 'b', 'c', 'd']

# 指向同一个对象的另一个名称而已
mylist = shoplist

del shoplist[0]

print "shoplist is %s" % shoplist

print "mylist is %s" % mylist

# 通过切片做一个完整的副本
mylist = shoplist[:]

del shoplist[-1]

print "shoplist is %s" % shoplist

print "mylist is %s" % mylist
