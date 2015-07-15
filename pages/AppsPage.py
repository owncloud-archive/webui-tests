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





class AppsPage(object):

    def __init__(self, driver):
        self.driver = driver
        #self.set_locators()

    def set_locators(self):
        self.apps_menu_not_enabled = ut.return_element_id(self.driver, "app-category-1", 10)
        self.apps_menu_enabled = ut.return_element_id(self.driver, "app-category-0", 10)
    
    

    def enable_app(self, app_id):
        self.apps_menu_not_enabled = ut.return_element_id(self.driver, "app-category-1", 10)
        self.apps_menu_not_enabled.click()
        time.sleep(3)
        app_id_xpath = ".//*[@id='" + app_id + "']/input"
        self.enable_app_button = ut.return_element_xpath(self.driver, app_id_xpath, 10)
        self.enable_app_button.click()
        self.apps_menu_enabled = self.driver.find_element_by_id("app-category-0")
        self.apps_menu_enabled.click()
        time.sleep(5)

    def disable_app(self, app_id):
        self.apps_menu_enabled = ut.return_element_id(self.driver, "app-category-0", 10)
        self.apps_menu_enabled.click()
        time.sleep(3)
        app_id_xpath = ".//*[@id='" + app_id + "']/input"
        self.disable_app_button = ut.return_element_xpath(self.driver, app_id_xpath, 10)
        self.disable_app_button.click()
        self.apps_menu_not_enabled = ut.return_element_id(self.driver, "app-category-1", 10)
        self.apps_menu_not_enabled.click()
        time.sleep(5)

    def go_to_disabled_apps(self):
        self.apps_menu_not_enabled = ut.return_element_id(self.driver, "app-category-1", 10)
        self.apps_menu_not_enabled.click()
        time.sleep(3)


    def go_to_files_page(self):
        self.left_menu_open = ut.return_element_xpath(self.driver, ".//*[@id='header']/a[2]", 200)    
        self.left_menu_open.click()
        time.sleep(5)
        self.left_files_page = ut.return_element_xpath(self.driver, ".//*[@id='apps']/ul/li[1]/a", 200)        
        self.left_files_page.click()