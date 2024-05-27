from playwright.sync_api import sync_playwright, Page, expect

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto('https://menzis.testsc.otap.menzis.nl/')
    page.locator('button:has-text("Accepteren")').click()
    page.locator('#navigationUserToggleButton').dblclick() 

    # Wacht tot Loginstub zichtbaar is en klik
    loginstub_button = page.locator('button:has-text("Loginstub")').first
    loginstub_button.wait_for(state='visible')
    loginstub_button.click()

    page.locator('input[placeholder="BSN"]').fill('5672498545')
    page.get_by_role("button", name="Verzekerdennummer").dblclick()

    # Emailadres controleren anders door naar Mijn omgeving
    email_element = page.locator("#Emailadres_Value")
    if email_element.is_visible():
        print("emailadres controle")
        page.get_by_label("E-mailadres", exact=True).click()
        page.get_by_label("E-mailadres", exact=True).fill("output.webtesten@menzis.nl")
        page.get_by_label("E-mailadres", exact=True).press("Tab")
        page.get_by_label("Herhaal e-mailadres").fill("output.webtesten@menzis.nl")
        page.get_by_role("button", name="Wijzigen").click()
        page.goto('https://menzis.testsc.otap.menzis.nl/')
    else:
        print("geen emailadres controle")

    page.goto('https://menzis.testsc.otap.menzis.nl/')

    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)