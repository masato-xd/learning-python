# coding: utf-8
from datetime import date
from datetime import timedelta
from datetime import datetime
import glob
import os


def get_yesterday(fmt, day_num=1):
    """获取前几天的日期，默认前一天"""
    today = date.today()
    oneday = timedelta(days=day_num)
    yesterday = today - oneday
    yesterday = yesterday.strftime(fmt)
    return yesterday

if __name__ == '__main__':
    fmt = '%y%m%d'
    fmt_csv = '%Y-%m-%d'

    os.system('mkdir /tmp/flow/')
    save_csv = '/tmp/flow/' + get_yesterday(fmt_csv) + '.csv'
    file_path = '/log/' + get_yesterday(fmt) + '/log_proxy.log.INFO*'
    file_path = glob.glob(file_path)
    file_path.sort()

    flow_keys = {}
    pid_keys = {}
    wo_appid = '31647'

    for file_object in file_path:
        if file_object:
            with open(file_object) as f:
                for line in f:
                    if '流量统计' in line.split():
                        phone = line.strip().split(',')[-4]
                        pid = line.strip().split(',')[-3]
                        flow_value = int(line.strip().split(',')[-1])

                        if phone:
                            if phone not in flow_keys.keys():
                                flow_keys[phone] = [flow_value, ]
                                pid_keys[phone] = pid
                            else:
                                flow_keys[phone].append(flow_value)
                                pid_keys[phone] = pid

    with open(save_csv, 'w+') as f:

        for phone, value in flow_keys.items():
            f.write(phone + ',' + pid_keys[phone] + ',' + wo_appid + ',' + str(sum(value)) + '\n')
