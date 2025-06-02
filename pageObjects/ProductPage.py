from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

class ProductPage:

    # Locators
    catalog_xpath = "//a[@class='nav-link active' and @href='#']"
    product_xpath = "//a[@href='/Admin/Product/List']"
    add_new_product_xpath = "//a[@href='/Admin/Product/Create']"
    product_name_id = "Name"
    short_description_id = "ShortDescription"
    full_description_id = "FullDescription_ifr"
    sku_id = "Sku"
    categories_searchbox_xpath = "(//input[@role='searchbox'])[1]"
    inventory_name = "ManageInventoryMethodId"
    save_button_xpath = "//i[contains(text(), 'Save')]"


    def __init__(self, driver):
        self.driver = driver

    def go_to_product(self):
        self.driver.find_element(By.XPATH, self.catalog_xpath).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.product_xpath).click()
        time.sleep(1)

    def click_add_new_product(self):
        self.driver.find_element(By.XPATH, self.add_new_product_xpath).click()
        time.sleep(1)


    def input_product_name_field(self, product_name):
        product_name_field =  self.driver.find_element(By.ID, self.product_name_id)
        product_name_field.clear()
        product_name_field.send_keys(product_name)
        time.sleep(1)

    def input_short_description_field(self, short_description):
        short_description_field = self.driver.find_element(By.ID, self.short_description_id)
        short_description_field.clear()
        short_description_field.send_keys(short_description)
        time.sleep(1)

    def input_full_description_field(self, full_description):
        full_description_field = self.driver.find_element(By.ID, self.full_description_id)
        full_description_field.clear()
        full_description_field.send_keys(full_description)
        time.sleep(1)

    def input_sku_field(self, sku):
        sku_field = self.driver.find_element(By.ID, self.sku_id)
        sku_field.clear()
        sku_field.send_keys(sku)
        time.sleep(1)

    def select_categories_field(self, categories):
        categories_searchbox = self.driver.find_element(By.XPATH, self.categories_searchbox_xpath)
        categories_searchbox.click()
        categories_searchbox.send_keys(categories)
        categories_searchbox.send_keys(Keys.RETURN)
        time.sleep(1)

    def select_inventory_method(self, inventory):
        inventory_name = self.driver.find_element(By.NAME, self.inventory_name)
        sl = Select(inventory_name)
        sl.select_by_visible_text(inventory)
        time.sleep(1)

    def click_save_button(self):
        self.driver.find_element(By.XPATH, self.save_button_xpath).click()
        time.sleep(3)



