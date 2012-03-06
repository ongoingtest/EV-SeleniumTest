#coding:utf-8
from selenium import selenium
import unittest
import time
from WebDriver.util.HTMLTestRunner import HTMLTestRunner



if __name__ == "__main__":

    testsuite = unittest.TestSuite()

    testsuite.addTest("test_ev_login_language_selection")
    testsuite.addTest("test_ev_login_language_selection_En")
    testsuite.addTest("login_loginVerification")

    filename = '/home/zignage/seleniumTest/ev-SeleniumWebDriver/result'
    fp = file(filename,'login')

    runner = HTMLTestRunner.HTMLTestRunner(
            stream=fp,
            title='Test Result',
            description='Test Report'
            )
 #   runner = unittest.TextTestRunner()
    runner.run(testsuite)

