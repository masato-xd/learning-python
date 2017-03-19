file_name = 'boys.txt'

with open(file_name) as f:
    the_num = f.read()
    print(the_num.lower().count('ha'))
