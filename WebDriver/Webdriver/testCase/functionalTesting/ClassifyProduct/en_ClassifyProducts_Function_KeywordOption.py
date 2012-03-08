from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from Webdriver.all_globals import *

class EnClassifyProductsFunctionKeywordOption(unittest.TestCase):
    def setUp(self):
        gb_setUp(self)
    
    def test_en_classify_products_function_keyword_option(self):
        driver = self.driver
        gb_login(self)
        driver.get(self.base_url + "/ev/classifyproducts")
        driver.find_element_by_xpath("//li[@id='categoryCol_category155']/div/span").click()
        try: self.assertNotEqual(u"apple", driver.find_element_by_css_selector("#categoryCol_keyword209 > div.keywordBg.itemContent > div.blockText").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"testKey", driver.find_element_by_css_selector("#categoryCol_keyword209 > div.keywordBg.itemContent > div.blockText").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_xpath("//li[@id='categoryCol_keyword209']/div/span[2]").click()
        driver.find_element_by_id("keywordName").clear()
        driver.find_element_by_id("keywordName").send_keys(u"apple")
        driver.find_element_by_id("okExistingKeyword").click()
        driver.refresh
        for i in range(60):
            try:
                if u"apple" == driver.find_element_by_css_selector("#categoryCol_keyword209 > div.keywordBg.itemContent > div.blockText").text: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertNotEqual(u"testKey", driver.find_element_by_css_selector("#categoryCol_keyword209 > div.keywordBg.itemContent > div.blockText").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"apple", driver.find_element_by_css_selector("#categoryCol_keyword209 > div.keywordBg.itemContent > div.blockText").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        #driver.find_element_by_xpath("//li[@id='categoryCol_category155']/div/span").click()
        driver.find_element_by_xpath("//li[@id='categoryCol_keyword209']/div/span[2]").click()
        driver.find_element_by_id("keywordName").clear()
        driver.find_element_by_id("keywordName").send_keys(u"testKey")
        driver.find_element_by_id("okExistingKeyword").click()
        for i in range(60):
            try:
                if u"testKey" == driver.find_element_by_css_selector("#categoryCol_keyword209 > div.keywordBg.itemContent > div.blockText").text: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertNotEqual(u"apple", driver.find_element_by_css_selector("#categoryCol_keyword209 > div.keywordBg.itemContent > div.blockText").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"testKey", driver.find_element_by_css_selector("#categoryCol_keyword209 > div.keywordBg.itemContent > div.blockText").text)
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
