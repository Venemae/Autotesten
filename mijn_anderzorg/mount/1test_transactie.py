
from playwright.sync_api import sync_playwright
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

def test1(playwright):
    options = {
        'args': [
            '--disable-gpu',
            '--disable-dev-shm-usage',
            '--disable-setuid-sandbox',
            '--no-first-run',
            '--no-sandbox',
            '--no-zygote',
            '--ignore-certificate-errors',
            '--disable-extensions',
            '--disable-infobars',
            '--disable-notifications',
            '--disable-popup-blocking',
            '--remote-debugging-port=9222'
        ],
        'headless': False 
    }

    browser = playwright.chromium.launch(**options)  
    # page = browser.new_page(ignore_https_errors=True)
    page = browser.new_page()

    # Navigate to your target URL
    page.goto(config['Transactie']['url'])
    page.get_by_role("link", name="Transacties").click()
    page.frame_locator("iframe[name=\"frContent\"]").get_by_role("link", name="VerzekerdeOverzicht").click()
    page.frame_locator("iframe[name=\"frContent\"]").frame_locator("iframe[name=\"frVerzekerde\"]").locator("#tbxVerzekerdennummer").click()
    page.frame_locator("iframe[name=\"frContent\"]").frame_locator("iframe[name=\"frVerzekerde\"]").locator("#tbxVerzekerdennummer").fill("296367573")
    page.frame_locator("iframe[name=\"frContent\"]").frame_locator("iframe[name=\"frVerzekerde\"]").get_by_role("button", name="ZOEKEN").click()
    page.frame_locator("iframe[name=\"frContent\"]").frame_locator("iframe[name=\"frVerzekerde\"]").get_by_role("link", name="transacties").click()
from playwright.sync_api import sync_playwright

def click_second_column_with_text(page, target_text):
    # Locate all rows in the table
    rows = page.locator('table tr')
    
    for row in rows:
        # Check if the row contains the target text
        if target_text in row.text().strip():
            # Locate all columns in the current row
            columns = row.locator('td')
            
            # Check if there are at least two columns
            if len(columns) >= 2:
                # Click on the second column
                columns[1].click()
                return True  # Click successful
            
            # If less than two columns, handle the error or continue
            else:
                print("Row found but less than two columns.")
                return False
    
    # If no row with the target text is found
    print(f"Row with text '{target_text}' not found.")
    return False

if __name__ == '__main__':
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        
        # Replace with your actual URL
        page.goto(config['Transactie']['url'])
        
        # Replace 'wacht op autorisatie' with your target text
        target_text = 'wacht op autorisatie'
        
        try:
            if click_second_column_with_text(page, target_text):
                print(f"Clicked on the second column of the row with text '{target_text}'.")
            else:
                print(f"Failed to click on the second column of the row with text '{target_text}'.")
        except Exception as e:
            print(f"Error occurred: {str(e)}")
        finally:
            browser.close()

    page.frame_locator("iframe[name=\"frContent\"]").frame_locator("iframe[name=\"frBRelatie\"]").get_by_role("button", name="Toe-eigenen").click()
    page.frame_locator("iframe[name=\"frContent\"]").frame_locator("iframe[name=\"frBRelatie\"]").get_by_role("button", name="Afkeuren").click()

    
if __name__ == '__main__':
    with sync_playwright() as playwright:
        run(playwright)
