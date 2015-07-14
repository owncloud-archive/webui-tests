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

def return_element_css(driver, css_selector, waiting=10):
    element = WebDriverWait(driver, waiting).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, css_selector))
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




