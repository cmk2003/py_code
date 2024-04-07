import requests
import json
if __name__=="__main__":
    #1、指定url
    post_url='https://fanyi.baidu.com/sug'
    kw=input("请输入词:")
    data = {
        'kw':kw
    }
    #2、UA伪装
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.78 Safari/537.36'
    }
    #3、发起请求
    response = requests.post(url=post_url,data=data,headers=header)
    #因为是json的
    dic_boj=response.json();
    # 4持久化存储
    filename="./"+kw+".json"
    fp = open(filename,'w',encoding='Utf-8')
    json.dump(dic_boj,fp=fp,ensure_ascii=False)

    print("爬取数据结束")
