from pageObjects.LoginPage import LoginPage
import pytest
from selenium.webdriver.common.by import By
from ultilities.readPropertises import ReadConfig

#Test UI man Login
class Test_Login_001:
    baseURL = ReadConfig.getURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    expect_login_title = ReadConfig.getExpectLoginPageTitle()
    actualLoginTitle_xpath = "//div[contains(@class, 'page-title')]"



    def test_LoginPageTitle(self,setup):
        self.driver = setup

        self.driver.get(self.baseURL)

        act_login_title = self.driver.find_element(By.XPATH, self.actualLoginTitle_xpath).text
        print("act", act_login_title)
        print("exp", self.expect_login_title)

        if act_login_title == self.expect_login_title:
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot("./Screenshots/"+"checkLoginPageTitle.png")
            self.driver.close()
            assert False
