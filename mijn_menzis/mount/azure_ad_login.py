from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=False)  # Set to True for headless mode
    context = browser.new_context()
    page = context.new_page()

    # Navigate to the application that uses Azure AD for authentication
    page.goto('https://your-application-url.com')

    # Wait for the Azure AD login page to load
    page.wait_for_selector('input[name="loginfmt"]')

    # Enter the Azure AD username (email)
    page.fill('input[name="loginfmt"]', 'your-email@domain.com')
    page.click('input[type="submit"]')

    # Wait for the password input to appear and enter the password
    page.wait_for_selector('input[name="passwd"]')
    page.fill('input[name="passwd"]', 'your-password')
    page.click('input[type="submit"]')

    # If MFA is enabled, handle it here (e.g., wait for MFA input and fill it)
    # This example assumes MFA is not required or is handled outside the script

    # Handle 'Stay signed in?' prompt if it appears
    stay_signed_in_selector = 'input[id="idBtn_Back"]'
    if page.is_visible(stay_signed_in_selector):
        page.click(stay_signed_in_selector)

    # Wait for navigation to the application after login
    page.wait_for_navigation()

    # Now you can proceed with further actions in your application
    # For example, navigating to different programs on-premises
    page.goto('https://your-application-url.com/program1')
    # Add assertions or further steps as needed
    # page.goto('https://your-application-url.com/program2')
    # page.goto('https://your-application-url.com/program3')

    # Close the browser
    browser.close()

with sync_playwright() as playwright:
    run(playwright)