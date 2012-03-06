#This one should be tested together with test case 'en_AddPostsToDisplay_SelectADevice'
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
import HTMLTestRunner
from Webdriver.all_globals import *

class AddPostsToDisplay(unittest.TestCase):
    def setUp(self):
        gb_setUp(self)
    
    def test_en_add_posts_to_display_content_verification(self):
        driver = self.driver
        gb_login(self)
        driver.get(self.base_url + "/ev/addpoststodisplay")
        gb_frame(self)
        driver.find_element_by_css_selector("span.bigDownArrow").click()
        driver.find_element_by_xpath("//li[@id='hierarchy_storeGroup199']/div/span").click()
        driver.find_element_by_xpath("//li[@id='hierarchy_store200']/div/span").click()
        driver.find_element_by_xpath("//li[@id='deviceContainersCol_device28']/div/div").click()
        driver.find_element_by_css_selector("span.bigDownArrow").click()
        try: self.assertEqual("Add Posts To Display", driver.title)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID, "pageTitle"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("", driver.find_element_by_css_selector("div.corporateLogo").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID, "welcomeTitle"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Logout", driver.find_element_by_xpath("//div[@id='header']/div[2]/div[2]/a/button").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Choose Media Player", driver.find_element_by_css_selector("span.deviceHeader").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Displays", driver.find_element_by_xpath("//div[@id='body']/div[2]/div[3]/div[2]/div").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID, "footer"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Help", driver.find_element_by_xpath("//div[@id='footer']/div").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "img"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Display", driver.find_element_by_css_selector("#displaysCol_display4 > div.displayContent > span").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Identify Display", driver.find_element_by_css_selector("#displaysCol_display4 > button.identifyDisplay").text)
        except AssertionError as e: self.verificationErrors.append(str(e))

    def test_en_add_posts_to_display_help_content(self):
        driver = self.driver
        gb_login(self)
        driver.get(self.base_url + "/ev/addpoststodisplay")
        driver.find_element_by_xpath("//div[@id='footer']/div").click()
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "span"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"In Non-touchscreen media players with multiple displays attached, this section allows posts to be assigned to specific displays.", driver.find_element_by_id("helpBody").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"Select a device from the Choose Media Player. All DIB(s) and all Displays attached to the media player will appear. Click on the post and drag to a display that you want the product information to be displayed on.", driver.find_element_by_id("helpBody").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_css_selector("img.exit").click()
        driver.refresh()
        
    def test_en_add_posts_to_display_select_a_device(self):
        driver = self.driver
        gb_login(self)
        driver.get(self.base_url + "/ev/addpoststodisplay")
        driver.find_element_by_css_selector("span.bigDownArrow").click()
        driver.find_element_by_xpath("//li[@id='hierarchy_storeGroup199']/div/span").click()
        driver.find_element_by_xpath("//li[@id='hierarchy_store200']/div/span").click()
        driver.find_element_by_xpath("//li[@id='deviceContainersCol_device28']/div/div").click()
        driver.find_element_by_css_selector("span.bigDownArrow").click()

    def test_en_add_posts_to_display_identify_device(self):
        driver = self.driver
        gb_login(self)
        driver.get(self.base_url + "/ev/addpoststodisplay")
        driver.find_element_by_css_selector("span.bigDownArrow").click()
        driver.find_element_by_xpath("//li[@id='hierarchy_storeGroup199']/div/span").click()
        driver.find_element_by_xpath("//li[@id='hierarchy_store200']/div/span").click()
        driver.find_element_by_xpath("//li[@id='deviceContainersCol_device28']/div/div").click()
        driver.find_element_by_css_selector("span.bigDownArrow").click()
        driver.find_element_by_css_selector("#displaysCol_display4 > button.identifyDisplay").click()
        driver.find_element_by_id("pop-up").click()
        try: self.assertEqual("Identifying Display", driver.find_element_by_css_selector("span").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Identifying Display", driver.find_element_by_css_selector("#idDisplayInner > div > span").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID, "identifyDisplayProgressBar"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_css_selector("img.exit").click()

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    testsuite = unittest.TestSuite()

    testsuite.addTest(AddPostsToDisplay("test_en_add_posts_to_display_content_verification"))
    testsuite.addTest(AddPostsToDisplay("test_en_add_posts_to_display_help_content"))
    testsuite.addTest(AddPostsToDisplay("test_en_add_posts_to_display_select_a_device"))
    testsuite.addTest(AddPostsToDisplay("test_en_add_posts_to_display_identify_device"))


    filename = '/home/zignage/seleniumTest/WebDriver/result/AddPostsToDisplay.html'
    fp = file(filename,'wb')

    runner = HTMLTestRunner.HTMLTestRunner(
            stream=fp,
            title='Test Result',
            description='Test Report'
            )
 #   runner = unittest.TextTestRunner()
    runner.run(testsuite)
