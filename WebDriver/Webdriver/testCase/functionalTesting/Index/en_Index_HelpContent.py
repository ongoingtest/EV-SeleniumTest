from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from Webdriver.all_globals import *

class EnIndexHelpContent(unittest.TestCase):
    def setUp(self):
        gb_setUp(self)
    
    def test_en_index_help_content(self):
        driver = self.driver
        gb_login(self)
        driver = self.driver
        driver.get(self.base_url + "/ev/index")
        driver.find_element_by_xpath("//div[@id='footer']/div").click()
        try: self.assertEqual(u"Help", driver.find_element_by_css_selector("span").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"Welcome to EV", driver.find_element_by_id("helpBody").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"The links on the left side of the page help you navigate through the system. Below is a list of the links and a brief description of what they do.", driver.find_element_by_id("helpBody").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"Manage In-Store Display - Modify products on display", driver.find_element_by_id("helpBody").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"Create Reports - Run reports on the log files uploaded by the media players", driver.find_element_by_id("helpBody").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"Upload Media - Where all media files are managed and grouped", driver.find_element_by_id("helpBody").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"Setup Products - Create products and accessories. Also where accessories are assigned to products", driver.find_element_by_id("helpBody").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"Setup Users - Create additional users to log into the system", driver.find_element_by_id("helpBody").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"Setup Stores/Structure - Create the company hierarchy and assign media players to groups", driver.find_element_by_id("helpBody").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"Setup Templates - Design multiple layouts of the products and accessories on display. Also schedule templates to the store hierarchy.", driver.find_element_by_id("helpBody").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"Setup Attract Loops - Compile videos into attract loops and schedule the attract loops to all or specific locations.", driver.find_element_by_id("helpBody").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"View Network Status - View media player health from the Post being coded to the media player being connected to the internet.", driver.find_element_by_id("helpBody").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"Help - View helpful documents for each page of the EV system", driver.find_element_by_id("helpBody").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"Help - View helpful documents for each page of the EV system", driver.find_element_by_id("helpBody").text)
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
    unittest.main()
