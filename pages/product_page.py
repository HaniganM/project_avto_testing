from .base_page import BasePage
from .locators import BacketPageLocators
from .locators import ProductPageLocators
from selenium.webdriver.support.ui import WebDriverWait

class ProductPage(BasePage):
    def go_to_backet_page(self):
        self.add_product()
        self.should_be_correct_name_product()
        self.should_be_correct_price_product()
        self.should_not_be_success_message()
        self.should_disappear_success_message()

    def add_product(self):
        add_to_basket = self.browser.find_element(*BacketPageLocators.ADD_TO_BASKET)
        add_to_basket.click()

    def should_be_correct_name_product(self):
        assert self.is_element_present(*BacketPageLocators.ADD_PRODUCT), "Message: Product is not basket"
        assert self.is_element_present(*BacketPageLocators.NAME_BOOK), "Product is not"
        messege_basket = self.browser.find_element(*BacketPageLocators.ADD_PRODUCT).text
        print(messege_basket)
        name_book = self.browser.find_element(*BacketPageLocators.NAME_BOOK).text
        print(name_book)
        assert name_book == messege_basket, "Name book is not message basket"

    def should_be_correct_price_product(self):
        assert self.is_element_present(*BacketPageLocators.TOTAL_PRICE), "Message price basket"
        assert self.is_element_present(*BacketPageLocators.BOOK_PRICE), "Sale price book"
        price_basket = self.browser.find_element(*BacketPageLocators.TOTAL_PRICE).text
        print(price_basket)
        price_book = self.browser.find_element(*BacketPageLocators.BOOK_PRICE).text
        print(price_book)
        assert price_book == price_basket, "Prices are different"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message should disappear"

