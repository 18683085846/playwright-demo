import time

import allure, os
import pytest
from Pages.LoginPage.LoginPage import LoginPage
from Pages.MyAccountPage.MyAccountPage import MyAccountPage
from Utils.ReadYaml import ReadYaml
from Common.AllurePretty import PrettyAllure
from Config.Config import Config


class TestLogin():

    @pytest.mark.run(order=0)
    @PrettyAllure.PrettyAllureWarpper
    @pytest.mark.parametrize("CaseData", ReadYaml(os.path.join(Config.test_datas_dir, "TestLoginData.yaml")).read())
    def test_login(self, page, CaseData: dict):
        new_page = LoginPage(page)
        # PrettyAllure(page, CaseData).PrettyAllureCase()
        new_page.goto_login(CaseData["url地址"])
        new_page.fill_username(CaseData["账号"])
        new_page.fill_password(CaseData["密码"])
        new_page.fill_verify_code(CaseData["验证码"])
        new_page.click_login_button()
        MyAccountPage(page).logout_to_be_visible(CaseData["断言元素定位"])
        # PrettyAllure(page, CaseData).PrettyAllureScreenShot()
