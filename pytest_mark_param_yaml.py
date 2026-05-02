# 开发者：苏慧
# _*_ coding=utf-8 _*_
# @Time：2026/5/3 0:13
# @Author: suhui
# @FileName: pytest_mark_param_yaml.py
# @Project: pytest_demo

import pytest
import yaml


def get_test_data():
    with open("tmp/test_data.yaml","r") as f:
        return yaml.safe_load(f)

@pytest.mark.parametrize("case",get_test_data())
def test_api_request(case):
    url = case ["url"]
    method = case ["method"]
    params = case ["params"]
    expected = case ["expected"]
    print(f"测试接口：{url},请求方法：{method}")
    assert True


