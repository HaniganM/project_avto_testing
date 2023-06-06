import time

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES
from .locators import BasePageLocators
from .locators import BacketPageLocators


import math
class BasePage():
#  Первым делом добавим конструктор — метод, который вызывается, когда мы создаем объект.
# Конструктор объявляется ключевым словом __init__. В него в качестве параметров мы передаем экземпляр драйвера и url адрес.
# Внутри конструктора сохраняем эти данные как аттрибуты нашего класса.
    def __init__(self, browser, url, timeout = 10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)# добовляем неявное ожидание

    def go_to_basket_page(self):
        basket_link = self.browser.find_element(*BacketPageLocators.BASKET_LINK)
        basket_link.click()

    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK) # * - значит что передали кортеж и его нужно распспаковать
        login_link.click()


    # Теперь добавим еще один метод open. Он должен открывать нужную страницу в браузере, используя метод get().
    def open(self):
        self.browser.get(self.url)

    # реализуем метод is_element_present, в котором будем перехватывать исключение.
    # В него будем передавать два аргумента: как искать (css, id, xpath и тд) и собственно что искать (строку-селектор).
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True


    # явное ожидание елемента, упадет как только увидет искомый элемент, если не появился, тест будет зеленый
    def is_not_element_present(self, how, what, timeout = 4):
        try:
            WebDriverWait(self.browser, timeout).until(ES.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    # явное ожидание , будет ждать до тех пор пока элемент не исчезнет
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(ES.presence_of_element_located((how,what)))
        except TimeoutException:
            return False
        return True

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link ist not presenten"


    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        time.sleep(5)
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")




