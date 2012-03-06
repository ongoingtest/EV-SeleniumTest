from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from Webdriver.all_globals import *

class EnAddProductsToPostsVerification(unittest.TestCase):
    def setUp(self):
        gb_setUp(self)
    
    def test_en_add_products_to_posts_verification(self):
        driver = self.driver
        gb_login(self)
        driver.get(self.base_url + "/ev/addproductstoposts")
        gb_frame(self)
        try: self.assertEqual("Add Products To Posts", driver.title)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.corporateLogo"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Add Products To Posts", driver.find_element_by_id("pageTitle").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Welcome", driver.find_element_by_css_selector("#welcomeTitle > span").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Logout", driver.find_element_by_xpath("//div[@id='header']/div[2]/div[2]/a/button").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Find Products/Accessories", driver.find_element_by_css_selector("div.productHeader").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn("All Manufacturers", driver.find_element_by_id("allManufacturersSelect").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn("All Categories", driver.find_element_by_id("allCategoriesSelect").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Choose Media Player", driver.find_element_by_css_selector("span.deviceHeader").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_css_selector("div.blockText.selectedText > span").click()
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "span.searchIcon"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID, "footer"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Help", driver.find_element_by_xpath("//div[@id='footer']/div").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "img"))
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
