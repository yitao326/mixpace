from mixpace.common.myunit import StartEnd
from mixpace.businessView.loginView import LoginView
import unittest
import logging

class TestLogin(StartEnd):
    csv_file = '../data/account.csv'

    def test_login_15300752801(self):
        logging.info('===test_login_15300752801===')
        l = LoginView(self.driver)
        data = l.get_csv_data(self.csv_file, 1)

        l.login_action(data[0], data[1])
        self.assertTrue(l.check_loginStatus())

    # @unittest.skip('test_login_15300752802')
    def test_login_15300752802(self):
        logging.info('===test_login_15300752802===')
        l = LoginView(self.driver)
        data = l.get_csv_data(self.csv_file, 2)

        l.login_action(data[0], data[1])
        self.assertTrue(l.check_loginStatus())

    # @unittest.skip('test_login_error')
    def test_login_error(self):
        logging.info('===test_login_error===')
        l = LoginView(self.driver)
        data = l.get_csv_data(self.csv_file, 3)

        l.login_action(data[0], data[1])
        self.assertTrue(l.check_loginStatus(), msg='login fail!')

if __name__ == '__main__':
    unittest.main()