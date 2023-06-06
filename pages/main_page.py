from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import MainPageLocators
from .locators import BacketPageLocators

# Создаем MainPage. Его нужно сделать наследником класса BasePage. Класс-предок в Python указывается в скобках:
# таким образом, класс MainPage будет иметь доступ ко всем атрибутам и методам своего класса-предка.
# перенесли методы в базе_пейдж, сюда поставили заглушку
# Как вы уже знаете, метод __init__ вызывается при создании объекта.
# Конструктор выше с ключевым словом super на самом деле только вызывает конструктор класса предка и передает ему все те аргументы,
# которые мы передали в конструктор MainPage.

class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)



