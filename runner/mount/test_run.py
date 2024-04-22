import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://myprivacy.dpgmedia.nl/consent?siteKey=ucf98legs1caotgh&callbackUrl=https%3A%2F%2Fwww.nu.nl%2Fprivacy-gate%2Faccept%3FredirectUri%3D%252F")
    page.frame_locator("iframe[title=\"SP Consent Message\"]").get_by_label("Akkoord").click()
    page.get_by_label("sluit venster").click()
    page.get_by_role("link", name="Astronomen zijn erachter").first.click()
    page.get_by_label("Hoofdnavigatie").get_by_label("Sport").click()
    page.get_by_role("link", name="Barcelona-trainer Xavi").first.click()
    with page.expect_popup() as page1_info:
        page.get_by_alt_text("Barcelona-trainer Xavi").click()
    page1 = page1_info.value
