#This test suites contains following aspects:
#1)Contention Verification: This is to test if all the elements are in that page and no picture etc missing.
#2)Test the content for 'Help' is complete;
#3)Test the add element function(create media group)
#4)Test the function of modifying the name of mediagroup and media
#5)Test the Drag And Drop function
#6)Test the search function
#7)Please note: *Deleting testing is not been implemented in this test. After testing, please delete the newly created items.
#               *Search function testing is not fully implemented here.
#               *Drag and drop test pass but there might be some problem with the testing case.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
##from WebDriver.testCase.BaseTestCase import BaseTestCase
import unittest, time, re
import HTMLTestRunner
from selenium.webdriver import ActionChains
from Webdriver.all_globals import *


class EnUploadMedia(unittest.TestCase):
    def setUp(self):
        gb_setUp(self)
    
    def test_en_upload_media_content_verification(self):
        driver = self.driver
        gb_login(self)
        driver.get(self.base_url + "/ev/uploadmedia")
        gb_frame(self)
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.corporateLogo"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"Upload Media", driver.title)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"Upload Media", driver.find_element_by_id("pageTitle").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.columnHeader"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"Media", driver.find_element_by_css_selector("span.columnHeaderText").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID, "filterMedia"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID, "sortMedia"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"--Sort--", driver.find_element_by_id("sortMedia").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"Sort by Name", driver.find_element_by_id("sortMedia").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"Sort by Type", driver.find_element_by_id("sortMedia").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"Sort by Size", driver.find_element_by_id("sortMedia").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"Sort by Date", driver.find_element_by_id("sortMedia").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"Assigned", driver.find_element_by_id("sortMedia").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"Unassigned", driver.find_element_by_id("sortMedia").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID, "filterMediaText"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("", driver.find_element_by_css_selector("span.searchIcon").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='mediaSpace']/div[2]/div"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='mediaSpace']/div[2]/span"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.handle"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID, "media_medium184Options"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "#mediaGroupSpace > div.columnHeader > span.columnHeaderText"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"Media Group", driver.find_element_by_css_selector("#mediaGroupSpace > div.columnHeader > span.columnHeaderText").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.createNewMediaGroup.commonButton"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"Create New Media Group", driver.find_element_by_css_selector("div.createNewMediaGroup.commonButton").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("", driver.find_element_by_css_selector("span.newMediaGroupButton.adder").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID, "mediaGroup_mediaGroupDelete179"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID, "mediaGroup_mediaGroup179Options"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.mediaGroupBg.itemContent > div.blockText"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "span.fold"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_xpath("//li[@id='mediaGroup_mediaGroup179']/div/span").click()
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "#mediaGroup_medium178 > div.mediaBg.itemContent > div.handle"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID, "mediaGroup_mediumDelete178"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "#mediaGroup_medium178 > div.mediaBg.itemContent > div.blockText"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID, "footer"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "img"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Help", driver.find_element_by_xpath("//div[@id='footer']/div").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID, "media_mediumDelete184"))
        except AssertionError as e: self.verificationErrors.append(str(e))

    def test_en_upload_media_content_verification_help(self):
        driver = self.driver
        gb_login(self)
        driver.get(self.base_url + "/ev/uploadmedia")
        driver.find_element_by_xpath("//div[@id='footer']/div").click()
        try: self.assertEqual("Help", driver.find_element_by_css_selector("span").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"Upload all types of media by clicking the Create New Media button. Media is uploaded from the local computer only.", driver.find_element_by_id("helpBody").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"Media Groups is an easy way to organize uploaded media.", driver.find_element_by_id("helpBody").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"Media removed from this area will remove the media from products or attract loops.", driver.find_element_by_id("helpBody").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_css_selector("img.exit").click()

    def test_en_upload_media_function_create_media(self):
        driver = self.driver
        gb_login(self)
        driver.get(self.base_url + "/ev/uploadmedia")
        driver.find_element_by_xpath("//div[@id='mediaSpace']/div[2]/div").click()
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        try: self.assertEqual("Upload Media", driver.find_element_by_css_selector("span").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        try: self.assertEqual("Close", driver.find_element_by_css_selector("button.exit.buttonStyle").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_css_selector("button.exit.buttonStyle").click()
        # Upload Media could not be tested with ide

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

    def test_en_upload_media_function_modify_media(self):
        driver = self.driver
        gb_login(self)
        driver.get(self.base_url + "/ev/uploadmedia")
        try: self.assertIn(u"MediaEditTest.avi", driver.find_element_by_id("mediaBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertNotIn(u"MediaSuccess.avi", driver.find_element_by_id("mediaBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("media_medium184Options").click()
        driver.find_element_by_css_selector("input.inputInfo").clear()
        driver.find_element_by_css_selector("input.inputInfo").send_keys("MediaSuccess.avi")
        driver.find_element_by_id("okExistingMedia").click()
        for i in range(60):
            try:
                if u"MediaSuccess.avi" == driver.find_element_by_css_selector("#media_medium184 > div.mediaBg.itemContent > div.blockText").text: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertNotIn(u"MediaEditTest.avi", driver.find_element_by_id("mediaBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"MediaSuccess.avi", driver.find_element_by_id("mediaBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))

        driver.find_element_by_id("media_medium184Options").click()
        driver.find_element_by_css_selector("input.inputInfo").clear()
        driver.find_element_by_css_selector("input.inputInfo").send_keys("MediaEditTest.avi")
        driver.find_element_by_id("okExistingMedia").click()
        for i in range(60):
            try:
                if u"MediaEditTest.avi" == driver.find_element_by_css_selector("#media_medium184 > div.mediaBg.itemContent > div.blockText").text: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertIn(u"MediaEditTest.avi", driver.find_element_by_id("mediaBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertNotIn(u"MediaSuccess.avi", driver.find_element_by_id("mediaBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))

    def test_en_upload_media_function_search(self):
        driver = self.driver
        gb_login(self)
        driver.get(self.base_url + "/ev/uploadmedia")
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.columnHeader"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "span.columnHeaderText"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        try: self.assertTrue(self.is_element_present(By.ID, "filterMediaText"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("", driver.find_element_by_css_selector("span.searchIcon").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("filterMediaText").clear()
        driver.find_element_by_id("filterMediaText").send_keys("av")
        driver.find_element_by_css_selector("span.searchIcon").click()
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        # ERROR: Caught exception [Error: locator strategy either id or name must be specified explicitly.]
        Select(driver.find_element_by_id("sortMedia")).select_by_visible_text("Sort by Name")
        #  sorting is pending 
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    testsuite = unittest.TestSuite()

    testsuite.addTest(EnUploadMedia("test_en_upload_media_content_verification"))
    testsuite.addTest(EnUploadMedia("test_en_upload_media_content_verification_help"))
    testsuite.addTest(EnUploadMedia("test_en_upload_media_function_create_media"))
    testsuite.addTest(EnUploadMedia("test_en_upload_media_function_drag_and_drop"))
    testsuite.addTest(EnUploadMedia("test_en_upload_media_function_media_group"))
    testsuite.addTest(EnUploadMedia("test_en_upload_media_function_modify_media"))
    testsuite.addTest(EnUploadMedia("test_en_upload_media_function_search"))
    filename = gb_filename_prefix+'/UploadMedia.html'
    fp = file(filename,'wb')

    runner = HTMLTestRunner.HTMLTestRunner(
            stream=fp,
            title='Test Result',
            description='Test Report'
            )
 #   runner = unittest.TextTestRunner()
    runner.run(testsuite)
