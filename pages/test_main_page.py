import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.main_page import MainPage
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
import pytest

@pytest.mark.login_guest
class TestLoginFromMainPage():
    
    def test_guest_can_go_to_login_page(self,browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
        page.open()                    # открываем страницу
        page.go_to_login_page()# выполняем метод страницы — переходим на страницу логина
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()
        time.sleep(3)
       
    def test_guest_should_see_login_link(self,browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()
        time.sleep(3)

def test_guest_cant_see_product_in_basket_opened_from_main_page(self,browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasketPage(browser, link)
    page.open()
    page.open_basket()
    page.message_that_there_is_no_item_in_the_cart()
    page.message_that_the_cart_is_empty()
    time.sleep(3)


#pytest --browser_name=chrome --language=en test_main_page.py
#pytest -v --tb=line --language=en test_main_page.py
#pytest -m login_guest --tb=line --language=en test_main_page.py


