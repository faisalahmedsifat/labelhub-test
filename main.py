import unittest
import login_logout_tests

def suite():
    test_loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # Add test cases and test classes to the suite in the desired order
    suite.addTest(test_loader.loadTestsFromTestCase(login_logout_tests.LoginLogoutTests.test_login_successful))
    # suite.addTest(test_loader.loadTestsFromTestCase(ProjectCreationDeletion))
    login_logout_tests = test_loader.loadTestsFromName('login_logout_tests.LoginLogoutTests.test_login_successful')
    print(login_logout_tests)
    # suite.addTest(lg.LoginLogoutTests("test_login_successful"))
    # # Sort the test cases within each test class
    # for test_class in [lg]:
    #     tests = test_loader.loadTestsFromTestCase(test_class)
    #     print(tests)

    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
