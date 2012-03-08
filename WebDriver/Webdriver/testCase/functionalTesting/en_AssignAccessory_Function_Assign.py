#Drag and drop test is not fully implemented yet.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from selenium.webdriver import ActionChains
from Webdriver.all_globals import *

class EnAssignAccessoryFunctionAssign(unittest.TestCase):
    def setUp(self):
        gb_setUp(self)
    
    def test_en_assign_accessory_function_assign(self):
        driver = self.driver
        gb_login(self)
        driver.get(self.base_url + "/ev/assignaccessories")
        driver.find_element_by_xpath("//li[@id='categories_category517']/div/span").click()
        driver.find_element_by_xpath("//li[@id='accessories_category514']/div/span").click()
        try: self.assertTrue(self.is_element_present(By.XPATH, "//li[@id='accessories_accessory636']/div/div"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.XPATH, "//li[@id='products_product637']/div/div"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        element = driver.find_element_by_xpath("//li[@id='accessories_accessory636']/div/div")
        target = driver.find_element_by_xpath("//li[@id='products_product637']/div/div")
        action_chains = ActionChains(driver)
        action_chains.drag_and_drop(element, target);

        #try: self.assertTrue(self.is_element_present(By.XPATH, "//li[@id='products_product637']/div/span"))
        #except AssertionError as e: self.verificationErrors.append(str(e))
        #driver.find_element_by_xpath("//li[@id='products_product637']/div/span").click()
        #try: self.assertIn(u"DragAcc1", driver.find_element_by_id("categoryBrowser").text)
        #except AssertionError as e: self.verificationErrors.append(str(e))
        #driver.find_element_by_css_selector("#product637_accessory636 > div.itemContent.accessoryBg > span.unassign").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
