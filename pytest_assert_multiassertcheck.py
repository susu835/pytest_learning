# 开发者：苏慧
# _*_ coding=utf-8 _*_
# @Time：2026/5/3 1:25
# @Author: suhui
# @FileName: pytest_assert_multiassertcheck.py
# @Project: pytest_demo


from pytest_check import check
def test_multi_assertions():
    user = {"name":"张5三", "age": 16, "email": "zhangsan@example.com"}
    check.equal(user["name"],"张三","用户名验证失败")
    check.greater(user["age"],18,"年龄必须大于18")
    check.is_true("@" in user["email"],"邮件格式验证失败")