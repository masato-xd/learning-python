# -*- coding: utf-8 -*-
import os


def rename_files():
    file_list = os.listdir(r"E:\test\prank\prank")  # 文件目录

    save_dir = os.getcwd()  # 当前工作目录, Current Work Dir

    os.chdir(r"E:\test\prank\prank")  # 切换工作目录

    for file_name in file_list:

        print(file_name)  # 打印出修改前后的文件名
        print(file_name.translate(None, "0123456789"))

        os.rename(file_name, file_name.translate(None, "0123456789"))  # 转换文件名


rename_files()
