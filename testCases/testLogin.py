from pageObjects.LoginPage import LoginPage
import pytest
from selenium.webdriver.common.by import By
from ultilities.readPropertises import ReadConfig
import time

#UI Check
class Test:
    baseURL = ReadConfig.getURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    expect_login_title = ReadConfig.getExpectLoginPageTitle()
    actualLoginTitle_xpath = "//div[contains(@class, 'page-title')]"
    input_email_xpath = "//input[contains(@id, 'Email')]"
    input_password_xpath = "//input[contains(@id, 'Password')]"
    button_login_xpath = "//button[contains(., 'Log in')]"
    checkbox_rememberme_xpath = "//input[contains(@id, 'RememberMe')]"
    nullInput = ""
    invalidValue = "abc"
    label_error1_xpath = "//span[contains(@id, 'Email-error') and contains(., 'Please enter your email')]"
    label_error2_xpath = "//li[contains(., 'The credentials provided are incorrect')]"
    label_error3_xpath = "//span[contains(@id, 'Email-error') and contains(., 'Wrong email')]"
    label_logout_xpath = "//a[contains(@class, 'nav-link') and contains(., 'Logout')]"



# Test scripts
    # TC01: Check Page Title
    def test_TC01(self,setup):
        print("TC01: Check Page Title")
        self.driver = setup

        self.driver.get(self.baseURL)

        act_login_title = self.driver.find_element(By.XPATH, self.actualLoginTitle_xpath).text
        print("act", act_login_title)
        print("exp", self.expect_login_title)

        if act_login_title == self.expect_login_title:
            print("The Page title is as expected")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot("./Screenshots/"+"checkLoginPageTitle.png")
            self.driver.close()
            assert False

    # TC02: Check Elements
    def test_checkElements(self, setup):
        print("TC02: Check Elements")
        self.driver = setup

        self.driver.get(self.baseURL)

        list_status = []

        if self.driver.find_element(By.XPATH, self.input_email_xpath):
            print("The Email textbox input field exists")
            list_status.append("Pass")
        else:
            print("The Email textbox input field doesn't exist")
            list_status.append("Fail")

        if self.driver.find_element(By.XPATH, self.input_password_xpath):
            print("The Password textbox input field exists")
            list_status.append("Pass")
        else:
            print("The Password textbox input field doesn't exist")
            list_status.append("Fail")

        if self.driver.find_element(By.XPATH, self.button_login_xpath):
            print("The Login button exists")
            list_status.append("Pass")
        else:
            print("The Login button doesn't exist")
            list_status.append("Fail")

        if self.driver.find_element(By.XPATH, self.checkbox_rememberme_xpath):
            print("The Remember checkbox exists")
            list_status.append("Pass")
        else:
            self.driver.save_screenshot("./Screenshots/" + "checkElementsExistence.png")
            print("The Remember checkbox doesn't exist")
            list_status.append("Fail")

        if "Fail" not in list_status:
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False

    # TC03: Check if login without input Email and Password
    def test_TC03(self, setup):
        print("TC03: Check if login without input Email and Password")

        self.driver = setup

        self.lp = LoginPage(self.driver)

        self.driver.get(self.baseURL)
        time.sleep(3)

        self.lp.setUsername(self.nullInput)

        self.lp.setPassword(self.nullInput)

        self.lp.clickLogin()
        time.sleep(2)

        if self.driver.find_element(By.XPATH, self.label_error1_xpath):
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False


    # TC04: Check if only input Email and leave Password blank
    def test_TC04(self, setup):
        print("TC04: Check if only input Email and leave Password blank")

        self.driver = setup

        self.lp = LoginPage(self.driver)

        self.driver.get(self.baseURL)
        time.sleep(3)

        self.lp.setUsername(self.username)

        self.lp.setPassword(self.nullInput)

        self.lp.clickLogin()
        time.sleep(2)

        if self.driver.find_element(By.XPATH, self.label_error2_xpath):
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False

    # TC05: Check if leave Email blank and input Password
    def test_TC05(self, setup):
        print("TC05: Check if leave Email blank and input Password")

        self.driver = setup

        self.lp = LoginPage(self.driver)

        self.driver.get(self.baseURL)
        time.sleep(3)

        self.lp.setUsername(self.nullInput)

        self.lp.setPassword(self.password)

        self.lp.clickLogin()
        time.sleep(2)

        if self.driver.find_element(By.XPATH, self.label_error1_xpath):
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False

    # TC06: Check if input invalid Email and valid Password
    def test_TC06(self, setup):
        print("TC06: Check if input invalid Email and valid Password")

        self.driver = setup

        self.lp = LoginPage(self.driver)

        self.driver.get(self.baseURL)
        time.sleep(3)

        self.lp.setUsername(self.invalidValue)

        self.lp.setPassword(self.password)

        self.lp.clickLogin()
        time.sleep(2)

        if self.driver.find_element(By.XPATH, self.label_error3_xpath):
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False

    # TC07: Check if input valid Email and invalid Password
    def test_TC07(self, setup):
        print("TC07: Check if input valid Email and invalid Password")

        self.driver = setup

        self.lp = LoginPage(self.driver)

        self.driver.get(self.baseURL)
        time.sleep(3)

        self.lp.setUsername(self.username)

        self.lp.setPassword(self.invalidValue)

        self.lp.clickLogin()
        time.sleep(2)

        if self.driver.find_element(By.XPATH, self.label_error2_xpath):
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False

    # TC08: Check if input valid Email and valid Password
    def test_TC08(self, setup):
        print("TC08: Check if input valid Email and valid Password")

        self.driver = setup

        self.lp = LoginPage(self.driver)

        self.driver.get(self.baseURL)
        time.sleep(3)

        self.lp.setUsername(self.username)

        self.lp.setPassword(self.password)

        self.lp.clickLogin()
        time.sleep(4)

        if self.driver.find_element(By.XPATH, self.label_logout_xpath):
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False
