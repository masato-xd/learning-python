# coding: utf-8
from datetime import date
from datetime import timedelta
from datetime import datetime
import glob
import os
import commands
import sys


def get_yesterday(fmt, day_num=1):
    """获取前几天的日期，默认前一天"""
    today = date.today()
    oneday = timedelta(days=day_num)
    yesterday = today - oneday
    yesterday = yesterday.strftime(fmt)
    return yesterday


def ftp_upload(file):
    """将日志文件上传到ftp服务器"""
    print("开始上传日志")
    (status, output) = \
        commands.getstatusoutput(
            "/usr/local/bin/ncftpput -m -R -r 3 -t 5 -P 10021 -u flow_qiuqiu -p '8#Fn5!s*yqey' %s / %s" % (ftp_ip, file))
    if status != 0:
        print output
    else:
        print output

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("\n    Used: python %s remote_ip\n" % sys.argv[0])
    else:
        fmt = '%y%m%d'
        fmt_csv = '%Y-%m-%d'
        ftp_ip = sys.argv[1]
        save_csv = '/tmp/flow/' + get_yesterday(fmt_csv) + '.csv'
        file_path = '/home/ftpflow/' + get_yesterday(fmt) + '/log_proxy.log.INFO*'
        file_path = glob.glob(file_path)
        file_path.sort()

        flow_keys = {}
        pid_keys = {}
        wo_appid = '31647'
        os.system('mkdir -p /tmp/flow/')

        for file_object in file_path:
            if file_object:
                with open(file_object) as f:
                    for line in f:
                        if '流量统计' in line.split():
                            phone = line.strip().split(',')[-4]
                            pid = line.strip().split(',')[-3]
                            flow_value = float(line.strip().split(',')[-1])
                            flow_value = flow_value / 1024 / 1024
                            flow_value = round(flow_value, 2)

                            if phone:
                                try:
                                    flow_keys[phone] = [flow_value, ]
                                    pid_keys[phone] = pid
                                except Exception as e:
                                    flow_keys[phone].append(flow_value)
                                    pid_keys[phone] = pid

        with open(save_csv, 'w+') as f:
            for phone, value in flow_keys.items():
                f.write(phone + ',' + pid_keys[phone] + ',' + wo_appid + ',' + str(sum(value)) + '\n')

        try:
            ftp_upload(save_csv)
        except Exception as e:
            print e
