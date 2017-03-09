# coding: utf-8
# filename: 9-11, my_admin.py
import admin

if __name__ == '__main__':
    my_admin = admin.User('xu', 'deng')
    my_admin.describe_user()
    my_admin.privileges.show_privileges()
