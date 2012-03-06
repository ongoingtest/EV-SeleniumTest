#Need to delete the media group 'CreateMediaGroup' manually after testing.
# coding: utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from Webdriver.all_globals import *

class EnUploadMediaFunctionMediaGroup(unittest.TestCase):
    def setUp(self):
        gb_setUp(self)
    
    def test_en_upload_media_function_media_group(self):
        driver = self.driver
        gb_login(self)
        driver.get(self.base_url + "/ev/uploadmedia")
        #try: self.assertEqual(u"ModifyMediaGroup", driver.find_element_by_css_selector("#mediaGroup_mediaGroup552 > div.mediaGroupBg.itemContent > div.blockText").text)
       # except AssertionError as e: self.verificationErrors.append(str(e))
        self.driver.implicitly_wait(30)
        try: self.assertNotIn(u"CreateMediaGroup", driver.find_element_by_id("mediaGroupBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertNotIn(u"ModifySuccess", driver.find_element_by_id("mediaGroupBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"ModifyMediaGroup", driver.find_element_by_id("mediaGroupBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_css_selector("div.createNewMediaGroup.commonButton").click()
        driver.find_element_by_id("mediaGroupName").clear()
        driver.find_element_by_id("mediaGroupName").send_keys("CreateMediaGroup")
        driver.find_element_by_id("mediaGroupPopupOK").click()
        driver.get(self.base_url + "/ev/uploadmedia")
        driver.find_element_by_id("mediaGroup_mediaGroup552Options").click()
        driver.find_element_by_id("mediaGroupName").clear()
        driver.find_element_by_id("mediaGroupName").send_keys("ModifySuccess")
        driver.find_element_by_id("mediaGroupPopupOK").click()
        for i in range(60):
            try:
                if u"ModifySuccess" == driver.find_element_by_css_selector("#mediaGroup_mediaGroup552 > div.mediaGroupBg.itemContent > div.blockText").text: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertIn(u"CreateMediaGroup", driver.find_element_by_id("mediaGroupBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"ModifySuccess", driver.find_element_by_id("mediaGroupBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertNotIn(u"ModifyMediaGroup", driver.find_element_by_id("mediaGroupBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.get(self.base_url + "/ev/uploadmedia")
        driver.find_element_by_id("mediaGroup_mediaGroup552Options").click()
        driver.find_element_by_id("mediaGroupName").clear()
        driver.find_element_by_id("mediaGroupName").send_keys("ModifyMediaGroup")
        driver.find_element_by_id("mediaGroupPopupOK").click()
        #driver.find_element_by_title("CreateMediaGroup")

        
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
