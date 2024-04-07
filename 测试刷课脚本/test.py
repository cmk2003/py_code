import pyautogui
import time
import sys
import keyboard


# 等待2秒钟，确保你有足够的时间切换到你想要进行操作的窗口（比如浏览器窗口）
time.sleep(2)
# 获取当前屏幕的宽度和高度
screen_width, screen_height = pyautogui.size()
#
# # 模拟鼠标点击浏览器地址栏（可以根据需要修改坐标）
# pyautogui.click(x=screen_width // 2, y=40)
#
# # # 输入网址并按下回车键（这里以百度网站为例）
# pyautogui.write("https://www.baidu.com")
# # 模拟按下回车键
# keyboard.press_and_release('enter')

# 等待加载网页，这个时间可以根据网速调整
# time.sleep(5)

# 模拟鼠标点击浏览器内的某个位置（这里以屏幕中央为例）
pyautogui.click(x=screen_width // 2, y=screen_height // 2+100)
# 获取屏幕截图
screenshot = pyautogui.screenshot()

# 保存截图到文件
screenshot.save("screenshot1.png")
# 这里可以继续模拟其他鼠标操作，比如拖拽、右键点击等

# 退出
sys.exit()
