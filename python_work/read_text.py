# coding: utf-8
import urllib


def read_text():
    ques = open("C:\Users\Administrator\Documents\quotes.txt")
    conn = ques.read()
    print conn
    print type(conn)
    check_profanity(conn)
    ques.close()


def check_profanity(check_of_file):
    # 打开一个连接(访问url)
    connection = urllib.urlopen(
        "http://www.wdylike.appspot.com/?q=" + check_of_file)
    output = connection.read()
    if "true" in output:
        print "语句包含x"
    elif "flase":
        print "语句不包含x"
    else:
        print "没有找到相关词语"
    connection.close()


read_text()
