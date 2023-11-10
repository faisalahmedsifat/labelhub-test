import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

class PerformanceTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url = "http://182.163.99.86"
        

    def tearDown(self):
        self.driver.quit()

    '''@author - Hasibullah Hasib'''
    def measure_load_time(self, url):
        """ 
        Measures the page load time of a given URL 
        """
        start_time = time.time()
        self.driver.get(url)
        load_time = time.time() - start_time
        return load_time
    
    '''@author - Hasibullah Hasib'''
    def test_login_page_load_time(self):
        """
        Tests the load time of the login page.

        Returns:
            None
        """
        load_time = self.measure_load_time(self.base_url + "/login")
        print(f"Login Page Load Time: {load_time} seconds")
        self.assertLess(load_time, 3, "Login page load time should be less than 3 seconds")

    '''@author - Hasibullah Hasib'''
    def test_login_action_response_time(self):
            """
            Tests the response time of the login action.

            This function tests the response time of the login action by measuring the time it takes for the login button
            to be clicked and for the next page to load or for a login failure message to be displayed.

            Returns:
                None
            """
            self.driver.get(self.base_url + "/login")
            self.driver.implicitly_wait(10)

            email_input = self.driver.find_element(By.XPATH, "//*[@id=\"username\"]")
            password_input = self.driver.find_element(By.XPATH, "//*[@id=\"password\"]")
            login_button = self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/form/button")

            email_input.send_keys("admin@gigatech.com")
            password_input.send_keys("Abc@123")

            start_time = time.time()
            login_button.click()
            # Wait for the next page or a login failure message to confirm the action is complete
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.find_element(By.TAG_NAME, "h1").text == "Dashboard" or
                               driver.find_element(By.CLASS_NAME, "error").is_displayed()
            )
            response_time = time.time() - start_time
            
            print(f"Login Action Response Time: {response_time} seconds")
            self.assertLess(response_time, 2, "Login action response time should be less than 2 seconds")



if __name__ == "__main__":
    unittest.main()
    print("Everything passed")
    
