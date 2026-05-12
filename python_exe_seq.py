# _*_ coding=utf-8 _*_
"""
@Project: pytest_demo
@FileName: python_exe_seq.py
@Time：2026/5/9 23:17
@Author: suhui
@Describe: ...
"""


def test_A():
    assert 1 == 2


class TestA:
    def test_class_A(self):
        pass

    def test_class_AA(self):
        pass


class TestB:
    def test_class_B(self):
        pass

    def test_class_BB(self):
        pass


def test_B():
    pass
