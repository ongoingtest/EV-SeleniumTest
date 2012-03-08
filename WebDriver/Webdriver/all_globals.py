# coding: utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

gb_ip = "192.168.1.204"
#gb_ip = "127.0.0.1"
gb_port = "8080"
#gb_ip = "74.101.218.58"
#gb_port = "9080"
gb_filename_prefix = '/home/zignage/EV-SeleniumTest/WebDriver/result'
#gb_filename_prefix = '/home/yueran/EV-SeleniumTest/WebDriver/result'

#Create Products
#manufacture:
gb_manTestValue = 6

def gb_setUp(self):
    self.driver = webdriver.Firefox()
    self.driver.implicitly_wait(30)
    self.base_url = "http://%s:%s" %(gb_ip, gb_port)
    self.verificationErrors = []

def gb_login(self):
    driver = self.driver
    driver.get(self.base_url + "/ev/login")
    driver.find_element_by_id("form.login").clear()
    driver.find_element_by_id("form.login").send_keys("yrtest")
    driver.find_element_by_id("form.password").clear()
    driver.find_element_by_id("form.password").send_keys("test")
    #driver.find_element_by_id("form.login").send_keys("andrew")
    #driver.find_element_by_id("form.password").clear()
    #driver.find_element_by_id("form.password").send_keys("andrew")
    driver.find_element_by_css_selector("span.commonButton.login_ok").click()

def gb_is_element_present(self, how, what):
    try: self.driver.find_element(by=how, value=what)
    except NoSuchElementException, e: return False
    return True

def gb_tearDown(self):
    self.driver.quit()
    self.assertEqual([], self.verificationErrors)

def gb_frame(self):
    driver = self.driver
    try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.corporateLogo"))
    except AssertionError as e: self.verificationErrors.append(str(e))
    try: self.assertEqual("Welcome", driver.find_element_by_css_selector("#welcomeTitle > span").text)
    except AssertionError as e: self.verificationErrors.append(str(e))
    try: self.assertEqual("Logout", driver.find_element_by_xpath("//div[@id='header']/div[2]/div[2]/a/button").text)
    except AssertionError as e: self.verificationErrors.append(str(e))
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
    try: self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='footer']/div/span"))
    except AssertionError as e: self.verificationErrors.append(str(e))
    try: self.assertEqual("Help", driver.find_element_by_xpath("//div[@id='footer']/div").text)
    except AssertionError as e: self.verificationErrors.append(str(e))
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
    try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.footerLogoImg > img"))
    except AssertionError as e: self.verificationErrors.append(str(e))
    try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "span[title=\"Manage InStore Display\"]"))
    except AssertionError as e: self.verificationErrors.append(str(e))
    try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "span[title=\"Create Reports\"]"))
    except AssertionError as e: self.verificationErrors.append(str(e))
    try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "span[title=\"Upload Media\"]"))
    except AssertionError as e: self.verificationErrors.append(str(e))
    try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "span[title=\"Setup Products\"]"))
    except AssertionError as e: self.verificationErrors.append(str(e))
    try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "span[title=\"Setup Users/Groups\"]"))
    except AssertionError as e: self.verificationErrors.append(str(e))
    try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "span[title=\"Setup Stores/Structure\"]"))
    except AssertionError as e: self.verificationErrors.append(str(e))
    try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "span[title=\"Setup Templates\"]"))
    except AssertionError as e: self.verificationErrors.append(str(e))
    try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "span[title=\"Setup Attract Loops\"]"))
    except AssertionError as e: self.verificationErrors.append(str(e))
    try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "span[title=\"View Network Status\"]"))
    except AssertionError as e: self.verificationErrors.append(str(e))
    driver.find_element_by_css_selector("span[title=\"Manage InStore Display\"]").click()
    try: self.assertTrue(self.is_element_present(By.LINK_TEXT, "Add Products to Posts"))
    except AssertionError as e: self.verificationErrors.append(str(e))
    try: self.assertTrue(self.is_element_present(By.LINK_TEXT, "Add Posts to Display"))
    except AssertionError as e: self.verificationErrors.append(str(e))
    driver.find_element_by_css_selector("span[title=\"Setup Products\"]").click()
    try: self.assertTrue(self.is_element_present(By.LINK_TEXT, "Classify Products"))
    except AssertionError as e: self.verificationErrors.append(str(e))
    try: self.assertTrue(self.is_element_present(By.LINK_TEXT, "Create Products"))
    except AssertionError as e: self.verificationErrors.append(str(e))
    try: self.assertTrue(self.is_element_present(By.LINK_TEXT, "Assign Accessories"))
    except AssertionError as e: self.verificationErrors.append(str(e))
    driver.find_element_by_css_selector("span[title=\"Setup Stores/Structure\"]").click()
    try: self.assertTrue(self.is_element_present(By.LINK_TEXT, "Store Hierarchy"))
    except AssertionError as e: self.verificationErrors.append(str(e))
    try: self.assertTrue(self.is_element_present(By.LINK_TEXT, "Group Media Players"))
    except AssertionError as e: self.verificationErrors.append(str(e))
    driver.find_element_by_css_selector("span[title=\"Setup Templates\"]").click()
    try: self.assertTrue(self.is_element_present(By.LINK_TEXT, "Template Styles"))
    except AssertionError as e: self.verificationErrors.append(str(e))
    try: self.assertTrue(self.is_element_present(By.LINK_TEXT, "Schedule Templates"))
    except AssertionError as e: self.verificationErrors.append(str(e))
    driver.find_element_by_css_selector("span[title=\"Setup Attract Loops\"]").click()
    try: self.assertTrue(self.is_element_present(By.LINK_TEXT, "Create Loops"))
    except AssertionError as e: self.verificationErrors.append(str(e))
    try: self.assertTrue(self.is_element_present(By.LINK_TEXT, "Schedule Loops"))
    except AssertionError as e: self.verificationErrors.append(str(e))