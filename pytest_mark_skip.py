# 开发者：苏慧
# _*_ coding=utf-8 _*_
# @Time：2026/5/3 17:49
# @Author: suhui
# @FileName: pytest_mark_skip.py
# @Project: pytest_demo


import pytest


@pytest.mark.skip(reason="该用例尚未实现")
def test_unimplemented():
    pass


import sys


@pytest.mark.skipif(sys.version_info < (3, 8), reason="python版本低于3.8，不支持该特性")
def test_python38_feature():
    pass


def test_runtime_skip():  # 测试函数内部根据动态条件控制用例的执行
    maintenance_mode = True
    if maintenance_mode:
        pytest.skip("系统维护模式，跳过该测试用例")
    assert True
