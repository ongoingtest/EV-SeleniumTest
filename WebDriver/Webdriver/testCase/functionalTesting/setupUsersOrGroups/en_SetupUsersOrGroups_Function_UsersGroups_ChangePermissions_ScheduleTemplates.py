from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class EnSetupUsersOrGroupsFunctionUsersGroupsChangePermissionsScheduleTemplates(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://192.168.1.204:8080/"
        self.verificationErrors = []
    
    def test_en_setup_users_or_groups_function_users_groups_change_permissions_schedule_templates(self):
        driver = self.driver
        driver.get(self.base_url + "/ev/setupusersorgroups")
        driver.find_element_by_id("userGroup_userGroupOptions173").click()
        driver.find_element_by_link_text("Schedule Templates").click()
        try: self.assertEqual("on", driver.find_element_by_id("scheduleTemplatesPermsChkBox").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("on", driver.find_element_by_id("assignTemplateSchedule").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("on", driver.find_element_by_id("removeTemplateSchedule").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("scheduleTemplatesPermsChkBox").click()
        try: self.assertEqual("off", driver.find_element_by_id("scheduleTemplatesPermsChkBox").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("off", driver.find_element_by_id("assignTemplateSchedule").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("off", driver.find_element_by_id("removeTemplateSchedule").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("okUserGroupOptions").click()
        driver.find_element_by_css_selector("button.exit").click()
        driver.find_element_by_css_selector("#multipleUsers > div.buttonStyle > button.exit").click()
        driver.find_element_by_css_selector("#userGroupOptions > #userGroupOptions > div.buttonStyle > button.exit").click()
        driver.refresh()
        driver.find_element_by_id("userGroup_userGroupOptions173").click()
        driver.find_element_by_link_text("Schedule Templates").click()
        try: self.assertEqual("off", driver.find_element_by_id("scheduleTemplatesPermsChkBox").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("off", driver.find_element_by_id("assignTemplateSchedule").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("", driver.find_element_by_id("removeTemplateSchedule").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("scheduleTemplatesPermsChkBox").click()
        try: self.assertEqual("on", driver.find_element_by_id("scheduleTemplatesPermsChkBox").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("on", driver.find_element_by_id("assignTemplateSchedule").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("on", driver.find_element_by_id("removeTemplateSchedule").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("okUserGroupOptions").click()
        driver.find_element_by_css_selector("button.exit").click()
        driver.find_element_by_css_selector("#multipleUsers > div.buttonStyle > button.exit").click()
        driver.find_element_by_css_selector("#userGroupOptions > #userGroupOptions > div.buttonStyle > button.exit").click()
        driver.refresh()
        driver.find_element_by_id("userGroup_userGroupOptions173").click()
        driver.find_element_by_link_text("Schedule Templates").click()
        try: self.assertEqual("on", driver.find_element_by_id("scheduleTemplatesPermsChkBox").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("on", driver.find_element_by_id("assignTemplateSchedule").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("on", driver.find_element_by_id("removeTemplateSchedule").get_attribute("value"))
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
