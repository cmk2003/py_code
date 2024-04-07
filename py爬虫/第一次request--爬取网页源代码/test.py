import requests
if __name__=="__main__":
    #1指定url
    url = 'http://www.news.cn/'
    #2发起请求
    response = requests.get(url=url)
    #3获取响应数据
    page_text = response.text
    print(page_text)
    #4持久化存储
    with open("新华网.html", "w", encoding='utf-8') as fp:
        fp.write(page_text)
    print("爬取数据结束")