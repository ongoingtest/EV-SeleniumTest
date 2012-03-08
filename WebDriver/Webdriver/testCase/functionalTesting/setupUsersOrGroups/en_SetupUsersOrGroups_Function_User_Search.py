from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class EnSetupUsersOrGroupsFunctionUsersSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://192.168.1.204:8080/"
        self.verificationErrors = []
    
    def test_en_setup_users_or_groups_function_users_search(self):
        driver = self.driver
        driver.get(self.base_url + "/ev/setupusersorgroups")
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow]]
        driver.find_element_by_id("filterTextUserColumn").clear()
        driver.find_element_by_id("filterTextUserColumn").send_keys("aa")
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        driver.find_element_by_id("filterTextUserColumn").clear()
        driver.find_element_by_id("filterTextUserColumn").send_keys("")
        # search function test result is False Negative, so pending for testing
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
