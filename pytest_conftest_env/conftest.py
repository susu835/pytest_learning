# 开发者：苏慧
# _*_ coding=utf-8 _*_
# @Time：2026/5/3 13:22
# @Author: suhui
# @FileName: conftest.py
# @Project: pytest_demo

'''实现测试环境隔离'''
import sqlite3

import pytest


@pytest.fixture(scope="session")
def db_connection():
    conn = sqlite3.connect("test.db")
    yield conn
    conn.close()


def pytest_addoption(parser):  # 固定内置钩子函数，注册pytest自定义命令行参数
    parser.addoption("--env", action="store", default="test", help="测试环境:dev/test/prod")


@pytest.fixture(scope="session")
def env(request):
    return request.config.getoption("--env")


@pytest.fixture(scope="session")
def base_url(env):
    if env == "dev":
        return "https://dev.example.com"
    elif env == "test":
        return "https://test.example.com"
    elif env == "prod":
        return "https://prod.example.com"
    else:
        raise ValueError(f"不支持的测试环境：{env}")
