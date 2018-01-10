#!python3
# coding: utf-8
import httplib
import urllib
import json
import sys

# please enter your id
username = 'qiuqiu_cdn'
password = 'qq5tgb$RFV'

httpClient = None
headers = {"Content-Type": "application/json"}
httpClient = httplib.HTTPConnection('api.cloudcdn.twocloud.cn', 5000, timeout=30)


def get_token():
    try:
        params = {'username': username, 'password': password}
        params = json.dumps(params)
        httpClient.request('POST', '/cdn_api/tokens', params, headers)
        response = httpClient.getresponse()
        reqs = response.read()
    except Exception, e:
        print e
    try:
        token = json.loads(reqs)
        token = token["access"]["token"]["id"]
        return token
    except Exception, e:
        print reqs
        sys.exit(1)


def prefetch(urls):
    token = get_token()
    try:
        headers = {"Content-Type": "application/json", "X-Auth-Token": token}
        # urls = urls.split(",")
        params = {"urls": urls}
        params = json.dumps(params)
        httpClient.request('POST', '/cdn_api/prefetch', params, headers)
        response = httpClient.getresponse()
        reqs = response.read()
    except Exception, e:
        print e
    reqid = json.loads(reqs)
    reqid = reqid["reqId"]
    return reqid


def get_status(reqid):
    token = get_token()
    try:
        headers = {"X-Auth-Token": token}
        params = ""
        httpClient.request('GET', '/cdn_api/req_status/' + reqid, '', headers)
        response = httpClient.getresponse()
        status = response.read()
    except Exception, e:
        print e
    status = json.loads(status)
    return status["task"]["taskStatus"]

if __name__ == '__main__':
    prefetch(urls)
