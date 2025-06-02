from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest


@pytest.fixture()
def setup(browser):
    print(browser)
    if browser == 'chrome':
        chrome_options = Options()
        chrome_options.binary_location = r'C:\Users\84975\Downloads\chrome-win64\chrome.exe'
        chrome_driver_path = r'C:\Users\84975\Downloads\chromedriver-win64\chromedriver.exe'
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