#!/usr/bin/python
#coding: utf-8

class Person():
    def __init__(self, name):
        self.name = name

    def sayHi(self):
        print 'HI, my name is %s' % self.name

p = Person('xd')

p.sayHi()
