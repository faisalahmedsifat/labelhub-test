import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
import login_logout_tests as unit_tests

from faker import Faker

class UserCreationDeletion(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url = "http://182.163.99.86"
        self.wait = WebDriverWait(self.driver, 10)

        ## same email won't work the second time. So we need to generate a fake email
        self.fake_email = "test_user@example.net"
        

    def tearDown(self):
        self.driver.quit()



    def test_user_creation_expected_data(self):
        """ Test the user creation feature """

        # use a function from UnitTest class


        # First we have to login
        unit_tests.LoginLogoutTests.test_login_successful(self)
        """
            supposed required fields for the user creation:
            1. Full Name
            2. Email
            3. Password
            4. Mobile 
            
            some optional:
            1. Gender
            2. Birthday
            3. Institution
            4. Qualification
            5. Role

        """

        user_button_from_sidebar = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/section/main/aside/div/div/div/div[3]/a/div')))
        user_button_from_sidebar.click()
        
        # get the text in h1 tag
        try:
            h1 = self.driver.find_element(By.TAG_NAME, "h1")
            self.assertEqual(h1.text, "Users")
        except:
            self.fail("Users page not found")

        add_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/section/main/div[2]/div[2]/section/div[2]/button')))
        add_button.click()

        # get the text from a xpath element
        try:
            add_user_text = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[1]")
            self.assertEqual(add_user_text.text, "Add User")
        except:
            self.fail("Add User page not found")

        # fill the form
        # full name xpath: //*[@id="floating-label-input-:r9f:"]
        full_name_input = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[1]/div[1]/input')
        full_name_input.send_keys("Test User")

        # # email xpath: //*[@id="floating-label-input-:r9k:"]
        email_input = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/div[1]/input')
        email_input.send_keys(self.fake_email)

        # # password xpath: //*[@id="floating-label-input-:r9i:"]
        password_input = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[1]/div[4]/input')
        password_input.send_keys("Abc@123")

        # # mobile xpath: //*[@id="floating-label-input-:r9n:"]
        mobile_input = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/div[4]/input')
        mobile_input.send_keys("01700000000")

        # # add user button xpath: /html/body/div[3]/div/div/div[3]/button
        add_user_button = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[3]/button')
        add_user_button.click()

        # wait
        # self.driver.implicitly_wait(10)

        # # get the text from a xpath element
        # first email of table xpath: //*[@id="root"]/section/main/div[2]/div[2]/section/div[3]/div[2]/div/table/tbody/tr[1]/td[3]
        # email_addess = self.wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/section/main/div[2]/div[2]/section/div[3]/div[2]/div/table/tbody/tr[1]/td[3]')))
        email_addess = self.wait.until(EC.text_to_be_present_in_element((By.XPATH, '/html/body/div/section/main/div[2]/div[2]/section/div[3]/div[2]/div/table/tbody/tr[1]/td[3]'), self.fake_email))
        # self.assertEqual(email_addess.text, self.fake_email)
        self.assertTrue(email_addess)

    def test_user_deletion_as_expected(self):
        """ Test the user deletion feature """
        driver = self.driver
        unit_tests.LoginLogoutTests.test_login_successful(self)

        user_button_from_sidebar = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/section/main/aside/div/div/div/div[3]/a/div')))
        user_button_from_sidebar.click()
        
        # get the text in h1 tag
        try:
            h1 = driver.find_element(By.TAG_NAME, "h1")
            self.assertEqual(h1.text, "Users")
        except:
            self.fail("Users page not found")

        # check if the email is the generated one from the previous test
        first_email = driver.find_element(By.XPATH, '/html/body/div/section/main/div[2]/div[2]/section/div[3]/div[2]/div/table/tbody/tr[1]/td[3]')
        self.assertEqual(first_email.text, self.fake_email)

        # delete the user
        first_user_table_row_delete_button = driver.find_element(By.XPATH, '/html/body/div/section/main/div[2]/div[2]/section/div[3]/div[2]/div/table/tbody/tr[1]/td[8]/div/span[3]/img')
        first_user_table_row_delete_button.click()

        # wait
        self.driver.implicitly_wait(10)

        # confirm the deletion
        delete_confirm_button = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[3]/button[1]')
        delete_confirm_button.click()

        # wait
        self.driver.implicitly_wait(10)

        # check again if the email is the generated one from the previous test
        email_addess = self.wait.until(EC.text_to_be_present_in_element((By.XPATH, '/html/body/div/section/main/div[2]/div[2]/section/div[3]/div[2]/div/table/tbody/tr[1]/td[3]'), self.fake_email))
        self.assertFalse(email_addess)



    

        

        



    




if __name__ == "__main__":
    unittest.main()
    print("Everything passed")
    