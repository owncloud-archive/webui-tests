import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        #self.driver = webdriver.Firefox()
        self.driver = webdriver.PhantomJS()
    
    def test_search_in_python_org(self):
        driver = self.driver
	driver.get("http://docker.oc.solidgear.es:51194")
        #self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("user")
        elem.send_keys("admin")
	elem2 = driver.find_element_by_name("password")
	elem2.send_keys("Password")
        elem2.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
