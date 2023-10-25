import os, allure
from time import sleep

import pytest
from TestPage.LoginPage.LoginPage import LoginPage
from common.ReadYaml import ReadYaml
from common.PrettyAllure import PrettyAllure
from common.Config import Config


class TestLogin:

    @pytest.mark.run(order=1)
    @PrettyAllure.PrettyAllureWarpper
    @pytest.mark.parametrize("CaseData", ReadYaml(os.path.join(Config.test_datas_dir, "TestLoginData.yaml")).read())
    def test_login(self, page, CaseData: dict):
        new_page = LoginPage(page)
        #PrettyAllure(page, CaseData).PrettyAllureCase()
        new_page.goto_login(CaseData["url地址"])
        new_page.fill_username(CaseData["账号"])
        new_page.fill_password(CaseData["密码"])
        new_page.click_login_button()
        sleep(1)
        new_page.login_to_be_visible(CaseData["断言元素定位"])


