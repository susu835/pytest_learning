# 开发者：苏慧
# _*_ coding=utf-8 _*_
# @Time：2026/5/3 0:45
# @Author: suhui
# @FileName: test_footcompare.py
# @Project: pytest_demo


class User:
    def __init__(self, id):
        self.id = id


def test_compare_users():
    user1 = User(1)
    user2 = User(2)
    assert user1 == user2
