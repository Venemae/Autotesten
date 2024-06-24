import pytest
from playwright.sync_api import Page, Playwright, expect
from configparser import ConfigParser
import re

def run(playwright):
    browser = playwright.chromium.launch(headless=False)  # Set to True for headless mode
    context = browser.new_context()
    page = context.new_page()

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

    page.get_by_label("Knop gebruikers menu").click()
    page.get_by_role("link", name="Mijn verzekering").dblclick()
    page.get_by_role("tab", name="Uw zorgpolis").click()
    page.get_by_role("link", name="Gegevens wijzigen").click()
    page.locator("dl").filter(has_text="NaamS.").get_by_role("link").click()
    page.get_by_role("button", name="Binnenlands postadres").click()
    page.get_by_role("link", name=" naar: Mijn gegevens").click()
    page.locator("dl").filter(has_text="Rekeningnummer voor").get_by_role("link").click()
    page.get_by_role("link", name=" naar: Mijn gegevens").click()
    page.locator("dd").filter(has_text="output.webtesten@menzis.").get_by_role("link").click()
    page.get_by_role("link", name=" naar: Mijn gegevens").click()
    page.locator("dd").filter(has_text="0591915001Wijzigen").get_by_role("link").click()
    page.get_by_label("Telefoonnummer 1").click()
    page.get_by_label("Telefoonnummer 1").fill("0612345677")
    page.get_by_label("Telefoonnummer 2").click()
    page.get_by_label("Telefoonnummer 2").fill("0501547892")
    page.get_by_role("button", name="Wijzigen").click()
    page.get_by_role("link", name="Terug naar Mijn gegevens").click()
    page.locator("dl").filter(has_text="Rekeningnummer voor").get_by_role("link").click()
    page.get_by_role("link", name=" naar: Mijn gegevens").click()

    
