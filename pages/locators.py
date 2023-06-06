from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')  # создаем пару , ключ- значение(кортеж)
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class MainPageLocators():
    pass

class LoginPageLocators():
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTRATION_FORM = (By.CSS_SELECTOR, '#register_form')
    LOGIN_USERNAME = (By.CSS_SELECTOR, '#id_login-username')
    LOGIN_PASSWORD = (By.CSS_SELECTOR, '#id_login-password')
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password')
    REGISTRATION_PASSWORD2 = (By.CSS_SELECTOR, 'id_registration-password2')

class BacketPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    ADD_PRODUCT = (By.CSS_SELECTOR, ".alertinner strong")
    NAME_BOOK = (By.CSS_SELECTOR, ".product_main h1")
    TOTAL_PRICE = (By.CSS_SELECTOR, "div#messages > .alert.alert-safe.alert-noicon.alert-info.fade.in strong")
    BOOK_PRICE = (By.CSS_SELECTOR, "div.col-sm-6.product_main > p.price_color")
    BASKET_LINK = (By.CSS_SELECTOR, 'span.btn-group .btn.btn-default')
    BASKET_EMPTY = (By.CSS_SELECTOR, '#content_inner > p')
    BASKET_NOT_EMPTY = (By.CSS_SELECTOR, 'h2.col-sm-6 h3')

class ProductPageLocators():
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages .alert:nth-child(1)')
