from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest


@pytest.fixture()
def setup(browser):
    print(browser)
    if browser == 'chrome':
        chrome_options = Options()
        chrome_options.binary_location = '/Users/ngocchien/Downloads/chrome-mac-arm64/Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing'
        chrome_driver_path = '/Users/ngocchien/Downloads/chromedriver-mac-arm64/chromedriver'
        service_options = webdriver.ChromeService(executable_path=chrome_driver_path)
        driver = webdriver.Chrome(service=service_options,
                                  options=chrome_options)
        print("\nLaunching Chrome browser")
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")