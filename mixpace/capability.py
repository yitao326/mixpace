from appium import webdriver
from selenium.common.exceptions import NoSuchElementException   # 导入异常模块
from selenium.webdriver.support.ui import WebDriverWait         # 导入显示等待模块
from time import sleep

desired_caps = {}
# 逍遥模拟器
# desired_caps['platformName'] = 'Android'
# desired_caps['deviceName'] = '127.0.0.1:21503'
# desired_caps['platformVersion'] = '5.1.1'
# 夜神模拟器
desired_caps['platformName'] = 'Android'
desired_caps['deviceName'] = '127.0.0.1:62001'
desired_caps['platformVersion'] = '4.4.2'
# 真机
# desired_caps['platformName'] = 'Android'
# desired_caps['platforVersion'] = '5.1.1'
# desired_caps['deviceName'] = '1546f493'

desired_caps['app'] = r'C:\Users\Administrator\Desktop\mixpace-dev-v1.8.0-official.apk'
desired_caps['appPackage'] = 'com.mixpace.android.mixpace'
desired_caps['appActivity'] = 'com.mixpace.android.mixpace.activity.WelcomeActivity'

desired_caps['noReset'] = 'True'    # True表示保留上次操作结果，False表示每次都是最新操作
desired_caps['unicodeKeyboard'] = 'True'    # 中文输入
desired_caps['resetKeyboard'] = 'True'      # 中文输入

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(2)

WebDriverWait(driver,3).until(lambda x:x.find_element_by_id('com.mixpace.android.mixpace:id/tvPass'))   #显示等待跳过按钮元素出现
driver.find_element_by_id('com.mixpace.android.mixpace:id/tvPass').click()     # 点击启动页跳过按钮
sleep(3)

# 判断如果有打开定位，则点击打开；没有则跳过异常
def check_openBtn():
    print('check openBtn')
    try:
        openBtn = driver.find_element_by_id('android:id/button1')
    except NoSuchElementException:
        print('no openBtn')
    else:
        openBtn.click()

# 判断如果有打开通知推送，则点击取消；没有则跳过异常
def check_cancelBtn():
    print('check cancelBtn')
    try:
        cancelBtn = driver.find_element_by_id('com.mixpace.android.mixpace:id/tv_cancel')
    except NoSuchElementException:
        print('no cancelBtn')
    else:
        cancelBtn.click()

check_openBtn()
check_cancelBtn()