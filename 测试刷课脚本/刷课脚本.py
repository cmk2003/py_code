import pyautogui
import time
import sys
import time
import keyboard
import os
from PIL import Image
import math
from skimage.metrics import structural_similarity as ssim
from skimage import io,transform

def image_similarity(image1_path, image2_path):
    image1 = io.imread(image1_path, as_gray=True)
    image2 = io.imread(image2_path, as_gray=True)

    # 调整图像大小为相同的尺寸
    min_height = min(image1.shape[0], image2.shape[0])
    min_width = min(image1.shape[1], image2.shape[1])
    image1 = transform.resize(image1[:min_height, :min_width], (min_height, min_width))
    image2 = transform.resize(image2[:min_height, :min_width], (min_height, min_width))

    # 计算SSIM，指定data_range为1
    similarity = ssim(image1, image2, data_range=1)

    return similarity

if __name__ == "__main__":
    # 等待2秒钟，确保你有足够的时间切换到你想要进行操作的窗口（比如浏览器窗口）
    time.sleep(2)
    # 获取当前屏幕的宽度和高度
    screen_width, screen_height = pyautogui.size()
    #鼠标点击播放
    pyautogui.click(x=screen_width // 2, y=700)

    #每隔一分钟截个图，进行比对，看看是否是弹窗或者结束

    # 设置截图保存的文件夹和文件名前缀
    screenshot_folder = "screenshots/"
    filename_prefix = "screenshot"

    # 创建保存截图的文件夹
    try:
        os.makedirs(screenshot_folder)
    except FileExistsError:
        # 如果文件夹已经存在，什么也不做
        pass
    #
    #修改起始位置
    temp = 1
    while True:
        # 获取当前时间作为文件名的一部分，确保文件名是唯一的
        current_time = time.strftime("%Y%m%d_%H%M%S")
        filename = f"{screenshot_folder}{filename_prefix}_{current_time}.png"

        # 截图并保存
        screenshot = pyautogui.screenshot(region=(0, 424, 2193, 1000))
        screenshot.save(filename)

        print(f"截图已保存为 {filename}")
        # 检查文件夹中的图片数量，如果超过10张，删除最早的图片
        screenshots = os.listdir(screenshot_folder)
        if len(screenshots) > 10:
            oldest_screenshot = min(screenshots, key=lambda x: os.path.getctime(os.path.join(screenshot_folder, x)))
            os.remove(os.path.join(screenshot_folder, oldest_screenshot))
            print(f"删除最早的截图: {oldest_screenshot}")

        #检验是否是弹窗或者是结束
        finish_path='finish.png'
        alert_path='alert.png'
        target_path=filename;

        similarity_finish = image_similarity(finish_path, target_path)
        similarity_alert = image_similarity(alert_path, target_path)


        if similarity_finish > similarity_alert and similarity_finish > 0.80:
            print("完成！")
            pyautogui.click(x=2347, y=775 + temp * 100)
            print('y的坐标是:{}'.format(810 + temp * 100))
            temp = temp + 1
            time.sleep(3)
            pyautogui.click(x=screen_width // 2, y=700)
            time.sleep(1)
            if(temp>8):
                sys.exit()
            # sys.exit()
            # pyautogui.click(x=2347, y=1400)
        if similarity_finish < similarity_alert and similarity_alert > 0.70:
            print("弹窗！")
            pyautogui.click(x=1043, y=960)
            time.sleep(1)
            pyautogui.click(x=1043, y=1038)
            time.sleep(1)
            pyautogui.click(x=1043, y=1100)
            pyautogui.click(x=1043, y=1150)
            pyautogui.click(x=1398, y=1372)
            time.sleep(1)
            pyautogui.click(x=1398, y=1372)
            # sys.exit()
        # 等待10s
        time.sleep(10)



    sys.exit()