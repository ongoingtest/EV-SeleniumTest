from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from Webdriver.all_globals import *
class EnSetupUsersOrGroupsContentVerification(unittest.TestCase):
    def setUp(self):
        gb_setUp(self)

# Before Test: Please delete user  'testtest@test.com', user group 'test123456' and 'test userGroup2123456'
    def test_en_setup_users_or_groups_content_verification(self):
        driver = self.driver
        gb_login(self)
        driver.get(self.base_url + "/ev/setupusersorgroups")
        gb_frame(self)
        try: self.assertEqual("Setup Users Or Groups", driver.title)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Setup Users Or Groups", driver.find_element_by_id("pageTitle").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='header']/div[2]/div[2]/a/button"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "span.columnHeaderText"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Users", driver.find_element_by_css_selector("span.columnHeaderText").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID, "filterUserColumn"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID, "filterTextUserColumn"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "span.searchIcon"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.createNewUser.commonButton"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "span.newUserButton.adder"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID, "users_userDelete149"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID, "users_userOptions149"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID, "users_userDelete149"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.userGroupColumn > div.columnHeader > span.columnHeaderText"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("User Groups", driver.find_element_by_css_selector("div.userGroupColumn > div.columnHeader > span.columnHeaderText").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID, "filterUserGroupColumn"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"User Name\nFirst Name\nLast Name", driver.find_element_by_id("filterUserColumn").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"First Name", driver.find_element_by_id("filterUserColumn").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"Last Name", driver.find_element_by_id("filterUserColumn").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID, "filterTextUserGroupColumn"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("", driver.find_element_by_css_selector("div.userGroupColumn > div.columnHeader > span.searchIcon").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.createNewUserGroup.commonButton"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "span.newUserGroupButton.adder"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Create New User", driver.find_element_by_css_selector("div.createNewUser.commonButton").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Create New User Group", driver.find_element_by_css_selector("div.createNewUserGroup.commonButton").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID, "userGroup_userGroupOptions150"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID, "userGroup_userGroupDelete150"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "#storeGroupsSpace > div.columnHeader > span.columnHeaderText"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Store Hierarchy", driver.find_element_by_css_selector("#storeGroupsSpace > div.columnHeader > span.columnHeaderText").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID, "filterStoreGroupColumn"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"User Name", driver.find_element_by_id("filterUserGroupColumn").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"First Name", driver.find_element_by_id("filterUserGroupColumn").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"Last Name", driver.find_element_by_id("filterUserGroupColumn").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"UserGroup Name", driver.find_element_by_id("filterUserGroupColumn").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID, "filterTextStoreGroupColumn"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("", driver.find_element_by_css_selector("#storeGroupsSpace > div.columnHeader > span.searchIcon").text)
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
