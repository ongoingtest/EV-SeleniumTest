from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
import HTMLTestRunner
from all_globals import *
#from Webdriver.testCase.login.login_loginVerification import *
from Webdriver.testCase.login import loginVerification as loginCase


class LoginLoginVerification(loginCase.LoginVerification):
    def setUp(self):
        gb_setUp(self)

 #Case 1: leave login and password empty.
    def test_login_login_verification_case1(self):
        loginCase.LoginVerification.tc_case1(self)

 #Case 2: leave password empty.
    def test_login_login_verification_case2(self):
        loginCase.LoginVerification.tc_case2(self)

#Case 3: leave login empty.
    def test_login_login_verification_case3(self):
        loginCase.LoginVerification.tc_case3(self)

#Case 4: Invalid username and/or password! 
    def test_login_login_verification_case4(self):
        loginCase.LoginVerification.tc_case4(self)

#Case 4: Correct login and password.
    def test_login_login_verification_case5(self):
        loginCase.LoginVerification.tc_case5(self)
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    testsuite = unittest.TestSuite()

    testsuite.addTest(LoginLoginVerification("test_login_login_verification_case1"))
    testsuite.addTest(LoginLoginVerification("test_login_login_verification_case2"))
    testsuite.addTest(LoginLoginVerification("test_login_login_verification_case3"))
    testsuite.addTest(LoginLoginVerification("test_login_login_verification_case4"))
    testsuite.addTest(LoginLoginVerification("test_login_login_verification_case5"))

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


