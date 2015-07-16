# -*- coding: utf-8 -*-
#!/usr/bin/env python

import sys
import os
import new
import unittest
from selenium import webdriver
from sauceclient import SauceClient


SAUCE_USERNAME = os.environ.get('SAUCE_USERNAME')
SAUCE_ACCESS_KEY = os.environ.get('SAUCE_ACCESS_KEY')
sauce = SauceClient(SAUCE_USERNAME, SAUCE_ACCESS_KEY)

browsers = [{"platform": "Mac OS X 10.9",                                      
             "browserName": "firefox",
             "version": "39"}]

def on_platforms(platforms):
    def decorator(base_class):
        module = sys.modules[base_class.__module__].__dict__
        for i, platform in enumerate(platforms):
            d = dict(base_class.__dict__)
            d['desired_capabilities'] = platform
            name = "%s_%s" % (base_class.__name__, i + 1)
            module[name] = new.classobj(name, (base_class,), d)
    return decorator



class SauceTestCase(unittest.TestCase):
    def setUp(self):
        self.desired_capabilities['name'] = self.id()

        if os.environ.get('TRAVIS'):
            self.desired_capabilities['tunnel-identifier'] = os.environ['TRAVIS_JOB_NUMBER']
            self.desired_capabilities['build'] = os.environ['TRAVIS_BUILD_NUMBER']

        hub_url = "%s:%s@localhost:4445" % (SAUCE_USERNAME, SAUCE_ACCESS_KEY)
        self.driver = webdriver.Remote(
            desired_capabilities=self.desired_capabilities,
            command_executor="http://%s/wd/hub" % hub_url
        )

        '''sauce_url = "http://%s:%s@ondemand.saucelabs.com:80/wd/hub"
        self.driver = webdriver.Remote(
            desired_capabilities=self.desired_capabilities,
            command_executor=sauce_url % (SAUCE_USERNAME, SAUCE_ACCESS_KEY)
        )
        '''
        
        self.driver.set_window_size(1280, 720)
        self.driver.implicitly_wait(30)
    
    def tearDown(self):
        print("Link to your job: https://saucelabs.com/jobs/%s" % self.driver.session_id)
        try:
            if sys.exc_info() == (None, None, None):
                sauce.jobs.update_job(self.driver.session_id, passed=True)
            else:
                sauce.jobs.update_job(self.driver.session_id, passed=False)
        finally:
            self.driver.quit()



