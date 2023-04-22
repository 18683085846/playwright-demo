# -*- coding:utf-8 -*- 
"""
describe：我的账户>个人中心>个人信息
Author：tang
Email：tangllyx@163.com
Time: 2023/4/22 
"""
import allure

from BasePage.BasePage import BasePage


class PersonalInformationPage(BasePage):
    # 元素定位器
    __profile_photo = "#preview"  # 头像
    __upload_pictures_iframe = '//iframe[contains(@id,"layui-layer-iframe")]'  # 上传头像的iframe框
    __webuploader_pick = '#filePicker input'  # 点击选择图片
    __upload_succeed = '.filelist > li >p.title'  # 上传成功
    __confirm_btn = 'div[class="saveBtn"]'  # 确定使用的按钮
    __confirm_save_btn = 'input[value="确认保存"]'  # 确认保存按钮
    __successfully = '//span[text()="操作成功"]'  # 操作成功

    @allure.step("去往个人信息页面")
    def goto_personal_information(self, url):
        self._goto_url(url)

    @allure.step("点击修改头像")
    def click_profile_photo(self):
        self._click(self.__profile_photo)

    @allure.step("上传头像文件")
    def webuploader_pick(self, files):
        self._file(locator=self.__webuploader_pick,
                   files=files,
                   frame_locator=self.__upload_pictures_iframe)

    @allure.step("等待上传成功")
    def upload_succeed(self):
        self._ele_to_be_visible_force(self.__upload_succeed,self.__upload_pictures_iframe)

    @allure.step("点击确定使用按钮")
    def click_confirm_btn(self):
        self._click(
            locator=self.__confirm_btn,
            frame_locator=self.__upload_pictures_iframe
        )

    @allure.step("点击保存按钮")
    def click_confirm_save_btn(self):
        self._click(
            locator=self.__confirm_save_btn,
        )

    @allure.step("断言操作成功可见")
    def except_successfully(self, locator):
        self._ele_to_be_visible(
            locator=locator
        )
