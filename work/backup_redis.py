#!/usr/bin/python
# coding: utf-8
# Filename: backup_redis.py

from datetime import date
from datetime import timedelta
from datetime import datetime
import os
import commands


def get_hours_ago_time():
    """获取前2小时时间"""
    now_time = datetime.now()

    d = now_time - timedelta(hours=2)
    return d.strftime("%m%d%H")


if __name__ == '__main__':
    today = datetime.now().strftime("%m%d")
    back_dir = '/home/qqdz/backup/' + today

    (status, output) = commands.getstatusoutput('/usr/local/bin/redis-cli -p 6102 bgsave')
    if status != 0:
        print output
    else:
        print output
