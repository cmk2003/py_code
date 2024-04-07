import requests

# 目标URL
url = 'http://ydfwpt.cug.edu.cn/login.html'

# 发送GET请求
session  = requests.Session()
response=session.get(url)
print(session.cookies)
# 获取JSESSIONID
jsessionid = None
if 'JSESSIONID' in session.cookies:
    jsessionid = session.cookies['JSESSIONID']

if jsessionid:
    print('JSESSIONID:', jsessionid)
else:
    print('未找到JSESSIONID')