from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from Webdriver.all_globals import *

class EnAddPostsToDisplaySelectADevice(unittest.TestCase):
    def setUp(self):
        gb_setUp(self)
    
    def test_en_add_posts_to_display_select_a_device(self):
        driver = self.driver
        gb_login(self)
        driver.get(self.base_url + "/ev/addpoststodisplay")
        driver.find_element_by_css_selector("span.bigDownArrow").click()
        driver.find_element_by_xpath("//li[@id='hierarchy_storeGroup199']/div/span").click()
        driver.find_element_by_xpath("//li[@id='hierarchy_store200']/div/span").click()
        driver.find_element_by_xpath("//li[@id='deviceContainersCol_device28']/div/div").click()
        driver.find_element_by_css_selector("span.bigDownArrow").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
