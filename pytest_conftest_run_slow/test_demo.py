# _*_ coding=utf-8 _*_
"""
@Project: pytest_demo
@FileName: python_exe_seq.py
@Time：2026/5/9 23:17
@Author: suhui
@Describe:
 给用例打上慢速用例标记：@pytest.mark.slow
 pytest可单独控制跑不跑  pytest-m slow   pytest -m 'not slow'
"""


import pytest

def test_normal_case():
    assert True


@pytest.mark.slow
def test_slow_case():
    import time
    time.sleep(2)
    assert True

