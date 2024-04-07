import requests
import json
if __name__=="__main__":
    url='http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    kw=input('请输入地址：')
    param = {
        'cname':'',
        'pid':'',
        'keyword': kw,
        'pageIndex': '1',
        'pageSize': '10'
    }
    # 2、UA伪装
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.78 Safari/537.36'
    }
    # 3、发起请求
    response = requests.post(url=url, data=param, headers=header)

    list_data=response.text

    # 4持久化存储
    fp = open('./kfc.html', 'w', encoding='Utf-8')
    json.dump(list_data, fp=fp, ensure_ascii=False)
    print("爬取数据结束")