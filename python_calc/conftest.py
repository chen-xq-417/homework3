from python_calc.calc import Calculator
from python_calc.test_calc import TestCalc, add_data, add_id, div_data, div_id, sub_data, sub_id, mul_data, mul_id
import pytest


@pytest.fixture(scope="module")
def get_calc():
    print("获取计算器实例")
    calc = Calculator()
    return calc


@pytest.fixture(params=add_data, ids=add_id)
def get_datas1(request):
    print("开始计算")
    data = request.param
    print(f"测试数据为： {data}")
    yield data
    print("结束计算")


@pytest.fixture(params=div_data, ids=div_id)
def get_datas2(request):
    print("开始计算")
    data = request.param
    print(f"测试数据为： {data}")
    yield data
    print("结束计算")


@pytest.fixture(params=sub_data, ids=sub_id)
def get_datas3(request):
    print("开始计算")
    data = request.param
    print(f"测试数据为： {data}")
    yield data
    print("结束计算")


@pytest.fixture(params=mul_data, ids=mul_id)
def get_datas4(request):
    print("开始计算")
    data = request.param
    print(f"测试数据为： {data}")
    yield data
    print("结束计算")
