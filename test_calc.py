import pytest
import yaml

from python_code.calc import Calculator

with open('./datas/calc.yaml') as f:
    datas = yaml.safe_load(f)['add']
    add_datas = datas['datas']
    myid = datas['myid']

    # 把 yaml 里的datas_1,和myid_1,分别赋值给divi_datas、divi_myid
    # datas1 = yaml.safe_load(f)['divi']
    divi_datas = datas['datas_1']
    divi_myid = datas['myid_1']


class TestCalc:

    def setup(self):
        self.calc = Calculator()
        print("开始计算")

    def teardown(self):
        print("计算结束")

    # 参数化，ids 是给用例起名字
    # add_datas 是yaml文件中设置的加法使用的数据列表
    # myid 是yaml文件中设置的加法测试用例的名称
    @pytest.mark.parametrize("a, b, expect", add_datas, ids=myid)
    def test_add(self, a, b, expect):
        # 调用 add 方法
        result = self.calc.add(a, b)
        # 判断 result 是浮点数，作出保留2位小数的处理
        if isinstance(result, float):
            result = round(result, 2)
        # 得到结果之后，需要写断言
        assert result == expect

    # 参数化，divi_datas 是yaml文件中设置除法使用的数据列表
    # divi_myid 是yaml文件中设置的除法测试用例名称
    @pytest.mark.parametrize("c, d, expect1", divi_datas, ids=divi_myid)
    def test_div(self, c, d, expect1):
        # 调用 div 方法
        result = self.calc.div(c, d)
        # 判断 result 是浮点数，作出保留2位小数的处理
        if isinstance(result, float):
            result = round(result, 2)
        # 得到结果之后，需要写断言
        assert result == expect1
