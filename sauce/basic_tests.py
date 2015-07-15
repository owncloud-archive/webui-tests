# -*- coding: utf-8 -*-
#!/usr/bin/env python

import sys
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
sys.path.append('../')
from config import Config
from pages import LoginPage
from pages import FilesPage
import sauce_utilities as SU
import utilities
import time

@SU.on_platforms(SU.browsers)
class basic_tests(SU.SauceTestCase):


    
    def test_login(self):
        driver = self.driver
        login_page = LoginPage.LoginPage(driver)
        login_page.open()
        login_page.login()
        self.assertTrue(utilities.is_element_present(driver, By.ID, "expandDisplayName"))

    def test_logout(self):
        driver = self.driver
        login_page = LoginPage.LoginPage(driver)
        login_page.open()
        login_page.login()
        files_page = FilesPage.FilesPage(driver)

        files_page.logout()
        time.sleep(3)
        self.assertTrue(utilities.is_element_present(driver, By.NAME, "password"))



if __name__ == "__main__":
    unittest.main()
