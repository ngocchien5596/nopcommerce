from pageObjects.AddNewCustomerPage import AddNewCustomerPage
from pageObjects.ProductPage import ProductPage
from pageObjects.LoginPage import LoginPage

class Test:

    baseURL = "https://admin-demo.nopcommerce.com/"

    def test_TC01(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        # Login
        self.login = LoginPage(self.driver)
        self.login.loginSuccess("admin@yourstore.com","admin")

        # Go to Add new product
        self.catalog = ProductPage(self.driver)
        self.catalog.go_to_product()
        self.catalog.click_add_new_product()

        # Input new product information
        self.catalog.input_product_name_field("iPhone 11 Pro")
        self.catalog.input_short_description_field("iOS 17.6.1")
        self.catalog.input_full_description_field("latest version of iPhone 11 Pro")
        self.catalog.input_sku_field("123465")
        self.catalog.select_categories_field("computer")
        self.catalog.select_inventory_method("Track inventory")

        # Click Save button
        self.catalog.click_save_button()
