from pages.main_page import MainPage
from pages.login_page import LoginPage
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)# инициализируем Page Object, передаем в конструктор экземпляр драйвера и УРЛ адресса
    page.open() # открываем страницу
    page.go_to_login_page() # переходим на страницу логина
    page.should_be_login_link()
    page_login = LoginPage(browser, link)
    page_login.should_be_login_form()
    page_login.should_be_register_form()
    page_login.should_be_login_url()

