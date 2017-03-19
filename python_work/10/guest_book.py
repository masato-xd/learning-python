# coding: utf-8

issue = "You can enter 'quit' exit!\n"
# issue += "please enter your name: "

full_name = ''

# while full_name != 'quit':
#     full_name = raw_input(issue)
#     if full_name != 'quit':
#         print('hello, ' + full_name)
#         with open('guest_book.txt', 'a') as file:
#             file.write(full_name + ' Welcome your arrival\n')


print(issue)
while True:
    full_name = raw_input("\nEnter your name: ")

    if full_name == 'quit':
        break
    print('hello, ' + full_name)
    with open('guest_book.txt', 'a') as file:
        file.write(full_name + ' Welcome your arrival\n')
