import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("chrome://newtab/")
    page.goto("chrome-error://chromewebdata/")
    page.goto("http://intranetapplications.test.otap.loods2.org/TransactionService.Pres.Internal/Default.aspx")
    page.get_by_role("link", name="Transacties").click()
    page.frame_locator("iframe[name=\"frContent\"]").get_by_role("link", name="Status").click()
    page.frame_locator("iframe[name=\"frContent\"]").frame_locator("iframe[name=\"frStatus\"]").get_by_text("wacht op autorisatie").click()
    page.frame_locator("iframe[name=\"frContent\"]").frame_locator("iframe[name=\"frStatus\"]").locator("#ddlTransactieType_dropDownList").select_option("4131")
    page.frame_locator("iframe[name=\"frContent\"]").frame_locator("iframe[name=\"frStatus\"]").get_by_role("button", name="ZOEKEN").click()
    page.frame_locator("iframe[name=\"frContent\"]").frame_locator("iframe[name=\"frStatus\"]").get_by_role("cell", name="verzekeringnemer").nth(2).click()
    page.frame_locator("iframe[name=\"frContent\"]").frame_locator("iframe[name=\"frStatus\"]").get_by_role("cell", name="-5-2024 08:36:38").first.click()
