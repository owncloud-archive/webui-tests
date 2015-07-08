# -*- coding: utf-8 -*-
#!/usr/bin/env python

import sys
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from config import Config

def login(driver):
    driver.get(Config['owncloud_url'])
    elem = driver.find_element_by_name("user")
    elem.send_keys(Config['owncloud_login'])
    elem = driver.find_element_by_name("password")
    elem.send_keys(Config['owncloud_password'])
    elem.send_keys(Keys.RETURN)


def logout(driver):
    elem = driver.find_element_by_id('expand')
    elem.click()
    driver.implicitly_wait(1)
    elem = driver.find_element_by_id('logout')
    elem.click()


def go_to_apps_menu(driver):
    elem = driver.find_element_by_xpath("/html/body/header/div/a[2]")
    elem.click()
    driver.implicitly_wait(1)
    elem = driver.find_element_by_xpath("/html/body/nav/div/div/ul/li[4]/a")
    elem.click()


def is_element_present(driver, how, what):
    try: driver.find_element(by=how, value=what)
    except NoSuchElementException as e: return False
    return True