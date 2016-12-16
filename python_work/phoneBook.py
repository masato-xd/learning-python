#!/usr/bin/python
# coding: utf-8
import pickle as p
import os
import sys

# 创建一个字典, 保存姓名, 关系, 电话
personDictionary = {'name': {'relationship': '', 'tel': ''}}

# 列表包含关系组成
relationshipList = ['家人', '朋友', '同事']


class Person():
'''调用此类, 会添加一个字典'''
# 当只输入姓名的时候, 默认(参数), 关系是 朋友, 电话 为空
    def __init__(self, name, relationship, tel):
        personDictionary[name] = {
            'relationship': relationship, 'tel': tel}


class Operation():

    @classmethod
    def Addperson(cls):
        addname = raw_input('请输入姓名:')
        addrelationship = input('请选择分组(0:家人, 1:朋友, 2:同事):')
        addtel = raw_input("请输入电话号码:")
        Person(addname, relationshipList[addrelationship], addtel)

    @classmethod
    def Delperson(cls):
        name = raw_input("请输入要删除的联系人姓名: ")
        del personDictionary[name]

    @classmethod
    def Search(cls):
        name = raw_input("请输入要查找的联系人姓名:")
        if name in personDictionary:
            print("姓名: %s, 关系: %s, 电话: %s" % (
                name,
                personDictionary[name]['relationship'],
                personDictionary[name]['tel']))
        else:
            print("联系人不存在")

    @classmethod
    def Quit(cls):
        global running
        running = False

    @classmethod
    def SaveQuit(cls):
        global running
        f = open(addressBookFile, "wb")
        p.dump(personDictionary, f)
        f.close()
        running = False


running = True

addressBookFile = 'addressbook.data'

if os.path.exists(addressBookFile):
    f = open(addressBookFile, 'rb')
    personDictionary = p.load(f)

else:
    jCommadn = raw_input("未找到通讯录文件, 是否创建?yes/no")
    if jCommadn == "yes":
        f = open(addressBookFile, 'wb')
        p.dump(personDictionary, f)
        f.close()
    elif jCommadn == "no":
        print "通讯录未创建"
        sys.exit()

while running:
    command = raw_input("请输入指令:")
    if command == 'add':
        Operation.Addperson()
        continue

    elif command == 'ser':
        Operation.Search()
        continue

    elif command == 'del':
        Operation.Delperson()
        continue
    elif command == 'quit':
        Operation.Quit()
        break

    elif command == 'sq':
        Operation.SaveQuit()
        break

    else:
        print("未找到指令")
        continue
