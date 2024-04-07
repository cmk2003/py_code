import pyautogui
import time
# 模拟鼠标点击
time.sleep(2)
pyautogui.click()

# 获取鼠标点击的位置
x, y = pyautogui.position()

# 输出鼠标点击的坐标
print(f"鼠标点击的位置：x={x}, y={y}")

#0 ，424
#x=2193, y=1589
