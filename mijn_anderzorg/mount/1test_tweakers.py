import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://tweakers.net/")
    page.get_by_role("menuitem", name="Smartphones").click()
    page.get_by_role("link", name="Samsung Galaxy A55 5G, 8GB ram, 128GB opslag Donkerblauw", exact=True).click()
    page.locator("#navMenu").get_by_role("link", name="Reviews").click()
    page.get_by_role("link", name="Vergelijk Games Games").click()
    page.get_by_role("link", name="Preview - Stalker 2: Heart of").click()
    page.get_by_role("link", name="Pricewatch").click()
    page.get_by_placeholder("Zoek een product").click()
    page.get_by_placeholder("Zoek een product").fill("fanatec")
    page.get_by_placeholder("Zoek een product").press("Enter")
    page.get_by_role("button", name="Alleen noodzakelijk").click()
    page.locator("#navMenu").get_by_role("link", name="Nieuws").click()
