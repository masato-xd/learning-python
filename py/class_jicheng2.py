#!/usr/bin/python
#coding: utf-8
# Filename: class_jicheng2.pyG


class SchoolMember(object):
    '''代表任何学校成员.'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print "初始化学校成员: %s" % self.name



    def info(self):
        '''告诉我详细信息'''
                                                        # 结尾加一个逗号, 可以取消自带的回车
        print "name: %s age: %d" % (self.name, self.age),


   
class Teacher(SchoolMember):
    '''代表老师'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print "初始化老师: %s" % self.name

    def info(self):
        SchoolMember.info(self)
        print "工资: %d" % self.salary

class Student(SchoolMember):
    '''代表学生'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print "初始化学生: %s" % self.name

    def info(self):
        SchoolMember.info(self)
        print "分数: %d" % self.marks

t = Teacher('teacher', 30, 5000)
s = Student('student', 18, 95)

print 
members = [t, s]

for member in members:
    member.info()
