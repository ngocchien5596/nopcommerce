from selenium.webdriver.common.by import  By
from selenium.webdriver.support.ui import Select

import time

class AddNewCustomerPage:

    # Locators
    icon_customer_xpath = "//li//a//i[contains(@class, 'nav-icon far fa-user')]"
    text_customer_xpath = "//li//a//p[text()=' Customers']"
    button_addNew_xpath = "//div//a[contains(., 'Add new')]"
    textbox_email_id = "Email"
    textbox_password_id = "Password"
    textbox_firstname_id = "FirstName"
    textbox_lastname_id = "LastName"
    radio_genderMale_id = "Gender_Male"
    radio_genderFemale_id = "Gender_Female"
    textbox_birthday_id = "DateOfBirth"
    textbox_companyName_id = "Company"
    checkbox_isTaxExempt_id = "IsTaxExempt"
    droplist_newsLetter_xpath = "//div[contains(@class, 'k-multiselect-wrap k-floatwrap')][1]"
    droplist_yourStoreNameValue_xpath = "//li[contains(., 'Your store name')]"
    droplist_testStore2Value_xpath = "//li[contains(., 'Test store 2')]"
    droplist_customerRole_xpath = "//ul[contains(@id, 'SelectedCustomerRoleIds_taglist')]//parent::div"
    droplist_AdministratorsValue_xpath = "//ul[contains(@id, 'SelectedCustomerRoleIds_listbox')]//li[contains(., 'Administrators')]"
    droplist_ForumModeratorsValue_xpath = "//ul[contains(@id, 'SelectedCustomerRoleIds_listbox')]//li[contains(., 'Forum Moderators')]"
    droplist_GuestsValue_xpath = "//ul[contains(@id, 'SelectedCustomerRoleIds_listbox')]//li[contains(., 'Guests')]"
    droplist_RegisteredValue_xpath = "//ul[contains(@id, 'SelectedCustomerRoleIds_listbox')]//li[contains(., 'Registered')]"
    droplist_VendorsValue_xpath = "//ul[contains(@id, 'SelectedCustomerRoleIds_listbox')]//li[contains(., 'Vendors')]"
    droplist_managerOfVendor_id = "VendorId"
    textbox_comment_id = "AdminComment"
    button_save_name = "save"

    # Data


    def __init__(self, driver):
        self.driver = driver

    def getToAddNewCustomerURL(self):
        self.driver.find_element(By.XPATH, self.icon_customer_xpath).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.text_customer_xpath).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.button_addNew_xpath).click()
        time.sleep(3)

    def setEmail(self, email):
        self.driver.find_element(By.ID, self.textbox_email_id).send_keys(email)
        time.sleep(1)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)
        time.sleep(1)

    def setFirstName(self, firstname):
        self.driver.find_element(By.ID, self.textbox_firstname_id).send_keys(firstname)
        time.sleep(1)

    def setLastName(self, lastname):
        self.driver.find_element(By.ID, self.textbox_lastname_id).send_keys(lastname)
        time.sleep(1)

    def setGender(self, gender):
        if gender == "Male":
            self.driver.find_element(By.ID, self.radio_genderMale_id).click()
            time.sleep(1)
        elif gender == "Female":
            self.driver.find_element(By.ID, self.radio_genderFemale_id).click()
            time.sleep(1)
        else:
            print("Please input Male or Female")

    def setBirthday(self, birthday):
        self.driver.find_element(By.ID, self.textbox_birthday_id).send_keys(birthday)
        time.sleep(1)

    def setCompanyName(self, company):
        self.driver.find_element(By.ID, self.textbox_companyName_id).send_keys(company)
        time.sleep(1)

    def setTax(self, yesno):
        if yesno == "Yes":
            self.driver.find_element(By.ID, self.checkbox_isTaxExempt_id).click()
            time.sleep(1)
        else:
            print("Please input Yes or No")

    def setNewsLetter(self, value):
        self.driver.find_element(By.XPATH, self.droplist_newsLetter_xpath).click()
        time.sleep(0.5)
        if value == "Your store name":
            element = self.driver.find_element(By.XPATH, self.droplist_yourStoreNameValue_xpath)
            self.driver.execute_script("arguments[0].click();", element)
            time.sleep(3)
        elif value == "Test store 2":
            element = self.driver.find_element(By.XPATH, self.droplist_testStore2Value_xpath)
            self.driver.execute_script("arguments[0].click();", element)
            time.sleep(3)
        else:
            print("Please input correct value: Your Store Name or Test store 2")

    def setCustomerRole(self, customerrole):
        self.driver.find_element(By.XPATH, self.droplist_customerRole_xpath).click()
        self.driver.save_screenshot("./Screenshots/" + "test.png")
        time.sleep(0.5)
        if customerrole == "Administrators":
            element = self.driver.find_element(By.XPATH, self.droplist_AdministratorsValue_xpath)
            self.driver.execute_script("arguments[0].click();", element)
            time.sleep(3)
        elif customerrole == "Forum Moderators":
            element = self.driver.find_element(By.XPATH, self.droplist_ForumModeratorsValue_xpath)
            self.driver.execute_script("arguments[0].click();", element)
            time.sleep(3)
        elif customerrole == "Guests":
            element = self.driver.find_element(By.XPATH, self.droplist_GuestsValue_xpath)
            self.driver.execute_script("arguments[0].click();", element)
            time.sleep(3)
        elif customerrole == "Registered":
            element = self.driver.find_element(By.XPATH, self.droplist_RegisteredValue_xpath)
            self.driver.execute_script("arguments[0].click();", element)
            time.sleep(3)
        elif customerrole == "Vendors":
            element = self.driver.find_element(By.XPATH, self.droplist_VendorsValue_xpath)
            self.driver.execute_script("arguments[0].click();", element)
            print("clicked")
            time.sleep(3)
        else:
            print("Please input correct value: Administrators, Forum Moderators, Guests, Registered or Vendors")

    def setManagerOfVendor(self, vendor):
        select = Select(self.driver.find_element(By.ID, self.droplist_managerOfVendor_id))
        select.select_by_visible_text(vendor)
        time.sleep(1)

    def setComment(self, comment):
        self.driver.find_element(By.ID, self.textbox_comment_id).send_keys(comment)
        time.sleep(1)

    def clickSave(self):
        self.driver.find_element(By.NAME, self.button_save_name).click()
        time.sleep(3)