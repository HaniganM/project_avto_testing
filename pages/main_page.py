from selenium.webdriver.common.by import By
from .base_page import BasePage

#Создаем MainPage. Его нужно сделать наследником класса BasePage. Класс-предок в Python указывается в скобках:
#таким образом, класс MainPage будет иметь доступ ко всем атрибутам и методам своего класса-предка.
class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, '#login_link')
        login_link.click()
