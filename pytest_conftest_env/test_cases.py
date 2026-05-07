# 开发者：苏慧
# _*_ coding=utf-8 _*_
# @Time：2026/5/3 17:03
# @Author: suhui
# @FileName: test_cases.py
# @Project: pytest_demo


def test_api_demo(base_url):
    print(f"当前环境的域名：{base_url}")
    url = f"{base_url}/api/login"
    print(f"请求地址：{url}")
