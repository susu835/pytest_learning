# 开发者：苏慧
# _*_ coding=utf-8 _*_
# @Time：2026/4/29 0:47
# @Author: suhui
# @FileName: pytest_mark_param_multi.py
# @Project: pytest_demo

import pytest

#带ids的
def idfn(val):
    # if isinstance(val, tuple):
    return f"{val[0]}+{val[1]}={val[2]}"
    # return str(val)

#只定义一个参数就不解包
@pytest.mark.parametrize("item",[(1,2,3),(0,0,0),(-1,1,0)],ids=idfn)
#定义多个参数会解包拆分，ids会依次接受单个字段而不是整行
# @pytest.mark.parametrize("a, b, expected",[(1,2,3),(0,0,0),(-1,1,0)],ids=idfn)
def test_addition(item):
    a, b, expected =item # 函数内部手动解包
    print(f"测试加法：{a}+{b}={expected}")
    assert a+b==expected
