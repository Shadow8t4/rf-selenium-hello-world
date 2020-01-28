from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import ui, expected_conditions
import time


def python_selenium_test(browser='chrome'):
    print('Hello, world!')

    if(browser.lower() == 'chrome'):
        browser = webdriver.Chrome()
    elif(browser.lower() == 'firefox'):
        browser = webdriver.Firefox()
    wait = ui.WebDriverWait(browser, 5)

    browser.get('https://www.phptravels.net/admin')

    wait.until(expected_conditions.visibility_of_element_located(
        (By.CSS_SELECTOR, '.input-outlined > input[name="email"]')))
    browser.find_element_by_css_selector(
        'label.input-outlined:nth-child(2) > span').click()
    browser.find_element_by_css_selector(
        '.input-outlined > input[name="email"]').send_keys('admin@phptravels.com')

    wait.until(expected_conditions.visibility_of_element_located(
        (By.CSS_SELECTOR, '.input-outlined > input[name="password"]')))
    browser.find_element_by_css_selector(
        'label.input-outlined:nth-child(3) > span').click()
    browser.find_element_by_css_selector(
        '.input-outlined > input[name="password"]').send_keys('demoadmin')

    browser.find_element_by_css_selector('button[type=submit]').click()

    wait.until(
        lambda browser: browser.find_element_by_id('logout'))

    time.sleep(5)
    browser.quit()


if(__name__ == '__main__'):
    python_selenium_test()
