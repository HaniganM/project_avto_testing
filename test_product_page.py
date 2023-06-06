import time
from pages.product_page import ProductPage
from pages.login_page import LoginPage


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

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    page_login = LoginPage(browser, link)
    page_login.should_be_login_url()



