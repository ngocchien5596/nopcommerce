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
    droplist_newsLetter_xpath = "//input[contains(@aria-labelledby, 'SelectedNewsletterSubscriptionStoreIds_label')]"
    droplist_newsLetter_id = "//div[contains(@class, 'input-group-append')]//select[contains(@id, 'SelectedNewsletterSubscriptionStoreIds')]"

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
    customerRole = "Vendors"
    comment = faker.sentence()


    # TC09: Check UI of Add New Customer Page
    def test_TC09(self, setup):
        self.driver = setup

        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        time.sleep(2)

        self.lp = LoginPage(self.driver)

        self.an = AddNewCustomerPage(self.driver)

        self.lp.loginSuccess(self.username, self.password)

        time.sleep(3)

        # Go to Add New Customer page
        self.an.getToAddNewCustomerURL()

        # Input all customer info fields

        self.an.setEmail(self.email1)
        print("Email is ", self.email1)

        self.an.setPassword(self.pw1)
        print("Password is ", self.pw1)

        self.an.setFirstName(self.firstName)
        print("First Name is ", self.firstName)

        self.an.setLastName(self.lastName)
        print("Last name is ", self.lastName)

        self.an.setGender(self.gender)
        print("Gender is ", self.gender)

        self.an.setBirthday(self.birthday)
        print("Birthday is ", self.birthday)

        self.an.setCompanyName(self.company)
        print("Company name is ", self.company)

        self.an.setTax(self.isTax)
        print("Tax is ", self.isTax)

        self.an.setNewsLetter(self.newsLetter)
        print("Newsletter is ", self.newsLetter)

        self.an.setCustomerRole(self.customerRole)
        print("Customer role is ", self.customerRole)

        self.an.setManagerOfVendor(self.vendor)
        print("Vendor is ", self.vendor)

        self.an.setComment(self.comment)
        print("Comment is ", self.comment)

        self.driver.save_screenshot("./Screenshots/"+"testAddNewCustomer.png")

        self.an.clickSave()
        time.sleep(2)

        self.driver.close()




