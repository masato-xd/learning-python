
file_path = \
    r"D:\Users\xudeng\Documents\GitHub\learning-python\python_work\10\pi_million_digits.txt"

# with open('pi_digits.txt') as file_object:
# with open(file_path) as file_object:
#     contents = file_object.read()
#     print(contents)


# with open(file_path) as file_object:
#     for line in file_object:
#         print line.rstrip()


# with open(file_path) as file_object:
#     lines = file_object.readlines()
#     for line in lines:
#         print line.rstrip()


# with open(file_path) as file_object:
#     lines = file_object.readlines()
# pi_string = ''
# for line in lines:
#     pi_string += line.strip()
# print(pi_string[:50])


with open(file_path) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = raw_input('Enter your birthday: ')
if birthday in pi_string:
    print('Your birthday appears in the first million digits of pi!')
else:
    print('Your birthday does not pi.')
