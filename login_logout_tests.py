import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
import time

class LoginLogoutTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url = "http://182.163.99.86"
        self.wait = WebDriverWait(self.driver, 10)
        self.load_again = True
        

    def tearDown(self):
        self.driver.quit()
        
    def test_login_successful(self):
        """
        Test case to verify successful login functionality.
        """
        driver = self.driver
        driver.get(self.base_url + "/login")
        
        # wait for the page to load
        driver.implicitly_wait(10)

        email_input = driver.find_element(By.XPATH, "//*[@id=\"username\"]")
        email_input.send_keys("admin@gigatech.com")

        password_input = driver.find_element(By.XPATH, "//*[@id=\"password\"]")
        password_input.send_keys("Abc@123")

        login_button = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/form/button")
        login_button.click()

        # get the text in h1 tag
        try:
            h1 = driver.find_element(By.TAG_NAME, "h1")
            self.assertEqual(h1.text, "Dashboard")
        except:
            self.fail("Login failed")
            
    def test_login_annotator_successful(self):
        """
        Test case to verify successful login functionality.
        """
        driver = self.driver
        driver.get(self.base_url + "/login")
        
        # wait for the page to load
        driver.implicitly_wait(10)

        email_input = driver.find_element(By.XPATH, "//*[@id=\"username\"]")
        email_input.send_keys("faisalahmedann@example.com")

        password_input = driver.find_element(By.XPATH, "//*[@id=\"password\"]")
        password_input.send_keys("Sifat@123")

        login_button = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/form/button")
        login_button.click()

        # get the text in h1 tag
        try:
            h1 = driver.find_element(By.TAG_NAME, "h1")
            self.assertEqual(h1.text, "Dashboard")
        except:
            self.fail("Login failed: No access to annotator")
            
    def test_login_validator_successful(self):
        """
        Test case to verify successful login functionality.
        """
        driver = self.driver
        driver.get(self.base_url + "/login")
        
        # wait for the page to load
        driver.implicitly_wait(10)

        email_input = driver.find_element(By.XPATH, "//*[@id=\"username\"]")
        email_input.send_keys("faisalahmedval@example.com")

        password_input = driver.find_element(By.XPATH, "//*[@id=\"password\"]")
        password_input.send_keys("Sifat@123")

        login_button = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/form/button")
        login_button.click()

        # get the text in h1 tag
        try:
            h1 = driver.find_element(By.TAG_NAME, "h1")
            self.assertEqual(h1.text, "Dashboard")
        except:
            self.fail("Login failed: No access to validator")


    '''@author-Hasib'''
    # No Locked state implemented
    def test_max_incorrect_login_attempts(self):
        """
        Test the transition to a 'locked' state after maximum incorrect login attempts.

        This test case checks if the lockout mechanism is triggered after 10 incorrect login attempts.
        It enters incorrect login credentials 10 times and checks if the lockout message is displayed.
        """
        driver = self.driver
        driver.get(self.base_url + "/login")
        driver.implicitly_wait(10)
        email_input = driver.find_element(By.XPATH, "//*[@id=\"username\"]")
        password_input = driver.find_element(By.XPATH, "//*[@id=\"password\"]")

        # Assuming the lockout mechanism is triggered after 10 incorrect attempts
        for _ in range(10):
            email_input.send_keys("admin@gigatech.com")
            password_input.send_keys("Abc@1234")
            login_button = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/form/button")
            login_button.click()
            # Clear fields for the next attempt
            email_input.clear()
            password_input.clear()

        # Check for lockout message
        try:
            lockout_message = driver.find_element(By.XPATH, "//div[contains(@class, 'lockout-message')]")
            self.assertIn("Your account has been locked", lockout_message.text)
        except:
            self.fail("Lockout message not found")

    '''@author-Hasib'''
    # Testing the Session Management of the Authentication feature
    def test_session_management(self):
        """
        Test that the session is initiated upon login and terminated upon logout.
        """
        driver = self.driver
        # Login first
        self.test_login_successful()
        # Check for a cookie that's set upon login, this is application specific
        try:
            session_cookie = driver.get_cookie("session")
            self.assertIsNotNone(session_cookie, "Session cookie should be set after login")

            # Now logout
            logout_button = driver.find_element(By.XPATH, "//a[@href='/logout']")
            logout_button.click()

            # Wait for logout to complete and redirect to login page
            driver.implicitly_wait(10)
            self.assertEqual(driver.current_url, self.base_url + "/login")

            # Check that session cookie is cleared after logout
            session_cookie = driver.get_cookie("session")
            self.assertIsNone(session_cookie, "Session cookie should be cleared after logout")
        except:
            self.fail("Session management failed")

    # Testing the logout feature
    def test_logout(self):
        """Test the logout feature.

        This method tests the logout feature by first ensuring that the user is logged in, then clicking on the
        expandable button to reveal the logout button. It then clicks on the logout button and ensures that the user is
        redirected to the login page.
        """
        wait = self.wait
        driver = self.driver
        self.test_login_successful()


        expandable_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="radix-:r5:"]')))
        expandable_button.click()


        # get the attribute "data-state" of the button
        data_state = expandable_button.get_attribute("data-state")
        self.assertEqual(data_state, "open")

        logout_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div')))
        logout_button.click()

        email_input = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="username"]')))
        self.assertEqual(driver.current_url, self.base_url + "/login")
        
    def test_login_unsuccessful_incorrect_username(self):
        """
        Test case to verify that login is unsuccessful with incorrect username.

        Steps:
        1. Navigate to login page.
        2. Enter incorrect email in email field.
        3. Enter valid password in password field.
        4. Click on login button.
        5. Verify that error message "Incorrect email or password" is displayed.

        """
        driver = self.driver
        driver.get(self.base_url + "/login")
        driver.implicitly_wait(10)

        email_input = driver.find_element(By.XPATH, "//*[@id=\"username\"]")
        email_input.send_keys("incorrect@gigatech.com")

        password_input = driver.find_element(By.XPATH, "//*[@id=\"password\"]")
        password_input.send_keys("Abc@123")

        login_button = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/form/button")
        login_button.click()

        try:
            time.sleep(1)
            error_message = self.wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/section/ol/li[1]/div[2]/div")))
            self.assertIn("Incorrect email or password", error_message.text)
        except:
            self.fail("Error message not found")

    def test_login_unsuccessful_incorrect_password(self):
        """
        Test that login is unsuccessful with an incorrect password.

        Steps:
        1. Navigate to the login page.
        2. Enter a valid email address.
        3. Enter an incorrect password.
        4. Click the login button.
        5. Verify that an error message is displayed indicating that the password is incorrect.
        """
        driver = self.driver
        driver.get(self.base_url + "/login")
        driver.implicitly_wait(10)

        email_input = driver.find_element(By.XPATH, "//*[@id=\"username\"]")
        email_input.send_keys("admin@gigatech.com")

        password_input = driver.find_element(By.XPATH, "//*[@id=\"password\"]")
        password_input.send_keys("incorrect")

        login_button = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/form/button")
        login_button.click()

        try:
            time.sleep(1)
            error_message = self.wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[2]/form/div[2]/div[2]/div/p")))
            self.assertIn("Please give at least one number, one lower and upper case letter, one special character", error_message.text)
        except:
            self.fail("Error message not found")

    def test_login_unsuccessful_incorrect_credentials(self):
        """
        Test case to verify that login is unsuccessful with incorrect credentials.

        Steps:
        1. Load the login page.
        2. Enter incorrect email and password.
        3. Click on the login button.
        4. Verify that the error message is displayed.

        """
        driver = self.driver
        if self.load_again:
            driver.get(self.base_url + "/login")
        driver.implicitly_wait(10)

        email_input = driver.find_element(By.XPATH, "//*[@id=\"username\"]")
        email_input.send_keys("incorrect@gigatech.com")

        password_input = driver.find_element(By.XPATH, "//*[@id=\"password\"]")
        password_input.send_keys("incorrect")

        login_button = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/form/button")
        login_button.click()

        try:
            time.sleep(1)
            error_message = self.wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[2]/form/div[2]/div[2]/div/p")))
            self.assertIn("Please give at least one number, one lower and upper case letter, one special character", error_message.text)
        except:
            self.fail("Error message not found")

    def test_login_successful_after_failed_attempt(self):
        """
        Test that login is successful after a failed attempt with incorrect credentials.
        
        This test case first attempts to login with incorrect credentials to ensure that the login fails.
        It then attempts to login again with correct credentials to ensure that the login is successful.
        """
        self.test_login_unsuccessful_incorrect_credentials()
        self.load_again = False
        self.test_login_successful()
        self.load_again = True

    def test_login_unsuccessful_empty_username(self):
            """
            Test case to verify that login is unsuccessful when the username field is left empty.

            Steps:
            1. Navigate to the login page
            2. Find the email input field and leave it empty
            3. Find the password input field and enter a valid password
            4. Click on the login button
            5. Wait for the error message to appear
            6. Verify that the error message contains the text "Required"
            """
            driver = self.driver
            driver.get(self.base_url + "/login")
            driver.implicitly_wait(10)

            email_input = driver.find_element(By.XPATH, "//*[@id=\"username\"]")
            email_input.send_keys("")

            password_input = driver.find_element(By.XPATH, "//*[@id=\"password\"]")
            password_input.send_keys("Abc@123")

            login_button = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/form/button")
            login_button.click()

            try:
                time.sleep(1)
                error_message = self.wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/form/div[1]/div/div/p")))
                self.assertIn("Required", error_message.text)
            except:
                self.fail("Error message not found")

    def test_login_unsuccessful_empty_password(self):
        """
        Test case to verify that login is unsuccessful when password field is empty.

        Steps:
        1. Open the login page.
        2. Enter the email address.
        3. Leave the password field empty.
        4. Click on the login button.
        5. Verify that an error message is displayed indicating that the password field is required.
        """
        driver = self.driver
        driver.get(self.base_url + "/login")
        driver.implicitly_wait(10)

        email_input = driver.find_element(By.XPATH, "//*[@id=\"username\"]")
        email_input.send_keys("admin@gigatech.com")

        password_input = driver.find_element(By.XPATH, "//*[@id=\"password\"]")
        password_input.send_keys("")

        login_button = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/form/button")
        login_button.click()

        try:
            time.sleep(1)
            error_message = self.wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[2]/form/div[2]/div[2]/div/p")))
            self.assertIn("Required", error_message.text)
        except:
            self.fail("Error message not found")

    def test_login_unsuccessful_empty_credentials(self):
            """
            Test case to verify that login is unsuccessful when empty credentials are provided.
            This test case navigates to the login page, enters empty email and password fields, clicks the login button,
            and verifies that the appropriate error messages are displayed on the page.
            """
            driver = self.driver
            driver.get(self.base_url + "/login")
            driver.implicitly_wait(10)

            email_input = driver.find_element(By.XPATH, "//*[@id=\"username\"]")
            email_input.send_keys("")

            password_input = driver.find_element(By.XPATH, "//*[@id=\"password\"]")
            password_input.send_keys("")

            login_button = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/form/button")
            login_button.click()

            try:
                time.sleep(1)
                error_message = self.wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/form/div[1]/div/div/p")))
                self.assertIn("Required", error_message.text)
                
                pass_error_message = self.wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[2]/form/div[2]/div[2]/div/p")))
                self.assertIn("Required", pass_error_message.text)
            except:
                self.fail("Error messages not found")
