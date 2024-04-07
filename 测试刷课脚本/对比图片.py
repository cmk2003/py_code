import pyautogui
import time
import sys
import time
import keyboard
import os
from PIL import Image
import math

# 获取当前屏幕的宽度和高度
screen_width, screen_height = pyautogui.size()

def image_similarity(image1_path, image2_path):
    image1 = Image.open(image1_path)
    image2 = Image.open(image2_path)

    # 将图片调整为相同的大小
    image1 = image1.resize(image2.size)

    # 将图片转换为灰度图像
    image1 = image1.convert("L")
    image2 = image2.convert("L")

    # 计算两张图片的像素差异
    diff = 0
    for i in range(image1.width):
        for j in range(image1.height):
            pixel1 = image1.getpixel((i, j))
            pixel2 = image2.getpixel((i, j))
            diff += abs(pixel1 - pixel2)

    # 计算相似度（值越小表示越相似）
    similarity = 1 - (diff / (image1.width * image1.height * 255))

    return similarity

# 比较两张图片的相似度
image1_path = "alert.png"
image2_path = "finish.png"
image3_path = "alert_test.png"
image4_path = "D:\python文件\测试刷课脚本\screenshots\screenshot_20231015_221159.png"
similarity_alert = image_similarity(image1_path, image4_path)
similarity_finish = image_similarity(image2_path, image4_path)

temp=1
if similarity_finish > similarity_alert and similarity_finish > 0.85:
    print("完成！")
    pyautogui.click(x=2347, y=1000+temp*100)
    temp=temp+1
    time.sleep(1)
    pyautogui.click(x=screen_width // 2, y=700)
    time.sleep(1)
    # pyautogui.click(x=2347, y=1400)
if similarity_finish < similarity_alert and similarity_alert > 0.85:
    print("弹窗！")
    pyautogui.click(x=1043, y=933)
    time.sleep(1)
    pyautogui.click(x=1043, y=1038)
    time.sleep(1)
    pyautogui.click(x=1398, y=1372)
    time.sleep(1)
    pyautogui.click(x=1398, y=1372)
# 打印相似度
print("图片相似度：", similarity_alert)
print("图片相似度：", similarity_finish)