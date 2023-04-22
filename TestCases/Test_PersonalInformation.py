# -*- coding:utf-8 -*- 
"""
describe：
Author：tang
Email：tangllyx@163.com
Time: 2023/4/22 
"""
import os.path

import pytest

from Pages.MyAccountPage.PersonalCenterPage.PersonalInformationPage import PersonalInformationPage
from Common.AllurePretty import PrettyAllure
from Config.Config import Config
from Utils.ReadYaml import ReadYaml


class TestPersonalInformation:

    @pytest.mark.parametrize("CaseData",
                             ReadYaml(os.path.join(Config.test_datas_dir, "TestPersonalInformation.yaml")).read())
    @PrettyAllure.PrettyAllureWarpper
    def test_personalinformation(self, page, CaseData):
        pi = PersonalInformationPage(page)
        pi.goto_personal_information(CaseData["url地址"])
        pi.click_profile_photo()
        pi.webuploader_pick(CaseData["files"])
        pi.upload_succeed()
        pi.click_confirm_btn()
        pi.click_confirm_save_btn()
        pi.except_successfully(CaseData["断言元素定位"])
