from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from Webdriver.all_globals import *

class EnAssignAccessoryContentVerification(unittest.TestCase):
    def setUp(self):
        gb_setUp(self)
    
    def test_en_assign_accessory_content_verification(self):
        driver = self.driver
        gb_login(self)
        driver.get(self.base_url + "/ev/assignaccessories")
        gb_frame(self)
        try: self.assertEqual("Assign Accessories", driver.title)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Assign Accessories", driver.find_element_by_id("pageTitle").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='header']/div[2]/div[2]/a/button"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "span.columnHeaderText"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Accessories", driver.find_element_by_css_selector("span.columnHeaderText").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID, "filterAccessories"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "span.searchIcon"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.productColumn > div.columnHeader > span.columnHeaderText"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Products", driver.find_element_by_css_selector("div.productColumn > div.columnHeader > span.columnHeaderText").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID, "filterProductsType"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"Products", driver.find_element_by_id("filterProductsType").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"Accessories", driver.find_element_by_id("filterProductsType").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID, "filterProducts"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("", driver.find_element_by_css_selector("div.productColumn > div.columnHeader > span.searchIcon").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID, "footer"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "img"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Help", driver.find_element_by_xpath("//div[@id='footer']/div").text)
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
