# 开发者：苏慧
# _*_ coding=utf-8 _*_
# @Time：2026/4/29 21:55
# @Author: suhui
# @FileName: pytest_mark_param_indirect.py
# @Project: pytest_demo


import pytest

@pytest.fixture
def user(request):
    user_type = request.param
    if user_type == "admin":
        return  {"username":"admin","role":"admin"}
    elif user_type == "user":
        return {"username":"user","role":"user"}
    else:
        return {"username":"guest","role":"guest"}

@pytest.mark.parametrize("user",["admin","user","guest"],indirect=True) #间接参数化，参数值传递给同名的user fixture
def test_user_info(user):
    print(f"当前用户信息：{user}")
    assert user["username"] is not None

