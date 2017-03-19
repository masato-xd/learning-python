# coding: utf-8


def count_words(filename):
    """计算文本中有多少个单词"""
    try:
        with open(filename) as file:
            contents = file.read()
    except IOError as e:
        # print("No such file or directory: " + filename)
        print(e)
    else:
        words_num = len(contents.split())
        print(filename + ' ' + str(words_num) + " danci")


filenames = ['alice.txt', 'hh', 'little_women.txt', 'moby_dick.txt']
for filename in filenames:
    count_words(filename)
