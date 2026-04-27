# 开发者：苏慧
# _*_ coding=utf-8 _*_
# @Time：2026/4/27 21:17
# @Author: suhui
# @FileName: fixture_scope.py
# @Project: pytest_demo

import pytest


@pytest.fixture(scope="session")
def session_fixture():
    print("\nsession fixture setup")
    yield
    print("\nsession fixture teardown")


@pytest.fixture(scope="module")
def module_fixture():
    print("\nmodule fixture setup")
    yield
    print("\nmodule fixture teardown")


@pytest.fixture(scope="class")
def class_fixture():
    print("\nclass fixture setup")
    yield
    print("\nclass fixture teardown")


@pytest.fixture
def function_fixture():
    print('\nfunction fixture setup')
    yield
    print("\nfunction fixture teardown")


class TestExample:
    def test_case1(self, session_fixture, module_fixture, class_fixture, function_fixture):
        print("\ntest_case1 executed")

    def test_case2(self, session_fixture, module_fixture, class_fixture, function_fixture):
        print("\ntest_case2 executed")
