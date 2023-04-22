# -*- coding:utf-8 -*-
"""
describe：登录页面
Author：tang
Email：tangllyx@163.com
Time: 2023/4/17
Software: PyCharm
"""
import allure
from BasePage.BasePage import BasePage


class LoginPage(BasePage):
    # 元素定位器
    __username = "#username"
    __password = "#password"
    __verify_code = "#verify_code"
    __login_button = 'a[name="sbtbutton"]'
    __button_logout = 'a[title="退出"]'

    def del_auth(self):
        self._del_auth()

    @allure.step("打开登录页面")
    def goto_login(self, url):
        self._goto_url(url)

    @allure.step("输入账号")
    def fill_username(self, value):
        self._fill(self.__username, value)

    @allure.step("输入密码")
    def fill_password(self, value):
        self._fill(self.__password, value)

    @allure.step("输入验证码")
    def fill_verify_code(self, value):
        self._fill(self.__verify_code, value)

    @allure.step("点击登录按钮")
    def click_login_button(self):
        self._click(self.__login_button)

    @allure.step("点击安全退出按钮")
    def click_button_logout(self):
        self._click(self.__button_logout)

    def browser_operation(self, reload=True, forward=False, back=False):
        self._browser_operation(reload=reload, forward=forward, back=back)
