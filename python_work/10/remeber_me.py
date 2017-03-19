# coding: utf-8
import json


def get_stored_username():
    """如何存储了用户名， 就获取它"""
    filename = 'username.json'

    try:
        with open(filename) as f:
            username = json.load(f)
    except Exception as e:
        return None
    else:
        return username


def get_new_username():
    """提示用户输入新的用户名,并保存"""
    username = raw_input("Tell me you name: ")
    filename = 'username.json'

    with open(filename, 'w') as f:
        json.dump(username, f)
    return username


def greet_user():
    """判断用户、问候用户， 并指出姓名"""
    username = get_stored_username()
    correct_name = raw_input(username + r" is your name? y\n?")
    if correct_name == 'y':
        print('Welcome back ' + username)
    else:
        username = get_new_username()
        print("We'll remember you when you welcome back " + username.title())


if __name__ == '__main__':
    greet_user()
