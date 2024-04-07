import requests



if __name__ == "__main__":

    #用户名和密码
    username='20211001363'
    password='101015'

    payload='{"stockdetail":{"12663":"122254","12664":"122273"},"serviceid":"1","stockid":"12664,","remark":""}'
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
        'param': '{"stockdetail": {"12874":"124291","12875": "124303", "12876": "124315"}, "serviceid": "3", "stockid": "12876,", "remark": ""}',
        'num': '1',
        'json': 'true'
    }

    response = requests.post(url, headers=headers, data=payload)

    # 输出响应内容
    print(response.text)