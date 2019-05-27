import allure
import pytest


class TestApp:
    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    @allure.step(title="这是一个测试步骤01")
    def test_app(self):
        allure.attach("标题", "具体内容")
        assert True

    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    @allure.step(title="这是一个测试步骤02")
    def test_app_1(self):
        allure.attach("标题2", "具体内容2")
        assert True