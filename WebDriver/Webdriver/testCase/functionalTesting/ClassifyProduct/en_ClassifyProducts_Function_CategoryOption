from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from Webdriver.all_globals import *

class EnClassifyProductsFunctionCategoryOption(unittest.TestCase):
    def setUp(self):
        gb_setUp(self)
    
    def test_en_classify_products_function_category_option(self):
        driver = self.driver
        gb_login(self)
        driver.get(self.base_url + "/ev/classifyproducts")
        try: self.assertNotEqual(u"apple", driver.find_element_by_css_selector("#categoryCol_category155 > div.itemContent.categoryBg > div.blockText").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"test", driver.find_element_by_css_selector("#categoryCol_category155 > div.itemContent.categoryBg > div.blockText").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("categoryCol_category155Options").click()
        driver.find_element_by_id("categoryName").clear()
        driver.find_element_by_id("categoryName").send_keys(u"apple")
        driver.find_element_by_id("okExistingCategory").click()
        driver.refresh
        for i in range(60):
            try:
                if u"apple" == driver.find_element_by_css_selector("#categoryCol_category155 > div.itemContent.categoryBg > div.blockText").text: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertNotEqual(u"test", driver.find_element_by_css_selector("#categoryCol_category155 > div.itemContent.categoryBg > div.blockText").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"apple", driver.find_element_by_css_selector("#categoryCol_category155 > div.itemContent.categoryBg > div.blockText").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("categoryCol_category155Options").click()
        driver.find_element_by_id("categoryName").clear()
        driver.find_element_by_id("categoryName").send_keys(u"test")
        driver.find_element_by_id("okExistingCategory").click()
        for i in range(60):
            try:
                if u"test" == driver.find_element_by_css_selector("#categoryCol_category155 > div.itemContent.categoryBg > div.blockText").text: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertNotEqual(u"apple", driver.find_element_by_css_selector("#categoryCol_category155 > div.itemContent.categoryBg > div.blockText").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"test", driver.find_element_by_css_selector("#categoryCol_category155 > div.itemContent.categoryBg > div.blockText").text)
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
