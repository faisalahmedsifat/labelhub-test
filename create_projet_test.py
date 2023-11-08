import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MySeleniumUnitTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url = "http://182.163.99.86"

    def tearDown(self):
        self.driver.quit()

    def test_create_project_successful(self):
        self.row_no = 1
        # driver = self.driver
        self.driver.get(self.base_url + "/login")
        self.project_name = "Test project creation 000030(HASIB)"

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

        time.sleep(2)

        select_project_button = self.driver.find_element(By.XPATH, f"//*[@id=\"root\"]/section/main/div[2]/div[2]/section/div[2]/div[2]/div/table/tbody/tr[{self.row_no}]/td[9]/div/span[1]/img")
        select_project_button.click()

        time.sleep(2)

        try:
            project_name_at_top = self.driver.find_element(By.XPATH,
                                                           "//*[@id=\"root\"]/section/main/div[2]/div[2]/section/div[2]/div[2]/div/table/tbody/tr[1]/td[2]/span")
            returned_project_name = project_name_at_top.text
            self.assertEqual(returned_project_name, self.project_name.title())

            # wait = WebDriverWait(self.driver, 10)
            # wait.until(EC.alert_is_present(), 'waiting for alert')
            # alert_message = self.driver.switch_to.alert.text
            # self.assertEqual(alert_message, "Project created successfully")
        except:
            self.fail("Project creation failed")

    # def test_delete_project(self):
    #     self.row_no = 1

    #     self.driver.get(self.base_url + "/login")
    #     self.project_name = "Test project creation 000022(HASIB)"

    #     # wait for the page to load
    #     # self.driver.implicitly_wait(5)
    #     time.sleep(5)

    #     email_input = self.driver.find_element(By.XPATH, "//*[@id=\"username\"]")
    #     email_input.send_keys("admin@gigatech.com")

    #     password_input = self.driver.find_element(By.XPATH, "//*[@id=\"password\"]")
    #     password_input.send_keys("Abc@123")

    #     login_button = self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/form/button")
    #     login_button.click()

    #     # wait for the page to load
    #     # self.driver.implicitly_wait(5)
    #     time.sleep(5)

    #     # Go to "Projects" page
    #     view_projects_button = self.driver.find_element(By.XPATH,
    #                                                     "//*[@id=\"root\"]/section/main/div[2]/div[2]/section/div/div[1]/div[1]/div/button")
    #     view_projects_button.click()

    #     time.sleep(3)

    #     delete_button = self.driver.find_element(By.XPATH,
    #                                              f"//*[@id=\"root\"]/section/main/div[2]/div[2]/section/div[2]/div[2]/div/table/tbody/tr[{self.row_no}]/td[9]/div/span[3]/img")
    #     project_name = self.driver.find_element(By.XPATH,
    #                                             f"//*[@id=\"root\"]/section/main/div[2]/div[2]/section/div[2]/div[2]/div/table/tbody/tr[{self.row_no}]/td[2]/span").text
    #     delete_button.click()

    #     confirmation_button = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[3]/button[1]")
    #     confirmation_button.click()

    #     time.sleep(1)

    #     new_project_name = self.driver.find_element(By.XPATH,
    #                                                 f"//*[@id=\"root\"]/section/main/div[2]/div[2]/section/div[2]/div[2]/div/table/tbody/tr[{self.row_no}]/td[2]/span").text

    #     self.assertNotEqual(project_name, new_project_name)


if __name__ == "__main__":
    unittest.main()
    print("Everything passed")
