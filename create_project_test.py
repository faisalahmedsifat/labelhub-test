import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class ProjectCreationDeletion(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url = "http://182.163.99.86"
        self.project_name = "Test Project Creation 000042"
        self.row_no = 1
        self.group_name = "GROUP NAME 05"

    def tearDown(self):
        self.driver.quit()

    def test_create_project_successful(self):
        """
        Tests the successful creation of a project by logging in as an admin user, navigating to the "Projects" page,
        clicking the "Create Project" button, filling out the project name and description, selecting the "NER" annotation
        type, selecting tags for NER, and clicking the "Create" button. Finally, it checks if the project was created
        successfully by verifying that the project name at the top of the "Projects" page matches the expected project name.
        """
        self.row_no = 1
        # driver = self.driver
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

        # wait for the page to load
        # self.driver.implicitly_wait(5)
        time.sleep(5)

        # Go to "Projects" page
        view_projects_button = self.driver.find_element(By.XPATH,
                                                        "//*[@id=\"root\"]/section/main/div[2]/div[2]/section/div/div[1]/div[1]/div/button")
        view_projects_button.click()

        # Click "Create Project" button
        create_project_button = self.driver.find_element(By.XPATH,
                                                         "//*[@id=\"root\"]/section/main/div[2]/div[2]/section/div[1]/button")
        create_project_button.click()

        # Give a name for the project
        project_name_input = self.driver.find_element(By.XPATH, "//*[@id=\"name\"]")
        project_name_input.send_keys(self.project_name)

        # Give a description for the project
        project_description_input = self.driver.find_element(By.XPATH, "//*[@id=\"description\"]")
        project_description_input.send_keys("Dummy test project")

        time.sleep(1)

        # Add "NER" annotation type
        select_annotation_type_button = self.driver.find_element(By.XPATH, "//*[@id=\"1\"]")
        select_annotation_type_button.click()

        # Select tags for NER
        tag_selection_button_1 = self.driver.find_element(By.XPATH,
                                                          "/html/body/div[3]/div/div/div[2]/div/div/section[1]/div[2]/div/div/div/div[1]/button")
        tag_selection_button_1.click()

        tag_selection_button_2 = self.driver.find_element(By.XPATH,
                                                          "/html/body/div[3]/div/div/div[2]/div/div/section[1]/div[2]/div/div/div/div[2]/button")
        tag_selection_button_2.click()

        tag_selection_button_3 = self.driver.find_element(By.XPATH,
                                                          "/html/body/div[3]/div/div/div[2]/div/div/section[1]/div[2]/div/div/div/div[3]/button")
        tag_selection_button_3.click()

        tag_selection_button_4 = self.driver.find_element(By.XPATH,
                                                          "/html/body/div[3]/div/div/div[2]/div/div/section[1]/div[2]/div/div/div/div[4]/button")
        tag_selection_button_4.click()

        # Click "Create" button
        create_button = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[3]/button")
        create_button.click()

        time.sleep(5)
        # /html/body/div/section/main/div[2]/div[2]/section/div/div[2]/div/table/tbody/tr[1]/td[9]/div/a
        select_project_button = self.driver.find_element(By.XPATH, f"/html/body/div/section/main/div[2]/div[2]/section/div[2]/div[2]/div/table/tbody/tr[1]/td[9]/div/span[1]")
        select_project_button.click()

        try:
            
            time.sleep(2)

            project_name_at_top = self.driver.find_element(By.XPATH,
                                                           "/html/body/div/section/main/div[2]/div[2]/section/section[1]/div/div[1]/h4")
            returned_project_name = project_name_at_top.text
            self.assertEqual(returned_project_name, self.project_name.title())

            # wait = WebDriverWait(self.driver, 10)
            # wait.until(EC.alert_is_present(), 'waiting for alert')
            # alert_message = self.driver.switch_to.alert.text
            # self.assertEqual(alert_message, "Project created successfully")
        except:
            self.fail("Project creation failed")

    def test_upload_data(self):
        """
        This method tests the functionality of uploading data to a project in Labelhub.
        It logs in to the Labelhub account, navigates to the project, selects the file to upload, and uploads it.

        Steps:
        1. Login to the Labelhub account using the provided credentials.
        2. Navigate to the project.
        3. Select the file to upload.
        4. Upload the file.
        5. If data is uploaded successfully, the test is passed.
        """
        self.row_no = 1
        self.driver.get(self.base_url + "/login")
        time.sleep(5)

        email_input = self.driver.find_element(By.XPATH, "//*[@id=\"username\"]")
        email_input.send_keys("admin@gigatech.com")

        password_input = self.driver.find_element(By.XPATH, "//*[@id=\"password\"]")
        password_input.send_keys("Abc@123")

        login_button = self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/form/button")
        login_button.click()

        time.sleep(5)

        view_projects_button = self.driver.find_element(By.XPATH,
                                                        "//*[@id=\"root\"]/section/main/div[2]/div[2]/section/div/div[1]/div[1]/div/button")
        view_projects_button.click()

        time.sleep(2)

        select_project_button = self.driver.find_element(By.XPATH, f"//*[@id=\"root\"]/section/main/div[2]/div[2]/section/div[2]/div[2]/div/table/tbody/tr[{self.row_no}]/td[9]/div/span")
        select_project_button.click()

        time.sleep(5)

        select_upload_button = self.driver.find_element(By.XPATH, "/html/body/div[1]/section/main/div[2]/div[2]/section/section[1]/div/div[2]/button[1]")
        select_upload_button.click()

        time.sleep(5)

        file_input = self.driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')

        check_NER_box = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div/section/div[1]/div/div/div[1]/div/div/div/button")
        check_NER_box.click()
        '''YOU HAVE TO CHANGE THE FILE PATH'''
        csv_file_path = "E:/Projects/CSE434/labelhub/bangla-text.csv"  # To absolute PATH 
        file_input.send_keys(csv_file_path)

        select_uploadData_button = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[3]/button")
        select_uploadData_button.click()

        time.sleep(5)

        # if data is uploaded successfully, the test is passed

    
    def test_create_group(self):
        """
        This method tests the creation of a new group in the LabelHub application.
        It logs in as an admin user, navigates to the projects page, selects a project,
        creates a new group with a specified name and label type, adds a validator to the group,
        and saves the changes.
        """

        self.row_no = 1
        self.driver.get(self.base_url + "/login")
        time.sleep(5)

        email_input = self.driver.find_element(By.XPATH, "//*[@id=\"username\"]")
        email_input.send_keys("admin@gigatech.com")

        password_input = self.driver.find_element(By.XPATH, "//*[@id=\"password\"]")
        password_input.send_keys("Abc@123")

        login_button = self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/form/button")
        login_button.click()

        time.sleep(5)

        view_projects_button = self.driver.find_element(By.XPATH,
                                                        "//*[@id=\"root\"]/section/main/div[2]/div[2]/section/div/div[1]/div[1]/div/button")
        view_projects_button.click()

        time.sleep(2)

        select_project_button = self.driver.find_element(By.XPATH, f"//*[@id=\"root\"]/section/main/div[2]/div[2]/section/div[2]/div[2]/div/table/tbody/tr[{self.row_no}]/td[9]/div/span")
        select_project_button.click()

        time.sleep(3)

        self.driver.find_element(By.XPATH, "/html/body/div/section/main/div[2]/div[2]/section/section[4]/div/div/div[1]/button").click()
        time.sleep(3)


        self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div/section[1]/div[1]/input").send_keys(self.group_name)
        self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div/section[1]/div[2]/button").send_keys("Ner")
        self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div/section[2]/div[1]/div/input").send_keys("sifat")
        time.sleep(3)
        self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div/section[2]/div[2]/div/table/tbody/tr/td[1]/button").click()
        self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div/section[2]/div[1]/button").send_keys("Validator")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div/section[2]/div[1]/div/input").send_keys("sifat")
        time.sleep(3)
        self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div/section[2]/div[2]/div/table/tbody/tr/td[1]/div/div/button").click()
        self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[3]/button").click()
        time.sleep(3)

        self.driver.find_element(By.XPATH, "/html/body/div/section/main/div[2]/div[2]/section/section[4]/div/div/div[2]/div/table/tbody/tr[1]/td[9]/div/span[1]/a/img").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "/html/body/div/section/main/div[2]/div[2]/section/section[1]/div/div[2]/button[1]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div/section/div/input").send_keys(2)
        time.sleep(1)
        self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[3]/button").click()
        time.sleep(5)
    
    def test_delete_project(self):
        """
        Test case to verify that a project can be deleted successfully.

        This test case logs in as an admin user, navigates to the "Projects" page,
        selects a project to delete, confirms the deletion, and verifies that the
        project is no longer present in the list of projects.

        Steps:
        1. Log in as an admin user
        2. Navigate to the "Projects" page
        3. Select a project to delete
        4. Confirm the deletion
        5. Verify that the project is no longer present in the list of projects
        """
        self.row_no = 1

        self.driver.get(self.base_url + "/login")
        self.project_name = "Test project creation 000022(HASIB)"

        time.sleep(5)

        email_input = self.driver.find_element(By.XPATH, "//*[@id=\"username\"]")
        email_input.send_keys("admin@gigatech.com")

        password_input = self.driver.find_element(By.XPATH, "//*[@id=\"password\"]")
        password_input.send_keys("Abc@123")

        login_button = self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/form/button")
        login_button.click()

        # wait for the page to load
        # self.driver.implicitly_wait(5)
        time.sleep(5)

        # Go to "Projects" page
        view_projects_button = self.driver.find_element(By.XPATH,
                                "//*[@id=\"root\"]/section/main/div[2]/div[2]/section/div/div[1]/div[1]/div/button")
        view_projects_button.click()

        time.sleep(3)

        delete_button = self.driver.find_element(By.XPATH,
                             f"//*[@id=\"root\"]/section/main/div[2]/div[2]/section/div[2]/div[2]/div/table/tbody/tr[{self.row_no}]/td[9]/div/span[3]/img")
        project_name = self.driver.find_element(By.XPATH,
                            f"//*[@id=\"root\"]/section/main/div[2]/div[2]/section/div[2]/div[2]/div/table/tbody/tr[{self.row_no}]/td[2]/span").text
        delete_button.click()

        # Click "Delete" icon

        confirmation_button = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[3]/button[1]")
        confirmation_button.click()

        time.sleep(1)

        new_project_name = self.driver.find_element(By.XPATH,
                                f"//*[@id=\"root\"]/section/main/div[2]/div[2]/section/div[2]/div[2]/div/table/tbody/tr[{self.row_no}]/td[2]/span").text

        self.assertNotEqual(project_name, new_project_name)


    def test_project_details(self):
        """
        This method tests the project details functionality by logging in as an admin user, navigating to the Projects page,
        clicking on the View button for a specific project, and verifying that the project name on the next page matches the
        project name on the previous page.
        """
        self.driver.get(self.base_url + "/login")

        # wait for the page to load
        # self.driver.implicitly_wait(5)
        time.sleep(3)

        email_input = self.driver.find_element(By.XPATH, "//*[@id=\"username\"]")
        email_input.send_keys("admin@gigatech.com")

        password_input = self.driver.find_element(By.XPATH, "//*[@id=\"password\"]")
        password_input.send_keys("Abc@123")

        login_button = self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/form/button")
        login_button.click()

        # wait for the page to load
        # self.driver.implicitly_wait(5)
        time.sleep(3)

        # Go to "Projects" page
        view_projects_button = self.driver.find_element(By.XPATH,
                                                        "//*[@id=\"root\"]/section/main/div[2]/div[2]/section/div/div[1]/div[1]/div/button")
        view_projects_button.click()

        time.sleep(3)

        # Click "View" icon
        view_button = self.driver.find_element(By.XPATH,
                                               f"//*[@id=\"root\"]/section/main/div[2]/div[2]/section/div[2]/div[2]/div/table/tbody/tr[{self.row_no}]/td[9]/div/span[1]/a/img")
        project_name = self.driver.find_element(By.XPATH,
                                                f"//*[@id=\"root\"]/section/main/div[2]/div[2]/section/div[2]/div[2]/div/table/tbody/tr[{self.row_no}]/td[2]/span").text
        view_button.click()

        time.sleep(3)

        # Get the Project name from the next page
        project_name_in_next_page = self.driver.find_element(By.XPATH,
                                                             "//*[@id=\"root\"]/section/main/div[2]/div[2]/section/section[1]/div/div[1]/h4").text

        self.assertEqual(project_name_in_next_page.title(), project_name)



if __name__ == "__main__":
    unittest.main()
    print("Everything passed")
