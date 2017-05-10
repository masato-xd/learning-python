#!/usr/bin/python
# coding: utf-8


import time

try:
    f = file('poem.txt')
    while True:
        line = f.readline()
        if len(line) == 0:
            break

        time.sleep(2)
        print line,

except KeyboardInterrupt:
    print "出现了吧异常"


# 不管出现异常与否, 最后总会执行
finally:
    f.close()
    print 'close the file'
