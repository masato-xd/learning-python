#!/usr/bin/python
#coding: utf-8


'''列表综合来导出一个新的列表'''

listone = [1, 2, 3, 4, 5, 6]

# 满足条件(i > 2) 进行一个操作 (i * 2), 原来的list 不会有任何更改
listtwo = [i * 2 for i in listone if i > 2]

print listtwo
