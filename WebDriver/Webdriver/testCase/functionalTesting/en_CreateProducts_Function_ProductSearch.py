from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class EnCreateProductsFunctionProductSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://192.168.1.204:8080/"
        self.verificationErrors = []
    
    def test_en_create_products_function_product_search(self):
        driver = self.driver
        driver.get(self.base_url + "/ev/createproducts")
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        driver.find_element_by_id("productSearch").clear()
        driver.find_element_by_id("productSearch").send_keys("ab")
        driver.find_element_by_id("productSearchButton").click()
        driver.find_element_by_css_selector("div.blockText.selectedText").click()
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        driver.find_element_by_css_selector("div.bigDownArrow").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow]]
        driver.find_element_by_id("productSearch").clear()
        driver.find_element_by_id("productSearch").send_keys("")
        Select(driver.find_element_by_id("selectedFilterValue")).select_by_visible_text("Invue Database")
        driver.find_element_by_id("productSearch").clear()
        driver.find_element_by_id("productSearch").send_keys("ab")
        driver.find_element_by_id("productSearchButton").click()
        # ERROR: Caught exception [ERROR: Unsupported command [isAlertPresent]]
        # ERROR: Caught exception [ERROR: Unsupported command [chooseOkOnNextConfirmation]]
        driver.find_element_by_id("productSearch").clear()
        driver.find_element_by_id("productSearch").send_keys("")
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
