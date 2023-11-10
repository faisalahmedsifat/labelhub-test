## `annotator_test.py`
### `test_annotation_successful`
```
        Test if the annotation process is successful by logging in, selecting a project, 
        annotating a field, and submitting the annotation. The test case passes if the 
        annotation field is present and the submit button is clicked.
        
```
## `annotator_test.py`
### `test_annotation_without_selecting_any_ner_values`
```
        This function tests the annotation process without selecting any NER values.
        It logs in to the website, selects a project, starts the annotation process, and submits the annotation without selecting any NER values.
        The test case passes if the annotation field is present and the submit button is clicked.
        
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
## `create_project_test.py`
### `test_create_project_successful`
```
        Tests the successful creation of a project by logging in as an admin user, navigating to the "Projects" page,
        clicking the "Create Project" button, filling out the project name and description, selecting the "NER" annotation
        type, selecting tags for NER, and clicking the "Create" button. Finally, it checks if the project was created
        successfully by verifying that the project name at the top of the "Projects" page matches the expected project name.
        
```
## `create_project_test.py`
### `test_delete_project`
```
        Test case to verify that a project can be deleted successfully.
        
```
## `create_project_test.py`
### `test_project_details`
```
        This method tests the project details functionality by logging in as an admin user, navigating to the Projects page,
        clicking on the View button for a specific project, and verifying that the project name on the next page matches the
        project name on the previous page.
        
```
## `login_logout_tests.py`
### `test_login_successful`
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
## `upload_data_test.py`
### `test_upload_data`
```
        This method tests the functionality of uploading data to a project in Labelhub.
        It logs in to the Labelhub account, navigates to the project, selects the file to upload, and uploads it.
        
```
## `upload_data_test.py`
### `test_create_group`
```
        This method tests the creation of a new group in the LabelHub application.
        It logs in as an admin user, navigates to the projects page, selects a project,
        creates a new group with a specified name and label type, adds a validator to the group,
        and saves the changes.
        
```
## `user_related_tests.py`
### `test_user_creation_expected_data`
```
        Test user creation with expected data.

        This function tests the user creation functionality by filling out the user creation form with expected data and
        verifying that the user is successfully created. It uses the Selenium WebDriver to interact with the web page.

        Args:
            self: The TestUserRelated class instance.

        Returns:
            None
        
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

        Returns:
        None
        
```
