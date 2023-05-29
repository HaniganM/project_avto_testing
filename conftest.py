import pytest
from selenium import webdriver

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose user language: ru/en/de or other")# for select language

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    browser = None
    print("\nstart chrome browser for test..")
    options = webdriver.ChromeOptions() # для проверяющего options=Options() не работает
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()