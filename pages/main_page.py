from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import MainPageLocators
from .locators import BacketPageLocators

#Создаем MainPage. Его нужно сделать наследником класса BasePage. Класс-предок в Python указывается в скобках:
#таким образом, класс MainPage будет иметь доступ ко всем атрибутам и методам своего класса-предка.
class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK) # * - значит что передали кортеж и его нужно распспаковать
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link ist not presenten"



