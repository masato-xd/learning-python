# coding=utf-8
def listP(list_old):
    list_new = []
    dict_new = {}
    dict_new = dict.fromkeys(list_old, 1)  # 调用dict内嵌函数生成新的dict对象
    # 将dict的key值直接转成list
    list_new = list(dict_new.keys())
    return list_new


list_old = [1, 12, 2, 2, 3, 3, 5, 6]

print "old_list:"

for i in list_old:
    print i,

list_result = []

list_result = listP(list_old)

print "\nnew_list:"
for i in list_result:
    print i,
