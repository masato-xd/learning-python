#!/usr/bin/python
#coding: utf-8


poem = '''\
编程很有趣
当你完成工作时
如果你想要你的工作很有趣:
    使用python
'''

# 打开并写模式
f = file('poem.txt', 'w')
f.write(poem)
f.close()

# 默认是读模式
f = file('poem.txt')

hile True:
    line = f.readline()
    if len(line) == 0:
        break

    print line,

f.close()
