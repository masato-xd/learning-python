#!/usr/bin/python
#coding: utf-8
#Auther: xd,20161206

import os,sys
import re
import glob
import fileinput

bgp_ip = 'a.a.a.a'
yd_ip = 'b.b.b.b'
nw_ip = 'c.c.c.c'
voice_tcp_ip = 'd.d.d.d'
voice_udp_ip = 'f.f.f.f'

jsonstr = '.json'
# 获取所有config文件
files = glob.glob('/tmp/dev/release/bin/config[0-9]*.json')


# 根据网卡名获取IP
def get_ip(ifname)
    pass


# 修改ip 
for jsonfile in files:
       
    for line in fileinput.input(jsonfile, inplace=1):
        print line.replace('1.1.1.1', bgp_ip).rstrip()

    for line in fileinput.input(jsonfile, inplace=1):
        print line.replace('2.2.2.2', yd_ip).rstrip()

    for line in fileinput.input(jsonfile, inplace=1):
        print line.replace('3.3.3.3', nw_ip).rstrip()

    for line in fileinput.input(jsonfile, inplace=1):
        print line.replace('4.4.4.4', voice_tcp_ip).rstrip()

    for line in fileinput.input(jsonfile, inplace=1):
        print line.replace('5.5.5.5', voice_udp_ip).rstrip()

    for line in fileinput.input(jsonfile, inplace=1):
        print line.replace('6.6.6.6', voice_udp_ip).rstrip()


print 'done'
