from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from Webdriver.all_globals import *

class EnAddProductsToPostsSearch(unittest.TestCase):
    def setUp(self):
        gb_setUp(self)
    
    def test_en_add_products_to_posts_search(self):
        driver = self.driver
        gb_login(self)
        driver.get(self.base_url + "/ev/addproductstoposts")
        driver.find_element_by_id("filterText").clear()
        try: self.assertIn(u"abcd", driver.find_element_by_id("allProductsSelect").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"test product 1 Aifonds", driver.find_element_by_id("allProductsSelect").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("filterText").send_keys("abcd")
        driver.find_element_by_css_selector("span.searchIcon").click()
        try: self.assertIn(u"abcd", driver.find_element_by_id("allProductsSelect").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertNotIn(u"test product 1 Aifonds", driver.find_element_by_id("allProductsSelect").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("body").click()
        driver.find_element_by_css_selector("span.bigDownArrow").click()
       # driver.find_element_by_xpath("//li[@id='hierarchy_company101']/div/span").click()
        #driver.find_element_by_xpath("//li[@id='hierarchy_company96']/div/span").click()
        #driver.find_element_by_xpath("//li[@id='deviceContainersCol_device27']/div/div").click()
        driver.find_element_by_css_selector("span.bigDownArrow").click()
        try: self.assertTrue(self.is_element_present(By.ID, "postList"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.refresh()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
