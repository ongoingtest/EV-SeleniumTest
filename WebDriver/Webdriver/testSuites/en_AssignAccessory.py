#Test case1: contentVerification
#Test case2: helpe content verification
#Test case3:assign product(Not fully implemented)
#Test case4:search function for accessory and product.
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import HTMLTestRunner
from selenium.webdriver import ActionChains
from Webdriver.all_globals import *

class EnAssignAccessory(unittest.TestCase):
    def setUp(self):
        gb_setUp(self)
    
    def test_en_assign_accessory_content_verification(self):
        driver = self.driver
        gb_login(self)
        driver.get(self.base_url + "/ev/assignaccessories")
        gb_frame(self)
        try: self.assertEqual("Assign Accessories", driver.title)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Assign Accessories", driver.find_element_by_id("pageTitle").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='header']/div[2]/div[2]/a/button"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "span.columnHeaderText"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Accessories", driver.find_element_by_css_selector("span.columnHeaderText").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID, "filterAccessories"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "span.searchIcon"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.productColumn > div.columnHeader > span.columnHeaderText"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Products", driver.find_element_by_css_selector("div.productColumn > div.columnHeader > span.columnHeaderText").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID, "filterProductsType"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"Products", driver.find_element_by_id("filterProductsType").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"Accessories", driver.find_element_by_id("filterProductsType").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID, "filterProducts"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("", driver.find_element_by_css_selector("div.productColumn > div.columnHeader > span.searchIcon").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID, "footer"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "img"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Help", driver.find_element_by_xpath("//div[@id='footer']/div").text)
        except AssertionError as e: self.verificationErrors.append(str(e))

    def test_en_assign_accessory_content_verification_help(self):
        driver = self.driver
        gb_login(self)
        driver.get(self.base_url + "/ev/assignaccessories")
        driver.find_element_by_xpath("//div[@id='footer']/div/span").click()
        try: self.assertTrue(self.is_element_present(By.ID, "title"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Help", driver.find_element_by_css_selector("span").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"Accessories are assigned to product categories. Accessories appear under the Accessories section and can be clicked and dragged from accessories to a product.", driver.find_element_by_id("helpBody").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"Accessories and Products can be searched through the boxes in the headers of each section.", driver.find_element_by_id("helpBody").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_css_selector("img.exit").click()
#The drag and drop function not fully implemented.
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
    def test_en_assign_accessory_function_search(self):
        driver = self.driver
        gb_login(self)
        driver.get(self.base_url + "/ev/assignaccessories")
        try: self.assertIn(u"abcf", driver.find_element_by_id("accessoryBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"abcg", driver.find_element_by_id("accessoryBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"accccd", driver.find_element_by_id("accessoryBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("filterAccessories").clear()
        driver.find_element_by_id("filterAccessories").send_keys("")
        # ERROR: Caught exception [ERROR: Unsupported command [clickAt]]
        driver.find_element_by_id("filterAccessories").clear()
        driver.find_element_by_id("filterAccessories").send_keys("ab")
        driver.find_element_by_css_selector("span.searchIcon").click()
        try: self.assertIn(u"abcf", driver.find_element_by_id("accessoryBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"abcg", driver.find_element_by_id("accessoryBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertNotIn(u"accccd", driver.find_element_by_id("accessoryBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("filterAccessories").clear()
        driver.find_element_by_id("filterAccessories").send_keys("")
        try: self.assertIn(u"abcd", driver.find_element_by_id("categoryBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"acccd", driver.find_element_by_id("categoryBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"test", driver.find_element_by_id("categoryBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("filterProducts").clear()
        driver.find_element_by_id("filterProducts").send_keys("test")
        try: self.assertNotIn(u"abcd", driver.find_element_by_id("categoryBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertNotIn(u"acccd", driver.find_element_by_id("categoryBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"test", driver.find_element_by_id("categoryBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("filterProducts").clear()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    testsuite = unittest.TestSuite()

    testsuite.addTest(EnAssignAccessory("test_en_assign_accessory_content_verification"))
    testsuite.addTest(EnAssignAccessory("test_en_assign_accessory_content_verification_help"))
    testsuite.addTest(EnAssignAccessory("test_en_assign_accessory_function_assign"))
    testsuite.addTest(EnAssignAccessory("test_en_assign_accessory_function_search"))


    filename = gb_filename_prefix+'/AssignAccessory.html'
    fp = file(filename,'wb')

    runner = HTMLTestRunner.HTMLTestRunner(
            stream=fp,
            title='Test Result',
            description='Test Report'
            )
 #   runner = unittest.TextTestRunner()
    runner.run(testsuite)
