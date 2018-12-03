import logging
from mixpace.page_object.common_fun import Common
from mixpace.page_object.desired_caps import appium_desired
from selenium.webdriver.common.by import By

class LoginView(Common):
    wodeBtn = (By.ID, 'com.mixpace.android.mixpace:id/rbMine')
    TXBtn = (By.ID, 'com.mixpace.android.mixpace:id/tvHead')
    username_type = (By.ID, 'com.mixpace.android.mixpace:id/phone')
    codeBtn = (By.ID, 'com.mixpace.android.mixpace:id/get_code')
    password_type = (By.ID, 'com.mixpace.android.mixpace:id/check_code')
    loginBtn = (By.ID, 'com.mixpace.android.mixpace:id/login_or_reg')

    def login_action(self, username, password):
        # self.check_openBtn()
        # self.check_cancelBtn()

        self.driver.find_element(*self.wodeBtn).click()
        self.driver.find_element(*self.TXBtn).click()

        logging.info('===login_action===')
        logging.info('username is:%s' %username)
        self.driver.find_element(*self.username_type).send_keys(username)

        logging.info('click codeBtn')
        self.driver.find_element(*self.codeBtn).click()

        logging.info('password is:%s' %password)
        self.driver.find_element(*self.password_type).send_keys(password)

        logging.info('click loginBtn')
        self.driver.find_element(*self.loginBtn).click()
        logging.info('login finished!')

if __name__ == '__main__':
    driver = appium_desired()