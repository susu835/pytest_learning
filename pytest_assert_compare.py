# 开发者：苏慧
# _*_ coding=utf-8 _*_
# @Time：2026/5/3 0:32
# @Author: suhui
# @FileName: pytest_assert_compare.py
# @Project: pytest_demo

def test_str_compare():
    assert 'test' == 'task'

def test_dict_compare():
    expected = {"code": 0, "msg": "success", "data": {"token": "xxx"}}
    actual = {"code": 0, "msg": "success", "data": {"token": "yyy"}}
    assert actual == expected

def test_list_compare():
    assert [1,2,3] == [1,2,4]
