from mixpace.common.myunit import StartEnd
from mixpace.businessView.registerView import RegisterView
import logging, random, unittest

class RegisterTest(StartEnd):
    def test_user_register(self):
        logging.info('===test_user_register===')
        r = RegisterView(self.driver)

        username = 'aaa' + 'fly' + str(random.randint(1000, 9000))
        password = 'bbb' + str(random.randint(1000, 9000))
        email = 'ccc' + str(random.randint(1000, 9000)) + '@163.com'
        # 设置断言
        self.assertTrue(r.register_action(username, password, email))

if __name__ == '__main__':
    unittest.main()