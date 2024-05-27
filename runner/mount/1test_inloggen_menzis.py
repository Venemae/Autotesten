#Inloggen Menzis

from lib2to3.pgen2 import driver
import re
from playwright.sync_api import Page, expect
import asyncio
from playwright.sync_api import sync_playwright


def test_example(page: Page) -> None:
    page.goto("https://menzis.testsc.otap.menzis.nl/")
    page.get_by_role("button", name="Accepteren").click()
    page.get_by_label("Knop gebruikers menu").click()
    page.get_by_role("button", name="Loginstub", exact=True).click()
    page.get_by_placeholder("BSN").dblclick()
    page.get_by_placeholder("BSN").fill("3639159106")
    page.get_by_role("button", name="Verzekerdennummer").dblclick()
    
    # emailcontrole standaard meenemen
    page.goto("https://menzis.testsc.otap.menzis.nl/mijn/gegevens/emailadres-controleren?url=/")
    page.get_by_label("E-mailadres", exact=True).click()
    page.get_by_label("E-mailadres", exact=True).fill("output.webtesten@menzis.nl")
    page.get_by_label("E-mailadres", exact=True).press("Tab")
    page.get_by_label("Herhaal e-mailadres").fill("output.webtesten@menzis.nl")
    page.get_by_role("button", name="Wijzigen").click()
    page.get_by_label("Knop gebruikers menu").click()
    page.goto("https://menzis.testsc.otap.menzis.nl/mijn/geldzaken")
    page.get_by_role("link", name="Laat alle declaraties zien").dblclick()
    page.locator("#content").get_by_role("link", name="Uitloggen").dblclick()
    
    print('test completed')