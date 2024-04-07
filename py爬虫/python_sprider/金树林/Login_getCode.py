import requests
from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings

disable_warnings(InsecureRequestWarning)  # Disable warnings about insecure requests

import requests

url = 'https://miappshop.jshulin.com/memberLogin/phoneCode?phone=15572261989&serviceType=6'
cookies = {
    'Mobile-Token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxNzc1MzI5MjYxNDI3MDIzODc0IiwiZXhwIjoxNzEyMTEwMDU0LCJpYXQiOjE3MTIxMDY0NTQsInVzZXJJZCI6IjE3NzUzMjkyNjE0MjcwMjM4NzQiLCJ1c2VybmFtZSI6IjE1NTcyMjYxOTg5In0.PwBPIsN-dH4v4Ysf8htMTYXyqnd4HS1JoZNmKd9B7ZA'
}

headers = {
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 9; SKW-A0 Build/PQ3A.190605.10261546; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.114 Mobile Safari/537.36 uni-app Html5Plus/1.0 (Immersed/24.0)'
}

# Assuming you're making a GET request; change to post(), etc., as necessary
response = requests.get(url, headers=headers, cookies=cookies)

print(response.text)
