# 开发者：苏慧
# _*_ coding=utf-8 _*_
# @Time：2026/5/3 0:51
# @Author: suhui
# @FileName: conftest.py
# @Project: pytest_demo


from test_footcompare import User

def pytest_assertrepr_compare(op, left, right):
    if isinstance(left, User) and isinstance(right, User) and op == "==":
        return [
            "User instance comparation:",
            f"Left User id: {left.id}",
            f"Right User id: {right.id}",
            "reason: User IDs are not equal"
        ]
    return  None