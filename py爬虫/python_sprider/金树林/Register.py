import requests
import py爬虫.python_sprider.rawDataToJson as rawDataToJson

url = 'https://miappshop.jshulin.com/memberLogin/memberRegister'

raw_headers = """
Mobile-Token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxNzc1MzI5MjYxNDI3MDIzODc0IiwiZXhwIjoxNzEyMTEwMDU0LCJpYXQiOjE3MTIxMDY0NTQsInVzZXJJZCI6IjE3NzUzMjkyNjE0MjcwMjM4NzQiLCJ1c2VybmFtZSI6IjE1NTcyMjYxOTg5In0.PwBPIsN-dH4v4Ysf8htMTYXyqnd4HS1JoZNmKd9B7ZA
user-agent: Mozilla/5.0 (Linux; Android 9; SKW-A0 Build/PQ3A.190605.10261546; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.114 Mobile Safari/537.36 uni-app Html5Plus/1.0 (Immersed/24.0)
Content-Type: application/json
Content-Length: 72
Host: miappshop.jshulin.com
Connection: Keep-Alive
Accept-Encoding: gzip
""".strip()

# Initialize dictionaries
headers= rawDataToJson.rawDataToJson(raw_headers)

# print(cookies,"\n")
print(headers)

data={"phone":"15572261989","fid":"","password":"1111111","phoneCode":"802780"}

response = requests.post(url, headers=headers, json=data)

print(response.text)
