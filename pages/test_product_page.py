from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.product_page import ProductPage
from pages.base_page import BasePage
import pytest

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019"  
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    product_page = ProductPage(browser, browser.current_url)
    product_page.should_be_url()
    page.should_be_correct_name()
    page.should_be_correct_price()
    #page.guest_can_add_product_to_basket()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    #Открываем страницу товара
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    #Добавляем товар в корзину
    page.add_product_to_basket()
    #Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    #Открываем страницу товара
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    #Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    page.should_not_be_success_message()
    
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    #Открываем страницу товара
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    #Добавляем товар в корзину
    page.add_product_to_basket()
    #Проверяем, что нет сообщения об успехе с помощью is_disappeared
    page.message_disappeared()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_link()
    
#@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=offer0",
#                                  "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=offer1",
#                                  "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=offer2",
#                                  "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=offer3",
#                                  "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=offer4",
#                                  "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=offer5",
#                                  "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=offer6",
#                                   pytest.param("http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=offer7",marks=pytest.mark.xfail),
#                                  "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=offer8",
#                                  "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=offer9"])
#@pytest.mark.parametrize('link', [0, 1, 2, 3, 4, 5, 6, pytest.param(7, marks=pytest.mark.xfail), 8, 9])
#def test_guest_can_add_product_to_basket(browser, link):
#    link = f"http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=offer{link}"
#    page = ProductPage(browser, link)
#    page.open()
#    page.add_product_to_basket()        
#    page.solve_quiz_and_get_code()
#    page.should_be_correct_name()                           
#    page.should_be_correct_price()


#pytest -s -v --browser_name=chrome --language=en test_product_page.py
    
#pytest -s -v --browser_name=chrome --language=en -m parametrize test_product_page.py
