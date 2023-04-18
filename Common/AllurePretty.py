# -*- coding:utf-8 -*- 
"""
describe：
Author：tang
Email：tallyx@163.com
Time: 2023/4/18 
Software: PyCharm
"""
import os.path
import time
import allure
import pytest
import functools
from Config.Config import Config
from playwright.sync_api import Page


class PrettyAllure(object):

    def __init__(self,page:Page,CaseData):
        self.page = page
        self.CaseData = CaseData

    def PrettyAllureCase(self):
        allure.dynamic.feature(self.CaseData.get("模块"))
        allure.dynamic.story(self.CaseData.get("功能"))
        allure.dynamic.severity(self.CaseData.get("优先级"))
        allure.dynamic.title(f'{self.CaseData.get("用例编号")}_{self.CaseData.get("用例标题")}')
        if self.CaseData.get("是否执行") != "Y":
            allure.dynamic.description("用例指定跳过")
            pytest.skip("用例指定跳过")

    def PrettyAllureScreenShot(self):
        filename = os.path.join(Config.test_screenshot_dir, f"{self.CaseData.get('用例标题')}.png")
        self.page.screenshot(path=filename)
        allure.attach.file(source=filename, name=self.CaseData.get('用例标题'), attachment_type=allure.attachment_type.PNG)

    # def PrettyAllureWarpper(self, func):
    #     """装饰器函数"""
    #     @functools.wraps(func)
    #     def inner(*args, **kwargs):
    #         # 添加用例信息
    #         self.PrettyAllureCase(CaseData=kwargs.get("CaseData"))  # 如何获取case_data?
    #         r = func(*args, **kwargs)  # 运行用例
    #         # 添加截图
    #         self.PrettyAllureScreenShot(CaseData=kwargs.get("CaseData"))
    #         return r
    #     return inner
