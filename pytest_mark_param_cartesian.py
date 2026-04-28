# 开发者：苏慧
# _*_ coding=utf-8 _*_
# @Time：2026/4/29 0:51
# @Author: suhui
# @FileName: pytest_mark_param_cartesian.py
# @Project: pytest_demo


import pytest

@pytest.mark.parametrize("user_role",["admin","user"])
@pytest.mark.parametrize("permission",["read","write"])
def test_permission_comb(user_role,permission):
    print(f"测试组合：用户角色{user_role},权限{permission}")
    if user_role == "admin":
        assert True # 管理员拥有所有权限
    else:
        assert permission == "read" # 普通用户拥有读的权限

