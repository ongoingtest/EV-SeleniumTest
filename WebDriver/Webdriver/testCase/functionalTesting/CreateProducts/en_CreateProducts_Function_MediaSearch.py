from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from Webdriver.all_globals import *

class EnCreateProductsFunctionMediaSearch(unittest.TestCase):
    def setUp(self):
        gb_setUp(self)
    
    def test_en_create_products_function_media_search(self):
        driver = self.driver
        gb_login(self)
        driver.get(self.base_url + "/ev/createproducts")
        try: self.assertIn("defaultBackgroundImage.jpg", driver.find_element_by_id("mediaSpace").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn("defaultSecondaryImage.jpg", driver.find_element_by_id("mediaSpace").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn("defaultLogo.png", driver.find_element_by_id("mediaSpace").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn("AVI_to_MPEG-4.avi", driver.find_element_by_id("mediaSpace").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("mediaSearchText").clear()
        driver.find_element_by_id("mediaSearchText").send_keys("defa")
        driver.find_element_by_id("mediaSearchButton").click()
        try: self.assertIn("defaultBackgroundImage.jpg", driver.find_element_by_id("mediaSpace").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn("defaultSecondaryImage.jpg", driver.find_element_by_id("mediaSpace").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn("defaultLogo.png", driver.find_element_by_id("mediaSpace").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertNotIn("AVI_to_MPEG-4.avi", driver.find_element_by_id("mediaSpace").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
