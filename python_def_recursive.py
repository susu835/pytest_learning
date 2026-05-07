# _*_ coding=utf-8 _*_
"""
@Project: pytest_demo
@FileName: python_def_recursive.py
@Time：2026/5/3 23:50
@Author: suhui
@Describe: ...
"""

import os


def show_file_tree(path,filecount = 0):
    if os.path.isdir(path):
        listdir = [os.path.join(path, i) for i in os.listdir(path)]
        for i in listdir:
            if os.path.isdir(i):
                _path = os.path.join(path, i)
                filecount = show_file_tree(_path,filecount)
            else:
                # print(i)
                filecount += 1
    return filecount


# def show_file_tree(path,filecount = 0):
#     if os.path.isdir(path):
#         for i in os.listdir(path):
#             _path = os.path.join(path,i)
#             if os.path.isdir(_path):
#                 filecount = show_file_tree(_path,filecount)
#             else:
#                 print(path)
#                 filecount += 1
#     return filecount

li=show_file_tree("E:\ss\mashang\课堂笔记")
print(li)







