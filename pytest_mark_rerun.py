# 开发者：苏慧
# _*_ coding=utf-8 _*_
# @Time：2026/5/3 18:00
# @Author: suhui
# @FileName: pytest_mark_rerun.py
# @Project: pytest_demo


'''
不稳定的测试用例，适用pytest-rerunfailures插件实现失败重跑
--reruns 3 --reruns-delay 2
--rerun-except requests.exception.ConnectionError
--reruns-max 3

'''

import requests

def test_api_flaky():
    response = requests.get("https://flaky-api.example.com")
    assert response.status_code == 200
