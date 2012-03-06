#This one works, but not fully verified.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
import unittest, time, re
from Webdriver.all_globals import *


class EnClassifyProductsFunctionDragAndDrop(unittest.TestCase):
    def setUp(self):
        gb_setUp(self)
    
    def test_en_classify_products_function_drag_and_drop(self):
        driver = self.driver
        gb_login(self)
        driver.get(self.base_url + "/ev/classifyproducts")
        driver.find_element_by_xpath("//li[@id='categoryCol_category514']/div/span").click()
#Verify process missing.
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "#categoryCol_subcategory515 > div.itemContent.subCategoryBg > div.handle"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "#categoryCol_category517 > div.categoryBg.itemContent > div.blockText"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        element = driver.find_element_by_css_selector("#categoryCol_subcategory515 > div.itemContent.subCategoryBg > div.handle")
        target = driver.find_element_by_css_selector("#categoryCol_category517 > div.categoryBg.itemContent > div.blockText")
        action_chains = ActionChains(driver)
        action_chains.drag_and_drop(element, target);

    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
