#!/usr/bin/python
#-*- coding: UTF-8 -*-
#import os
#from threading import Thread
#
#def get_data(num):
#    print('sum to {0} with pid {1}'.format(num, os.getpid()))
#    return sum([i for i in range(num)])
#
#def main():
#    data = [ i for i in range(10) ]
#    threads = []
#    for num in data:
#        thread = Thread(target=get_data, args=(num,))
#        thread.start()
#        threads.append(thread)
#
#    for thread in threads:
#        thread.join()
#
#if __name__ == '__main__':
#    main()

import requests
from multiprocessing import Pool

def get_website_data(url):
    r = requests.get(url)
    return r.url

def main():
    urls = ['http://mingxinglai.com',
            'http://www.baidu.com',
            'http://163.com']
    pool = Pool(2)
    print pool.map(get_website_data, urls)

main()
