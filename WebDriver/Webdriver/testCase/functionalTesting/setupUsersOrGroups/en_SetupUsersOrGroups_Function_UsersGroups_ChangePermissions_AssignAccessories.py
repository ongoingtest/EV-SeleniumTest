from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from Webdriver.all_globals import *

#User group permission id:
#Office: userGroup_userGroupOptions173
#Home: userGroup_userGroupOptions16

class EnSetupUsersOrGroupsFunctionUsersGroupsChangePermissionsAssignAccessories(unittest.TestCase):
    def setUp(self):
        gb_setUp(self)
    
    def test_en_setup_users_or_groups_function_users_groups_change_permissions_assign_accessories(self):
        driver = self.driver
        gb_login(self)
        driver.get(self.base_url + "/ev/setupusersorgroups")
        driver.find_element_by_css_selector("div.userGroupColumn > div.mediaScroll").click()
        #driver.find_element_by_id("userGroup_userGroupOptions173").click()
        driver.find_element_by_id("userGroup_userGroupOptions16").click()
        driver.find_element_by_link_text("Assign Accessories").click()
        self.driver.implicitly_wait(30)
        try: self.assertEqual("off", driver.find_element_by_id("assignAccessoriesPermsChkBox").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("off", driver.find_element_by_id("assignAccessoryToProduct").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("off", driver.find_element_by_id("deleteAccessoryAssignment").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("assignAccessoriesPermsChkBox").click()
        self.driver.implicitly_wait(60)
        try: self.assertEqual("on", driver.find_element_by_id("assignAccessoriesPermsChkBox").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("on", driver.find_element_by_id("assignAccessoryToProduct").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("on", driver.find_element_by_id("deleteAccessoryAssignment").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        #driver.find_element_by_id("assignAccessoriesPermsChkBox").click()
        driver.find_element_by_id("deleteAccessoryAssignment").click()
        driver.find_element_by_id("assignAccessoryToProduct").click()
        self.driver.implicitly_wait(60)
        try: self.assertEqual("off", driver.find_element_by_id("assignAccessoriesPermsChkBox").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("off", driver.find_element_by_id("assignAccessoryToProduct").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("off", driver.find_element_by_id("deleteAccessoryAssignment").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("okUserGroupOptions").click()
        driver.refresh()
        #driver.find_element_by_id("userGroup_userGroupOptions173").click()
        driver.find_element_by_id("userGroup_userGroupOptions16").click()
        driver.find_element_by_link_text("Assign Accessories").click()
        self.driver.implicitly_wait(60)
        try: self.assertEqual("off", driver.find_element_by_id("assignAccessoriesPermsChkBox").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("off", driver.find_element_by_id("assignAccessoryToProduct").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("off", driver.find_element_by_id("deleteAccessoryAssignment").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("okUserGroupOptions").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
