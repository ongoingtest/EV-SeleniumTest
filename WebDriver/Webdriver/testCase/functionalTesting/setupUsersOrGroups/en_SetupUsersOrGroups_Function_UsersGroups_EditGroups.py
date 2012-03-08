from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class EnSetupUsersOrGroupsFunctionUsersGroupsEditGroups(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://192.168.1.204:8080/"
        self.verificationErrors = []
    
    def test_en_setup_users_or_groups_function_users_groups_edit_groups(self):
        driver = self.driver
        driver.get(self.base_url + "/ev/setupusersorgroups")
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        driver.find_element_by_id("userGroup_userGroupOptions179").click()
        driver.find_element_by_id("userGroupName").clear()
        driver.find_element_by_id("userGroupName").send_keys("ModifiedUserGroup")
        driver.find_element_by_id("okUserGroupOptions").click()
        driver.find_element_by_css_selector("button.exit").click()
        driver.find_element_by_css_selector("#multipleUsers > div.buttonStyle > button.exit").click()
        driver.find_element_by_css_selector("#userGroupOptions > #userGroupOptions > div.buttonStyle > button.exit").click()
        driver.refresh()
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        driver.find_element_by_id("userGroup_userGroupOptions179").click()
        driver.find_element_by_id("title").click()
        driver.find_element_by_id("userGroupName").clear()
        driver.find_element_by_id("userGroupName").send_keys("EditUserGroup")
        driver.find_element_by_id("okUserGroupOptions").click()
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
