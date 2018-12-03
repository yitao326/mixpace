from capability import driver
from time import sleep

# 获取屏幕宽度
def get_size():
    x = driver.get_window_size()['width']   # 获取宽度
    y = driver.get_window_size()['height']  # 获取高度
    return x, y
# 打印出屏幕尺寸
l = get_size()
print(l)

# 下拉页面刷新
def dropDown():
    l = get_size()
    x1 = int(l[0]*0.5)        # 0代表x,1代表y
    y1 = int(l[1]*0.3)
    y2 = int(l[1]*0.8)
    driver.swipe(x1, y1, x1, y2, 1000)
for i in range(2):
    dropDown()
    sleep(2)

# 向左屏幕滑动
def swipeLeft():
    l = get_size()
    x1 = int(l[0]*0.9)
    y1 = int(l[1]*0.1)
    x2 = int(l[0]*0.2)
    driver.swipe(x1, y1, x2, y1, 1000)
for i in range(5):
    swipeLeft()
    sleep(2)

# 向下屏幕滑动
def SlideDown():
    l = get_size()
    x1 = int(l[0]*0.5)
    y1 = int(l[1]*0.8)
    y2 = int(l[1]*0.2)
    driver.swipe(x1, y1, x1, y2, 1000)
for i in range(10):
    SlideDown()
    sleep(2)