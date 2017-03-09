# coding: utf-8


class User(object):

    def __init__(self, first_name, last_name, **args):
        """初始化用户的基本属性"""
        self.first_name = first_name
        self.last_name = last_name
        self.args = args
        self.login_attempts = 0

    def describe_user(self):
        """返回描述性的信息"""
        full_name = self.first_name + self.last_name
        print("姓名: " + full_name.title() + '\n其他信息: ' + str(self.args) + '\n')

    def show_login_attempts(self):
        print("登陆次数: " + str(self.login_attempts))

    def greet_user(self):
        """对用户打招呼"""
        full_name = self.first_name + self.last_name
        print("Hello! " + full_name.title() + '\n')

    def increment_login_attemps(self, new_login_num):
        """累加登陆次数"""
        if new_login_num >= self.login_attempts:
            self.login_attempts += new_login_num
        else:
            print("登陆次数无法回退")

    def reset_login_attemps(self):
        """重置登陆尝试次数"""
        self.login_attempts = 0

if __name__ == '__main__':

    bali = User('ba', 'li')
    bali.describe_user()

    bali.increment_login_attemps(1)
    bali.show_login_attempts()

    bali.reset_login_attemps()
    bali.show_login_attempts()
