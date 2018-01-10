#!python3
# coding: utf-8
# author: xd
# date: 17-08-15

import sys
import os
import http.client
import urllib
import json
import time

username = 'qiuqiu_cdn'
password = 'qq5tgb$RFV'

http_Client = None
headers = {"Content-Type": "application/json"}
http_Client = http.client.HTTPConnection('122.11.47.186', 5000, timeout=30)


def get_token():
    try:
        params = {'username': username, 'password': password}
        params = json.dumps(params)
        http_Client.request('POST', '/cdn_api/tokens', params, headers)
        response = http_Client.getresponse()
        reqs = response.read()
    except Exception as e:
        print(e)
    try:
        token = json.loads(reqs)
        token = token["access"]["token"]["id"]
        return token
    except Exception as e:
        print(reqs)
        sys.exit(1)


def prefetch(urls):
    token = get_token()
    try:
        headers = {"Content-Type": "application/json", "X-Auth-Token": token}
        params = {"urls": urls}
        params = json.dumps(params)
        http_Client.request('POST', '/cdn_api/prefetch', params, headers)
        response = http_Client.getresponse()
        reqs = response.read()
        # print(type(reqs))
    except Exception as e:
        print(e)
    reqid = json.loads(reqs)
    # for k, v in reqid.items():
    #    print(k, v)
    return reqid


def main(path, ver):
    html_path = r'http://cdn1.battleofballs.com/'
    urls = []

    with os.scandir(path) as dir_entry:
        for entry in dir_entry:
            if entry.is_dir() and "旧资源" not in entry.name:
                print('\n' + "        目录名称是: " + "[ " + ver + '/' + entry.name + " ]")
                for root, dirs, files in os.walk(entry.path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        if "旧资源" not in file_path and "common" in file_path:
                            if "reslow" in ver:
                                reslow = ver.split('/')
                                ver = reslow[1] + '/' + reslow[2]
                            full_html = html_path + ver + "/" + '/'.join(file_path.replace('\\', '/').split('/')[6:])
                            urls.append(full_html)
                            print(full_html)
    print('\n')
    return urls

if __name__ == '__main__':

    try:
        ver = sys.argv[1].split('_')[-1]
        urls = main(sys.argv[1], ver.replace('\\', '/'))
        for url in [urls[i:i + 10] for i in range(0, len(urls), 10)]:
            prefetch(url)
            time.sleep(1)
        print("预热成功")

    except IndexError:
        print("\n" + "  Used: " + sys.argv[0] + " full_path" + "\n")

    except Exception as e:
        print('\n', e)
