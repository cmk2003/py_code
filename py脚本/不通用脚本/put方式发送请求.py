import requests

url = 'http://node5.anna.nssctf.cn:28558/super-secret-route-nobody-will-guess'
#payload = {'key1': 'value1', 'key2': 'value2'}

response = requests.put(url)

print(response.status_code)
print(response.content)
