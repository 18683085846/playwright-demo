from playwright.sync_api import expect, Page


class BasePage:

    def __init__(self, page: Page):
        self.page = page

    def _goto_url(self, url):
        self.page.goto(url)

    def _click(self, locator, frame_locator=None):
        try:
            if frame_locator is not None:
                self.page.frame_locator(frame_locator).locator(locator).click()
            else:
                self.page.click(locator)
        except Exception as e:
            print(e)

    def _fill(self, locator, value, frame_locator=None):
        try:
            if frame_locator is not None:
                self.page.frame_locator(selector=frame_locator).locator(selector_or_locator=locator).fill(value)
            else:
                self.page.fill(selector=locator, value=value)
        except Exception as e:
            print(e)

    def _ele_to_be_visible(self, locator):
        return expect(self.page.locator(locator)).to_be_visible()

    def _browser_operation(self, reload=False, forward=False, back=False):
        if reload:
            self.page.reload()
        if back:
            self.page.go_back()
        if forward:
            self.page.go_forward()

    def screenshot(self, path, full_page=True, locator=None):
        if locator is not None:
            self.page.locator(locator).screenshot(path=path)
            return path
        self.page.screenshot(path=path, full_page=full_page)
        return path
