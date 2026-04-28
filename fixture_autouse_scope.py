# 开发者：苏慧
# _*_ coding=utf-8 _*_
# @Time：2026/4/29 0:18
# @Author: suhui
# @FileName: fixture_autouse_scope.py
# @Project: pytest_demo

import pytest


@pytest.fixture(scope="session")
def session_fixture(function_fixture):
    return function_fixture


@pytest.fixture
def function_fixture():
    print("yield前置")
    yield
    print("yield后置")


def test_case1(session_fixture):
    print("test_case1")


def test_case2(session_fixture):
    print("test_case2")
