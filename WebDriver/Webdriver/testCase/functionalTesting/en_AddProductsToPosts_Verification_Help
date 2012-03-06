from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from Webdriver.all_globals import *

class EnAddProductsToPostsHelp(unittest.TestCase):
    def setUp(self):
        gb_setUp(self)
    
    def test_en_add_products_to_posts_help(self):
        driver = self.driver
        gb_login(self)
        driver.get(self.base_url + "/ev/addproductstoposts")
        driver.find_element_by_xpath("//div[@id='footer']/div").click()
        try: self.assertEqual("Help", driver.find_element_by_css_selector("span").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"A Media Player needs to be selected first before a product can be applied. Select a media from the Choose Media Player section.", driver.find_element_by_id("helpBody").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"Once a media player is selected. Search through the Find Product section for the product to be placed on the post. Once the product is found, Click and Drag the product from the picture box and drop it in the desired post location.", driver.find_element_by_id("helpBody").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_css_selector("img.exit").click()
        driver.find_element_by_css_selector("span[title=\"Manage InStore Display\"]").click()
        driver.find_element_by_link_text("Add Posts to Display").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
