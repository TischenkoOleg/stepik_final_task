from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import BasePageLocators
class BasketPage(BasePage):

    def message_that_there_is_no_item_in_the_cart(self):
        assert self.is_not_element_present(*BasePageLocators.BASKET_LOCATOR), \
            "Success message is presented, but should not be"
         # Проверяем, что нет товара в корзине
        
    def message_that_the_cart_is_empty(self):
        assert self.is_disappeared(*BasePageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
         #Проверяем, что есть сообщение о том что корзина пуста


