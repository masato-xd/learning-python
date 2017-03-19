# coding: utf-8

issue = "You can enter 'quit' exit:"
# print(issue)

full_name = raw_input("Plear enter your name: ")

with open('guest.txt', 'w') as file:
    file.write(full_name)
