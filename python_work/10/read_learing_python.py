# coding: utf-8
file_name = 'learing_python.txt'

with open(file_name) as file:
    contents = file.read()
    print(contents)
    print('-' * 10)


with open(file_name) as files:
    for file in files:
        print(file.rstrip())
    print('-' * 20)


with open(file_name) as files:
    lines = files.readlines()

learing_txt = ''
for line in lines:
    learing_txt += line.strip() + '.'
print(learing_txt)
print('-' * 20)


with open(file_name) as files:
    for file in files:
        print(file.replace('Python', 'c').strip())
