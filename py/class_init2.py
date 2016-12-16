#!/usr/bin/python
#coding: utf-8

class Student():
    # self 永远存在, 代表实例对象自己
    # name, age 代表这个类的两个属性
    # 创建一个对象的时候自动初始化
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


    # 数据封装
    # 类的方法
    def print_info(self):
        print '%s : %s'% (self.name, self.age)



    def get_grade(self):
        
        if self.score >= 90:
            return 'A'
        elif self.score >= 70:
            return 'B'
        else :
            return 'C'




bali = Student("bali", 20, 99)

marry = Student("marry", 19, 75)


# 直接调用方法, 得到结果
bali.print_info()
marry.print_info()

print bali.get_grade()
print marry.get_grade()
