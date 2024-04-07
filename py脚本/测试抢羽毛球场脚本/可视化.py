import tkinter as tk
import requests

import urllib.parse
import json

def submit():
    username = username_entry.get()
    password = password_entry.get()
    encoded_string=url_entry.get()
    print(str(username))
    print(password)
    print(encoded_string)

    # # 解码URL编码字符串
    # decoded_string = urllib.parse.unquote(encoded_string)
    #
    # # 解析JSON字符串
    # parsed_json = json.loads(decoded_string)
    #
    # # 将字典对象转换为JSON字符串，替换单引号为双引号
    # json_with_double_quotes = json.dumps(parsed_json)
    #
    # # 打印解析结果
    # print(json_with_double_quotes)
    # encoded_string=json_with_double_quotes

    # 目标URL
    url = 'http://ydfwpt.cug.edu.cn/login.html'

    # 发送GET请求
    session = requests.Session()
    response = session.get(url)
    print(session.cookies)
    # 获取JSESSIONID
    jsessionid = None
    if 'JSESSIONID' in session.cookies:
        jsessionid = session.cookies['JSESSIONID']

    if jsessionid:
        print('JSESSIONID:', jsessionid)
    else:
        print('未找到JSESSIONID')

    # 定义请求头信息
    # jsession = jsessionid

    # 定义请求URL
    url = 'http://ydfwpt.cug.edu.cn/login.html'

    # 定义请求头部信息
    headers = {
        'Host': 'ydfwpt.cug.edu.cn',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'http://ydfwpt.cug.edu.cn',
        'DNT': '1',
        'Connection': 'close',
        'Referer': 'http://ydfwpt.cug.edu.cn/login/pre.html?continueurl=http://ydfwpt.cug.edu.cn/product/show.html?id=1',
        'Cookie': 'JSESSIONID=' + jsessionid,
        'Upgrade-Insecure-Requests': '1'
    }

    # 定义请求体数据
    payload = {
        'dlm': str(username),
        'mm': str(password),
        'yzm': '1',
        'logintype': 'sno',
        'continueurl': '',
        'openid': ''
    }

    # 发送POST请求
    response1 = requests.post(url, headers=headers, data=payload)

    ####

    ####      定场

    ####

    url = 'http://ydfwpt.cug.edu.cn/order/tobook.html'

    headers = {
        'Host': 'ydfwpt.cug.edu.cn',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Origin': 'http://ydfwpt.cug.edu.cn',
        'DNT': '1',
        'Connection': 'close',
        'Referer': 'http://ydfwpt.cug.edu.cn/product/show.html?id=1',
        'Cookie': 'JSESSIONID=' + jsessionid + '; errortime=0'
    }

    payload = {
        'param': encoded_string,
        'num': '1',
        'json': 'true'
    }

    response = requests.post(url, headers=headers, data=payload)

    # 输出响应内容
    print(response.text)



# 创建主窗口
root = tk.Tk()
root.title("输入用户名和密码和url")

# 设置窗口宽度
window_width = 800
window_height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width / 2) - (window_width / 2)
y_coordinate = (screen_height / 2) - (window_height / 2)

root.geometry("%dx%d+%d+%d" % (window_width, window_height, x_coordinate, y_coordinate))

# 设置字体和颜色
font_style = ("Helvetica", 12)
bg_color = "#f0f0f0"

# 创建用户名和密码的标签和输入框
username_label = tk.Label(root, text="用户名：", font=font_style, bg=bg_color)
username_label.pack(pady=10)
username_entry = tk.Entry(root, font=font_style, bg=bg_color)
username_entry.insert(0, "20211001363")  # 设置默认值为"123456"
username_entry.pack(pady=5)

password_label = tk.Label(root, text="密码：", font=font_style, bg=bg_color)
password_label.pack(pady=10)
password_entry = tk.Entry(root, font=font_style, bg=bg_color)  # 密码输入框，显示为*
password_entry.insert(0, "101015")  # 设置默认值为"123456"
password_entry.pack(pady=5)

url_label = tk.Label(root, text="编码的url：", font=font_style, bg=bg_color)
url_label.pack(pady=10)
url_entry = tk.Entry(root, font=font_style, bg=bg_color,width=150)  # url输入框，显示为*
url_entry.pack(pady=5)
# 创建提交按钮
submit_button = tk.Button(root, text="提交", command=submit, font=font_style, bg="#4caf50", fg="white")
submit_button.pack(pady=20)

# 显示处理后的编码字符串的标签
result_label = tk.Label(root, text="", font=font_style, bg=bg_color)
result_label.pack()

# 启动主循环
root.mainloop()
