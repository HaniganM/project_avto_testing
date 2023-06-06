from .base_page import BasePage
from .locators import BacketPageLocators

class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_basket_url()

    def should_be_basket_url(self):
        # реализуйте проверку на корректный url адрес
        assert "basket" in self.browser.current_url, "url is not correct"


    def should_be_what_product_is_not_basket(self):
        assert self.is_not_element_present(*BacketPageLocators.BASKET_NOT_EMPTY), \
            "Basket empty"

    def should_be_what_basket_is_empty(self):
        assert self.is_element_present(*BacketPageLocators.BASKET_EMPTY), \
            "Bascket is not empty"


