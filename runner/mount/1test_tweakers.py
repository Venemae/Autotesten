import re
import time
# from playwright.sync_api import Page, expect
from playwright.sync_api import sync_playwright
from playwright.sync_api import Page, expect
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=2000)
    page = browser.new_page()
    
def test_example(page: Page) -> None:
    page.goto("https://tweakers.net/")
    page.get_by_role("link", name="Nieuws", exact=True).click()
    page.get_by_role("link", name="Reviews").click()
    page.get_by_role("button", name="Alleen noodzakelijk").click()
    page.get_by_role("link", name="Best Buy Guides").click()
    page.get_by_role("link", name="Pricewatch").click()
    page.get_by_placeholder("Zoek een product").click()
    page.get_by_placeholder("Zoek een product").fill("fanatec")
    page.get_by_placeholder("Zoek een product").press("Enter")
    page.locator("#listingContainer").get_by_text("Fanatec", exact=True).click()
    page.get_by_role("link", name="Meer").click()
    page.locator("#navMenu").get_by_role("link", name="Over Tweakers").click()
    page.get_by_placeholder("Zoek in de site").click()
    page.get_by_placeholder("Zoek in de site").fill("voorwaarden")
    page.get_by_placeholder("Zoek in de site").press("Enter")
    page.get_by_text("be quiet! LGA1700").click()
    page.goto("https://www.google.nl/")
    
    print("test completed")
    
