# _*_ coding=utf-8 _*_
"""
@Project: pytest_demo
@FileName: python_func_decorator.py
@Time：2026/5/7 22:51
@Author: suhui
@Describe: ...
"""



def f_decoratorA(pre):
    def f_decoratorB(func):
        def f(*args,**kwargs):
            print(f"{pre}收到参数{args},{kwargs}")
            res = func(*args,*kwargs)
            print(f"{pre}返回结果{res}")
            return res
        return f
    return f_decoratorB


@f_decoratorA('Debug')
def add(a,b):
    return a+b

# addt = f_decoratorA('Debug')(add)
add(1,3)

