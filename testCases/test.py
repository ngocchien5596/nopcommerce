from pageObjects.LoginPage import LoginPage
from pageObjects.AddNewCustomerPage import AddNewCustomerPage
import pytest
from selenium.webdriver.common.by import By
from ultilities.readPropertises import ReadConfig
import time
from faker import Faker
from selenium.webdriver.support.ui import Select

class Test:
    baseURL = ReadConfig.getURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    expect_login_title = ReadConfig.getExpectLoginPageTitle()
    droplist_newsLetter_xpath = "//div[contains(@class, 'k-multiselect-wrap k-floatwrap')][1]"
    droplist_yourStoreName_xpath = "//li[contains(., 'Your store name')]"

    # Data Test
    faker = Faker()
    email1 = faker.unique.email()
    pw1 = faker.text(8)
    firstName = faker.unique.first_name()
    lastName = faker.unique.last_name()
    gender = "Female"
    birthday = "5/5/1996"
    company = faker.unique.company()
    isTax = "Yes"
    newsLetter = "Your store name"
    vendor = "Vendor 1"
    customerRole = "Administrators"
    comment = faker.sentence()

    def test_01(self, setup):
        self.driver = setup

        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        time.sleep(2)

        self.lp = LoginPage(self.driver)

        self.an = AddNewCustomerPage(self.driver)

        self.lp.loginSuccess(self.username, self.password)

        self.driver.get("https://admin-demo.nopcommerce.com/Admin/Customer/Create")
        time.sleep(3)

        self.driver.find_element(By.XPATH, self.droplist_newsLetter_xpath).click()
        print("Clicked droplist")
        time.sleep(3)

        element = self.driver.find_element(By.XPATH, self.droplist_yourStoreName_xpath)
        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(3)
        print("Selected")
