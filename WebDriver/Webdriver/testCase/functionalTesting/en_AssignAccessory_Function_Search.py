from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from Webdriver.all_globals import *

class EnAssignAccessoryFunctionSearch(unittest.TestCase):
    def setUp(self):
        gb_setUp(self)
    
    def test_en_assign_accessory_function_search(self):
        driver = self.driver
        gb_login(self)
        driver.get(self.base_url + "/ev/assignaccessories")
        try: self.assertIn(u"abcf", driver.find_element_by_id("accessoryBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"abcg", driver.find_element_by_id("accessoryBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"accccd", driver.find_element_by_id("accessoryBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("filterAccessories").clear()
        driver.find_element_by_id("filterAccessories").send_keys("")
        # ERROR: Caught exception [ERROR: Unsupported command [clickAt]]
        driver.find_element_by_id("filterAccessories").clear()
        driver.find_element_by_id("filterAccessories").send_keys("ab")
        driver.find_element_by_css_selector("span.searchIcon").click()
        try: self.assertIn(u"abcf", driver.find_element_by_id("accessoryBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"abcg", driver.find_element_by_id("accessoryBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertNotIn(u"accccd", driver.find_element_by_id("accessoryBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("filterAccessories").clear()
        driver.find_element_by_id("filterAccessories").send_keys("")
        try: self.assertIn(u"abcd", driver.find_element_by_id("categoryBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"acccd", driver.find_element_by_id("categoryBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"test", driver.find_element_by_id("categoryBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("filterProducts").clear()
        driver.find_element_by_id("filterProducts").send_keys("test")
        try: self.assertNotIn(u"abcd", driver.find_element_by_id("categoryBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertNotIn(u"acccd", driver.find_element_by_id("categoryBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"test", driver.find_element_by_id("categoryBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("filterProducts").clear()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
