import re
from sys import path
from urllib import response
from playwright.sync_api import Page, expect
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    page = browser.new_page()
# def test_example(page: Page) -> None:
    page.goto("https://www1.acc.menzis.nl/")
    page.get_by_role("button", name="Accepteren").click()
    page.get_by_label("Knop gebruikers menu").click()
    page.get_by_role("button", name="Loginstub").click()
    page.get_by_role("button", name="Advanced").click()
    page.get_by_role("link", name="Proceed to stub-menzis-acc.").click()
    page.get_by_placeholder("BSN").click()
    page.get_by_placeholder("BSN").click()
    page.get_by_placeholder("BSN").dblclick()
    page.get_by_placeholder("BSN").fill("959857561")
    page.goto("https://www1.acc.menzis.nl/mijn/gegevens/emailadres-controleren?url=/")
    page.get_by_label("E-mailadres", exact=True).click()
    page.get_by_label("E-mailadres", exact=True).fill("output.webtesten@menzis.nl")
    page.get_by_label("E-mailadres", exact=True).click()
    page.get_by_label("Herhaal e-mailadres").click()
    page.get_by_label("Herhaal e-mailadres").fill("output.webtesten@menzis.nl")
    page.goto("https://www1.acc.menzis.nl/")
