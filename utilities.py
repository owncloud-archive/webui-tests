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
import time
from selenium.common.exceptions import NoSuchElementException


def return_element_xpath(driver, xpath, waiting=10):
    element = WebDriverWait(driver, waiting).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )
    return element

def return_element_id(driver, id, waiting=10):
    element = WebDriverWait(driver, waiting).until(
        EC.presence_of_element_located((By.ID, id))
    )
    return element

def is_element_present_waiting(driver, how, what, waiting=10):
    try:
        element = WebDriverWait(driver, waiting).until(
            EC.presence_of_element_located((how, what))
        )
    except NoSuchElementException as e: return False
    return True


def is_element_present(driver, how, what):
    try: driver.find_element(by=how, value=what)
    except NoSuchElementException as e: return False
    return True


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
    #driver.implicitly_wait(1)

    elem = return_element_xpath(driver, ".//*[@id='header']/a[2]", 200)    
    elem.click()
    
    time.sleep(5)

    elem = return_element_xpath(driver, ".//*[@id='apps-management']/a", 200)        
    elem.click()


def enable_app(driver, app_id):
    elem = return_element_id(driver, "app-category-1", 10)
    elem.click()

    time.sleep(3)

    app_id_xpath = ".//*[@id='" + app_id + "']/input"
    elem = return_element_xpath(driver, app_id_xpath, 10)
    elem.click()

    
    elem = driver.find_element_by_id("app-category-0")
    elem.click()
    
    time.sleep(5)
    



def disable_app(driver, app_id):
    elem = return_element_id(driver, "app-category-0", 10)
    elem.click()
    
    time.sleep(3)

    app_id_xpath = ".//*[@id='" + app_id + "']/input"
    elem = return_element_xpath(driver, app_id_xpath, 10)
    elem.click()
        
    elem = return_element_id(driver, "app-category-1", 10)
    elem.click()

    time.sleep(5)
    






