import requests
import py爬虫.python_sprider.rawDataToJson as rawDataToJson
import py爬虫.python_sprider.金树林.Login as LoginSys

rawHeaders = '''
Mobile-Token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxNzc1MzI5MjYxNDI3MDIzODc0IiwiZXhwIjoxNzEyMTM0ODc3LCJpYXQiOjE3MTIxMzEyNzcsInVzZXJJZCI6IjE3NzUzMjkyNjE0MjcwMjM4NzQiLCJ1c2VybmFtZSI6IjE1NTcyMjYxOTg5In0.nC1T20BbTLMXkK6mQxZcRKMpGSG1trllY-nozcePq58
user-agent: Mozilla/5.0 (Linux; Android 9; SKW-A0 Build/PQ3A.190605.10261546; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.114 Mobile Safari/537.36 uni-app Html5Plus/1.0 (Immersed/24.0)
Content-Type: application/json
Content-Length: 107
Host: miappshop.jshulin.com
Connection: Keep-Alive
Accept-Encoding: gzip
'''.strip()

headers = rawDataToJson.rawDataToJson(rawHeaders)
print(headers)

data = {"cityNo": "", "limit": 10, "orderByContent": "", "page": 1, "productCategoryId": "1649599340962672642",
        "enabled": 1}
url = "https://miappshop.jshulin.com/pro/searchByPage"

Token_json=LoginSys.login();
print(Token_json)
cookies = {
        "token": Token_json['token']
}

r = requests.post(url, cookies=cookies, headers=headers, json=data)
print(r.text)
