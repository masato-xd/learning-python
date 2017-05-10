#!/bin/env python
# coding: utf-8
import urllib
import urllib2
import sys
import json
import time

print "start"
url = 'http://api.cn-wolf.cn/Edition/BattleOfBalls/API/ld.php?url=%s' % sys.argv[1]
req = urllib2.Request(url)

# 模拟get请求头
req.add_header('Referer', 'http://www.qiuqiu6.com/?qqdrsign=04952')
req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36')
req.add_header('Host', 'api.cn-wolf.cn')
req.add_header('Origin', 'http://www.qiuqiu6.com')
req.add_header('Accept', 'application/json, text/javascript, */*; q=0.01')
req.add_header('Accept-Encoding', 'gzip, deflate, sdch')
req.add_header('Accept-Language', 'zh-CN,zh;q=0.8')


res = urllib2.urlopen(req).read()
print "res", res

json_data = json.loads(res)

id = json_data.get('id', 0)
print "id", id

ts = int(time.time() * 1000)
for i in xrange(5):
    url = 'http://cn.battleofballs.com/share?type=3&id=%s&callback=jQuery3000009113890918245549_%s&_=%s' % (id, ts, ts + 1)
    print url
    print urllib.urlopen(url).read()


url_b = 'http://api.cn-wolf.cn/Edition/BattleOfBalls/API/?url=%s' % sys.argv[1]
req_b = urllib2.Request(url_b)
req_b.add_header('Referer', 'http://www.qiuqiu6.com/?qqdrsign=04952')
req_b.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36')
req_b.add_header('Host', 'api.cn-wolf.cn')
req_b.add_header('Origin', 'http://www.qiuqiu6.com')
req_b.add_header('Accept', 'application/json, text/javascript, */*; q=0.01')
req_b.add_header('Accept-Encoding', 'gzip, deflate, sdch')
req_b.add_header('Accept-Language', 'zh-CN,zh;q=0.8')
res_b = urllib2.urlopen(req_b).read()
print "res", res_b


print "end"
