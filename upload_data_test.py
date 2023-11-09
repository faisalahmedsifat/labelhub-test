import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

'''@author-HASIB'''
class UploadDataUnitTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url = "http://182.163.99.86"

    def tearDown(self):
        self.driver.quit()

    def test_upload_data(self):
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
        csv_file_path = "/Users/hasibullah/Desktop/My Mac/Study Materials/Summer 2023/CSE434/Labelhub/labelhub-test/bangla-text.csv"  # To absolute PATH 
        file_input.send_keys(csv_file_path)

        select_uploadData_button = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[3]/button")
        select_uploadData_button.click()

        time.sleep(5)

        try:
            project_name_at_top = self.driver.find_element(By.XPATH,
                                                           "//*[@id=\"root\"]/section/main/div[2]/div[2]/section/div[2]/div[2]/div/table/tbody/tr[1]/td[2]/span")
            returned_project_name = project_name_at_top.text
            self.assertEqual(returned_project_name, self.project_name.title())
        except:
            self.fail("Project creation failed")

    
    def test_create_group(self):
        self.group_name = "GROUP NAME"
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





if __name__ == "__main__":
    unittest.main()
    print("Everything passed")