#!/usr/bin/python
#coding: utf-8

class ShortInputException(Exception):
    '''用户自定义异常'''
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast




try:
    s = raw_input("输入一些内容--->")
    if len(s) < 3:
        # 提出异常
        raise ShortInputException(len(s), 3)
    # 在这里可以做其他工作
    print "输入大于3个字符"

except EOFError:
    print "\n出现EOF异常"

# 这是2.6之前的语法, 现在的语法是 ShortInputException as x, x是ShortInputException 类的对象
except ShortInputException, x:
# except ShortInputException as x:
    print "ShortInputException: 输入的长度是 %d, 至少需要 %d" % (x.length, x.atleast)

else:
    print "没有任何异常"
