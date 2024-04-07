import requests
#UA检测机制:如果浏览器检测到不是用户从浏览器上进行输入的话，就会502
#UA伪装:把爬虫伪造成浏览器访问请求，则可以绕过检查机制（加上User-Agent）
if __name__=="__main__":
    #1指定url
    url = 'https://www.sogou.com/web?query=hello'
    header={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.78 Safari/537.36'
    }
    #2处理url携带的参数：封装到字典
    kw=input("enter a word:")
    param={
        'query' : kw
    }
    #3发起请求
    response = requests.get(url=url,params=param,headers=header)
    #4响应数据
    page_text = response.text

    # 4持久化存储
    filename=kw+'.html'
    with open(filename, "w", encoding='utf-8') as fp:
        fp.write(page_text)
    print("爬取数据结束")
