# import re
# from playwright.sync_api import Page, expect

# #pakket aanpassen
# def test_example(page: Page) -> None:
#     page.get_by_role("button", name="Accepteren").click()
#     page.get_by_label("Knop gebruikers menu").click()
#     page.get_by_role("button", name="Loginstub", exact=True).click()
#     page.get_by_placeholder("BSN").click()
#     page.get_by_placeholder("BSN").fill("7683476495")
#     page.goto("https://menzis.testsc.otap.menzis.nl/mijn/gegevens/emailadres-controleren?url=/")
#     page.get_by_label("E-mailadres", exact=True).click()
#     page.get_by_label("E-mailadres", exact=True).fill("output.webtesten@menzis.nl")
#     page.get_by_label("E-mailadres", exact=True).press("Tab")
#     page.get_by_label("Herhaal e-mailadres").fill("output.webtesten@menzis.nl")
#     page.get_by_role("button", name="Wijzigen").click()
#     page.get_by_label("Knop gebruikers menu").click()
#     page.get_by_role("link", name="Mijn verzekering").click()
#     page.goto("https://menzis.testsc.otap.menzis.nl/mijn/verzekering/pakket-wijzigen")
#     page.locator("#PakketWijzigenLijst_0__Aanvullendeverzekering_Value").select_option("MEV1")
#     page.get_by_role("button", name="Volgende").click()
#     page.goto("https://menzis.testsc.otap.menzis.nl/mijn/verzekering/pakket-wijzigen?done=1")
#     page.get_by_role("heading", name="Wat kunt u verwachten?").click()
#     page.get_by_role("heading", name="Klaar!").click()

import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://intranetapplications.test.otap.loods2.org/TransactionService.Pres.Internal/Default.aspx")
    page1.get_by_role("link", name="Transacties").click()
    page1.frame_locator("iframe[name=\"frContent\"]").get_by_role("link", name="VerzekerdeOverzicht").click()
    page1.frame_locator("iframe[name=\"frContent\"]").frame_locator("iframe[name=\"frVerzekerde\"]").locator("#tbxVerzekerdennummer").click()
    page1.frame_locator("iframe[name=\"frContent\"]").frame_locator("iframe[name=\"frVerzekerde\"]").locator("#tbxVerzekerdennummer").fill("7683476495")
    page1.frame_locator("iframe[name=\"frContent\"]").frame_locator("iframe[name=\"frVerzekerde\"]").get_by_role("button", name="ZOEKEN").click()
    page1.frame_locator("iframe[name=\"frContent\"]").get_by_role("link", name="Status").click()
    page1.frame_locator("iframe[name=\"frContent\"]").get_by_role("link", name="Relatie").click()
    page1.frame_locator("iframe[name=\"frContent\"]").frame_locator("iframe[name=\"frBRelatie\"]").locator("#ddlZoekwijze").select_option("1")
    page1.frame_locator("iframe[name=\"frContent\"]").frame_locator("iframe[name=\"frBRelatie\"]").locator("#tbxRelatienummer").click()
    page1.frame_locator("iframe[name=\"frContent\"]").frame_locator("iframe[name=\"frBRelatie\"]").locator("#tbxRelatienummer").fill("")
    page1.frame_locator("iframe[name=\"frContent\"]").frame_locator("iframe[name=\"frBRelatie\"]").locator("#tbxRelatienummer").click()
    page1.frame_locator("iframe[name=\"frContent\"]").frame_locator("iframe[name=\"frBRelatie\"]").locator("#tbxRelatienummer").fill("7683476495")
    page1.frame_locator("iframe[name=\"frContent\"]").frame_locator("iframe[name=\"frBRelatie\"]").get_by_role("button", name="ZOEKEN").click()
    page1.frame_locator("iframe[name=\"frContent\"]").get_by_role("link", name="Status").click()
    page1.frame_locator("iframe[name=\"frContent\"]").frame_locator("iframe[name=\"frStatus\"]").get_by_text("wacht op autorisatie").click()
    page1.frame_locator("iframe[name=\"frContent\"]").frame_locator("iframe[name=\"frStatus\"]").get_by_role("button", name="ZOEKEN").click()
