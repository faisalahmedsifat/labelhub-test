import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import login_logout_tests as unit_tests

from faker import Faker
import time


class UserCreationDeletion(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url = "http://182.163.99.86"
        self.wait = WebDriverWait(self.driver, 10)

        self.fake = Faker()
        self.fake_name = self.fake.name()
        self.fake_email = self.fake.email()
        self.institution_name = "North South University"
        self.qualification = "NA"
        self.password = "Abc@123"
        self.mobile = "01234567890"
        self.gender = "Male"  # "Male", "Female", "Other"
        self.role = "ANNOTATOR"  # "MANAGER", "ANNOTATOR", "VALIDATOR", "GUEST"
        self.dob = "2000-01-01"

    def tearDown(self):
        self.driver.quit()

    def test_user_creation_expected_data(self, outside_call=False):
        """
        Test user creation with expected data.

        This function tests the user creation functionality by filling out the user creation form with expected data and
        verifying that the user is successfully created. It uses the Selenium WebDriver to interact with the web page.

        Args:
            self: The TestUserRelated class instance.

        Returns:
            None
        """

        # Navigate to the login page
        self.driver.get(self.base_url + "/login")

        # Wait for the page to load
        time.sleep(5)

        # Fill out the login form
        email_input = self.driver.find_element(By.XPATH, "//*[@id=\"username\"]")
        email_input.send_keys("admin@gigatech.com")

        password_input = self.driver.find_element(By.XPATH, "//*[@id=\"password\"]")
        password_input.send_keys("Abc@123")

        login_button = self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/form/button")
        login_button.click()

        # Wait for the page to load
        time.sleep(5)

        # Click the user button in the sidebar
        user_button_from_sidebar = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/section/main/aside/div/div/div/div[3]/a/div')))
        user_button_from_sidebar.click()

        # Verify that the Users page is loaded
        try:
            h1 = self.driver.find_element(By.TAG_NAME, "h1")
            self.assertEqual(h1.text, "Users")
        except:
            self.fail("Users page not found")

        # Click the Add button
        add_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/section/main/div[2]/div[2]/section/div[2]/button')))
        add_button.click()

        # Verify that the Add User page is loaded
        try:
            add_user_text = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[1]")
            self.assertEqual(add_user_text.text, "Add User")
        except:
            self.fail("Add User page not found")

        # Fill out the user creation form
        full_name_input = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[1]/div[1]/input')
        full_name_input.send_keys(self.fake_name)

        email_input = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/div[1]/input')
        email_input.send_keys(self.fake_email)

        password_input = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[1]/div[4]/input')
        password_input.send_keys(self.password)

        mobile_input = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/div[4]/input')
        mobile_input.send_keys(self.mobile)

        gender_input = self.driver.find_element(By.XPATH,
                                                f'//*[@id="floating-label-input-:rl:"]/option[text()="{self.gender}"]')
        gender_input.click()

        role_input = self.driver.find_element(By.XPATH,
                                              f'//*[@id="floating-label-input-:ro:"]/option[text()="{self.role}"]')
        role_input.click()

        institution_input = self.driver.find_element(By.XPATH,
                                                     '//*[@id="floating-label-input-:rm:"]')
        institution_input.send_keys(self.institution_name)

        qualification_input = self.driver.find_element(By.XPATH,
                                                       '//*[@id="floating-label-input-:rr:"]')
        qualification_input.send_keys(self.qualification)

        date_input = self.driver.find_element(By.XPATH,
                                              '//*[@id="floating-label-input-:rq:"]')
        self.driver.execute_script(f'document.getElementById("floating-label-input-:rq:").value = "{self.dob}"')

        # Click the Add User button
        add_user_button = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[3]/button')
        add_user_button.click()

        # Wait for the page to load
        time.sleep(3)

        # Verify that the user was successfully created
        email_address = self.driver.find_element(By.XPATH,
                                                 '/html/body/div/section/main/div[2]/div[2]/section/div[3]/div[2]/div/table/tbody/tr[1]/td[3]')
        if not outside_call:
            self.assertEqual(email_address.text, self.fake_email)

    def test_user_deletion_as_expected(self):
        """
        Test case to verify that a user can be deleted successfully.

        Steps:
        1. Login as admin user.
        2. Navigate to the Users page.
        3. Get the first email address from the table.
        4. Delete the user.
        5. Confirm the deletion.
        6. Verify that the email address of the deleted user is not present in the table.

        Returns:
        None
        """
        
        self.driver.get(self.base_url + "/login")

        # wait for the page to load
        # self.driver.implicitly_wait(5)
        time.sleep(5)

        email_input = self.driver.find_element(By.XPATH, "//*[@id=\"username\"]")
        email_input.send_keys("admin@gigatech.com")

        password_input = self.driver.find_element(By.XPATH, "//*[@id=\"password\"]")
        password_input.send_keys("Abc@123")

        login_button = self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/form/button")
        login_button.click()

        user_button_from_sidebar = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/section/main/aside/div/div/div/div[3]/a/div')))
        user_button_from_sidebar.click()

        # get the text in h1 tag
        try:
            h1 = self.driver.find_element(By.TAG_NAME, "h1")
            self.assertEqual(h1.text, "Users")
        except:
            self.fail("Users page not found")

        # Get first email in the table
        first_email = self.driver.find_element(By.XPATH,
                                               '/html/body/div/section/main/div[2]/div[2]/section/div[3]/div[2]/div/table/tbody/tr[1]/td[3]')

        # delete the user
        first_user_table_row_delete_button = self.driver.find_element(By.XPATH,
                                                                      '/html/body/div/section/main/div[2]/div[2]/section/div[3]/div[2]/div/table/tbody/tr[1]/td[8]/div/span[3]/img')
        first_user_table_row_delete_button.click()

        # wait
        self.driver.implicitly_wait(10)

        # confirm the deletion
        delete_confirm_button = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[3]/button[1]')
        delete_confirm_button.click()

        # wait
        self.driver.implicitly_wait(10)

        # check again if the email is the generated one from the previous test
        new_email_address = self.driver.find_element(By.XPATH,
                                                     '/html/body/div/section/main/div[2]/div[2]/section/div[3]/div[2]/div/table/tbody/tr[1]/td[3]').text

        self.assertNotEqual(first_email, new_email_address)

    def test_create_and_delete_same_email_user(self):
        """
        Test case to verify that after deleting a user, same email cannot be used to create a new user

        Steps:
        1. Login as admin user.
        2. Navigate to the Users page.
        3. Create a user with an email
        4. Delete the user.
        5. Create another user with the same email
        6. Verify that the new user was not created
        """

        self.fake_email = self.fake.email()

        self.test_user_creation_expected_data()

        table = self.driver.find_element(By.XPATH, "//*[@id=\"root\"]/section/main/div[2]/div[2]/section/div[3]/div[2]/div/table")

        # Get the number of rows in the table
        rows = table.find_elements(By.TAG_NAME, "tr")
        row_no = 0

        # get the row number of the project where the tr value matches the project name
        for row in rows:
            if self.fake_email in row.text:
                break
            else:
                row_no += 1

        delete_button = self.driver.find_element(By.XPATH, f"//*[@id=\"root\"]/section/main/div[2]/div[2]/section/div[3]/div[2]/div/table/tbody/tr[{row_no}]/td[8]/div/span[3]/img")
        delete_button.click()
        self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[3]/button[1]").click()

        time.sleep(2)

        # logout
        self.driver.find_element(By.XPATH, "/html/body/div/section/main/div[2]/div[1]/nav/div/button").click()
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div").click()

        time.sleep(2)

        self.test_user_creation_expected_data(outside_call=True)

        # Check whether there is an element with required text
        try:
            # message = "Sorry there seem to be an inactive/deleted user associated with this email, reactivate it or use a new email to register"
            # message_element = self.driver.find_elements(By.XPATH, f"//*[contains(text(), {message})]")
            # print(message_element)
            #
            # if not message_element:
            #     self.fail("Message not found")

            top_row_email_address = self.driver.find_element(By.XPATH,
                                                     '/html/body/div/section/main/div[2]/div[2]/section/div[3]/div[2]/div/table/tbody/tr[1]/td[3]')

            self.assertNotEqual(top_row_email_address.text, self.fake_email)
        except Exception as e:
            self.fail("Test failed")


if __name__ == "__main__":
    unittest.main()
    print("Everything passed")
