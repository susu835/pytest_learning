# 开发者：苏慧
# _*_ coding=utf-8 _*_
# @Time：2026/5/3 18:35
# @Author: suhui
# @FileName: test_mark_demo.py
# @Project: pytest_demo
import sys

import pytest


@pytest.mark.smoke
@pytest.mark.api
def test_user_login():
    assert True


@pytest.mark.api
def test_user_profile():
    assert True

@pytest.mark.skip('暂时跳过不执行')
def test_skip():
    pass

@pytest.mark.skipif(sys.platform=='win32',reason='windows不执行跳过')
def test_skipif():
    pass