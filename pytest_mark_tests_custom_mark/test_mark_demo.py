# 开发者：苏慧
# _*_ coding=utf-8 _*_
# @Time：2026/5/3 18:35
# @Author: suhui
# @FileName: test_mark_demo.py
# @Project: pytest_demo


import pytest


@pytest.mark.smoke
@pytest.mark.api
def test_user_login():
    assert True


@pytest.mark.api
def test_user_profile():
    assert True
