# coding: utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
import HTMLTestRunner
from all_globals import *
from Webdriver.testCase.login import languageSelection as loginCase1
from Webdriver.testCase.login import languageSelection_en as loginCase2
from Webdriver.testCase.login import languageSelection_de as loginCase3
#from Webdriver.testCase.login import languageSelection_es as loginCase4
#from Webdriver.testCase.login import languageSelection_fr as loginCase5
#from Webdriver.testCase.login import *

class LoginLanguageSelection(loginCase1.LanguageSelection,loginCase2.LoginLanguageSelectionEn,loginCase3.LoginLanguageSelectionDe):
    def setUp(self):
        gb_setUp(self)
    
    def test_login_language_selection(self):
        loginCase1.LanguageSelection.test_login_language_selection(self)

#Verify Element for different languages.        
#Verify Element for en
    def test_login_language_selection_en(self):
        loginCase2.LoginLanguageSelectionEn.test_login_language_selection_en(self)

#Verify Element for de
    def test_login_language_selection_de(self):
        loginCase3.LoginLanguageSelectionDe.test_login_language_selection_de(self)

#Verify Element for es
    def test_login_language_selection_es(self):
 #       loginCase4.LoginLanguageSelectionEs.test_login_language_selection_es(self)
        driver = self.driver
        driver.get(self.base_url + "/ev/login")
        Select(driver.find_element_by_css_selector("select.languageSelection")).select_by_visible_text("Español")
        #driver.implicitly_wait(30)
        for i in range(60):
            try:
                if u"Página de Login" == driver.title: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual(u"Página de Login", driver.title)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"Bienvenido", driver.find_element_by_class_name("txtWelcome").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("", driver.find_element_by_id("form.login").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("", driver.find_element_by_id("form.password").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"OK", driver.find_element_by_css_selector("span.commonButton.login_ok").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"¿Olvido su ID?", driver.find_element_by_id("txtForgotID").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"¿Olvido su clave?", driver.find_element_by_id("txtForgotPassword").text)
        except AssertionError as e: self.verificationErrors.append(str(e))

#Verify Element for fr
    def test_login_language_selection_fr(self):
 #       loginCase5.LoginLanguageSelectionFr.test_login_language_selection_fr(self)
        driver = self.driver
        #driver.refresh
        driver.get(self.base_url + "/ev/login")
        self.driver.implicitly_wait(30)
        Select(driver.find_element_by_css_selector("select.languageSelection")).select_by_visible_text("Français")
        driver.implicitly_wait(30)
        for i in range(60):
            try:
                if u"Page de connexion" == driver.title: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual(u"Page de connexion", driver.title)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"Bienvenue", driver.find_element_by_class_name("txtWelcome").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("", driver.find_element_by_id("form.login").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("", driver.find_element_by_id("form.password").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"OK", driver.find_element_by_css_selector("span.commonButton.login_ok").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"Oublié votre ID?", driver.find_element_by_id("txtForgotID").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"Oublié votre mot de passe?", driver.find_element_by_id("txtForgotPassword").text)
        except AssertionError as e: self.verificationErrors.append(str(e))

#Verify Element for it
    def test_login_language_selection_it(self):
        driver = self.driver
        #driver.refresh
        driver.get(self.base_url + "/ev/login")
        self.driver.implicitly_wait(30)
        Select(driver.find_element_by_css_selector("select.languageSelection")).select_by_visible_text("Italiano")
        driver.implicitly_wait(30)
        for i in range(60):
            try:
                if u"Pagina di Login" == driver.title: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual(u"Pagina di Login", driver.title)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"Benvenuto", driver.find_element_by_class_name("txtWelcome").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("", driver.find_element_by_id("form.login").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("", driver.find_element_by_id("form.password").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"OK", driver.find_element_by_css_selector("span.commonButton.login_ok").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"Hai dimenticato il tuo ID?", driver.find_element_by_id("txtForgotID").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"Hai dimenticato la tua Password?", driver.find_element_by_id("txtForgotPassword").text)
        except AssertionError as e: self.verificationErrors.append(str(e))

#Verify Element for ja
    def test_login_language_selection_ja(self):
        driver = self.driver
        driver.get(self.base_url + "/ev/login")
        Select(driver.find_element_by_css_selector("select.languageSelection")).select_by_visible_text("日本語")
        driver.implicitly_wait(30)
        for i in range(60):
            try:
                if u"ログインページ" == driver.title: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual(u"ログインページ", driver.title)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"ようこそ", driver.find_element_by_class_name("txtWelcome").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("", driver.find_element_by_id("form.login").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("", driver.find_element_by_id("form.password").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"OK", driver.find_element_by_css_selector("span.commonButton.login_ok").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"IDを忘れましたか？", driver.find_element_by_id("txtForgotID").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"パスワードを忘れましたか？", driver.find_element_by_id("txtForgotPassword").text)
        except AssertionError as e: self.verificationErrors.append(str(e))

#Verify Element for nl
    def test_login_language_selection_nl(self):
        driver = self.driver
        driver.get(self.base_url + "/ev/login")
        Select(driver.find_element_by_css_selector("select.languageSelection")).select_by_visible_text("Nederlands")
        driver.implicitly_wait(30)
        for i in range(60):
            try:
                if u"Login Pagina" == driver.title: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual(u"Login Pagina", driver.title)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"Welkom", driver.find_element_by_class_name("txtWelcome").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("", driver.find_element_by_id("form.login").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("", driver.find_element_by_id("form.password").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"OK", driver.find_element_by_css_selector("span.commonButton.login_ok").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"Je ID vergeten?", driver.find_element_by_id("txtForgotID").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"Je wachtwoord vergeten?", driver.find_element_by_id("txtForgotPassword").text)
        except AssertionError as e: self.verificationErrors.append(str(e))

#Verify Element for pt
    def test_login_language_selection_pt(self):
        driver = self.driver
        driver.get(self.base_url + "/ev/login")
        Select(driver.find_element_by_css_selector("select.languageSelection")).select_by_visible_text("Português")
        driver.implicitly_wait(30)
        for i in range(60):
            try:
                if u"Página de Login" == driver.title: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual(u"Página de Login", driver.title)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"Seja bem-vindo", driver.find_element_by_class_name("txtWelcome").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("", driver.find_element_by_id("form.login").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("", driver.find_element_by_id("form.password").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"Aprovar", driver.find_element_by_css_selector("span.commonButton.login_ok").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"Esqueceu sua ID?", driver.find_element_by_id("txtForgotID").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"Esqueceu sua Senha?", driver.find_element_by_id("txtForgotPassword").text)
        except AssertionError as e: self.verificationErrors.append(str(e))

#Verify Element for ru
    def test_login_language_selection_ru(self):
        driver = self.driver
        driver.get(self.base_url + "/ev/login")
        Select(driver.find_element_by_css_selector("select.languageSelection")).select_by_visible_text("Pусский")
        driver.implicitly_wait(30)
        for i in range(60):
            try:
                if u"Страница входа" == driver.title: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual(u"Страница входа", driver.title)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"Добро пожаловать", driver.find_element_by_class_name("txtWelcome").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("", driver.find_element_by_id("form.login").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("", driver.find_element_by_id("form.password").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"Ок", driver.find_element_by_css_selector("span.commonButton.login_ok").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"Забыли ваш ID?", driver.find_element_by_id("txtForgotID").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"Забыли ваш пароль?", driver.find_element_by_id("txtForgotPassword").text)
        except AssertionError as e: self.verificationErrors.append(str(e))

#Verify Element for tr
    def test_login_language_selection_tr(self):
        driver = self.driver
        driver.get(self.base_url + "/ev/login")
        Select(driver.find_element_by_css_selector("select.languageSelection")).select_by_visible_text("Türkçe")
        driver.implicitly_wait(30)
        for i in range(60):
            try:
                if u"Giriþ Sayfasý" == driver.title: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual(u"Giriþ Sayfasý", driver.title)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"Hoþgeldiniz", driver.find_element_by_class_name("txtWelcome").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("", driver.find_element_by_id("form.login").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("", driver.find_element_by_id("form.password").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"Tamam", driver.find_element_by_css_selector("span.commonButton.login_ok").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"Kullanýcý Kimliðinizi mý unuttunuz?", driver.find_element_by_id("txtForgotID").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"Þifrenizi mi unuttunuz?", driver.find_element_by_id("txtForgotPassword").text)
        except AssertionError as e: self.verificationErrors.append(str(e))

#Verify Element for zh
    def test_login_language_selection_zh(self):
        driver = self.driver
        driver.get(self.base_url + "/ev/login")
        Select(driver.find_element_by_css_selector("select.languageSelection")).select_by_visible_text("中文")
        driver.implicitly_wait(30)
        for i in range(60):
            try:
                if u"登录页面" == driver.title: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual(u"登录页面", driver.title)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"欢迎", driver.find_element_by_class_name("txtWelcome").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("", driver.find_element_by_id("form.login").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("", driver.find_element_by_id("form.password").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"确定", driver.find_element_by_css_selector("span.commonButton.login_ok").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"忘记 ID ?", driver.find_element_by_id("txtForgotID").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"忘记密码?", driver.find_element_by_id("txtForgotPassword").text)
        except AssertionError as e: self.verificationErrors.append(str(e))




    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    testsuite = unittest.TestSuite()

    testsuite.addTest(LoginLanguageSelection("test_login_language_selection"))
    testsuite.addTest(LoginLanguageSelection("test_login_language_selection_en"))
    testsuite.addTest(LoginLanguageSelection("test_login_language_selection_de"))
    testsuite.addTest(LoginLanguageSelection("test_login_language_selection_es"))
    testsuite.addTest(LoginLanguageSelection("test_login_language_selection_fr"))
    testsuite.addTest(LoginLanguageSelection("test_login_language_selection_it"))
    testsuite.addTest(LoginLanguageSelection("test_login_language_selection_ja"))
    testsuite.addTest(LoginLanguageSelection("test_login_language_selection_nl"))
    testsuite.addTest(LoginLanguageSelection("test_login_language_selection_pt"))
    testsuite.addTest(LoginLanguageSelection("test_login_language_selection_ru"))
    testsuite.addTest(LoginLanguageSelection("test_login_language_selection_tr"))
    testsuite.addTest(LoginLanguageSelection("test_login_language_selection_zh"))

    filename = gb_filename_prefix+'/languageSelection.html'
    fp = file(filename,'wb')

    runner = HTMLTestRunner.HTMLTestRunner(
            stream=fp,
            title='Test Result',
            description='Test Report'
            )
 #   runner = unittest.TextTestRunner()
    runner.run(testsuite)
