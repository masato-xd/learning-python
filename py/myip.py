#!/usr/bin/python
#coding: utf-8

#import socket
#
#my_name = socket.getfqdn(socket.gethostname())
#
#my_ip = socket.gethostbyname(my_name)
#
#print my_name, my_ip

import socket
import fcntl
import struct
import sys
  
'''根据网卡名获取ip'''

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])


if __name__ == '__main__':

    
    if len(sys.argv) < 2:

        print "使用方法: ./myip.py eth0"
        sys.exit()

    else:

        ifname = sys.argv[1]

        print get_ip_address(ifname)
