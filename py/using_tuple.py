#!/usr/bin/python
#coding: utf-8


zoo = ('wolf', 'daxiang', 'houzi')

print "Number of animals in the zoo is", len(zoo)

new_zoo = ('changjinglu', 'she', zoo)

print 'new_zoo is', len(new_zoo)

print 'all animals new_zoo', new_zoo

print 'old zoo are', new_zoo[2]

print 'new zoo zuihou yige dongwu', new_zoo[2][2]


age = 22
name = 'bili'

print 'name is %s, age is %d' % (name, age)
print '%d' % age
