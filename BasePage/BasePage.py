# -*- coding:utf-8 -*-
"""
describe：
Author：tang
Email：tangllyx@163.com
Time: 2023/4/18
"""

from playwright.sync_api import expect, Page
from BuildInLibrary.BuildInLibrary import BuildInLibrary


class BasePage:

    def __init__(self, page: Page):
        self.page = page

    def _goto_url(self, url):
        """打开网页"""
        self.page.goto(url)

    def _click(self, locator, frame_locator=None):
        """
        点击元素
        :param locator: 传入元素定位器
        :param frame_locator: 传入frame框架的的定位器，如果没有传入，则一般点击
        :return:
        """
        try:
            if frame_locator is not None:
                self.page.frame_locator(frame_locator).locator(locator).click()
            else:
                self.page.click(locator)
        except Exception as e:
            print(e)

    def _fill(self, locator, value, frame_locator=None):
        """
        定位元素，输入内容
        :param locator:传入元素定位器
        :param value:传入输入的值
        :param frame_locator: 传入frame框架
        :return:
        """
        value = BuildInLibrary().repalce_parameter(value)
        try:
            if frame_locator is not None:
                self.page.frame_locator(selector=frame_locator).locator(selector_or_locator=locator).fill(value)
            else:
                self.page.fill(selector=locator, value=value)
        except Exception as e:
            print(e)

    def _ele_to_be_visible(self, locator):
        """断言元素可见"""
        return expect(self.page.locator(locator)).to_be_visible()

    def _browser_operation(self, reload=False, forward=False, back=False):
        """浏览器操作，reload 刷新，forward 前进，back 后退"""
        if reload:
            self.page.reload()
        if back:
            self.page.go_back()
        if forward:
            self.page.go_forward()

    def screenshot(self, path, full_page=True, locator=None):
        """截图功能，默认截取全屏，如果传入定位器表示截取元素"""
        if locator is not None:
            self.page.locator(locator).screenshot(path=path)
            return path
        self.page.screenshot(path=path, full_page=full_page)
        return path
