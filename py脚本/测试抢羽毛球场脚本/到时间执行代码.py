import time
import tkinter as tk
import requests

import urllib.parse
import json
while True:
    current_time = time.localtime()
    hour = current_time.tm_hour
    minute = current_time.tm_min

    # 检查是否是13点01分
    if hour == 13 and minute == 1 or 1==1:

        username = '20211003657'
        password = '183813'
        encoded_string = '{"stockdetail": {"12708": "123106", "12709": "123125"}, "serviceid": "1", "stockid": "12709,", "remark": ""}'
        #                 {"stockdetail": {"12707": "123083", "12708": "123102", "12709": "123121"}, "serviceid": "1", "stockid": "12709,", "remark": ""}
        #                 {"stockdetail":{                    "12708":"123101","12709":"123120"},"serviceid":"1","stockid":"12709,","remark":""}
        #{"stockdetail": {"12707": "123081", "12708": "123100", "12709": "123119"}, "serviceid": "1", "stockid": "12709,", "remark": ""}
        print(str(username))
        print(password)
        print(encoded_string)
        # 在这里放入你希望执行的任务代码
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

    # 等待一段时间后再继续检查，避免频繁检查浪费资源
    time.sleep(1)  # 等待60秒（1分钟）
