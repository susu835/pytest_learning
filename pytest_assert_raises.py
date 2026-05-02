# 开发者：苏慧
# _*_ coding=utf-8 _*_
# @Time：2026/5/3 0:37
# @Author: suhui
# @FileName: pytest_assert_raises.py
# @Project: pytest_demo

import pytest


def test_invalid_input():
    with pytest.raises(ValueError, match=r"invalid literal for int\(\) with base 10: 'abc'"):
        int("abc")
