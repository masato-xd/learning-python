#!/usr/bin/python
#coding: utf-8

class Animal(object):
    '''创建一个继承自object的animal类
    
        定义一个run方法.'''
    def run(self):
        print "Animal is run...."



# 继承自Animal
class Dog(Animal):
    # 重写父类方法
    def run(self):
        print 'dog is run....'


class Cat(Animal):
    def run(self):
        print 'cat is run...'

# python中, 只要传入的对象有对应的(run())方法, 就可以实现函数
def run_twice(animal):
    animal.run()
    animal.run()

class Wugui(object):
    def run(self):
        print 'speed so lowly....'


if __name__ == "__main__":

    animal = Animal()
    dog = Dog()
    cat = Cat()
    wugui = Wugui()

    print type(cat)
    run_twice(wugui)
