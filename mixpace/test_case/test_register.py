from mixpace.common.myunit import StartEnd
from mixpace.businessView.registerView import RegisterView
import logging, random, unittest

class RegisterTest(StartEnd):
    def test_user_register(self):
        logging.info('===test_user_register===')
        r = RegisterView(self.driver)

        username = '188' + str(random.randint(1000, 9000)) + str(random.randint(1000, 9000))
        password = '111111'
        # 设置断言
        self.assertTrue(r.register_action(username, password))

if __name__ == '__main__':
    unittest.main()