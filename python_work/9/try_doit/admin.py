# coding: utf-8
from user import User

# class User(object):

#     def __init__(self, first_name, last_name, **args):
#         """初始化用户的基本属性"""
#         self.first_name = first_name
#         self.last_name = last_name
#         self.args = args
#         self.login_attempts = 0
#         self.privileges = Privileges()

#     def describe_user(self):
#         """返回描述性的信息"""
#         full_name = self.first_name + self.last_name
#         print("姓名: " + full_name.title() + '\n其他信息: ' + str(self.args))

#     def greet_user(self):
#         """对用户打招呼"""
#         full_name = self.first_name + self.last_name
#         print("Hello! " + full_name.title() + '\n')


class Admin(User):

    """docstring for Admin"""

    def __init__(self, first_name, last_name, **args):
        super(Admin, self).__init__(first_name, last_name, **args)
        self.first_name = first_name
        self.last_name = last_name
        self.args = args


class Privileges(object):

    """docstring for Privileges"""

    def __init__(self, privileges=['can add post',
                                   'can delete post',
                                   'can ban user']):
        self.privileges = privileges

    def show_privileges(self):
        for l in self.privileges:
            print(l)

if __name__ == '__main__':

    xd = User('x', 'd')

    xd.describe_user()
    xd.greet_user()
    xd.privileges.show_privileges()
