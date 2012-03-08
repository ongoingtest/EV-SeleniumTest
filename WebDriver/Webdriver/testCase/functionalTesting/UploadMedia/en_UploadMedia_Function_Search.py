#Sorting is pending.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from Webdriver.all_globals import *

class EnUploadMediaFunctionSearch(unittest.TestCase):
    def setUp(self):
        gb_setUp(self)
    
    def test_en_upload_media_function_search(self):
        driver = self.driver
        gb_login(self)
        driver.get(self.base_url + "/ev/uploadmedia")
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.columnHeader"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "span.columnHeaderText"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        try: self.assertTrue(self.is_element_present(By.ID, "filterMediaText"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("", driver.find_element_by_css_selector("span.searchIcon").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("filterMediaText").clear()
        driver.find_element_by_id("filterMediaText").send_keys("av")
        driver.find_element_by_css_selector("span.searchIcon").click()
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        # ERROR: Caught exception [Error: locator strategy either id or name must be specified explicitly.]
        Select(driver.find_element_by_id("sortMedia")).select_by_visible_text("Sort by Name")
        #  sorting is pending 
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
