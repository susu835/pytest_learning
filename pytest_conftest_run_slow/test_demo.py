# 开发者：苏慧
# _*_ coding=utf-8 _*_
# @Time：2026/5/3 17:42
# @Author: suhui
# @FileName: test_demo.py
# @Project: pytest_demo


import pytest

def test_normal_case():
    assert True


@pytest.mark.slow
def test_slow_case():
    import time
    time.sleep(2)
    assert True