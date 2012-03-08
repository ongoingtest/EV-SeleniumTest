from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class EnSetupUsersOrGroupsFunctionUsersEditUsers(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://192.168.1.204:8080/"
        self.verificationErrors = []
    
    def test_en_setup_users_or_groups_function_users_edit_users(self):
        driver = self.driver
        driver.get(self.base_url + "/ev/setupusersorgroups")
        driver.find_element_by_id("users_userOptions149").click()
        driver.find_element_by_id("firstName").clear()
        driver.find_element_by_id("firstName").send_keys("ccz")
        driver.find_element_by_id("lastName").clear()
        driver.find_element_by_id("lastName").send_keys("ddz")
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys("ccz@gmail.com")
        driver.find_element_by_id("userName").clear()
        driver.find_element_by_id("userName").send_keys("cdz")
        driver.find_element_by_id("okSingleUser").click()
        driver.find_element_by_css_selector("button.exit").click()
        driver.find_element_by_css_selector("#multipleUsers > div.buttonStyle > button.exit").click()
        driver.find_element_by_css_selector("#userGroupOptions > #userGroupOptions > div.buttonStyle > button.exit").click()
        driver.find_element_by_id("users_userOptions149").click()
        driver.find_element_by_id("firstName").clear()
        driver.find_element_by_id("firstName").send_keys("Modify")
        driver.find_element_by_id("lastName").clear()
        driver.find_element_by_id("lastName").send_keys("Modify")
        driver.find_element_by_id("userName").clear()
        driver.find_element_by_id("userName").send_keys("ModifyUser")
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys("mm@gmail.com")
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
