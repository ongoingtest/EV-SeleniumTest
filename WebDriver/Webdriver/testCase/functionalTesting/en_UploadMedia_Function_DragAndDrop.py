#Drag and drop function test pass, but there might be some problem with the test case. 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from Webdriver.all_globals import *

import unittest, time, re

class EnUploadMediaFunctionDragAndDrop(unittest.TestCase):
    def setUp(self):
        gb_setUp(self)
    
    def test_en_upload_media_function_drag_and_drop(self):
        driver = self.driver
        gb_login(self)
        driver.get(self.base_url + "/ev/uploadmedia")
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "#mediaGroup_mediaGroup604 > div.mediaGroupBg.itemContent > div.blockText"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "#media_medium187 > div.mediaBg.itemContent > div.blockText"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        element = driver.find_element_by_css_selector("#media_medium187 > div.mediaBg.itemContent > div.handle")
        target = driver.find_element_by_css_selector("#mediaGroup_mediaGroup604 > div.mediaGroupBg.itemContent > div.blockText")
        action_chains = ActionChains(driver)
        action_chains.drag_and_drop(element, target);
        #try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "#mediaGroup_mediaGroup604 > div.mediaGroupBg.itemContent > span.fold"))
        #except AssertionError as e: self.verificationErrors.append(str(e))
        #driver.find_element_by_xpath("//li[@id='mediaGroup_mediaGroup220']/div/span").click()
        #driver.find_element_by_id("mediaGroup_mediumDelete187").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
