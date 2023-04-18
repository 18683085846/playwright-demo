import os

import allure
import pytest
from playwright.sync_api import sync_playwright
from Config.Config import Config

pageobject = None


@pytest.fixture(scope="function")
def page():
    global pageobject
    with sync_playwright() as play:
        browser = play.chromium.launch(headless=False, channel="chrome")
        context = browser.new_context()
        # 录制日志
        context.tracing.start(screenshots=True, snapshots=True, sources=True)
        if pageobject is None:
            pageobject = context.new_page()
        yield pageobject
        pageobject = None
        context.tracing.stop(path="trace.zip")
        context.close()
        browser.close()


# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     """
#     获取每个用例状态的钩子函数
#     :param item: 测试用例
#     :param call: 测试步骤
#     :return:
#     """
#     # 获取钩子方法的调用结果
#     out_come = yield
#     rep = out_come.get_result()  # 从钩子方法的调用结果中获取测试报告
#     # rep.when表示测试步骤，仅仅获取用例call 执行结果是失败的情况, 不包含 setup/teardown
#     if rep.when == "call" and rep.failed:
#         mode = "a" if os.path.exists("failures") else "w"
#         with open("failures", mode) as f:
#             # let's also access a fixture for the fun of it
#             if "CaseData" in item.fixturenames:
#                 print(item.funcargs["CaseData"],type(item.funcargs["CaseData"]))
#                 extra = " (%s)" % item.funcargs["CaseData"]
#             else:
#                 extra = ""
#             f.write(rep.nodeid + extra + "\n")
#         # 添加allure报告截图
#         if hasattr(pageobject, "screenshot"):
#             with allure.step('添加失败截图...'):
#                 path = Config.test_screenshot_dir + os.path.sep + item.funcargs["CaseData"].get("用例编号") + "失败截图.png"
#                 file = pageobject.screenshot(path=path)
#                 allure.attach(file, "失败截图",
#                               allure.attachment_type.PNG)
