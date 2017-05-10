# coding: utf-8
import urllib


words = []


def read_text():
    with open('words.txt') as files:
        for f in files:
            words.append(f.rstrip())


def check_files(user_input):
    if user_input in words:
        print "包含x"
    else:
        print "不包含"


read_text()
issue = "Enter 'quit' exit!"

while True:
    user_input = raw_input(issue + '\t' + 'please input string:')

    if user_input != 'quit':
        check_files(user_input)

    else:
        print "退出"
        break
