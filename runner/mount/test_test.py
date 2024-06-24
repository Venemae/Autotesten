import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_example():
    # Initialize the WebDriver (assuming Chrome, but you can use any browser)
    driver = webdriver.Chrome()

    try:
        # Navigate to the initial URL
        driver.get("https://www2.tst.menzis.nl/")
        
        # Accept cookies
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Accepteren']"))).click()
        
        # Open the user menu
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LABEL, "Knop gebruikers menu"))).click()
        
        # Click the Loginstub button
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Loginstub' and @exact='true']"))).click()
        
        # Enter BSN
        bsn_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='BSN']")))
        bsn_field.click()
        bsn_field.send_keys("4056694174")
        
        # Navigate to the email address check page
        driver.get("https://www2.tst.menzis.nl/mijn/gegevens/emailadres-controleren?url=/")
        
        # # Fill in the email address
        # email_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LABEL, "E-mailadres", exact=True)))
        # email_field.click()
        # email_field.send_keys("output.webtesten@menzis.nl")
        # email_field.send_keys(Keys.TAB)
        
        # Repeat the email address
        repeat_email_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LABEL, "Herhaal e-mailadres")))
        repeat_email_field.click()
        repeat_email_field.send_keys("output.webtesten@menzis.nl")
        
        # Navigate to the various pages
        driver.get("https://www2.tst.menzis.nl/")
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LABEL, "Knop gebruikers menu"))).click()
        driver.get("https://www2.tst.menzis.nl/mijn/geldzaken")
        driver.get("https://www2.tst.menzis.nl/mijn/geldzaken/rekeningen/rekening-details")
        driver.get("https://www2.tst.menzis.nl/mijn/geldzaken/betalingsregelingen/betalingsregeling-aanvragen")
        
        # Click on change payment details
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Betaalgegevens wijzigen"))).click()
        
        # Open the user menu and logout
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LABEL, "Knop gebruikers menu"))).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Uitloggen"))).click()
    
    finally:
        # Close the browser
        driver.quit()