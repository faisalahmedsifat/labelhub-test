import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import login_logout_tests as unit_tests

from faker import Faker
import time
import random


class Annotator(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url = "http://182.163.99.86"
        self.row_no = 0
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.implicitly_wait(10)
        self.project_name = "Project1"

    def tearDown(self):
        self.driver.quit()
        
        
    def test_annotation_successful(self):
        """
        Test if the annotation process is successful by logging in, selecting a project, 
        annotating a field, and submitting the annotation. The test case passes if the 
        annotation field is present and the submit button is clicked.
        """
        
        self.driver.get(self.base_url + "/login")

        email_input = self.driver.find_element(By.XPATH, "//*[@id=\"username\"]")
        email_input.send_keys("faisalahmedann@example.com")

        password_input = self.driver.find_element(By.XPATH, "//*[@id=\"password\"]")
        password_input.send_keys("Sifat@123")

        login_button = self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/form/button")
        login_button.click()
        
        time.sleep(5)
            
        projects_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/section/main/aside/div/div/div/div[2]/a/div')))
        projects_button.click()
        
        # self.driver.implicitly_wait(10)
        
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
            print(row.text)
            if project_name in row.text:
                present_row = row
                break
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
            ner_field = self.driver.find_element(By.XPATH, '/html/body/div/section/main/div[2]/div[2]/section[3]/div/div/div')
            
            #if the field is present, then the test case passes
            self.assertTrue(ner_field)
        except:
            self.fail("Annotation field is not present: ")

        noun_divs = self.driver.find_elements(By.XPATH, '/html/body/div/section/main/div[2]/div[2]/section[2]/div/div')
        ner_words = self.driver.find_elements(By.XPATH, '/html/body/div/section/main/div[2]/div[2]/section[3]/div/div/div')
        for spans in noun_divs:
            spans.click()
            time.sleep(2)
            
            # randomly select a span from the ner_words list
            random_span = random.choice(ner_words)
            random_span.click()
            time.sleep(2)
            break;
        
        submit_button = self.driver.find_element(By.XPATH, '/html/body/div/section/main/div[2]/div[2]/section[3]/div/div/footer/button[1]')
        submit_button.click()
        
        # the test case passes if the submit button was clicked
        self.assertTrue(submit_button) 
        
    def test_annotation_submission_without_selection(self):
        
        """
        This function tests the annotation process without selecting any NER values.
        It logs in to the website, selects a project, starts the annotation process, and submits the annotation without selecting any NER values.
        The test case passes if the annotation field is present and the submit button is clicked.
        """

        self.driver.get(self.base_url + "/login")

        email_input = self.driver.find_element(By.XPATH, "//*[@id=\"username\"]")
        email_input.send_keys("faisalahmedann@example.com")

        password_input = self.driver.find_element(By.XPATH, "//*[@id=\"password\"]")
        password_input.send_keys("Sifat@123")

        login_button = self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/form/button")
        login_button.click()
        
        time.sleep(5)

        
            
        projects_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/section/main/aside/div/div/div/div[2]/a/div')))
        projects_button.click()
        
        # self.driver.implicitly_wait(10)
        
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
            print(row.text)
            if project_name in row.text:
                present_row = row
                break
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
            ner_field = self.driver.find_element(By.XPATH, '/html/body/div/section/main/div[2]/div[2]/section[3]/div/div/div')
            
            #if the field is present, then the test case passes
            self.assertTrue(ner_field)
        except:
            self.fail("Annotation field is not present: ")

        
        submit_button = self.driver.find_element(By.XPATH, '/html/body/div/section/main/div[2]/div[2]/section[3]/div/div/footer/button[1]')
        submit_button.click()
        
        # time.sleep(5)
        
        try:
            time.sleep(5)
            
            # get the dialog box
            dialog_box_button = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[3]/button[1]')
            dialog_box_button.click()
            self.assertTrue(dialog_box_button)
        except:
            self.fail("Alert box is not present")
        
    def test_annotation_skip(self):
        """
        This method tests the functionality of the "Skip" button in the annotation page.
        It logs in to the LabelHub website, navigates to the project page, selects a project,
        and clicks on the "Start" button to start annotating. It then checks if the annotation field
        is present and clicks on the "Skip" button. Finally, it checks if the annotation field is no longer present.
        """
        self.driver.get(self.base_url + "/login")

        email_input = self.driver.find_element(By.XPATH, "//*[@id=\"username\"]")
        email_input.send_keys("faisalahmedann@example.com")

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
            print(row.text)
            if project_name in row.text:
                present_row = row
                break

        print(present_row)

        # get the last td element in the row
        tds = present_row.find_elements(By.TAG_NAME, "td")
        last_td = tds[len(tds) - 1]

        #get the div element in the last td element
        div = last_td.find_element(By.TAG_NAME, "div")
        div.click()
        time.sleep(2)

        start_button = self.driver.find_element(By.XPATH, '/html/body/div/section/main/div[2]/div[2]/section/section[4]/div/div/div[2]/div/table/tbody/tr/td[9]/div/a')
        start_button.click()
        test_at_a_random_pos = None
        time.sleep(2)
        try:
            ner_field = self.driver.find_element(By.XPATH, '/html/body/div/section/main/div[2]/div[2]/section[3]/div/div/div')
            # /html/body/div[1]/section/main/div[2]/div[2]/section[3]/div/div/div/span[2]
            test_at_a_random_pos = self.driver.find_element(By.XPATH, '/html/body/div/section/main/div[2]/div[2]/section[3]/div/div/div/span[2]')
            #if the field is present, then the test case passes
            self.assertTrue(ner_field)
        except:
            self.fail("Annotation field is not present: ")

        skip_button = self.driver.find_element(By.XPATH, '/html/body/div[1]/section/main/div[2]/div[2]/section[3]/div/div/footer/button[2]')
        skip_button.click()

        time.sleep(2)

        try:
            ner_field = self.driver.find_element(By.XPATH, '/html/body/div/section/main/div[2]/div[2]/section[3]/div/div/div')
            self.fail("Annotation field is still present after clicking on Skip button")
        except:
            pass
        
        
    def test_annotation_reject(self):
        
        self.driver.get(self.base_url + "/login")

        email_input = self.driver.find_element(By.XPATH, "//*[@id=\"username\"]")
        email_input.send_keys("faisalahmedann@example.com")

        password_input = self.driver.find_element(By.XPATH, "//*[@id=\"password\"]")
        password_input.send_keys("Sifat@123")

        login_button = self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/form/button")
        login_button.click()
        
        time.sleep(5)

        
            
        projects_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/section/main/aside/div/div/div/div[2]/a/div')))
        projects_button.click()
        
        # self.driver.implicitly_wait(10)
        
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
            print(row.text)
            if project_name in row.text:
                present_row = row
                break
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
            ner_field = self.driver.find_element(By.XPATH, '/html/body/div/section/main/div[2]/div[2]/section[3]/div/div/div')
            
            #if the field is present, then the test case passes
            self.assertTrue(ner_field)
        except:
            self.fail("Annotation field is not present: ")

        
        reject_button = self.driver.find_element(By.XPATH, '/html/body/div/section/main/div[2]/div[2]/section[3]/div/div/footer/button[3]')
        reject_button.click()
        
        # time.sleep(5)
        
        try:
            time.sleep(5)
            # /html/body/div[3]/div/div/div[3]/button[1]
            # get the dialog box
            dialog_box_button = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[3]/button[1]')
            dialog_box_button.click()
            self.assertTrue(dialog_box_button)
        except:
            self.fail("Alert box is not present")
        

    
    
    


if __name__ == "__main__":
    unittest.main()
    print("Everything passed")
