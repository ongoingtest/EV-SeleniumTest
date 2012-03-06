from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
import HTMLTestRunner
from Webdriver.all_globals import *


class LoginVerification(unittest.TestCase):
    def setUp(self):
        gb_setUp(self)
    
 #Case 1: leave login and password empty.
    def tc_case1(self):
        driver = self.driver
        driver.get(self.base_url + "/ev/login")
        driver.find_element_by_css_selector("span.commonButton.login_ok").click()
        try: self.assertEqual("Please enter your login id and password.", driver.find_element_by_id("warningMessage").text)
        except AssertionError as e: self.verificationErrors.append(str(e))

 #Case 2: leave password empty.
    def tc_case2(self):
        driver = self.driver
        driver.get(self.base_url + "/ev/login")
        driver.find_element_by_id("form.login").clear()
        driver.find_element_by_id("form.login").send_keys("andrew")
        driver.find_element_by_css_selector("span.commonButton.login_ok").click()
        try: self.assertEqual("Please enter your password.", driver.find_element_by_id("warningMessage").text)
        except AssertionError as e: self.verificationErrors.append(str(e))

#Case 3: leave login empty.
    def tc_case3(self):
        driver = self.driver
        driver.get(self.base_url + "/ev/login")
        driver.find_element_by_id("form.login").clear()
        driver.find_element_by_id("form.login").send_keys("")
        driver.find_element_by_id("form.password").clear()
        driver.find_element_by_id("form.password").send_keys("andrew")
        driver.find_element_by_css_selector("span.commonButton.login_ok").click()
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "span.commonButton.login_ok"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Please enter your login id.", driver.find_element_by_id("warningMessage").text)
        except AssertionError as e: self.verificationErrors.append(str(e))

#Case 4: Invalid username and/or password!
    def tc_case4(self):
        driver = self.driver
        driver.get(self.base_url + "/ev/login")
        driver.find_element_by_id("form.login").clear()
        driver.find_element_by_id("form.login").send_keys("aaaa")
        driver.find_element_by_id("form.password").clear()
        driver.find_element_by_id("form.password").send_keys("bbbb")
        driver.find_element_by_css_selector("span.commonButton.login_ok").click()
        try: self.assertEqual("Invalid username and/or password!", driver.find_element_by_id("warningMessage").text)
        except AssertionError as e: self.verificationErrors.append(str(e))

#Case 5: Correct login and password.
    def tc_case5(self):
        driver = self.driver
        driver.get(self.base_url + "/ev/login")
        driver.find_element_by_id("form.password").clear()
        driver.find_element_by_id("form.password").send_keys("")
        driver.find_element_by_id("form.login").clear()
        driver.find_element_by_id("form.login").send_keys("yrtest")
        driver.find_element_by_id("form.password").clear()
        driver.find_element_by_id("form.password").send_keys("test")
        driver.find_element_by_css_selector("span.commonButton.login_ok").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    testsuite = unittest.TestSuite()

    testsuite.addTest(LoginVerification("tc_case1"))
    testsuite.addTest(LoginVerification("tc_case2"))
    testsuite.addTest(LoginVerification("tc_case3"))
    testsuite.addTest(LoginVerification("tc_case4"))
    testsuite.addTest(LoginVerification("tc_case5"))

    #filename = '/home/zignage/seleniumTest/WebDriver/result/loginVerification.html'
    filename = gb_filename_prefix+'/loginVerification.html'
    fp = file(filename,'wb')

    runner = HTMLTestRunner.HTMLTestRunner(
            stream=fp,
            title='Test Result',
            description='Test Report'
            )
 #   runner = unittest.TextTestRunner()
    runner.run(testsuite)


