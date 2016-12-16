#!/usr/bin/python
#coding: utf-8

class Student():
    def __init__(self, name, age, score):
        # 加__ 代表将变量设为私有变量
        self.__name = name
        self.__age = age
        self.__score = score


    # 数据封装
    # 类的方法
    def print_info(self):
        print '%s : %s'% (self.__name, self.__age)

    # 给私有变量设置get方法
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    # 给私有变量设置set方法
    def set_age(self, age):
        # 可以在set中设置条件判断
        if 0 <= age <= 100:

            self.__age = age

        else:
            # 设置错误提示
            raise ValueError("age must 10<= age <=100")


if __name__ == '__main__':

    bali = Student("bali", 20, 99)
    print 'name:%s, age:%d' % (bali.get_name(), bali.get_age())
    
    bali.set_age(222)
    print "name:%s, 年龄改为: %d" % (bali.get_name(), bali.get_age())
    
    bali.get_age()
    
    
    
    
    
    
    # 直接调用方法, 得到结果
    #bali.print_info()
    #marry.print_info()

