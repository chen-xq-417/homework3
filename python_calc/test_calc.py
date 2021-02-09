import allure
import pytest
import yaml

from python_calc.calc import Calculator

with open('calc.yaml') as f:
    datas = yaml.safe_load(f)['data']

    add_data = datas['add_data']
    add_id = datas['add_id']

    div_data = datas['div_data']
    div_id = datas['div_id']

    sub_data = datas['sub_data']
    sub_id = datas['sub_id']

    mul_data = datas['mul_data']
    mul_id = datas['mul_id']


@allure.feature('测试计算器')
class TestCalc:

    @allure.story("测试加法")
    @pytest.mark.run(order=1)
    @pytest.mark.add
    def test_add(self, get_calc, get_datas1):
        # 调用 add 方法
        with allure.step("测试用例-数值相加"):
            result = get_calc.add(get_datas1[0], get_datas1[1])
        # 判断如果reult 是浮点型，则保留两位小数
        if isinstance(result, float):
            result = round(result, 2)
        # 得到结果，需要断言判断
        assert result == get_datas1[2]

    @allure.story("测试除法")
    @pytest.mark.run(order=4)
    @pytest.mark.div
    def test_div(self, get_calc, get_datas2):
        # 调用 div 方法
        with allure.step("测试用例-数值相除"):
            result = get_calc.div(get_datas2[0], get_datas2[1])
        if isinstance(result, float):
            result = round(result, 2)
        assert result == get_datas2[2]

    @allure.story("测试减法")
    @pytest.mark.run(order=2)
    @pytest.mark.sub
    def test_sub(self, get_calc, get_datas3):
        # 调用 sub 方法
        with allure.step("测试用例-数值相减"):
            result = get_calc.sub(get_datas3[0], get_datas3[1])
        if isinstance(result, float):
            result = round(result, 2)
        assert result == get_datas3[2]

    @allure.story("测试乘法")
    @pytest.mark.run(order=3)
    @pytest.mark.mul
    def test_mul(self, get_calc, get_datas4):
        with allure.step("测试用例-数值相乘"):
            result = get_calc.mul(get_datas4[0], get_datas4[1])
        if isinstance(result, float):
            result = round(result, 2)
        assert result == get_datas4[2]
