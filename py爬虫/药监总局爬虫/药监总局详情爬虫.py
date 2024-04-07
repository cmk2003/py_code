import requests
import json
if __name__=="__main__":
    url='https://www.nmpa.gov.cn/datasearch/search-result.html'
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.78 Safari/537.36'
    }
    page_text = requests.get(url=url,headers=header).text

    fp = open('./1.html', 'w', encoding='Utf-8')
    json.dump(page_text, fp=fp, ensure_ascii=False)
