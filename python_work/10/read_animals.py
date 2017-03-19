# coding: utf-8
file_name = 'cat.txt'

try:
    with open(file_name) as file_object:
        contents = file_object.read()
except IOError:
    print("file no")
else:
    print(contents)
