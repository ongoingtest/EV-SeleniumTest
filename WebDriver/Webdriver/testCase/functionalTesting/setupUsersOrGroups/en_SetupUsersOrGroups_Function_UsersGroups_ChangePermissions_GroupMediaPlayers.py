from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class EnSetupUsersOrGroupsFunctionUsersGroupsChangePermissionsGroupMediaPlayers(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://192.168.1.204:8080/"
        self.verificationErrors = []
    
    def test_en_setup_users_or_groups_function_users_groups_change_permissions_group_media_players(self):
        driver = self.driver
        driver.get(self.base_url + "/ev/setupusersorgroups")
        driver.find_element_by_id("userGroup_userGroupOptions173").click()
        driver.find_element_by_link_text("Group Media Players").click()
        driver.find_element_by_id("title").click()
        try: self.assertEqual("on", driver.find_element_by_id("groupMediaPlayersPermsChkBox").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("on", driver.find_element_by_id("assignDevicesToGroups").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("on", driver.find_element_by_id("renameDevices").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("groupMediaPlayersPermsChkBox").click()
        try: self.assertEqual("off", driver.find_element_by_id("groupMediaPlayersPermsChkBox").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("off", driver.find_element_by_id("assignDevicesToGroups").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("off", driver.find_element_by_id("renameDevices").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("renameDevices").click()
        driver.find_element_by_id("assignDevicesToGroups").click()
        try: self.assertEqual("on", driver.find_element_by_id("renameDevices").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("on", driver.find_element_by_id("assignDevicesToGroups").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("on", driver.find_element_by_id("groupMediaPlayersPermsChkBox").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("okUserGroupOptions").click()
        driver.find_element_by_css_selector("button.exit").click()
        driver.find_element_by_css_selector("#multipleUsers > div.buttonStyle > button.exit").click()
        driver.find_element_by_css_selector("#userGroupOptions > #userGroupOptions > div.buttonStyle > button.exit").click()
        driver.refresh()
        driver.find_element_by_id("userGroup_userGroupOptions173").click()
        driver.find_element_by_link_text("Group Media Players").click()
        try: self.assertEqual("on", driver.find_element_by_id("groupMediaPlayersPermsChkBox").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("on", driver.find_element_by_id("assignDevicesToGroups").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("on", driver.find_element_by_id("renameDevices").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
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
