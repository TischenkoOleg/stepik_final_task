import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
link = "http://selenium1py.pythonanywhere.com/"
def test_guest_can_go_to_login_page(browser):
    browser.get(link)
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()
    time.sleep(10)
