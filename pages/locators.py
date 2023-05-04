from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    #LOGIN_LINK = (By.CSS_SELECTOR, "i.icon-signin")

class LoginPageLocators():
    PAGE_URL = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/" #this link works for --language=en
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    
class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PAGE_URL = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019"
    BOOK_NAME = (By.TAG_NAME, "h1")
    BOOK_BASKET_NAME = (By.CLASS_NAME, "alert.alert-safe.alert-noicon.alert-success.fade.in .alertinner  strong")
    PRICE = (By.CLASS_NAME, "col-sm-6.product_main .price_color")
    PRICE_BASKET = (By.CLASS_NAME, "alert.alert-safe.alert-noicon.alert-info.fade.in .alertinner  strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
