import re
from playwright.sync_api import Page, expect
from playwright.sync_api import sync_playwright


def test_example(page: Page) -> None:
    with sync_playwright() as p:
#             # Launch the browser
#             browser = p.firefox.launch(headless=False)
    # page.frame_locator("iframe[title=\"SP Consent Message\"]").get_by_label("Akkoord").click()
        page.goto("https://intranetapplications.test.otap.loods2.org/TransactionService.Pres.Internal/Default.aspx")
    # page.goto("chrome-error://chromewebdata/")
    page.get_by_role("button", name="Advanced").click()
    page.get_by_role("link", name="Proceed to").click()
    page.goto("https://intranetapplications.test.otap.loods2.org/TransactionService.Pres.Internal/Default.aspx")
    page.get_by_role("link", name="Transacties").click()



# from playwright.sync_api import sync_playwright

# def click_first_cell_link():
#     try:
#         with sync_playwright() as p:
#             # Launch the browser
#             browser = p.firefox.launch(headless=False)
#             # Open a new page
#             page = browser.new_page()
#             # Navigate to the URL
#             page.goto("https://intranetapplications.test.otap.loods2.org/TransactionService.Pres.Internal/Default.aspx")

#             # Wait for the table to be visible (adjust selector as needed)
#             page.wait_for_selector('table#ucBerichtOverzicht_gvResultaten')

#             # Sort by the 'Nummer' column if necessary
#             print("Clicking the 'Nummer' column to sort")
#             page.click('a[href="javascript:__doPostBack(\'ucBerichtOverzicht$gvResultaten\',\'Sort$Nummer\')"]')
            
#             # Wait for sorting to complete if necessary (you might need to wait for some network activity or specific element)
#             page.wait_for_load_state('networkidle')  # or another appropriate wait

#             # Find and click the link in the first cell of the 'Nummer' column
#             first_cell_link = page.query_selector('table#ucBerichtOverzicht_gvResultaten > tbody > tr:nth-child(1) > td:nth-child(1) > a')
#             if first_cell_link:
#                 print("Clicking the first cell link")
#                 first_cell_link.click()
#             else:
#                 print("First cell link not found")
            
#             # Keep the browser open
#             page.wait_for_timeout(5000)  # Wait for a while to see the result
#             browser.close()
#     except Exception as e:
#         print(f"An error occurred: {e}")

# click_first_cell_link()
