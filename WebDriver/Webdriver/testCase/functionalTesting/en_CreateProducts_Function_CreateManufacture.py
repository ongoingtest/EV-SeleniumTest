from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class EnCreateProductsFunctionCreateManufacture(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://192.168.1.204:8080/"
        self.verificationErrors = []
    
    def test_en_create_products_function_create_manufacture(self):
        driver = self.driver
        driver.get(self.base_url + "/ev/createproducts")
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        Select(driver.find_element_by_id("detailManufacturer")).select_by_visible_text("--New Manufacturer--")
        driver.find_element_by_id("addManufacturer").click()
        driver.find_element_by_id("manufacturerName").clear()
        driver.find_element_by_id("manufacturerName").send_keys("yr111test")
        driver.find_element_by_id("newManufacturer").click()
        driver.refresh()
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        Select(driver.find_element_by_id("detailManufacturer")).select_by_visible_text("yr111test")
        driver.find_element_by_id("addManufacturer").click()
        driver.find_element_by_id("manufacturerName").clear()
        driver.find_element_by_id("manufacturerName").send_keys("yrcopytest 111")
        driver.find_element_by_id("saveManufacturer").click()
        Select(driver.find_element_by_id("detailManufacturer")).select_by_visible_text("1")
        driver.refresh()
        Select(driver.find_element_by_id("detailManufacturer")).select_by_visible_text("yrcopytest 111")
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        driver.find_element_by_css_selector("span[title=\"Setup Products\"]").click()
        driver.find_element_by_link_text("Assign Accessories").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
