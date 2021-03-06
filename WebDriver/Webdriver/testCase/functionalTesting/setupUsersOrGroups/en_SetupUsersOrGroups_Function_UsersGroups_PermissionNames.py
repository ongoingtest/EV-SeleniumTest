from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from Webdriver.all_globals import *
class EnSetupUsersOrGroupsFunctionUsersGroupsPermissionNames(unittest.TestCase):
    def setUp(self):
        gb_setUp(self)
    
    def test_en_setup_users_or_groups_function_users_groups_permission_names(self):
        driver = self.driver
        gb_login(self)
        driver.get(self.base_url + "/ev/setupusersorgroups")
        driver.find_element_by_id("userGroup_userGroupOptions173").click()
        try: self.assertEqual("User Group Options", driver.find_element_by_id("title").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"User Group Name",driver.find_element_by_id("userGroupHeader").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"Duplicate User Group",driver.find_element_by_id("duplicateUserGroup").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID, "userGroupName"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.LINK_TEXT, "Permissions"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.LINK_TEXT, "Create Attract Loops"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Create Attract Loops", driver.find_element_by_css_selector("label").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Adjust Order Of Videos", driver.find_element_by_xpath("//label[@id='adjustOrderOfVideos']").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Create Attract Loop", driver.find_element_by_xpath("//label[@id='createAttractLoop']").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID, "userGroup_userGroupOptions173"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Delete Video Assignments", driver.find_element_by_xpath("//label[@id='deleteVideoAssignments']").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Schedule Templates", driver.find_element_by_link_text("Schedule Templates").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_link_text("Schedule Templates").click()
        try: self.assertEqual("Schedule Templates", driver.find_element_by_css_selector("#scheduleTemplatesPerms > div.boldText > label").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Assign Template Schedule", driver.find_element_by_xpath("//label[@id='assignTemplateSchedule']").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Remove Template Schedule", driver.find_element_by_xpath("//label[@id='removeTemplateSchedule']").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_link_text("Template Styles").click()
        try: self.assertEqual("Template Styles", driver.find_element_by_css_selector("#templateStylesPerms > div.boldText > label").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Create Templates", driver.find_element_by_xpath("//label[@id='createTemplates']").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Delete Templates", driver.find_element_by_xpath("//label[@id='deleteTemplates']").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Rename Templates", driver.find_element_by_xpath("//label[@id='renameTemplates']").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Edit Text And Media Background", driver.find_element_by_xpath("//label[@id='editTextAndMediaBackground']").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Edit Text Color", driver.find_element_by_xpath("//label[@id='editTextColor']").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Edit Logo", driver.find_element_by_xpath("//label[@id='editLogo']").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Move And Resize Text Regions", driver.find_element_by_xpath("//label[@id='moveAndResizeTextRegions']").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Move And Resize Media Regions", driver.find_element_by_xpath("//label[@id='moveAndResizeMediaRegions']").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_link_text("Create Products").click()
        try: self.assertEqual("Create Products", driver.find_element_by_link_text("Create Products").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Create Products", driver.find_element_by_css_selector("#createProductsPerms > div.boldText > label").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Create New Products", driver.find_element_by_xpath("//label[@id='createNewProducts']").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Delete Products", driver.find_element_by_xpath("//label[@id='deleteProducts']").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Add Media To Product", driver.find_element_by_xpath("//label[@id='addMediaToProduct']").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Adjust Product Price", driver.find_element_by_xpath("//label[@id='adjustProductPrice']").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Adjust Product Model", driver.find_element_by_xpath("//label[@id='adjustProductModel']").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Adjust Product S K U", driver.find_element_by_xpath("//label[@id='adjustProductSKU']").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Add Product Description", driver.find_element_by_xpath("//label[@id='addProductDescription']").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Add Additional Text", driver.find_element_by_xpath("//label[@id='addAdditionalText']").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Adjust Keyword Assignments", driver.find_element_by_xpath("//label[@id='adjustKeywordAssignments']").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_link_text("Media Manager").click()
        try: self.assertEqual("Media Manager", driver.find_element_by_link_text("Media Manager").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Media Manager", driver.find_element_by_css_selector("#mediaManagerPerms > div.boldText > label").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Upload New Media", driver.find_element_by_xpath("//label[@id='uploadNewMedia']").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Delete Media", driver.find_element_by_xpath("//label[@id='deleteMedia']").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_link_text("Group Media Players").click()
        try: self.assertEqual("Group Media Players", driver.find_element_by_link_text("Group Media Players").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Group Media Players", driver.find_element_by_css_selector("#groupMediaPlayersPerms > div.boldText > label").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Assign Devices To Groups", driver.find_element_by_xpath("//label[@id='assignDevicesToGroups']").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Rename Devices", driver.find_element_by_xpath("//label[@id='renameDevices']").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_link_text("Network Manager").click()
        try: self.assertEqual("Network Manager", driver.find_element_by_link_text("Network Manager").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Network Manager", driver.find_element_by_css_selector("#networkManagerPerms > div.boldText > label").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Reset Media Player Password", driver.find_element_by_xpath("//label[@id='resetMediaPlayerPassword']").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Lock Unlock Device", driver.find_element_by_xpath("//label[@id='lockUnlockDevice']").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_link_text("Assign Accessories").click()
        try: self.assertEqual("Assign Accessories", driver.find_element_by_link_text("Assign Accessories").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Assign Accessories", driver.find_element_by_css_selector("#assignAccessoriesPerms > div.boldText > label").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Assign Accessory To Product", driver.find_element_by_xpath("//label[@id='assignAccessoryToProduct']").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Delete Accessory Assignment", driver.find_element_by_xpath("//label[@id='deleteAccessoryAssignment']").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_link_text("Store Hierarchy").click()
        try: self.assertEqual("Store Hierarchy", driver.find_element_by_link_text("Store Hierarchy").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Create Stores", driver.find_element_by_xpath("//label[@id='createStores']").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Create Store Groups", driver.find_element_by_xpath("//label[@id='createStoreGroups']").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Create Companies", driver.find_element_by_xpath("//label[@id='createCompanies']").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Adjust Hierarchy", driver.find_element_by_xpath("//label[@id='adjustHierarchy']").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Rename Items In Hierarchy", driver.find_element_by_xpath("//label[@id='renameItemsInHierarchy']").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Delete Items In Hierarchy", driver.find_element_by_xpath("//label[@id='deleteItemsInHierarchy']").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_link_text("Assign Permissions").click()
        try: self.assertEqual("Assign Permissions", driver.find_element_by_link_text("Assign Permissions").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Assign Permissions", driver.find_element_by_css_selector("#assignPermissionsPerms > div.boldText > label").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Create New Users", driver.find_element_by_xpath("//label[@id='createNewUsers']").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Edit User Information", driver.find_element_by_xpath("//label[@id='editUserInformation']").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Delete Users", driver.find_element_by_xpath("//label[@id='deleteUsers']").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Create User Groups", driver.find_element_by_xpath("//label[@id='createUserGroups']").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Edit User Groups", driver.find_element_by_xpath("//label[@id='editUserGroups']").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Delete User Groups", driver.find_element_by_xpath("//label[@id='deleteUserGroups']").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Assign User Group To Stores", driver.find_element_by_xpath("//label[@id='assignVisibilizersToBaseDeviceContainers']").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_link_text("Create Reports").click()
        try: self.assertEqual("Create Reports", driver.find_element_by_link_text("Create Reports").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Create Reports", driver.find_element_by_css_selector("#createReportsPerms > div.boldText > label").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("View Basic Reports", driver.find_element_by_xpath("//label[@id='viewReports']").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("View Advanced Reports", driver.find_element_by_xpath("//label[@id='viewAdvancedReports']").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_link_text("Schedule Loops").click()
        try: self.assertEqual("Schedule Loops", driver.find_element_by_link_text("Schedule Loops").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Schedule Loops", driver.find_element_by_css_selector("#scheduleAttractLoopsPerms > div.boldText > label").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Assign Loop Schedule", driver.find_element_by_xpath("//label[@id='assignLoopSchedule']").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Remove Loop Schedule", driver.find_element_by_xpath("//label[@id='removeLoopSchedule']").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Edit Start Date", driver.find_element_by_xpath("//label[@id='editStartDate']").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Edit End Date", driver.find_element_by_xpath("//label[@id='editEndDate']").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Edit Start Time", driver.find_element_by_xpath("//label[@id='editStartTime']").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Edit End Time", driver.find_element_by_xpath("//label[@id='editEndTime']").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Edit Days Of Week", driver.find_element_by_xpath("//label[@id='editDaysOfWeek']").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_link_text("Classify Products").click()
        try: self.assertEqual("Classify Products", driver.find_element_by_link_text("Classify Products").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Classify Products", driver.find_element_by_css_selector("#classifyProductsPerms > div.boldText > label").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Add Product Category Subcategory", driver.find_element_by_xpath("//label[@id='addProductCSc']").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Delete Product Category Subcategory", driver.find_element_by_xpath("//label[@id='deleteProductCSc']").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Edit Product Category Subcategory", driver.find_element_by_xpath("//label[@id='editProductCSc']").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Add Product Keyword", driver.find_element_by_xpath("//label[@id='addProductKeyword']").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Delete Product Keyword", driver.find_element_by_xpath("//label[@id='deleteProductKeyword']").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Cancel", driver.find_element_by_css_selector("button.exit").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "button.exit"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Save", driver.find_element_by_id("okUserGroupOptions").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID, "okUserGroupOptions"))
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
