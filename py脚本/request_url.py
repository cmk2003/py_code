import requests

url = "http://192.168.38.149/index.php?page=profile&user_id=1"
headers = {
    "X-Forwarded-For": "127.0.0.1"
}

try:
    response = requests.get(url, headers=headers)
    # 检查响应的状态码，200表示请求成功
    if response.status_code == 200:
        print("成功获取响应报文：")
        print(response.text)
    else:
        print(f"请求失败，状态码：{response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"请求发生异常：{e}")
