# _*_ coding=utf-8 _*_
"""
@Project: pytest_demo
@FileName: conftest.py
@Time：2026/5/9 2:42
@Author: suhui
@Describe: ...
"""


import pytest


def pytest_addoption(parser):
    parser.addoption('--env', help='运行环境：test/dev')
    # parser.addoption('--env', default='test', help='运行环境：test/dev')


@pytest.fixture(scope='session')
def base_url(request):
    cmd_env = request.config.getoption('--env')
    print(cmd_env)
    env = request.config.getini('default_env')
    print(env)
    # env = request.config.getoption('--env')
    # if cmd_env:
    # if env == 'test':
    #     # env = cmd_env
    #     base_url = 'https://api.test.com'
    # elif env == 'dev':
    #     base_url = 'https://api.dev.com'
    # else:
    #     print(f'{env}不存在')
    # return base_url