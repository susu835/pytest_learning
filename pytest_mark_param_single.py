# 开发者：苏慧
# _*_ coding=utf-8 _*_
# @Time：2026/4/29 0:28
# @Author: suhui
# @FileName: pytest_mark_param_single.py
# @Project: pytest_demo

import pytest


@pytest.mark.parametrize("num", [1, 2, -2, 5])
def test_is_positive(num):
    print(f"测试数字:{num}")
    assert num > 0
