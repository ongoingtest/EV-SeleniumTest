from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from Webdriver.all_globals import *

class EnSetupUsersOrGroupsFunctionUsersGroupsCreateGroups(unittest.TestCase):
    def setUp(self):
        gb_setUp(self)
    
    def test_en_setup_users_or_groups_function_users_groups_create_groups(self):
        driver = self.driver
        gb_login(self)
        driver.get(self.base_url + "/ev/setupusersorgroups")
        try: self.assertNotIn(u"CreateUserGroup",driver.find_element_by_class_name("userGroupColumn").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_css_selector("div.createNewUserGroup.commonButton").click()
        driver.find_element_by_id("userGroupName").clear()
        driver.find_element_by_id("userGroupName").send_keys("CreateUserGroup")
        driver.find_element_by_id("okUserGroupOptions").click()
        self.driver.implicitly_wait(30)
        try: self.assertIn(u"CreateUserGroup",driver.find_element_by_class_name("userGroupColumn").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.refresh()
        try: self.assertIn(u"CreateUserGroup",driver.find_element_by_class_name("userGroupColumn").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
