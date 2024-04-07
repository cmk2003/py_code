import requests
import json
if __name__=="__main__":
    #1、目标url
    url='https://movie.douban.com/j/chart/top_list'
    param = {
        'type': '24',
        'interval_id': '100:90',
        'action':'',
        'start': '0',#从数据库的第几部开始取
        'limit': '20'#一次请求取多少个
    }
    #2、UA伪装
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.78 Safari/537.36'
    }
    #3、发请求
    response = requests.get(url=url,params=param,headers=header)

    list_data = response.json();
    # 4持久化存储
    fp = open('./豆瓣.json', 'w', encoding='Utf-8')
    json.dump(list_data, fp=fp, ensure_ascii=False)

    print("爬取数据结束")
