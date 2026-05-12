# _*_ coding=utf-8 _*_
"""
@Project: pytest_demo
@FileName: test_max.py
@Time：2026/5/10 1:23
@Author: suhui
@Describe: ...
"""
import pytest


@pytest.mark.xfail(reason='该功能有bug')
def test_max():
    assert 1 == 2

# strict 失败的用例是否显示为failed开关   run 参数是否执行，false不再执行
@pytest.mark.xfail(reason='该功能有bug',strict=True,run=False)
def test_xpass():
    assert 1 == 1

@pytest.fixture
def login():
    print('登录成功')

def test_query(login):
    print('查询成功')


def test_assert_false():
    assert False,"兜底"