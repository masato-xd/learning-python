# coding:utf-8

from datetime import date
from datetime import timedelta
from datetime import datetime
import os
import sys
import socket
import commands


hostname = socket.gethostname()


def get_now_time():
    """获取当前时间"""
    now_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return now_time


def get_yesterday():
    """获取昨天的日期"""
    today = date.today()
    oneday = timedelta(days=1)
    yesterday = today - oneday
    yesterday = yesterday.strftime(fmt)
    return yesterday


def ftp_upload(dirs):
    """将日志文件上传到ftp服务器"""
    print("开始上传日志")
    (status, output) = commands.getstatusoutput('/usr/local/bin/ncftpput -m -R -r 3 -t 5 -u bob -p dWh4Myd4 %s /%s %s' % (ftp_ip, hostname, dirs))
    if status != 0:
        print output
    else:
        print output


def del_dir(dir):

    pass


def check_port(ftp_ip):
    """判断端口是否连通"""
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.settimeout(5)
    try:
        sk.connect((ftp_ip, 21))
        sk.close()
        return 1
    except Exception as e:
        sk.close()
        print(get_now_time() + ' Server port 21 not connect!')
        return 0


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("\n     used: python %s remote_ip\n" % sys.argv[0])
    else:
        ftp_ip = sys.argv[1]
        fmt = '%y%m%d'
        back_dir = "/log/%s" % get_yesterday()
        if not os.path.exists(back_dir):
            os.system('mkdir -p %s' % back_dir)
            os.system('mv /log/*20%s* %s' % (get_yesterday(), back_dir))
            print(get_now_time() + " mv ok")
        else:
            print(get_now_time() + " Directory exists")

        if check_port(ftp_ip):
            ftp_upload(back_dir)
        else:
            pass