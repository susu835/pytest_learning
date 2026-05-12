# 开发者：苏慧
# _*_ coding=utf-8 _*_
# @Time：2026/5/3 17:03
# @Author: suhui
# @FileName: test_cases.py
# @Project: pytest_demo
import pytest

# pytestmark = pytest.mark.skip('本文件的测试用例跳过')
pytest.skip('跳过本文件中的测试用例',allow_module_level=True)

def test_api_demo(base_url):
    print(f"当前环境的域名：{base_url}")
    url = f"{base_url}/api/login"
    print(f"请求地址：{url}")
