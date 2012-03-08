#Note: This one is pending because I have not figure out how to test upload a media from local folder.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from Webdriver.all_globals import *

class EnUploadMediaFunctionCreateMedia(unittest.TestCase):
    def setUp(self):
        gb_setUp(self)
    
    def test_en_upload_media_function_create_media(self):
        driver = self.driver
        gb_login(self)
        driver.get(self.base_url + "/ev/uploadmedia")
        driver.find_element_by_xpath("//div[@id='mediaSpace']/div[2]/div").click()
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        try: self.assertEqual("Upload Media", driver.find_element_by_css_selector("span").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        try: self.assertEqual("Close", driver.find_element_by_css_selector("button.exit.buttonStyle").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_css_selector("button.exit.buttonStyle").click()
        # Upload Media could not be tested with ide
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
