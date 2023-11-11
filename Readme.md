## `annotator_test.py`
### `test_annotation_successful`
```
        Test if the annotation process is successful by logging in, selecting a project, 
        annotating a field, and submitting the annotation. The test case passes if the 
        annotation field is present and the submit button is clicked.
        
```
## `annotator_test.py`
### `test_annotation_submission_without_selection`
```
        This function tests the annotation process without selecting any NER values.
        It logs in to the website, selects a project, starts the annotation process, and submits the annotation without selecting any NER values.
        The test case passes if the annotation field is present and the submit button is clicked.
        
```
## `annotator_test.py`
### `test_annotation_skip`
```
        This method tests the functionality of the "Skip" button in the annotation page.
        It logs in to the LabelHub website, navigates to the project page, selects a project,
        and clicks on the "Start" button to start annotating. It then checks if the annotation field
        is present and clicks on the "Skip" button. Finally, it checks if the annotation field is no longer present.
        
```
## `annotator_test.py`
### `test_annotation_reject`
```
        This test case checks if the annotation field is present and rejects the annotation.
        It first creates a project and logs in with the given credentials.
        Then it navigates to the project and finds the row with the project name.
        It clicks on the last td element of the row and starts the annotation.
        It checks if the annotation field is present and rejects the annotation.
        Finally, it checks if the alert box is present.
        
```
## `annotator_test.py`
### `test_annotation_empty_text`
```
        Test annotation with empty text.
        
```
## `annotator_test.py`
### `test_annotation_max_length_text`
```
        Test annotation with maximum length text.
        
```
## `annotator_test.py`
### `test_annotation_exceeding_max_length_text`
```
        Test annotation with text exceeding maximum length.
        
```
## `annotator_test.py`
### `test_annotation_submission_without_NER`
```
        Test annotation submission without selecting any NER.
        
```
## `boundary_value_test.py`
### `test_email_boundary_values`
```
        Test email boundary conditions.

        This test case checks the boundary conditions for email input field. It tests the minimum and maximum length of the
        local part of the email, presence of "@" symbol, presence of domain and top-level domain, and a valid email format.
        
```
## `boundary_value_test.py`
### `test_password_complexity_boundary_values`
```
        Test password complexity boundary conditions.

        This method tests the boundary conditions for password complexity, including passwords that are below the minimum
        length, passwords that meet the minimum length but are missing certain types of characters, passwords that are just
        below the maximum length, passwords that meet the maximum length, and passwords that exceed the maximum length.

        The method uses a dictionary of boundary values, with each key representing a specific test case and each value
        representing a password to be tested. For each test case, the method enters the password into the password field on
        the login page, along with a valid username, and clicks the login button. The method then asserts that the resulting
        page contains an error message indicating that the password is invalid.

        
```
## `boundary_value_test.py`
### `test_input_length_boundary_values`
```
        Test max input length boundary conditions.

        This method tests the max input length boundary conditions, including inputs of length equal to maxlength
        attribute, inputs that are just above the maxlength, and inputs that are below the maxlength.

        The method uses a dictionary of boundary values, with each key representing a specific test case and each value
        representing inputs to be tested. For each test case, the method enters the email and into their respective
        fields on the login page, and clicks the login button. The method then asserts that the resulting page contains
        an error message indicating that the email and password is invalid.
        
```
## `create_project_test.py`
### `test_create_project_successful`
```
        Tests the successful creation of a project by logging in as an admin user, navigating to the "Projects" page,
        clicking the "Create Project" button, filling out the project name and description, selecting the "NER" annotation
        type, selecting tags for NER, and clicking the "Create" button. Finally, it checks if the project was created
        successfully by verifying that the project name at the top of the "Projects" page matches the expected project name.
        
```
## `create_project_test.py`
### `test_upload_data`
```
        This method tests the functionality of uploading data to a project in Labelhub.
        It logs in to the Labelhub account, navigates to the project, selects the file to upload, and uploads it.

        Steps:
        1. Login to the Labelhub account using the provided credentials.
        2. Navigate to the project.
        3. Select the file to upload.
        4. Upload the file.
        5. If data is uploaded successfully, the test is passed.
        
```
## `create_project_test.py`
### `test_create_group`
```
        This method tests the creation of a new group in the LabelHub application.
        It logs in as an admin user, navigates to the projects page, selects a project,
        creates a new group with a specified name and label type, adds a validator to the group,
        and saves the changes.
        
```
## `create_project_test.py`
### `test_delete_project`
```
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
        
```
## `create_project_test.py`
### `test_project_details`
```
        This method tests the project details functionality by logging in as an admin user, navigating to the Projects page,
        clicking on the View button for a specific project, and verifying that the project name on the next page matches the
        project name on the previous page.
        
```
## `create_project_test.py`
### `test_project_creation_valid_data`
```
        Test project creation with valid data.
        
```
## `create_project_test.py`
### `test_project_creation_invalid_data`
```
        Test project creation with invalid data.
        
```
## `create_project_test.py`
### `test_project_deletion_valid_project`
```
        Test project deletion with valid project.
        
```
## `create_project_test.py`
### `test_project_deletion_invalid_project`
```
        Test project deletion with invalid project.
        
```
## `login_logout_tests.py`
### `test_login_successful`
```
        Test case to verify successful login functionality.
        
```
## `login_logout_tests.py`
### `test_login_annotator_successful`
```
        Test case to verify successful login functionality.
        
```
## `login_logout_tests.py`
### `test_login_validator_successful`
```
        Test case to verify successful login functionality.
        
```
## `login_logout_tests.py`
### `test_max_incorrect_login_attempts`
```
        Test the transition to a 'locked' state after maximum incorrect login attempts.

        This test case checks if the lockout mechanism is triggered after 10 incorrect login attempts.
        It enters incorrect login credentials 10 times and checks if the lockout message is displayed.
        
```
## `login_logout_tests.py`
### `test_session_management`
```
        Test that the session is initiated upon login and terminated upon logout.
        
```
## `login_logout_tests.py`
### `test_logout`
```Test the logout feature.

        This method tests the logout feature by first ensuring that the user is logged in, then clicking on the
        expandable button to reveal the logout button. It then clicks on the logout button and ensures that the user is
        redirected to the login page.
        
```
## `login_logout_tests.py`
### `test_login_unsuccessful_incorrect_username`
```
        Test case to verify that login is unsuccessful with incorrect username.

        Steps:
        1. Navigate to login page.
        2. Enter incorrect email in email field.
        3. Enter valid password in password field.
        4. Click on login button.
        5. Verify that error message "Incorrect email or password" is displayed.

        
```
## `login_logout_tests.py`
### `test_login_unsuccessful_incorrect_password`
```
        Test that login is unsuccessful with an incorrect password.

        Steps:
        1. Navigate to the login page.
        2. Enter a valid email address.
        3. Enter an incorrect password.
        4. Click the login button.
        5. Verify that an error message is displayed indicating that the password is incorrect.
        
```
## `login_logout_tests.py`
### `test_login_unsuccessful_incorrect_credentials`
```
        Test case to verify that login is unsuccessful with incorrect credentials.

        Steps:
        1. Load the login page.
        2. Enter incorrect email and password.
        3. Click on the login button.
        4. Verify that the error message is displayed.

        
```
## `login_logout_tests.py`
### `test_login_successful_after_failed_attempt`
```
        Test that login is successful after a failed attempt with incorrect credentials.
        
```
## `login_logout_tests.py`
### `test_login_unsuccessful_empty_username`
```
        Test case to verify that login is unsuccessful when the username field is left empty.
        
```
## `login_logout_tests.py`
### `test_login_unsuccessful_empty_password`
```
        Test case to verify that login is unsuccessful when password field is empty.

        Steps:
        1. Open the login page.
        2. Enter the email address.
        3. Leave the password field empty.
        4. Click on the login button.
        5. Verify that an error message is displayed indicating that the password field is required.
        
```
## `login_logout_tests.py`
### `test_login_unsuccessful_empty_credentials`
```
        Test case to verify that login is unsuccessful when empty credentials are provided.
        
```
## `performance_test.py`
### `measure_load_time`
``` 
        Measures the page load time of a given URL 
        
```
## `performance_test.py`
### `test_login_page_load_time`
```
        Tests the load time of the login page.

        Returns:
            None
        
```
## `performance_test.py`
### `test_login_action_response_time`
```
            Tests the response time of the login action.

            This function tests the response time of the login action by measuring the time it takes for the login button
            to be clicked and for the next page to load or for a login failure message to be displayed.

            Returns:
                None
            
```
## `user_related_tests.py`
### `test_user_creation_expected_data`
```
        Test user creation with expected data.

        This function tests the user creation functionality by filling out the user creation form with expected data and
        verifying that the user is successfully created. It uses the Selenium WebDriver to interact with the web page.

        
```
## `user_related_tests.py`
### `test_user_deletion_as_expected`
```
        Test case to verify that a user can be deleted successfully.

        Steps:
        1. Login as admin user.
        2. Navigate to the Users page.
        3. Get the first email address from the table.
        4. Delete the user.
        5. Confirm the deletion.
        6. Verify that the email address of the deleted user is not present in the table.
        
```
## `user_related_tests.py`
### `test_user_creation_missing_data`
```
        Test user creation with missing data.
        
```
## `user_related_tests.py`
### `test_user_creation_invalid_data`
```
        Test user creation with invalid data.
        
```
## `user_related_tests.py`
### `test_user_deletion_invalid_user`
```
        Test user deletion with invalid user.
        
```
## `user_related_tests.py`
### `test_user_creation_duplicate_data`
```
        Test user creation with duplicate data.
        
```
## `validator_test.py`
### `test_validation_successful`
```
        Tests if the validation is successful by performing the following steps:
        1. Logs in to the website using the provided credentials.
        2. Clicks on the projects button.
        3. Finds the project with the given name.
        4. Clicks on the start button for the project.
        5. Tries to click on the like button and fails if it is not found.
        
```
## `validator_test.py`
### `test_validation_edit_successful`
```
        Test case to validate successful editing of a project in LabelHub.
        This function logs in to LabelHub, navigates to the projects page, finds the project with the given name,
        clicks on the edit button, selects a tag, and submits the changes.
        
```
## `validator_test.py`
### `test_validation_edit_reject_successful`
```
        This test function tests the successful rejection of an edited project in LabelHub. 
        It logs in to the LabelHub account, navigates to the project, edits the project, 
        rejects the changes, and verifies that the changes were rejected successfully.
        
```
## `validator_test.py`
### `test_project_selection_invalid_project`
```
        Test project selection with invalid project name.
        
```
## `validator_test.py`
### `test_project_editing_invalid_tag`
```
        Test project editing with invalid tag.
        
```
## `validator_test.py`
### `test_project_rejection_invalid_project`
```
        Test project rejection with invalid project.
        
```
