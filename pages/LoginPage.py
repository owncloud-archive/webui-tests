# -*- coding: utf-8 -*-
#!/usr/bin/env python

import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
sys.path.append('../')
from config import Config


class LoginPage(object):

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(Config['owncloud_url'])
        self.set_locators()


    def set_locators(self):
        self.user_textbox = self.driver.find_element_by_name("user")
        self.password_textbox = self.driver.find_element_by_name("password")

    def login(self):
        self.user_textbox.send_keys(Config['owncloud_login'])
        self.password_textbox.send_keys(Config['owncloud_password'])
        self.password_textbox.send_keys(Keys.RETURN)
















