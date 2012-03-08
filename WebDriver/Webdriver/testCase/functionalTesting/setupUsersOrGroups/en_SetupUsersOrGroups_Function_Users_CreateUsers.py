from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class EnSetupUsersOrGroupsFunctionUsersCreateUsers(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://192.168.1.204:8080/"
        self.verificationErrors = []
    
    def test_en_setup_users_or_groups_function_users_create_users(self):
        driver = self.driver
        driver.get(self.base_url + "/ev/setupusersorgroups")
        driver.find_element_by_css_selector("div.createNewUser.commonButton").click()
        driver.find_element_by_id("firstName").clear()
        driver.find_element_by_id("firstName").send_keys("testtest")
        driver.find_element_by_id("lastName").clear()
        driver.find_element_by_id("lastName").send_keys("testtest")
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys("testtest@test.com")
        driver.find_element_by_id("userName").clear()
        driver.find_element_by_id("userName").send_keys("testtest")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("test")
        driver.find_element_by_id("repeatPassword").clear()
        driver.find_element_by_id("repeatPassword").send_keys("test")
        driver.find_element_by_id("okSingleUser").click()
        driver.find_element_by_css_selector("button.exit").click()
        driver.find_element_by_css_selector("#multipleUsers > div.buttonStyle > button.exit").click()
        driver.find_element_by_css_selector("#userGroupOptions > #userGroupOptions > div.buttonStyle > button.exit").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
