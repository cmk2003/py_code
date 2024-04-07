import multiprocessing
import requests
import time
import json
import argparse

json_data_='{"stockdetail":{"18960":"185501","18961":"185513"},"serviceid":"3","stockid":"18961,","remark":""}'



def process_task(username, password, encoded_string):
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
    parsed_data = json.loads(response.text)
    print(parsed_data['message'])


if __name__ == "__main__":#20211001363  #101015  20211003657 183813
    username = '20211001363'
    password = '101015'
    json_data = json_data_
#################################################################################
    ###两个小时变成三个小时
    data = json.loads(json_data)
    stock_id_12703 = data.get("stockid").strip(",")
    modified_value = str(int(stock_id_12703) -2)
    print(modified_value)

    value_122983 = str(int(data["stockdetail"][stock_id_12703]) - 38)
    print("value_122983", value_122983)

    data["stockdetail"][str(modified_value)] = value_122983

    # 按照stockdetail字典的键进行排序
    sorted_stockdetail = {k: data["stockdetail"][k] for k in sorted(data["stockdetail"])}

    # 更新data字典中的stockdetail键
    data["stockdetail"] = sorted_stockdetail

    # 将字典转换为JSON字符串
    sorted_json_data = json.dumps(data)

    # 打印更新后的JSON字符串
    # print(sorted_json_data)

    ###一个场变成三个场
    data = json.loads(sorted_json_data)
    # print(data)
    encoded_string=json.dumps(data)
    # print(encoded_string)
    # 循环遍历stockdetail字典，将所有值加一
    payload = []
    payload.append(encoded_string)
    for i in range(3):
        for key in data['stockdetail']:
            data['stockdetail'][key] = str(int(data['stockdetail'][key]) + 1)
        encoded_string1 = json.dumps(data)
        payload.append(encoded_string1)
        # print(encoded_string1)

    for i in payload:
        print("payload", i)



################################################################################################################
    # 创建两个进程并发执行任务
    while True:
        current_time = time.localtime()
        hour = current_time.tm_hour
        minute = current_time.tm_min

        # 检查是否是13点01分
        if (hour == 12 and minute == 0) or(hour == 12 and minute == 1) or 1==1:

            processes = []
            for i in range(len(payload)):
                process=multiprocessing.Process(target=process_task, args=(username, password, payload[i]))
                processes.append(process)
                process.start();
            # 等待所有进程执行完成
            for process in processes:
                process.join()
                # time.sleep(.5)

        time.sleep(1)