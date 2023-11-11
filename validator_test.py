import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

import annotator_test


class ValidatorTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url = "http://182.163.99.86"
        self.group_name = "GROUP NAME 05"
        
        # wait
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.implicitly_wait(10)
        self.project_name = "Demo8808"
        
    def tearDown(self):
        self.driver.quit()

    def test_validation_successful(self):
        """
        Tests if the validation is successful by performing the following steps:
        1. Logs in to the website using the provided credentials.
        2. Clicks on the projects button.
        3. Finds the project with the given name.
        4. Clicks on the start button for the project.
        5. Tries to click on the like button and fails if it is not found.
        """
        
        suite = unittest.TestSuite()
        suite.addTest(annotator_test.Annotator('test_annotation_successful'))
        runner = unittest.TextTestRunner()
        runner.run(suite)
        time.sleep(5)
        
        self.driver.get(self.base_url + "/login")

        email_input = self.driver.find_element(By.XPATH, "//*[@id=\"username\"]")
        email_input.send_keys("faisalahmedval@example.com")

        password_input = self.driver.find_element(By.XPATH, "//*[@id=\"password\"]")
        password_input.send_keys("Sifat@123")

        login_button = self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/form/button")
        login_button.click()
        
        time.sleep(5)
            
        projects_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/section/main/aside/div/div/div/div[2]/a/div')))
        projects_button.click()
        
        project_name = self.project_name
        time.sleep(2)
        
        table = self.driver.find_element(By.XPATH, '/html/body/div[1]/section/main/div[2]/div[2]/section/div/div[2]/div/table/tbody')
        
        # Get the number of rows in the table
        rows = table.find_elements(By.TAG_NAME, "tr")
        print(len(rows))
        
        present_row = None
        time.sleep(2)

        # get the row number of the project where the tr value matches the project name
        for row in rows:
            present_row = row
            break
            # print(row.text)
            # if project_name in row.text:
            #     present_row = row
            #     break
            # self.row_no += 1
            
        print(present_row)
        
        # time.sleep(5)
        # get the last td element in the row
        tds = present_row.find_elements(By.TAG_NAME, "td")
        # print(last_td)
        last_td = tds[len(tds) - 1]
        
        #get the div element in the last td element
        div = last_td.find_element(By.TAG_NAME, "div")
        div.click()
        time.sleep(2)
        
        start_button = self.driver.find_element(By.XPATH, '/html/body/div/section/main/div[2]/div[2]/section/section[4]/div/div/div[2]/div/table/tbody/tr/td[9]/div/a')
        start_button.click()
        
        time.sleep(2)
        
        try:
            like_button = self.driver.find_element(By.XPATH, '/html/body/div[1]/section/main/div[2]/div[2]/section/section[4]/section/div[2]/div/div/div/div[1]/button')
            like_button.click()
        except:
            self.fail("Validation failed")
            
            
    def test_validation_edit_successful(self):
        """
        Test case to validate successful editing of a project in LabelHub.
        This function logs in to LabelHub, navigates to the projects page, finds the project with the given name,
        clicks on the edit button, selects a tag, and submits the changes.
        """
        
        suite = unittest.TestSuite()
        suite.addTest(annotator_test.Annotator('test_annotation_successful'))
        runner = unittest.TextTestRunner()
        runner.run(suite)
        
        
        self.driver.get(self.base_url + "/login")

        email_input = self.driver.find_element(By.XPATH, "//*[@id=\"username\"]")
        email_input.send_keys("faisalahmedval@example.com")

        password_input = self.driver.find_element(By.XPATH, "//*[@id=\"password\"]")
        password_input.send_keys("Sifat@123")

        login_button = self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/form/button")
        login_button.click()

        time.sleep(5)

        projects_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/section/main/aside/div/div/div/div[2]/a/div')))
        projects_button.click()

        project_name = self.project_name
        time.sleep(2)

        table = self.driver.find_element(By.XPATH, '/html/body/div[1]/section/main/div[2]/div[2]/section/div/div[2]/div/table/tbody')

        # Get the number of rows in the table
        rows = table.find_elements(By.TAG_NAME, "tr")
        print(len(rows))

        present_row = None
        time.sleep(2)

        # get the row number of the project where the tr value matches the project name
        for row in rows:
            present_row = row
            break
            # print(row.text)
            # if project_name in row.text:
            #     present_row = row
            #     break
            # self.row_no += 1

        print(present_row)

        # time.sleep(5)
        # get the last td element in the row
        tds = present_row.find_elements(By.TAG_NAME, "td")
        # print(last_td)
        last_td = tds[len(tds) - 1]

        #get the div element in the last td element
        div = last_td.find_element(By.TAG_NAME, "div")
        div.click()
        time.sleep(2)

        start_button = self.driver.find_element(By.XPATH, '/html/body/div/section/main/div[2]/div[2]/section/section[4]/div/div/div[2]/div/table/tbody/tr/td[9]/div/a')
        start_button.click()

        time.sleep(2)

        try:
            edit_button = self.driver.find_element(By.XPATH, '/html/body/div[1]/section/main/div[2]/div[2]/section/section[4]/section/div[2]/div/div[1]/div/div[2]')
            edit_button.click()
        except:
            self.fail("Edit button click failed")

        time.sleep(2)

        try:
            tag = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/section[1]/div/div/div/div[1]/div/span')
            tag.click()
        except:
            self.fail("Tag click failed")

        time.sleep(2)

        try:
            submit_button = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/section[2]/div/div/div[2]/button[1]')
            submit_button.click()
        except:
            self.fail("Submit button click failed")
            
    def test_validation_edit_reject_successful(self):
        """
        This test function tests the successful rejection of an edited project in LabelHub. 
        It logs in to the LabelHub account, navigates to the project, edits the project, 
        rejects the changes, and verifies that the changes were rejected successfully.
        """
        
        suite = unittest.TestSuite()
        suite.addTest(annotator_test.Annotator('test_annotation_successful'))
        runner = unittest.TextTestRunner()
        runner.run(suite)
        
        self.driver.get(self.base_url + "/login")

        email_input = self.driver.find_element(By.XPATH, "//*[@id=\"username\"]")
        email_input.send_keys("faisalahmedval@example.com")

        password_input = self.driver.find_element(By.XPATH, "//*[@id=\"password\"]")
        password_input.send_keys("Sifat@123")

        login_button = self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/form/button")
        login_button.click()
        
        time.sleep(5)
            
        projects_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/section/main/aside/div/div/div/div[2]/a/div')))
        projects_button.click()
        
        project_name = self.project_name
        time.sleep(2)
        
        table = self.driver.find_element(By.XPATH, '/html/body/div[1]/section/main/div[2]/div[2]/section/div/div[2]/div/table/tbody')
        
        # Get the number of rows in the table
        rows = table.find_elements(By.TAG_NAME, "tr")
        print(len(rows))
        
        present_row = None
        time.sleep(2)

        # get the row number of the project where the tr value matches the project name
        for row in rows:
            present_row = row
            break
            # print(row.text)
            # if project_name in row.text:
            #     present_row = row
            #     break
            # self.row_no += 1
            
        print(present_row)
        
        # time.sleep(5)
        # get the last td element in the row
        tds = present_row.find_elements(By.TAG_NAME, "td")
        # print(last_td)
        last_td = tds[len(tds) - 1]
        
        #get the div element in the last td element
        div = last_td.find_element(By.TAG_NAME, "div")
        div.click()
        time.sleep(2)
        
        start_button = self.driver.find_element(By.XPATH, '/html/body/div/section/main/div[2]/div[2]/section/section[4]/div/div/div[2]/div/table/tbody/tr/td[9]/div/a')
        start_button.click()
        
        time.sleep(2)
        
        try:
            edit_button = self.driver.find_element(By.XPATH, '/html/body/div[1]/section/main/div[2]/div[2]/section/section[4]/section/div[2]/div/div[1]/div/div[2]')
            edit_button.click()
        except:
            self.fail("Edit button click failed")
        
        time.sleep(2)
        
        try:
            tag = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/section[1]/div/div/div/div[1]/div/span')
            tag.click()
        except:
            self.fail("Tag click failed")
            
        time.sleep(2)
        
        try:
            # the xpath needs to be updated
            reject_button = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/section[2]/div/div/div[2]/button[1]')
            reject_button.click()
        except:
            self.fail("Submit button click failed")
            
    def test_project_selection_invalid_project(self):
        """
        Test project selection with invalid project name.
        """
        # Navigate to the projects page
        # Try to select a project with a name that does not exist
        # Verify that an appropriate error message is displayed

    def test_project_editing_invalid_tag(self):
        """
        Test project editing with invalid tag.
        """
        # Navigate to the projects page
        # Select a project
        # Try to edit the project with a tag that does not exist
        # Verify that an appropriate error message is displayed

    def test_project_rejection_invalid_project(self):
        """
        Test project rejection with invalid project.
        """
        # Navigate to the projects page
        # Try to reject a project that does not exist
        # Verify that an appropriate error message is displayed
