#!/usr/bin/python
# coding: utf-8
import pickle as p
import os
import sys

personDictionary = {'name': {'relationship': '', 'tel': ''}}
relationshipList = ['家人', '朋友', '同事']


class Person():

#    def __init__(self, name, relationship=relationshipList[1], tel='None'):
    def __init__(self, name, relationship, tel):
        personDictionary[name] = {
            'relationship': relationship, 'tel': tel}


class Operation():

    @staticmethod
    def Addperson():
        addname = raw_input('请输入姓名:')
        addrelationship = input('请选择分组(0:家人, 1:朋友, 2:同事):')
        addtel = raw_input("请输入电话号码:")
        Person(addname, relationshipList[addrelationship], addtel)

    @staticmethod
    def Delperson():
        name = raw_input("请输入要删除的联系人姓名: ")
        del personDictionary[name]

    @staticmethod
    def Search():
        name = raw_input("请输入要查找的联系人姓名:")
        if name in personDictionary:
            print("姓名: %s, 关系: %s, 电话: %s" % (
                name,
                personDictionary[name]['relationship'],
                personDictionary[name]['tel']))
        else:
            print("联系人不存在")

    @staticmethod
    def Quit():
        global running
        running = False

    @staticmethod
    def SaveQuit():
        global running
        f = open(addressBookFile, "w")
        p.dump(personDictionary, f)
        f.close()
        running = False


running = True

addressBookFile = 'addressbook.data'

if os.path.isfile(addressBookFile):
    f = open(addressBookFile, 'r')
    personDictionary = p.load(f)

else:
    jCommadn = raw_input("未找到通讯录文件, 是否创建?yes/no")
    if jCommadn == "yes":
        f = open(addressBookFile, 'w')
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
