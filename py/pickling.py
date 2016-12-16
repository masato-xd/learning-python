#!/usr/bin/python
#coding: utf-8


import cPickle as p

# 我们将对象存储到这个文件名的文件中
shoplistfile = 'shoplist.data'


shoplist = ['apple', 'mango', 'carrot']


f = file(shoplistfile, 'w')
p.dump(shoplist, f) # shoplist的数据 ---p.dump---> shoplist.data
f.close()

del shoplist


f = file(shoplistfile)
storefile = p.load(f)  # storefile <---p.load--- 储存的文件(shoplist.data)
print storefile
