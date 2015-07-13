# -*- coding: utf-8 -*-
#!/usr/bin/env python

import sys
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
sys.path.append('../')
from config import Config
import utilities as ut
import time
from selenium.common.exceptions import NoSuchElementException




class AdminPage(object):

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

    def go_to_files_page(self):
        self.left_menu_open = ut.return_element_xpath(self.driver, ".//*[@id='header']/a[2]", 200)    
        self.left_menu_open.click()
        time.sleep(5)
        self.left_files_page = ut.return_element_xpath(self.driver, ".//*[@id='apps']/ul/li[1]/a", 200)        
        self.left_files_page.click()


    def set_up_sftp(self):
        self.combobox_external_storage = Select(ut.return_element_id(self.driver, 'selectBackend'))
        self.combobox_external_storage.select_by_visible_text('SFTP')
        time.sleep(3)
        self.SFTP_Host = ut.return_element_xpath(self.driver, ".//*[@id='externalStorage']/tbody/tr[1]/td[4]/input[1]", 200)
        self.SFTP_Username = ut.return_element_xpath(self.driver, ".//*[@id='externalStorage']/tbody/tr[1]/td[4]/input[2]", 200)
        self.SFTP_Password = ut.return_element_xpath(self.driver, ".//*[@id='externalStorage']/tbody/tr[1]/td[4]/input[3]", 200)
        self.SFTP_remote_subfolder = ut.return_element_xpath(self.driver, ".//*[@id='externalStorage']/tbody/tr[1]/td[4]/input[4]", 200)
        
        self.SFTP_Host.send_keys(Config['SFTP_Host'])
        time.sleep(1)
        self.SFTP_Username.send_keys(Config['SFTP_Username'])
        time.sleep(1)
        self.SFTP_Password.send_keys(Config['SFTP_Password'])
        time.sleep(1)
        self.SFTP_remote_subfolder.send_keys(Config['SFTP_remote_subfolder'])
        time.sleep(3)





