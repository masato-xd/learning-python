# coding: utf-8
from jicheng import Parent


class Child(Parent):

    """docstring for Child"""

    def __init__(self, last_name, eye_color, age):
        print("子类的构造函数被调用")
        Parent.__init__(self, last_name, eye_color)
        self.age = age

        # 方法覆盖, 父类中有同名的方法
    def print_info(self):
        print self.last_name
        print self.eye_color
        print self.age

miley_cyrus = Child("cyrus", "red", 20)
# print(miley_cyrus.last_name)
# print(miley_cyrus.age)
miley_cyrus.print_info()
