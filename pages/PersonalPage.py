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



class PersonalPage(object):

	
   def __init__(self, driver):
        self.driver = driver
        #self.set_locators()

   def set_locators(self):
        self.apps_menu_not_enabled = ut.return_element_id(self.driver, "app-category-1", 10)
        self.apps_menu_enabled = ut.return_element_id(self.driver, "app-category-0", 10)
   
   def go_to_personal_page(self):
       self.driver.find_element_by_id('expand').click()
       #Wait to show the menu
       time.sleep(1)
       #Click in users menu
       self.driver.find_element_by_xpath(".//*[@id='expanddiv']/ul/li[1]/a").click()      
    
   def logout(self):    
        self.driver.find_element_by_id('expand').click()
        #Wait to show the menu
        time.sleep(1)
        self.right_menu_logout = ut.return_element_id(self.driver, 'logout', 15)
        time.sleep(1)
        self.right_menu_logout.click()

   def go_to_apps_menu(self):
        self.left_menu_open = ut.return_element_xpath(self.driver, ".//*[@id='header']/a[2]", 200)    
        self.left_menu_open.click()
        time.sleep(5)
        self.left_menu_apps = ut.return_element_xpath(self.driver, ".//*[@id='apps-management']/a", 200)        
        self.left_menu_apps.click() 
   
   def set_full_name(self,new_admin_name):
        #Clear previous full name
        self.driver.find_element_by_id('displayName').clear()
        #Write the new full names
        self.driver.find_element_by_id('displayName').send_keys(new_admin_name)
       
   def set_password(self,password,new_admin_pwd):   
        #Write the old password
        self.driver.find_element_by_id('pass1').send_keys(password)
        #write the new password
        self.driver.find_element_by_id('pass2').send_keys(new_admin_pwd)
        #Click to set the new password
        self.driver.find_element_by_id('passwordbutton').click()
 









