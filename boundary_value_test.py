import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

class MySeleniumUnitTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url = "http://182.163.99.86"
        

    def tearDown(self):
        self.driver.quit()

    def test_email_boundary_values(self):
        """ Test email boundary conditions """
        self.driver.get(self.base_url + "/login")

          
        # wait for the page to load
        self.driver.implicitly_wait(10)


        # Assuming the local part of the email should be at least 1 character and at most 10 characters as an example.
        min_length_local = 1
        max_length_local = 10

        boundary_values = {
            "just_below_min_local": "",  # No local part
            "min_length_local": "a@example.com",  # Min length for local part
            "just_above_min_local": "ab@example.com",  # Just above min length for local part
            "just_below_max_local": "a" * (max_length_local - 1) + "@example.com",  # Just below max length for local part
            "max_length_local": "a" * max_length_local + "@example.com",  # Max length for local part
            "above_max_local": "a" * (max_length_local + 1) + "@example.com",  # Above max length for local part
            "no_at_symbol": "invalidemail.com",  # No "@" symbol
            "no_domain": "invalidemail@",  # No domain part
            "no_top_level_domain": "invalidemail@example",  # No top-level domain like .com, .net, etc.
            "valid_email": "valid.email@example.com"  # A valid email format
        }

        for test_case, email in boundary_values.items():
            with self.subTest(test_case=test_case):
                email_input = self.driver.find_element(By.XPATH, "//*[@id=\"username\"]")
                email_input.clear()
                email_input.send_keys(email)
                password_input = self.driver.find_element(By.XPATH, "//*[@id=\"password\"]")
                password_input.clear()
                password_input.send_keys("ValidPassword123!")  # Use a valid password here
                login_button = self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/form/button")
                login_button.click()
   
    def test_password_complexity_boundary_values(self):
        """ Test password complexity boundary conditions """
        self.driver.get(self.base_url + "/login")
          
        # wait for the page to load
        self.driver.implicitly_wait(10)


        # Define boundary values
        boundary_values = {
            "below_min_length": "Aa1!",  # 5 characters, missing the min length of 6
            "min_length_no_number": "Aa!aa",  # Exactly 6 characters but missing a number
            "min_length_no_upper": "aa1!aa",  # Exactly 6 characters but missing an uppercase letter
            "min_length_no_lower": "AA1!AA",  # Exactly 6 characters but missing a lowercase letter
            "min_length_no_special": "Aa1aa1",  # Exactly 6 characters but missing a special character
            "min_length_valid": "Aa1!aa",  # Exactly 6 characters, valid
            "just_below_max_length": "Aa1!aAa1!aA",  # 13 characters, valid
            "max_length_valid": "Aa1!aAa1!aAa",  # Exactly 14 characters, valid
            "above_max_length": "Aa1!aAa1!aAa1",  # 15 characters, exceeding the max length of 14
        }

        for test_case, password in boundary_values.items():
            with self.subTest(test_case=test_case):
                email_input = self.driver.find_element(By.XPATH, "//*[@id=\"username\"]")
                email_input.clear()
                email_input.send_keys("validUsername")  # Use a valid username here
                password_input = self.driver.find_element(By.XPATH, "//*[@id=\"password\"]")
                password_input.clear()
                password_input.send_keys(password)
                login_button = self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/form/button")
                login_button.click()               

if __name__ == "__main__":
    unittest.main()
