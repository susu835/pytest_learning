# 开发者：苏慧
# _*_ coding=utf-8 _*_
# @Time：2026/4/29 0:47
# @Author: suhui
# @FileName: pytest_mark_param_multi.py
# @Project: pytest_demo

import pytest

@pytest.mark.parametrize("a,b,expected",[(1,2,3),(0,0,0),(-1,1,0)])
def test_addition(a,b,expected):
    print(f"测试加法：{a}+{b}={expected}")
    assert a+b==expected


#带ids的
# def idfn(val):
#     if isinstance(val,tuple):
#         return f"{val[0]}+{val[1]}={val[2]}"
#     return str(val)
#
# @pytest.mark.parametrize("a,b,expected",[(1,2,3),(0,0,0),(-1,1,0)],ids=idfn)
# def test_addition(a,b,expected):
#     print(f"测试加法：{a}+{b}={expected}")
#     assert a+b==expected
