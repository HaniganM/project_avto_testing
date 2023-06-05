import pytest
from selenium import webdriver

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options


def pytest_addoption(parser):
    parser.addoption('--name_browser', action='store', default=None,
                     help="Choose browser") # for select browser
    parser.addoption('--language', action='store', default=None,
                     help="Choose user language: ru/en/de or other")# for select language

@pytest.fixture(scope="function")
def browser(request):
    name_browser = request.config.getoption("name_browser")
    language = request.config.getoption("language")
    browser = None
    if name_browser == "chrome":
        print("\nstart chrome browser for test..")
        options = webdriver.ChromeOptions()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
    elif name_browser == "firefox":
        print("\nstart firefox browser for test..")
        options = Options()
        options.set_preference("intl.accept_languages", language)
        browser = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()