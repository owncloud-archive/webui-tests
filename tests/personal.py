# -*- coding: utf-8 -*-
#!/usr/bin/env python

import sys
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
sys.path.append('../')
from config import Config
import utilities
import time

from pages import LoginPage
from pages import FilesPage
from pages import AppsPage
from pages import PersonalPage

class Personal(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        #self.driver = webdriver.Chrome()
        #self.driver = webdriver.PhantomJS()
        self.driver.set_window_size(1280, 720)
    
    '''
    def test_logout(self):
        driver = self.driver
        login_page = LoginPage.LoginPage(driver)
        login_page.open()
        login_page.login()
        files_page = FilesPage.FilesPage(driver)
        files_page.logout()
        time.sleep(3)
        self.assertTrue(utilities.is_element_present(driver, By.NAME, "password"))
    '''

    #LOGIN
    def step1(self):
        driver = self.driver
        login_page = LoginPage.LoginPage(driver)
        login_page.open()
        login_page.login()
        time.sleep(2)

    #GO TO Personal
    def step2(self):
        driver = self.driver
        files_page = FilesPage.FilesPage(driver)
        files_page.go_to_personal_page()
        time.sleep(2)


    #CHANGE Password
    def step3(self):
        driver = self.driver
        personal_page = PersonalPage.PersonalPage(driver)
        personal_page.set_password(Config["owncloud_password"],Config["new_admin_password"]) 
    #--  (TO DO assert)


    #CHANGE full name
    def step5(self):
        driver = self.driver
        personal_page = PersonalPage.PersonalPage(driver)
        personal_page.set_full_name(Config["new_admin_name"])
        time.sleep(2) 

    #LOGOUT
    def step6(self):
        driver = self.driver
        personal_page = PersonalPage.PersonalPage(driver)
        personal_page.logout()

    #LOGIN
    def step7(self):
        driver = self.driver
        login_page = LoginPage.LoginPage(driver)
        login_page.open()
        login_page.login(Config["owncloud_login"],Config["new_admin_password"])
        self.assertTrue(utilities.is_element_present(driver, By.ID, "expandDisplayName"))

    ##GO TO Personal
    def step8(self):
        driver = self.driver
        files_page = FilesPage.FilesPage(driver)
        files_page.go_to_personal_page()
        time.sleep(2)

    #CHANGE Password to ORIGINAL
    def step9(self):
        driver = self.driver
        personal_page = PersonalPage.PersonalPage(driver)
        personal_page.set_password(Config["new_admin_password"],Config["owncloud_password"])
    #--  (TO DO assert)

    #CHANGE full name to ORIGINAL
    def step5(self):
        driver = self.driver
        personal_page = PersonalPage.PersonalPage(driver)
        personal_page.set_full_name(Config["admin"])
        time.sleep(2)


    def steps(self):
        for name in sorted(dir(self)):
            if name.startswith("step"):
                yield name, getattr(self, name) 

    def test_steps(self):
        for name, step in self.steps():
#--            try:
            step()
#--            except Exception as e:
#--                self.fail("{} failed ({}: {})".format(step, type(e), e))
    
    
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
