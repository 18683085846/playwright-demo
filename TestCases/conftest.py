import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="class")
def page():
    with sync_playwright() as play:
        browser = play.chromium.launch(headless=False, channel="chrome")
        context = browser.new_context()
        # 录制日志
        context.tracing.start(screenshots=True, snapshots=True, sources=True)
        page = context.new_page()
        yield page
        # 保存日志
        context.tracing.stop(path="trace.zip")
        context.close()
        browser.close()


@pytest.fixture(scope="function")
def context():
    with sync_playwright() as play:
        browser = play.chromium.launch(headless=False, channel="chrome")
        context = browser.new_context()
        # 录制日志
        context.tracing.start(screenshots=True, snapshots=True, sources=True)
        yield context
        # 保存日志
        context.tracing.stop(path="trace.zip")
        context.close()
        browser.close()
