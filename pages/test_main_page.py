import time
from pages.main_page import MainPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page.open()                    # открываем страницу
    page.go_to_login_page()        # выполняем метод страницы — переходим на страницу логина
    time.sleep(5)
    
#pytest --browser_name=chrome --language=en test_main_page.py
#pytest -v --tb=line --language=en test_main_page.py