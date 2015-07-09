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


class basic_tests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        #self.driver = webdriver.PhantomJS()
    
    def test_login(self):
        driver = self.driver
        utilities.login(driver)
        self.assertTrue(utilities.is_element_present(driver, By.ID, "expandDisplayName"))


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
