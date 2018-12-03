class BaseView(object):
    def __init__(self, driver):
        self.driver = driver
    # 封装定位方法
    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    def find_elements(self, *loc):
        return self.driver.find_elements(*loc)
    # 封装获取屏幕尺寸
    def get_window_size(self, *loc):
        return self.driver.get_window_size(*loc)
    # 封装滑动操作
    def swipe(self, start_x, start_y, end_x, end_y, duration):
        return self.swipe(start_x, start_y, end_x, end_y, duration)
    