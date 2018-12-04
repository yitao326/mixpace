import logging, random
from mixpace.common.desired_caps import appium_desired
from mixpace.common.common_fun import Common, By, NoSuchElementException


class RegisterView(Common):
    # 我的模块点击头像登录
    rbMine = (By.ID, 'com.mixpace.android.mixpace:id/rbMine')
    ivHead = (By.ID, 'com.mixpace.android.mixpace:id/ivHead')

    # 输入手机号获取验证码点击登录
    phone = (By.ID, 'com.mixpace.android.mixpace:id/phone')
    get_code = (By.ID, 'com.mixpace.android.mixpace:id/get_code')
    check_code = (By.ID, 'com.mixpace.android.mixpace:id/check_code')
    login_or_reg = (By.ID, 'com.mixpace.android.mixpace:id/login_or_reg')

    # 设置密码
    etPassword = (By.ID, 'com.mixpace.android.mixpace:id/etPassword')
    etPasswordAgain = (By.ID, 'com.mixpace.android.mixpace:id/etPasswordAgain')
    btnLogin = (By.ID, 'com.mixpace.android.mixpace:id/btnLogin')

    btnJoin = (By.ID, 'com.mixpace.android.mixpace:id/btnJoin')

    # 设置资料
    ivRight = (By.ID, 'com.mixpace.android.mixpace:id/ivRight')
    rlNickname = (By.ID, 'com.mixpace.android.mixpace:id/rlNickname')
    etNickname = (By.ID, 'com.mixpace.android.mixpace:id/etNickname')
    tvRight = (By.ID, 'com.mixpace.android.mixpace:id/tvRight')

    def register_action(self,register_username,register_password):
        # self.check_openBtn()
        # self.check_cancelBtn()

        self.driver.find_element(*self.rbMine).click()
        self.driver.find_element(*self.ivHead).click()

        logging.info('输入手机号 %s' % register_username)
        self.driver.find_element(*self.phone).send_keys(register_username)
        self.driver.find_element(*self.get_code).click()
        logging.info('输入验证码 %s' % register_password)
        self.driver.find_element(*self.check_code).send_keys(register_password)
        self.driver.find_element(*self.login_or_reg).click()

        self.driver.find_element(*self.etPassword).send_keys('111111')
        self.driver.find_element(*self.etPasswordAgain).send_keys('111111')
        self.driver.find_element(*self.btnLogin).click()

    def check_register_status(self):
        logging.info('=====判断是否登录成功=====')
        try:
            self.driver.find_element(*self.btnJoin)
        except NoSuchElementException:
            logging.error('注册失败!')
            self.getScreenShot('注册失败')
            return False
        else:
            logging.info('注册成功!')
            return True


if __name__ == '__main__':
    driver = appium_desired()
    register = RegisterView(driver)

    username = '188' + str(random.randint(1000, 9000)) + str(random.randint(1000, 9000))
    password = '111111'

    register.register_action(username, password)
