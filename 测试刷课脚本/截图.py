import pyautogui
import time
import os
# 设置截图保存的文件夹和文件名前缀
screenshot_folder = "screenshots/"
filename_prefix = "screenshot"

# 创建保存截图的文件夹
try:
    os.makedirs(screenshot_folder)
except FileExistsError:
    # 如果文件夹已经存在，什么也不做
    pass

# 循环截图
time.sleep(2)
while True:
    # 获取当前时间作为文件名的一部分，确保文件名是唯一的
    current_time = time.strftime("%Y%m%d_%H%M%S")
    filename = f"{screenshot_folder}{filename_prefix}_{current_time}.png"

    # 截图并保存
    # 0 ，424
    # x=2193, y=1589
    screenshot = pyautogui.screenshot(region=(0,424,2193,1000))
    screenshot.save(filename)

    print(f"截图已保存为 {filename}")
    # 检查文件夹中的图片数量，如果超过10张，删除最早的图片
    screenshots = os.listdir(screenshot_folder)
    if len(screenshots) > 10:
        oldest_screenshot = min(screenshots, key=lambda x: os.path.getctime(os.path.join(screenshot_folder, x)))
        os.remove(os.path.join(screenshot_folder, oldest_screenshot))
        print(f"删除最早的截图: {oldest_screenshot}")
    # 等待1分钟
    time.sleep(1)
