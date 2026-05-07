# 开发者：苏慧
# _*_ coding=utf-8 _*_
# @Time：2026/5/3 17:36
# @Author: suhui
# @FileName: conftest.py
# @Project: pytest_demo


import pytest

def pytest_addoption(parser):
    parser.addoption("--run-slow", action = "store_true", default = False, help = "运行标记为slow的测试用例")

# def pytest_configure(config):
#     config.addinivalue_line("markers","slow:标记慢速测试用例")

def pytest_collection_modifyitems(config,items):
    if not config.getoption("--run-slow"):
        skip_slow = pytest.mark.skip(reason="需加 --run-slow 才执行")
        for item in items:
            if "slow" in item.keywords:
                item.add_marker(skip_slow)
