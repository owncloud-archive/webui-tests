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
import time


class ExternalStorage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        #self.driver = webdriver.Chrome()
        #self.driver = webdriver.PhantomJS()
        self.driver.set_window_size(1280, 720)
    

    def step1(self):
        #ENABLE EXTERNAL STORAGE APP
        driver = self.driver
        utilities.login(driver)
        utilities.go_to_apps_menu(driver)
        utilities.enable_app(driver, 'app-files_external')
        self.assertTrue(utilities.is_element_present_waiting(driver, By.ID, "app-files_external", 20))

    def step2(self):
        #DISABLE EXTERNAL STORAGE APP
        driver = self.driver
        utilities.disable_app(driver, 'app-files_external')
        self.assertTrue(utilities.is_element_present(driver, By.ID, "app-files_external"))

    def steps(self):
        for name in sorted(dir(self)):
            if name.startswith("step"):
                yield name, getattr(self, name) 

    def test_steps(self):
        for name, step in self.steps():
            try:
                step()
            except Exception as e:
                self.fail("{} failed ({}: {})".format(step, type(e), e))
    
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
