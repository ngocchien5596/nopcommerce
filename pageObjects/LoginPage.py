from selenium.webdriver.common.by import  By


class LoginPage:

    textbox_username_id =  "Email"
    textbox_password_id = "Password"
    button_login_xpath = "//div[contains(@class, 'buttons') and contains(., 'Log in')]"


    def __init__(self, driver):
        self.driver = driver

    def setUsername(self, username):
        user_name_input = self.driver.find_element(By.ID, self.textbox_username_id)
        user_name_input.clear()
        user_name_input.send_keys(username)

    def setPassword(self, password):
        password_input = self.driver.find_element(By.ID, self.textbox_password_id)
        password_input.clear()
        password_input.send_keys(password)

    def clickLogin(self):
        login_button = self.driver.find_element(By.XPATH, self.button_login_xpath)
        login_button.click()

    def loginSuccess(self, username, password):
        self.setUsername(username)
        self.setPassword(password)
        self.clickLogin()



