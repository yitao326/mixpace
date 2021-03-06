import logging
from mixpace.common.common_fun import Common
from mixpace.common.desired_caps import appium_desired
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class LoginView(Common):
    wodeBtn = (By.ID, 'com.mixpace.android.mixpace:id/rbMine')
    TXBtn = (By.ID, 'com.mixpace.android.mixpace:id/tvHead')
    username_type = (By.ID, 'com.mixpace.android.mixpace:id/phone')
    codeBtn = (By.ID, 'com.mixpace.android.mixpace:id/get_code')
    password_type = (By.ID, 'com.mixpace.android.mixpace:id/check_code')
    loginBtn = (By.ID, 'com.mixpace.android.mixpace:id/login_or_reg')
    myMili = (By.ID, 'com.mixpace.android.mixpace:id/ll_rice')
    ivHead = (By.ID, 'com.mixpace.android.mixpace:id/ivHead')
    rlExit = (By.ID, 'com.mixpace.android.mixpace:id/rlExit')
    btnConfirm = (By.ID, 'com.mixpace.android.mixpace:id/btnConfirm')

    def login_action(self, username, password):
        # self.check_openBtn()
        # self.check_cancelBtn()

        self.driver.find_element(*self.wodeBtn).click()
        self.driver.find_element(*self.TXBtn).click()

        logging.info('===login_action===')
        logging.info('�ֻ������� :%s' %username)
        self.driver.find_element(*self.username_type).send_keys(username)

        logging.info('��ȡ��֤��')
        self.driver.find_element(*self.codeBtn).click()

        logging.info('��֤������ :%s' %password)
        self.driver.find_element(*self.password_type).send_keys(password)

        logging.info('�����¼')
        self.driver.find_element(*self.loginBtn).click()
        logging.info('��¼���!')

    def check_loginStatus(self):
        logging.info('===����Ƿ��¼�ɹ�===')
        try:
            self.driver.find_element(*self.myMili)
        except NoSuchElementException:
            logging.error('��¼ʧ��!')
            self.getScreenShot('��¼ʧ��!')
            return False
        else:
            logging.info('��¼�ɹ�')
            self.logout_action()
            return True

    def logout_action(self):
        logging.info('===�˳���¼===')
        self.driver.find_element(*self.ivHead).click()
        self.driver.find_element(*self.rlExit).click()
        self.driver.find_element(*self.btnConfirm).click()




if __name__ == '__main__':
    driver = appium_desired()
    l = LoginView(driver)
    l.login_action('15300752801', '111112')
    l.check_loginStatus()