from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait         # 导入显示等待模块
from time import sleep
import yaml
import logging
import logging.config

CON_LOG = '../log/log.conf'
logging.config.fileConfig(CON_LOG)
logging = logging.getLogger()

def appium_desired():
    file = open('../yaml/desired_caps.yaml', 'r')
    data = yaml.load(file)

    desired_caps = {}
    desired_caps['platformName'] = data['platformName']
    desired_caps['platformVersion'] = data['platformVersion']
    desired_caps['deviceName'] = data['deviceName']

    desired_caps['app'] = data['app']
    desired_caps['appPackage'] = data['appPackage']
    desired_caps['appActivity'] = data['appActivity']
    desired_caps['noReset'] = data['noReset']
    desired_caps['unicodeKeyboard'] = data['unicodeKeyboard']
    desired_caps['resetKeyboard'] = data['resetKeyboard']

    logging.info('start app...')
    driver = webdriver.Remote('http://'+str(data['ip'])+':'+str(data['port'])+'/wd/hub', desired_caps)
    driver.implicitly_wait(2)

    WebDriverWait(driver,3).until(lambda x:x.find_element_by_id('com.mixpace.android.mixpace:id/tvPass'))   #显示等待跳过按钮元素出现
    driver.find_element_by_id('com.mixpace.android.mixpace:id/tvPass').click()     # 点击启动页跳过按钮
    sleep(3)
    return driver

if __name__ == '__main__':
    appium_desired()