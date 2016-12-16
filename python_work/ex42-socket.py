# coding: utf-8
import socket
# AF_INET --- IPv4 协议
# SOCK_STREAM --- 面向流的TCP协议
# s 一个socket 对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('www.sina.com.cn', 80))

s.send('GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

# 接收数据
buffera = []

while True:
    d = s.recv(1024)
    if d:
        buffera.append(d)
    else:
        break
data = ''.join(buffera)

s.close()

header, html = data.split('\r\n\r\n', 1)
print header

with open('sina.html', 'wb') as f:
    f.write(html)
