import requests
from core.api_uitl import Api
from utils.read_data import base_data
import allure
from api.api import login_query

@allure.feature("登录模块")
class TestLogin:
    @allure.story("登录")
    @allure.title("正常登录")
    def test_login(self):
        result = login_query()
        assert result.success is True