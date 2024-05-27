import pytest
from playwright.sync_api import Page, Playwright
from configparser import ConfigParser
import re
from playwright.sync_api import Page, expect

# Load configuration file
file = 'config.ini'
config = ConfigParser()
config.read(file)

@pytest.mark.parametrize("page_url", [config['Inloggen']['url']])
def test_inloggen_menzis(page: Page, page_url: str):
    page.goto(page_url)
    page.locator('button:has-text("Accepteren")').click()
    page.locator('#navigationUserToggleButton').dblclick() 

    # Wacht tot Loginstub zichtbaar is en klik
    loginstub_button = page.locator('button:has-text("Loginstub")').first
    loginstub_button.wait_for(state='visible')
    loginstub_button.click()

    page.locator('input[placeholder="BSN"]').fill(config['Inloggen']['bsn'])
    page.get_by_role("button", name="Verzekerdennummer").dblclick()

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

    page.goto(page_url)
    
