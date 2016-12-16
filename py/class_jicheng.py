#!/usr/bin/python
#coding: utf-8


class Animal(object):
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



if __name__ == "__main__":
    dog = Dog()
    cat = Cat()
    
    
    dog.run()
    cat.run()

    print dir(dog)
    print dir(cat)
