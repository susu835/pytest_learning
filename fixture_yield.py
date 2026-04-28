# 开发者：苏慧
# _*_ coding=utf-8 _*_
# @Time：2026/4/28 23:01
# @Author: suhui
# @FileName: fixture_yield.py
# @Project: pytest_demo

import sqlite3

import pytest


@pytest.fixture(scope="module")
def db_connection():
    print("连接sqlite数据库")
    conn = sqlite3.connect(":memory:")  # 创建一个内存数据库连接（数据存在RAM中，速度快但是关闭即销毁）
    yield conn
    conn.close()
    print("数据库连接已关闭")


def test_db_insert(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("CREATE TABLE users (id INT,name TEXT)")
    cursor.execute("INSERT into users values (1,'Alice')")
    db_connection.commit()
    # 验证插入结果
    cursor.execute("SELECT * FROM users where id=1")
    result = cursor.fetchone()
    assert result == (1, 'Alice')
