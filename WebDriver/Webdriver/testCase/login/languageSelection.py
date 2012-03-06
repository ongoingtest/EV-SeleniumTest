# coding: utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
import HTMLTestRunner
from Webdriver.all_globals import *

class LanguageSelection(unittest.TestCase):
    def setUp(self):
        gb_setUp(self)
    
    def test_login_language_selection(self):
        driver = self.driver
        driver.get(self.base_url + "/ev/login")
        self.driver.implicitly_wait(30)
        driver = self.driver
        languageList = ["English","中文","Deutsch","Nederlands","Français","Italiano","日本語","Português","Pусский","Español","Türkçe"]
        for language in languageList:
            Select(driver.find_element_by_css_selector("select.languageSelection")).select_by_visible_text(language)
            self.driver.implicitly_wait(30)


    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()


