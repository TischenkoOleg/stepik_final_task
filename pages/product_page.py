from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators

class ProductPage(BasePage):
    
    def add_product_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        button.click()
    def should_be_url(self):
        #реализуйте проверку на корректный url адрес
        assert ProductPageLocators.PAGE_URL == self.url, \
            f"URL is incorrect: {self.url}"

    def should_be_correct_name(self):
        #  Название товара в сообщении должно совпадать с тем товаром, который вы действительно добавили.
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        book_basket_name = self.browser.find_element(*ProductPageLocators.BOOK_BASKET_NAME).text
        assert book_name == book_basket_name, \
            f"The book name is not correct: '{book_basket_name}' instead of '{book_name}'"

    def should_be_correct_price(self):
        # Стоимость корзины совпадает с ценой товара.
        price = self.browser.find_element(*ProductPageLocators.PRICE).text
        basket_price = self.browser.find_element(*ProductPageLocators.PRICE_BASKET).text
        assert price == basket_price, \
            f"The price is not correct: '{price}' instead of '{basket_price}'"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
            # Проверяем, что нет сообщения об успехе
        
    def message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
        #Проверяем, что нет сообщения об успехе с помощью is_disappeared
