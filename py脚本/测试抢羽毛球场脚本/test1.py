import requests

import urllib.parse
import json

if __name__ == "__main__":

    #用户名和密码
    # 给定的URL编码字符串
    encoded_string = "%7B%22stockdetail%22%3A%7B%2212875%22%3A%22124303%22%2C%2212876%22%3A%22124315%22%7D%2C%22serviceid%22%3A%223%22%2C%22stockid%22%3A%2212876%2C%22%2C%22remark%22%3A%22%22%7D"

    # 解码URL编码字符串
    decoded_string = urllib.parse.unquote(encoded_string)

    # 解析JSON字符串
    parsed_json = json.loads(decoded_string)

    # 将字典对象转换为JSON字符串，替换单引号为双引号
    json_with_double_quotes = json.dumps(parsed_json)

    # 打印解析结果
    print(json_with_double_quotes)

    ####

    ####      登录

    ####
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
    jsession=jsessionid

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
        'Cookie': 'JSESSIONID='+jsessionid,
        'Upgrade-Insecure-Requests': '1'
    }

    # 定义请求体数据
    payload = {
        'dlm': '20211003657',
        'mm': '183813',
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
        'Cookie': 'JSESSIONID='+jsessionid+'; errortime=0'
    }

    payload = {
        'param': '{"stockdetail":{"11857":"115489","11858":"115508","11859":"115527"},"serviceid":"1","stockid":"11859,","remark":""}',
        'num': '1',
        'json': 'true'
    }

    response = requests.post(url, headers=headers, data=payload)

    # 输出响应内容
    print(response.text)