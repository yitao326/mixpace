from appium import webdriver
from time import sleep
from selenium.common.exceptions import NoSuchElementException       # 导入异常模块
from selenium.webdriver.support.ui import WebDriverWait             # 导入显示等待模块
import yaml
import logging
import logging.config

file = open('../config/mixpace_caps.yaml', 'r')
data = yaml.load(file)

CON_LOG = 'log.conf'
logging.config.fileConfig(CON_LOG)
logging = logging.getLogger()

desired_caps = {}
desired_caps['platformName'] = data['platformName']
desired_caps['platformVersion'] = data['platformVersion']
desired_caps['deviceName'] = data['deviceName']

desired_caps['app'] = data['app']
desired_caps['appPackage'] = data['appPackage']
desired_caps['appActivity'] = data['appActivity']
desired_caps['noReset'] = data['noReset']

logging.info('start app...')
driver = webdriver.Remote('http://'+str(data['ip'])+':'+str(data['port'])+'/wd/hub', desired_caps)
driver.implicitly_wait(2)

WebDriverWait(driver,3).until(lambda x:x.find_element_by_id('com.mixpace.android.mixpace:id/tvPass'))   # 显示等待跳过按钮元素出现
driver.find_element_by_id('com.mixpace.android.mixpace:id/tvPass').click()     # 点击启动页跳过按钮
sleep(3)

# 判断如果有打开定位，则点击打开；没有则跳过异常
def check_openBtn():
    logging.info('check openBtn')
    try:
        openBtn = driver.find_element_by_id('android:id/button1')
    except NoSuchElementException:
        logging.info('no openBtn')
    else:
        openBtn.click()

# 判断如果有打开通知推送，则点击取消；没有则跳过异常
def check_cancelBtn():
    logging.info('check cancelBtn')
    try:
        cancelBtn = driver.find_element_by_id('com.mixpace.android.mixpace:id/tv_cancel')
    except NoSuchElementException:
        logging.info('no cancelBtn')
    else:
        cancelBtn.click()

check_openBtn()
check_cancelBtn()