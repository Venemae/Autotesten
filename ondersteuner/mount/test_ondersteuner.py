# Open Clienten details van verzekerde x

import pytest
import time
from playwright.sync_api import Page, Playwright
from configparser import ConfigParser
import re
from playwright.sync_api import Page, expect

# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False, slow_mo=3000)
#     page = browser.new_page()

# Load configuration file
file = 'config.ini'
config = ConfigParser()
config.read(file)

@pytest.mark.parametrize("page_url", [config['PvO']['url']])
def test_inloggen_PvO(page: Page, page_url: str):
    page.goto(page_url)
    page.locator('button:has-text("Accepteren")').click()
    page.get_by_role("button", name="Ondersteuner Loginstub").click()

#    page.locator('input[placeholder="#Name"]').fill(config['PvO']['relnr'])
    page.locator("#Name").fill(config['PvO']['relnr'])
    page.get_by_role("button", name="Inloggen").click()
    # page.get_by_label("Knop gebruikers menu").click()

    # Emailadres controleren anders door naar Mijn omgeving
    email_element = page.locator("#Emailadres_Value")
    if email_element.is_visible():
        print("emailadres controle")
        page.get_by_label("E-mailadres", exact=True).click()
        page.get_by_label("E-mailadres", exact=True).fill(config['Inloggen']['email'])
        page.get_by_label("E-mailadres", exact=True).press("Tab")
        page.get_by_label("Herhaal e-mailadres").fill(config['Inloggen']['email'])
        page.get_by_role("button", name="Wijzigen").click()
        page.goto(page_url)
    else:
        print("geen emailadres controle")

    page.get_by_role("link", name="Cliënten overzicht").click()
    page.get_by_label("Verzekerdennummer of BSN").click()
    page.get_by_label("Verzekerdennummer of BSN").fill(config['PvO']['verznr1'])
    page.click('#ondersteuner-client-zoeken-button')
    page.click('xpath=//*[@id="summarylist-clienten-form"]/div/ul/li/button')
    page.click('button[name="action:NaarLink"]')
    page.locator('button:has-text("Accepteren")').click()
    page.click('#ONDPORT-STUB-SSO-Ondersteunersportaal-Menzis_consument2020')
        
    time.sleep(10)
