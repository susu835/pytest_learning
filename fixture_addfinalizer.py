# 开发者：苏慧
# _*_ coding=utf-8 _*_
# @Time：2026/4/28 23:22
# @Author: suhui
# @FileName: fixture_addfinalizer.py
# @Project: pytest_demo

'''
直接手动写f.close(),用例中途奔溃，报错，会永远不执行，文件永远关不掉
addfinalizer，全局兜底，无论成功失败报错，都会执行
'''

import pytest


@pytest.fixture
def file_handler(request):
    f = None

    # 清理函数，提前注册后置--以下是后置
    def teardown():
        if f:
            f.close()
        print("临时文件已经关闭")

    # 提前注册后置
    request.addfinalizer(teardown)
    # 下面所有都是前置
    print("开始打开文件")
    f = open("tmp/temp.txt", "w")
    return f


def test_file_write(file_handler):
    file_handler.write("test connect")
    file_handler.flush()  # 数据先写入缓存区，读取操作是读的磁盘上的文案就。不稳定的情况下，缓存还没到磁盘可能读到空串。flush强制刷新缓冲区，数据立刻写入磁盘
    with open("tmp/temp.txt", "r") as f:
        content = f.read()
    assert content == "test connect"
