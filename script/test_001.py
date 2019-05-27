import allure
import pytest


class TestApp:
    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    @allure.step(title="这是一个测试步骤01")
    def test_app(self):
        allure.attach("标题", "具体内容")
        assert True