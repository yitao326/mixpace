from mixpace.page_object.baseView import BaseView
from mixpace.page_object.desired_caps import appium_desired
from selenium.common.exceptions import NoSuchElementException
import logging
from selenium.webdriver.common.by import By

class Common(BaseView):
    openBtn = (By.ID, 'android:id/button1')
    cancelBtn = (By.ID, 'com.mixpace.android.mixpace:id/tv_cancel')

    def check_openBtn(self):
        logging.info('====check_openBtn====')
        try:
            openBtn = driver.find_element(*self.openBtn)
        except NoSuchElementException:
            logging.info('no openBtn')
        else:
            openBtn.click()

    def check_cancelBtn(self):
        logging.info('===check cancelBtn===')
        try:
            cancelBtn = driver.find_element(*self.cancelBtn)
        except NoSuchElementException:
            logging.info('no cancelBtn')
        else:
            cancelBtn.click()

if __name__ == '__main__':
    driver = appium_desired()
    com = Common(driver)
    com.check_openBtn()
    com.check_cancelBtn()



