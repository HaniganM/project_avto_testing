from .base_page import BasePage
from .locators import BacketPageLocators

class ProductPage(BasePage):
    def go_to_backet_page(self):
        self.add_product()
        self.should_be_correct_name_product()
        self.should_be_correct_price_product()

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

