from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
import pytest



@pytest.mark.login_guest
class TestLoginFromMainPage():
    # фикстура для api
    # -----------------
    #@pytest.fixture(scope="function", autouse=True)
    #def setup(self):
    #   self.product = ProductFactory(title="Best book created by robot")
    #    # создаем по апи
    #    self.link = self.product.link
    #    yield
    #    # после этого ключевого слова начинается teardown
    #    # выполнится после каждого теста в классе
    #    # удаляем те данные, которые мы создали
    #    self.product.delete()
    # --------------------
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)# инициализируем Page Object, передаем в конструктор экземпляр драйвера и УРЛ адресса
        page.open() # открываем страницу
        page.go_to_login_page() # переходим на страницу логина
        page.should_be_login_link()
        page_login = LoginPage(browser, link)
        page_login.should_be_login_form()
        page_login.should_be_register_form()
        page_login.should_be_login_url()

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser,link)
    page.open()
    page.go_to_basket_page()
    page_basket = BasketPage(browser, link)
    page_basket.should_be_basket_page()
    page_basket.should_be_what_product_is_not_basket()
    page_basket.should_be_what_basket_is_empty()


