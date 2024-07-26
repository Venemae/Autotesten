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
    
    page.get_by_label("Knop gebruikers menu").click()
    page.click('a[href="/gegevens"]')
        
    page.click('a[href="/gegevens/telefoonnummer-wijzigen"]')
    
    #telefoonnummer wijzigen value +1
    selector = 'input[data-fieldname="MobielTelefoonnummer"]'
    page.wait_for_selector(selector)
    current_value = page.query_selector(selector).get_attribute('value')
    numeric_part = ''.join(filter(str.isdigit, current_value))
        
    if numeric_part:
        new_numeric_value = numeric_part[:-1] + str(int(numeric_part[-1]) + 1)
            
        new_value = f"{new_numeric_value[:3]}-{new_numeric_value[3:]}"
            
        page.fill(selector, new_value)
        print(f"Filled the input field with incremented value: {new_value}")
    else:
        print("The current value is not a valid phone number format.")
                
    page.get_by_role("button", name="Wijzigen").click()