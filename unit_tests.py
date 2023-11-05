import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class MySeleniumUnitTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.base_url = "http://182.163.99.86"
        

    def tearDown(self):
        self.driver.quit()
        
    def test_login_successful(self):
        # driver = self.driver
        self.driver.get(self.base_url + "/login")
        
        # wait for the page to load
        self.driver.implicitly_wait(10)

        email_input = self.driver.find_element(By.XPATH, "//*[@id=\"username\"]")
        email_input.send_keys("admin@gigatech.com")

        password_input = self.driver.find_element(By.XPATH, "//*[@id=\"password\"]")
        password_input.send_keys("Abc@123")

        login_button = self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/form/button")
        login_button.click()

        # get the text in h1 tag
        try:
            h1 = self.driver.find_element(By.TAG_NAME, "h1")
            self.assertEqual(h1.text, "Dashboard")
        except:
            self.fail("Login failed")

   

if __name__ == "__main__":
    unittest.main()
    print("Everything passed")
    