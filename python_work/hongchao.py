# coding: utf-8
"""
	取出文件两列数值中，第二列相同，第一列取最大
	"""

file_object = r'D:\Users\xudeng\Documents\hot.txt'

user_dicts = {}

with open(file_object) as f:
    for line in f:

        user_info = line.split()[-1]
        user_num, user_id = user_info.split(',')
        if user_id not in user_dicts:
            user_dicts[user_id] = [int(user_num)]
        else:
            user_dicts[user_id].append(int(user_num))


with open(r'D:\Users\xudeng\Documents\user.txt', 'a') as f:
    for key, value in user_dicts.items():
        f.write(key + ',' + str(max(value)) + '\n')

# max对比字符串遇到'9'是最大,的问题
