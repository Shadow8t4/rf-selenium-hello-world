from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import ui, expected_conditions
from selenium.webdriver.chrome.options import Options as chromeOptions
from selenium.webdriver.firefox.options import Options as firefoxOptions
import time


def python_selenium_test(browser_var='chrome'):
    print('Hello, world!')
    
    if('headless' in browser_var.lower()):
        if('chrome' in browser_var.lower()):
            chrome_options = chromeOptions()
            chrome_options.add_argument("--headless")
            browser = webdriver.Chrome(chrome_options=chrome_options)
        elif('firefox' in browser_var.lower()):
            firefox_options = firefoxOptions()
            firefox_options.add_argument("--headless")
            browser = webdriver.Firefox(options=firefox_options)
    else:
        if('chrome' in browser_var.lower()):
            browser = webdriver.Chrome()
        elif('firefox' in browser_var.lower()):
            browser = webdriver.Firefox()
    wait = ui.WebDriverWait(browser, 5)

    browser.get('https://the-internet.herokuapp.com/login')

    wait.until(expected_conditions.visibility_of_element_located(
        (By.ID, 'username')))
    browser.find_element_by_id(
        'username').click()
    browser.find_element_by_id(
        'username').send_keys('tomsmith')

    wait.until(expected_conditions.visibility_of_element_located(
        (By.ID, 'password')))
    browser.find_element_by_id(
        'password').click()
    browser.find_element_by_id(
        'password').send_keys('SuperSecretPassword!')

    browser.find_element_by_css_selector('button[type=submit]').click()

    wait.until(
        lambda browser: browser.find_element_by_css_selector('.button > i.icon-signout'))

    time.sleep(5)
    browser.quit()


if(__name__ == '__main__'):
    python_selenium_test()
