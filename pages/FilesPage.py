# -*- coding: utf-8 -*-
#!/usr/bin/env python

import sys
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from config import Config
sys.path.append('../')
import utilities as ut
import time
from selenium.common.exceptions import NoSuchElementException




class FilesPage(object):

    def __init__(self, driver):
        self.driver = driver
        self.set_locators()

    def set_locators(self):
        self.right_menu_open = self.driver.find_element_by_id('expand')

    
    def logout(self):
        self.right_menu_open.click()
        self.right_menu_logout = ut.return_element_id(self.driver, 'logout', 15)
        time.sleep(1)
        self.right_menu_logout.click()

    def go_to_apps_menu(self):
        self.left_menu_open = ut.return_element_xpath(self.driver, ".//*[@id='header']/a[2]", 200)    
        self.left_menu_open.click()
        time.sleep(5)
        self.left_menu_apps = ut.return_element_xpath(self.driver, ".//*[@id='apps-management']/a", 200)        
        self.left_menu_apps.click()

    def go_to_admin_page(self):
        self.right_menu_open.click()
        self.right_admin_page = ut.return_element_xpath(self.driver, ".//*[@id='expanddiv']/ul/li[3]/a", 200)
        time.sleep(1)
        self.right_admin_page.click()

    def look_for_element_in_visible_files_list(self, name):
        list_elements = self.driver.find_elements(By.CSS_SELECTOR, 'td.filename .innernametext')
        visible_filenames = [ elem.text for elem in list_elements ]
        if name in visible_filenames:
            return True
        else:
            return False


