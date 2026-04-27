# 开发者：苏慧
# _*_ coding=utf-8 _*_
# @Time：2026/4/27 23:01
# @Author: suhui
# @FileName: fixture_param.py
# @Project: pytest_demo

import pytest


@pytest.fixture(params=["admin", "user", "guest"])
def user_role(request):
    # request.param是pytest提供的内置对象，用于获取当前参数值
    return request.param


def test_api_access(user_role):
    print(f"测试用户角色：{user_role}")
    # 模拟不同角色的接口访问逻辑
    if user_role == "admin":
        assert True  # 管理员可以访问所有接口
    elif user_role == "user":
        assert True  # 普通用户可以访问部分接口
    else:
        assert True  # 游客仅可以访问公开接口
