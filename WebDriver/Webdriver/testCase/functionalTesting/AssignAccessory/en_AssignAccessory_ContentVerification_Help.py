from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from Webdriver.all_globals import *

class EnAssignAccessoryContentVerificationHelp(unittest.TestCase):
    def setUp(self):
        gb_setUp(self)
    
    def test_en_assign_accessory_content_verification_help(self):
        driver = self.driver
        gb_login(self)
        driver.get(self.base_url + "/ev/assignaccessories")
        driver.find_element_by_xpath("//div[@id='footer']/div/span").click()
        try: self.assertTrue(self.is_element_present(By.ID, "title"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Help", driver.find_element_by_css_selector("span").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"Accessories are assigned to product categories. Accessories appear under the Accessories section and can be clicked and dragged from accessories to a product.", driver.find_element_by_id("helpBody").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"Accessories and Products can be searched through the boxes in the headers of each section.", driver.find_element_by_id("helpBody").text)
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
