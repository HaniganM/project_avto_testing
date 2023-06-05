import time
from pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page_basket = ProductPage(browser, link)
    page_basket.open()
    time.sleep(5)
    page_basket.add_product()
    page_basket.solve_quiz_and_get_code()
    time.sleep(5)
    page_basket.should_be_correct_name_product()
    page_basket.should_be_correct_price_product()
