from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from Webdriver.all_globals import *

class EnClassifyProductsContentVerification(unittest.TestCase):
    def setUp(self):
        gb_setUp(self)
    
    def test_en_classify_products_content_verification(self):
        driver = self.driver
        gb_login(self)
        driver.get(self.base_url + "/ev/classifyproducts")
        gb_frame(self)
        try: self.assertEqual("", driver.find_element_by_css_selector("div.corporateLogo").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Classify Products", driver.title)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Classify Products", driver.find_element_by_id("pageTitle").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("", driver.find_element_by_css_selector("div.corporateLogo").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='header']/div[2]/div[2]/a/button"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID, "welcomeTitle"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"Before you add products to the database we will need to define the product categories, sub categories and the keywords. This will help the system compare your apples to apples. After the class is created you will associate that class to a category and then create up to 10 keywords. Product keywords will be as defining in either absolute values or value ranges.", driver.find_element_by_class_name("categoryCol").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "span.columnHeaderText"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Product Categories, Sub Categories & Keywords", driver.find_element_by_css_selector("span.columnHeaderText").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("New Product Category", driver.find_element_by_css_selector("div.blockText").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("New Product Sub Category", driver.find_element_by_css_selector("div.itemContent.subCategoryBg > div.blockText").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("New Product Keyword", driver.find_element_by_css_selector("div.itemContent.keywordBg > div.blockText").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "span.add"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(u"Product Classifications", driver.find_element_by_css_selector("div.classificationCol > div.columnHeader > span.columnHeaderText").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID, "categoryCol_category155Options"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID, "155"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "img"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID, "footer"))
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
