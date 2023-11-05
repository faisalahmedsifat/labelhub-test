import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class MySeleniumUnitTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
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

    '''@author-Hasib'''
    # No Locked state implemented
    def test_max_incorrect_login_attempts(self):
        """ Test the transition to a 'locked' state after maximum incorrect login attempts """
        self.driver.get(self.base_url + "/login")
        self.driver.implicitly_wait(10)
        email_input = self.driver.find_element(By.XPATH, "//*[@id=\"username\"]")
        password_input = self.driver.find_element(By.XPATH, "//*[@id=\"password\"]")

        # Assuming the lockout mechanism is triggered after 10 incorrect attempts
        for _ in range(10):
            email_input.send_keys("admin@gigatech.com")
            password_input.send_keys("Abc@1234")
            login_button = self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/form/button")
            login_button.click()
            # Clear fields for the next attempt
            email_input.clear()
            password_input.clear()
        
        # Check for lockout message
        lockout_message = self.driver.find_element(By.XPATH, "//div[contains(@class, 'lockout-message')]")
        self.assertIn("Your account has been locked", lockout_message.text)

    '''@author-Hasib'''
    # Testing the Session Management of the Authentication feature
    def test_session_management(self):
        """ Test that the session is initiated upon login and terminated upon logout """
        # Login first
        self.test_login_successful()
        # Check for a cookie that's set upon login, this is application specific
        session_cookie = self.driver.get_cookie("session")
        self.assertIsNotNone(session_cookie, "Session cookie should be set after login")

        # Now logout
        logout_button = self.driver.find_element(By.XPATH, "//a[@href='/logout']")
        logout_button.click()

        # Wait for logout to complete and redirect to login page
        self.driver.implicitly_wait(10)
        self.assertEqual(self.driver.current_url, self.base_url + "/login")

        # Check that session cookie is cleared after logout
        session_cookie = self.driver.get_cookie("session")
        self.assertIsNone(session_cookie, "Session cookie should be cleared after logout")

   

if __name__ == "__main__":
    unittest.main()
    print("Everything passed")
    