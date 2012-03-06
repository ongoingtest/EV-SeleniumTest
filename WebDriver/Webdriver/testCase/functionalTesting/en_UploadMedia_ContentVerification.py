from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
##from WebDriver.testCase.BaseTestCase import BaseTestCase
import unittest, time, re
from Webdriver.all_globals import *

class EnUploadMediaContentVerification(unittest.TestCase):
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
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
