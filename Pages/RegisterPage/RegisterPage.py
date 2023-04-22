# -*- coding:utf-8 -*- 
"""
describe：注册页面
Author：tang
Email：tangllyx@163.com
Time: 2023/4/20 
"""
import allure

from BasePage.BasePage import BasePage


class RegisterPage(BasePage):
    __username = "#username"
    __verify_code = 'input[placeholder="图像验证码"]'
    __password = "#password"
    __password2 = "#password2"
    __checktxt = "#checktxt"
    __btn_agree = ".regbtn.J_btn_agree"

    def del_auth(self):
        self._del_auth()

    @allure.step("前往注册页面")
    def goto_register(self, url):
        self._goto_url(url)

    @allure.step("输入用户名")
    def type_username(self, username):
        self._type(self.__username, username)

    @allure.step("输入验证码")
    def type_verify_code(self, verify_code):
        self._type(self.__verify_code, verify_code)

    @allure.step("输入密码")
    def type_password(self, password):
        self._type(self.__password, password)

    @allure.step("输入确认密码")
    def type_password2(self, password2):
        self._type(self.__password2, password2)

    @allure.step("勾选同意")
    def click_checktxt(self):
        if not self._ele_is_checked(self.__checktxt):
            self._click(self.__checktxt)

    @allure.step("点击同意注册按钮")
    def click_btn_agree(self, ):
        self._click(self.__btn_agree)

    @allure.step("点击断言元素")
    def click_ele(self,locator):
        self._click(locator)