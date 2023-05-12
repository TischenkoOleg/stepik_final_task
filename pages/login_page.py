from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By
import pytest

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert LoginPageLocators.PAGE_URL in self.url, \
            f"URL is incorrect: {self.url}"
    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "login form is not presented" 

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "register form is not presented" 

    def register_new_user(self, email, password):
        #assert self.gmail.is_element_present(*LoginPageLocators.USER_GMAIL), "user gmail is not presented"
        #assert self.password.is_element_present(*LoginPageLocators.USER_PASSWORD), "user password is not presented"
        #assert self.password.is_element_present(*LoginPageLocators.CONFIRM_PASSWORD), "confirm password is not presented"
        #assert self.is_element_present(*LoginPageLocators.REGISTER_BUTTON), "register button is not presented"
  
        self.browser.find_element(*LoginPageLocators.USER_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.USER_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()


        
        




        
