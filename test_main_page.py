import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
link = "http://selenium1py.pythonanywhere.com/"
def test_guest_can_go_to_login_page(browser):
    browser.get(link)
    go_to_login_page(browser)


def go_to_login_page(browser):
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()
    time.sleep(5)
    
#pytest --browser_name=chrome --language=en test_main_page.py
