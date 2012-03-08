from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from Webdriver.all_globals import *

class EnCreateProductsContentVerificationHelp(unittest.TestCase):
    def setUp(self):
        gb_setUp(self)
    
    def test_en_create_products_content_verification_help(self):
        driver = self.driver
        gb_login(self)
        driver.get(self.base_url + "/ev/createproducts")
        driver.find_element_by_xpath("//div[@id='footer']/div").click()
        try: self.assertTrue(self.is_element_present(By.ID, "title"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Help", driver.find_element_by_id("title").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"To create a new product, Click on the New button, Select the product radio button, then begin filling in all the product information. Click and drag images and videos from the media section into the slideshow, secondary image and video sections. Then under the Keywords section, begin selecting the keyword information.", driver.find_element_by_id("helpBody").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"To edit a product. Click on the Please select product dropdown and select the product you wish to edit.", driver.find_element_by_id("helpBody").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"To create a new Accessory, Click on the New button, select the accessory radio button, then begin filling in all the product information. Click and drag images and videos from the media section into the slideshow , secondary image and video sections.", driver.find_element_by_id("helpBody").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"To Edit an Accessory, Click on the Please select product dropdown and select the accessory you wish to edit.", driver.find_element_by_id("helpBody").text)
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
