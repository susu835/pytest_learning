# 开发者：苏慧
# _*_ coding=utf-8 _*_
# @Time：2026/5/3 17:36
# @Author: suhui
# @FileName: conftest.py
# @Project: pytest_demo


import pytest

def pytest_addoption(parser):
    parser.addoption("--run-slow", action = "store_true", default = False, help = "运行标记为slow的测试用例")

def pytest_configure(config):
    config.addinivalue_line("markers","slow:标记慢速测试用例")

def pytest_collection_modifyitems(config,items):
    """
    :describe
     pytest 内置的钩子函数（hook），注册自定义命令行参数 --run-slow
     pytest 在收集完所有测试用例之后、执行测试之前自动调用这个函数。
    :param
     --config：来自 pytest 运行时的全局配置对象（命令行参数、配置文件、标记等）
     --items：来自 pytest 收集到的所有测试用例列表
    """
    if not config.getoption("--run-slow"):
        skip_slow = pytest.mark.skip(reason="需加 --run-slow 才执行")
        for item in items:
            if "slow" in item.keywords:
                item.add_marker(skip_slow)
