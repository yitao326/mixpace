from mixpace.baseView.baseView import BaseView
from mixpace.common.desired_caps import appium_desired
from selenium.common.exceptions import NoSuchElementException
import logging
from selenium.webdriver.common.by import By
import time, os
import csv

# 封装公共模块
class Common(BaseView):
    openBtn = (By.ID, 'android:id/button1')
    cancelBtn = (By.ID, 'com.mixpace.android.mixpace:id/tv_cancel')
    # 进入首页判断是否需要定位弹框
    def check_openBtn(self):
        logging.info('====定位弹窗====')
        try:
            openBtn = driver.find_element(*self.openBtn)
        except NoSuchElementException:
            logging.info('没有定位弹窗')
        else:
            openBtn.click()
    # 进入首页判断是否需要推送弹框
    def check_cancelBtn(self):
        logging.info('===权限窗口===')
        try:
            cancelBtn = driver.find_element(*self.cancelBtn)
        except NoSuchElementException:
            logging.info('没有权限窗口')
        else:
            cancelBtn.click()
    # 获取屏幕尺寸
    def get_size(self):
        x = self.driver.get_window_size()['width']  # 获取宽度
        y = self.driver.get_window_size()['height']  # 获取高度
        return x, y
    # 向左滑动
    def dropDown(self):
        logging.info('左滑')
        l = self.get_size()
        x1 = int(l[0] * 0.5)  # 0代表x,1代表y
        y1 = int(l[1] * 0.3)
        y2 = int(l[1] * 0.8)
        self.driver.swipe(x1, y1, x1, y2, 1000)
    # 获取时间格式
    def getTime(self):
        self.now = time.strftime("%Y-%m-%d %H_%M_%S")
        return self.now
    # 截图
    def getScreenShot(self,module):
        time = self.getTime()
        image_file = os.path.dirname(os.path.dirname(__file__))+'/screenshots/%s_%s.png' %(module, time)

        logging.info('get %s screenshot' %module)
        self.driver.get_screenshot_as_file(image_file)
    # 引入data测试数据
    def get_csv_data(self, csv_file, line):
        logging.info('===get_csv_data===')
        with open(csv_file, 'r', encoding='utf-8-sig') as file:
            reader = csv.reader(file)
            for index, row in enumerate(reader, 1):
                if index == line:
                    return row

if __name__ == '__main__':
    driver = appium_desired()
    com = Common(driver)
    com.check_openBtn()
    com.check_cancelBtn()
    com.dropDown()
    com.getScreenShot('启动APP')