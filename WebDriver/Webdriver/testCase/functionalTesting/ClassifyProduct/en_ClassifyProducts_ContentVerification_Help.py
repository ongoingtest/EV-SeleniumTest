from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from Webdriver.all_globals import *

class EnClassifyProductsContentVerificationHelp(unittest.TestCase):
    def setUp(self):
        gb_setUp(self)
    
    def test_en_classify_products_content_verification_help(self):
        driver = self.driver
        gb_login(self)
        driver.get(self.base_url + "/ev/classifyproducts")
        driver.find_element_by_xpath("//div[@id='footer']/div").click()
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "span"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"This is where Categories for products are created. Along with subcategories and Keywords.", driver.find_element_by_id("helpBody").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"To create Categories and keywords, click on the plus sign to the right of the selection. Once an item is created, it will appear under the Products section.", driver.find_element_by_id("helpBody").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_css_selector("img.exit").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
