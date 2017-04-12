# coding:utf-8

from datetime import date
from datetime import timedelta
from datetime import datetime
import os
import sys
import socket
import commands

now_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
hostname = socket.gethostname()


def getYesterday():
    """获取昨天的日期"""
    today = date.today()
    oneday = timedelta(days=1)
    yesterday = today - oneday
    yesterday = yesterday.strftime(fmt)
    return yesterday


def ftp_upload(dirs):
    """将日志文件上传到韩国ftp服务器"""
    print("开始上传日志")
    (status, output) = commands.getstatusoutput('/usr/local/bin/ncftpput -m -R -r 1 -t 3 -u bob -p dWh4Myd4 %s /%s %s' % (ftp_ip, hostname, dirs))
    if status != 0:
        print output
    else:
        print output


def del_dir(dir):
    pass


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("used: python %s remote_ip" % sys.argv[0])
    else:
        ftp_ip = sys.argv[1]
        fmt = '%y%m%d'
        back_dir = "/log/%s" % getYesterday()
        if not os.path.exists(back_dir):
            os.system('mkdir -p %s' % back_dir)
            os.system('mv /log/*20%s* %s' % (getYesterday(), back_dir))
            print(now_time + " mv ok")
        else:
            pass

        ftp_upload(back_dir)
