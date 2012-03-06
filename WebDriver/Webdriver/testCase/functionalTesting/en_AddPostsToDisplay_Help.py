from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from Webdriver.all_globals import *

class EnAddPostsToDisplayHelpContent(unittest.TestCase):
    def setUp(self):
        gb_setUp(self)
    
    def test_en_add_posts_to_display_help_content(self):
        driver = self.driver
        gb_login(self)
        driver.get(self.base_url + "/ev/addpoststodisplay")
        gb_frame(self)
        driver.find_element_by_xpath("//div[@id='footer']/div").click()
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "span"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"In Non-touchscreen media players with multiple displays attached, this section allows posts to be assigned to specific displays.", driver.find_element_by_id("helpBody").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"Select a device from the Choose Media Player. All DIB(s) and all Displays attached to the media player will appear. Click on the post and drag to a display that you want the product information to be displayed on.", driver.find_element_by_id("helpBody").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_css_selector("img.exit").click()
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
