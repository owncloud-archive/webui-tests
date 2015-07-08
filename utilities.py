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
    driver.implicitly_wait(1)



def enable_app(driver, app_id):
    elem = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "app-category-1"))
    )
    
    elem.click()
    driver.implicitly_wait(10)
    app_id_xpath = ".//*[@id='" + app_id + "']/input"
    elem = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, app_id_xpath))
    )
    
    elem.click()
    driver.implicitly_wait(10)
    elem = driver.find_element_by_id("app-category-0")
    elem.click()
    driver.implicitly_wait(10)



def disable_app(driver, app_id):
    elem = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "app-category-0"))
    )

    elem.click()
    driver.implicitly_wait(10)
    app_id_xpath = ".//*[@id='" + app_id + "']/input"
    elem = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, app_id_xpath))
    )
    
    elem.click()
    driver.implicitly_wait(10)
    elem = driver.find_element_by_id("app-category-1")
    elem.click()
    driver.implicitly_wait(10)





def is_element_present(driver, how, what):
    try: driver.find_element(by=how, value=what)
    except NoSuchElementException as e: return False
    return True
