###执行脚本
1.main方法
- (1)~~很少用，很少用~~
- (2)pytest.main(['-v','-s'])

2.pytest工具

###用例管理和运行管理
1.执行顺序
- 一个测试模块，先测试函数后测试类
- 同类型有多个，则按行号
```
python_exe_seq.py::test_A PASSED                                         [ 16%]
python_exe_seq.py::TestA::test_class_A PASSED                            [ 33%]
python_exe_seq.py::TestA::test_class_AA PASSED                           [ 50%]
python_exe_seq.py::TestB::test_class_B PASSED                            [ 66%]
python_exe_seq.py::TestB::test_class_BB PASSED                           [ 83%]
python_exe_seq.py::test_B PASSED                                         [100%]
```
2.断言管理

(1)assert断言

`assert 条件,"断言失败提示信息"`
```
示例
assert isintance(age,int),"年龄类型是整数"
assert 0<age<20,'年龄范围不对'
assert res == 200,'接口响应结果不对'
assert len(data)>0,'列表不能为空
assert 'name' in dict,'字段不存在'
assert sys.version_info_major,'版本/环境不对'
assert False:'兜底逻辑，逻辑错误'
```
（2）指定异常断言
```
with pytest.raise(异常类型) as e:
   要执行的代码
```
3.运行管理

`pytest [参数操作] [文件或者文件夹]`
- pytest -m
- pytest -x 遇到失败停止
- pytest -v verbose详细信息
- pytest -s show stdout,print、日志输出到控制台
- pytest -rA reportAll 执行结束后打印一个简短的总结报告
- pytest -k '关键字'
- pytest -m '标记符号'
- pytest --pyargs package_name  有时候测试的用例不在常用的文件夹，可以通过指定包来执行包内可收集到的测试用例

4.运行的失败管理
- pytest -x  第一个失败就停止
- pytest --maxfail=2 第二个失败就停止
- pytest --lf last fail 只执行上一轮失败的用例
- pytest --lf --collect-only 只收集不执行

pytest-rerunfailures 插件：自动重试加重跑，很稳
-pytest -reruns = 1 失败重跑1次

@pytest.mark.skip 跳过某些测试用例
@pytest.mark.skipif 满足条件就跳过用例

pytestmark = pytest.mark.skip('本文件的测试用例跳过')  跳过模块文件
pytest.skip('跳过本文件中的测试用例',allow_module_level=True)  跳过模块文件

@pytest.mark.xfail  执行显示用例标记为xfailed预期失败(已知的bug不希望被识别为failed)
预期失败执行却通过会标记xpass，说明断言有误或者功能有问题
预期失败用例只标记不执行，则加参数run=False

### fixture功能
1.依赖注入
```
@pytest.fixture
def login():
    print('登录成功')

def test_query(login):
    print('查询成功')
```
2.应用在初始化设置
>数据初始化  连接初始化等
```
@pytest.fixture
def data():
    print('读取数据scv成功并有return返回')

def test_login(data):
    print('查询到登录的账号登录成功')
```
3.应用在配置销毁
- yield代替return
```
@pytest.fixture(scope='moudule')
def open():
    print('打开浏览器')
    yield
    print('关闭浏览器')

def test_login(open):
    pass
def test_query(open):
    pass
```
- addfinalizer 

yield执行过程中出错无法执行yield之后的函数

addfinalizer执行过程中即使出错也会执行后面的函数,*特殊场景才会用4%*

4.不同层级scope
- 会话session级别使用fixture和conftest.py配合
    - 跨模块则需要在.py之上，因此采用单独的conftest.py文件。pytest会自动识别该文件
  ```
   conftest.py
   @pytest.fixture
   def login():
      print("公用模块")
  
   test_fixture.py
   def test_car(login):
      pass
   def test_bike(login):
      pass
  ```
   执行过程找不到login，会自动去本目录下的conftest.py中查找

5.自动调用fixture 
- autouse=True
```
@pytest.fixture(autouse=True)
def open():
    print("打开浏览器")

def test_A():
    pass
    
def test_B():
    pass    
```
- @pytest.mark.usefixtures
`@pytest.mark.usefixtures('open')`

6.不同层级上重写fixture
- 文件夹层级重写fixture
```
|-tests
|--conftest.py  username方法+fixture
|--test_A.py    test_username方法使用fixture并验证
|--subfolder
|---conftest.py  重写username方法+fixture
|---test_A.py   test_username方法使用fixture并验证重写成功
```

- 模块层级重写fixture
```
|-tests
|--conftest.py  username方法+fixture
|--test_A.py    username方法+fixture重写
```

- 用例参数中重写fixture 冷门不看
### pytest数据驱动和参数传递
1.参数化应用
```
@pytest.mark.parametrize('argnames',[argvalues,..])

@pytest.mark.parametrize('name',['zhang','li','wang'])
@pytest.mark.parametrize('name,age',[('zhang',12),('li',13)])
```

2.参数值结合csv
```
def csv

```


