import time

import allure
import pytest
from Pages.LoginPage.LoginPage import LoginPage
from Pages.MyAccountPage.MyAccountPage import MyAccountPage
from Utils.ReadYaml import ReadYaml
from Common.AllurePretty import PrettyAllure


class TestLogin():

    @pytest.mark.parametrize("CaseData", ReadYaml(r"E:\playwright-demo\TestDatas\TestLoginData.yaml").read())
    def test_login(self, page, CaseData: dict):
        # allure.dynamic.feature(CaseData.get("模块"))
        # allure.dynamic.story(CaseData.get("功能"))
        # allure.dynamic.severity(CaseData.get("优先级"))
        # allure.dynamic.title(f'{CaseData.get("用例编号")}_{CaseData.get("用例标题")}')
        # if CaseData.get("是否执行") != "Y":
        #     pytest.skip("用例指定跳过")

        new_page = LoginPage(page)
        al = PrettyAllure(page, CaseData)
        al.PrettyAllureCase()
        new_page.goto_login(CaseData["url地址"])
        new_page.fill_username(CaseData["账号"])
        new_page.fill_password(CaseData["密码"])
        new_page.fill_verify_code(CaseData["验证码"])
        new_page.click_login_button()
        MyAccountPage(page).logout_to_be_visible(CaseData["断言元素定位"])
        assert 1==2
        al.PrettyAllureScreenShot()
        # path = new_page.screenshot(
        #     path=r'E:\playwright-demo\TestReport\screenshot_path\screenshot%s.png' % (str(int(time.time()))))
        # new_page.browser_operation(reload=True)
        # allure.attach.file(source=path, name="截图", attachment_type=allure.attachment_type.PNG)
