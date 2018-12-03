from mixpace.common.myunit import StartEnd
from mixpace.businessView.loginView import LoginView
import unittest
import logging
import warnings

warnings.filterwarnings('ignore')

class TestLogin(StartEnd):
    def test_login_15300752801(self):
        logging.info('===test_login_15300752801===')
        l = LoginView(self.driver)
        l.login_action('15300752801', '111111')

    # def test_login_15300752802(self):
    #     logging.info('===test_login_15300752802===')
    #     l = LoginView(self.driver)
    #     l.login_action('15300752802', '111111')
    #
    # def test_login_error(self):
    #     logging.info('===test_login_error===')
    #     l = LoginView(self.driver)
    #     l.login_action('18000000000', '222222')

if __name__ == '__main__':
    unittest.main()