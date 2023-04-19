# -*- coding:utf-8 -*- 
"""
describe：我的账号页面
Author：tang
Email：tangllyx@163.com
Time: 2023/4/17 
Software: PyCharm
"""
import allure

from BasePage.BasePage import BasePage

class MyAccountPage(BasePage):
    # 定位器
    __logout = 'a[title = "退出"]'

    @allure.step("断言安全退出可见")
    def logout_to_be_visible(self,locator):
        return self._ele_to_be_visible(locator)


