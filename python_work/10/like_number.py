# coding: utf-8
import json


def get_new_number():
    num = raw_input("Tell me you like number: ")
    file_name = 'like_number.json'
    with open(file_name, 'w') as f:
        json.dump(num, f)
    return num


def get_stored_number():
    file_name = 'like_number.json'
    try:
        with open(file_name) as f:
            num = json.load(f)
    except:
        return None
    else:
        return num


def greet_number():
    num = get_stored_number()
    if num:
        print("I know your favorite number!It's " + num)
    else:
        num = get_new_number()
        print('You like number is ' + num)

greet_number()
