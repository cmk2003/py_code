import requests
import py爬虫.python_sprider.rawDataToJson as rawDataToJson

def login():
    url_ = 'https://miappshop.jshulin.com/memberLogin/login'

    data = {'username': '15572261989', 'password': 'asdfghjkl'}

    raw_data = '''
Mobile-Token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxNzc1MzI5MjYxNDI3MDIzODc0IiwiZXhwIjoxNzEyMTEwMDU0LCJpYXQiOjE3MTIxMDY0NTQsInVzZXJJZCI6IjE3NzUzMjkyNjE0MjcwMjM4NzQiLCJ1c2VybmFtZSI6IjE1NTcyMjYxOTg5In0.PwBPIsN-dH4v4Ysf8htMTYXyqnd4HS1JoZNmKd9B7ZA
user-agent: Mozilla/5.0 (Linux; Android 9; SKW-A0 Build/PQ3A.190605.10261546; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.114 Mobile Safari/537.36 uni-app Html5Plus/1.0 (Immersed/24.0)
Content-Type: application/json
Content-Length: 49
Host: miappshop.jshulin.com
Connection: Keep-Alive
Accept-Encoding: gzip
    '''

    # Ensure no leading whitespace in header names
    # headers = rawDataToJson.rawDataToJson('\n'.join([line.strip() for line in raw_data.strip().split('\n')]))
    headers = rawDataToJson.rawDataToJson(raw_data)
    # Note: This approach assumes your rawDataToJson function expects a string input and returns a dictionary.

    res = requests.post(url_, headers=headers, json=data, verify=False)
    print(res.json()['data']['token'])
    return res.json()['data']

login()
