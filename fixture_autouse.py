# 开发者：苏慧
# _*_ coding=utf-8 _*_
# @Time：2026/4/27 23:12
# @Author: suhui
# @FileName: fixture_autouse.py
# @Project: pytest_demo
import time

import pytest


@pytest.fixture(autouse=True)
def record_test_time():
    start_time = time.time()
    print(f"\n用例开始执行时间{start_time}")
    yield
    end_time =time.time()
    print(f"用例执行结束时间{end_time}")
    print(f"执行用例耗时{start_time-end_time:.2f}秒")


def test_case_1():
    print("\n执行test_case_1")

def test_case_2():
    print("\n执行test_case_2")