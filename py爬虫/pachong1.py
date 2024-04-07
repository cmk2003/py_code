import requests
from bs4 import BeautifulSoup
from email.mime.text import MIMEText
from email.header import Header
import smtplib
def request_page(url,headers):
    response = requests.get(url,headers=headers)
    response.encoding = response.apparent_encoding
    return response.text

def parse_page(html):

    soup = BeautifulSoup(html, 'html.parser')

    data = ''
    all_topics = soup.find_all(class_='category-wrap_iQLoo horizontal_1eKyQ')
    for each_topic in all_topics:
        topic_times = each_topic.find('div', class_='hot-index_1Bl1a')  # 搜索指数
        topic_name = each_topic.find('div', class_='c-single-text-ellipsis')  # 标题
        topic_rank = each_topic.find(["a" , "div"]) # 排名
        if  topic_rank !=None and topic_name!=None and topic_times!=None:
            topic_rank = each_topic.find(["a" , "div"]).get_text().replace(' ', '').replace('\n', '')
            topic_name = each_topic.find('div', class_='c-single-text-ellipsis').get_text().replace(' ', '').replace('\n', '')
            topic_times = each_topic.find('div', class_='hot-index_1Bl1a').get_text().replace(' ', '').replace('\n', '')
            tplt = "排名：{0:^4}\t标题：{1:{3}^15}\t热度：{2:^8}"
            data = data + '\n'+tplt.format(topic_rank, topic_name, topic_times, chr(12288))
    return data


def create_content():
    url = 'https://top.baidu.com/board?tab=realtime'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0'}
    html = request_page(url, headers)
    data = parse_page(html)
    msg = MIMEText(data,'plain','utf-8')
    msg["Subject"]=Header('百度热搜','utf-8')
    return msg

def send_message():
    from_addr = input('请输入发送邮箱：')
    pwd = input('请输入验证码：')
    to_addr = input('请输入接收邮箱：')

    stmp = smtplib.SMTP()
    stmp.connect('smtp.qq.com',25)

    stmp.login(from_addr,pwd)
    content = create_content()
    stmp.sendmail(from_addr,to_addr,content.as_string())

    stmp.quit()
    print('successful')

if __name__=='__main__':
    send_message()