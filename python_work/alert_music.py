# -*- coding: UTF-8 -*-
import webbrowser
import time

count = 0
print(u"当前时间:%s" % time.ctime())
while True:
    count += 1
    print(u"当前循环到第%s次" % count)

    time.sleep(50*60)

    webbrowser.open("http://www.xiami.com/radio/play/id/2")
