import requests

URL = "http://192.168.38.129:8080/"
PROXY_ENABLED = False
PROXY = "http://192.168.38.129:8080/" if PROXY_ENABLED else None

# 添加headers以模拟浏览器请求
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

try:
    response = requests.get(URL + "/geoserver/ows?service=WFS&version=1.0.0&request=GetCapabilities",
                            proxies={"http": PROXY}, verify=True, headers=headers)

    response.raise_for_status()  # 如果请求不成功，会引发HTTPError异常

    print(response.text)  # 打印响应内容

except requests.exceptions.HTTPError as errh:
    print ("HTTP Error:",errh)

except requests.exceptions.ConnectionError as errc:
    print ("Error Connecting:",errc)

except requests.exceptions.Timeout as errt:
    print ("Timeout Error:",errt)

except requests.exceptions.RequestException as err:
    print ("Something went wrong:",err)
