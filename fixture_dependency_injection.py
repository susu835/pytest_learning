# 开发者：苏慧
# _*_ coding=utf-8 _*_
# @Time：2026/4/27 22:27
# @Author: suhui
# @FileName: fixture_dependency_injection.py
# @Project: pytest_demo

import pytest


@pytest.fixture
def login():
    # 前置操作：模拟用户登录，获取token
    token = "test_token_123"
    print("\n执行登录操作，获取token")
    yield token
    print("\n执行退出登录操作")


def test_user_profile(login):
    # 通过函数参数接收fixture的返回值
    print(f"当前的用户的token是:{login}")
    assert login == "test_token_123"
