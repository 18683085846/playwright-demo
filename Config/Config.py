# -*- coding:utf-8 -*- 
"""
describe：配置文件
Author：tang
Email：tallyx@163.com
Time: 2023/4/17 
Software: PyCharm
"""
import os


class Config:
    # 项目地址
    url = "http://124.223.40.245:83"

    # 项目根目录
    root_dir = os.path.split(os.path.split(__file__)[0])[0]
    test_cases_dir = root_dir + os.path.sep + "TestCases"
    test_files_dir = root_dir + os.path.sep + "TestFiles"
    test_report_dir = root_dir + os.path.sep + "TestReport" + os.path.sep + "AllureReport"
    test_result_dir = root_dir + os.path.sep + "TestReport" + os.path.sep + "AllureResult"
    test_screenshot_dir = root_dir + os.path.sep + "TestReport" + os.path.sep + "Screenshot"

if __name__ == '__main__':
    print(Config.root_dir)
    print(Config.test_cases_dir)
