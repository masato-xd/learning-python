#!/usr/bin/python
#coding: utf-8


import os
import time

# 1. The files and directories to be backed up are specified in a list.
source = ['/etc/passwd', '/etc/sysconfig/network-scripts/']
# If you are using Windows, use source = [r'C:\Documents', r'D:\Work'] or something like that

# 2. The backup must be stored in a main backup directory
# 主备分目录
target_dir = '/mnt/' # Remember to change this to what you will be using

# 日期作为子目录存在主备份目录中
today = target_dir + time.strftime('%Y%m%d')

# 当前备份时间作为zip文档名
now = time.strftime('%H%M%S')

if not os.path.exists(today):
    os.mkdir(today)
    print 'Successfully created dir', today

# os.sep 根据系统自动选择分隔符
target = today + os.sep + now +'.zip'

zip_command = "zip -qr '%s' %s" % (target, ' '.join(source))

if os.system(zip_command) == 0:
    print 'Successful backup to', target
else:
    print 'Backup FAILED'
