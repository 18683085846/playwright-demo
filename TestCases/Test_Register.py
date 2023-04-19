# -*- coding:utf-8 -*- 
"""
describe：注册用例
Author：tang
Email：tangllyx@163.com
Time: 2023/4/20 
"""
import time
import allure, os
import pytest
from Pages.LoginPage.LoginPage import LoginPage
from Pages.RegisterPage.RegisterPage import RegisterPage
from Pages.MyAccountPage.MyAccountPage import MyAccountPage
from Utils.ReadYaml import ReadYaml
from Common.AllurePretty import PrettyAllure
from Config.Config import Config


class TestRegister:

    @pytest.mark.run(order=0)
    @PrettyAllure.PrettyAllureWarpper
    @pytest.mark.parametrize("CaseData", ReadYaml(os.path.join(Config.test_datas_dir, "TestRegisterData.yaml")).read())
    def test_register(self, page, CaseData: dict):
        rp = RegisterPage(page)
        rp.goto_register(url=CaseData["url地址"])
        rp.type_username(username=CaseData["用户名"])
        rp.type_verify_code(CaseData["验证码"])
        rp.type_password(CaseData["密码"])
        rp.type_password2(CaseData["确认密码"])
        rp.click_checktxt()
        rp.click_btn_agree()
        MyAccountPage(page).logout_to_be_visible(CaseData["断言元素定位"])
        rp.click_ele(CaseData["断言元素定位"])
