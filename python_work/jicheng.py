# coding: utf-8


class Parent(object):

    """创建一个父类"""

    def __init__(self, last_name, eye_color):
        print "父类的构造函数被调用"
        self.last_name = last_name
        self.eye_color = eye_color

    def print_info(self):
        print self.last_name
        print self.eye_color

if __name__ == '__main__':

    # 必须有实例变量的参数
    billy_cyrus = Parent("cyrus", "blue")
    billy_cyrus.print_info()
