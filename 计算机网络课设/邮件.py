from socket import *
# from tkinter import*
# from tkinter import messagebox
from email.parser import Parser
import poplib
from email.header import decode_header
from email.utils import parseaddr
import base64
import re


# y邮箱服务商
def send():
    mailserver = "smtp.qq.com"
    # myname = "1657299258@qq.com"
    # mypassword = "asdfghjkl4"#独立密码
    # user = '1657299258'
    username = 'MTY1NzI5OTI1OA=='
    #pass="alyxvzpugztccbdb"
    password = 'YWx5eHZ6cHVnenRjY2JkYg=='

    # 发送方和接受方地址
    fromaddress = '1657299258@qq.com'
    # fromaddress=sender
    # 建立一个tcp套接字,
    serverport = 25
    clientsocket = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP)
    # 建立连接
    clientsocket.connect((mailserver, serverport))
    # 确认服务器已经准备就绪,decode()是对base64的解码
    recv1 = clientsocket.recv(1024).decode()
    # print(recv1)
    if '220' != recv1[:3]:
        print('服务器还没准备好')

    # 发送HELO命令标识发件人自己的身份，信息要加密之后再传输
    hellomessage = 'HELO  Alice\r\n'
    clientsocket.send(hellomessage.encode())
    recv2 = clientsocket.recv(1024).decode()
    # print(recv2)Text = "密码：",
    if '250' != recv2[:3]:
        print('服务器没有收到邮件')

    # userna = input("请输入用户名：")
    # # userna=1657299258#smtp用户名
    # userpad = input("请输入用户密码：")
    # # userpad='alyxvzpugztccbdb'#smtp用户密码
    # # if (userna == myname and userpad == mypassword):
    # #     string = str("登录成功")
    # #     print(string)
    # # else:
    # #     print("密码错误，重新登录")
    # #     return

    # 使用AUTH登录smtp服务器，用户名和密码都要加密
    clientsocket.sendall('AUTH LOGIN\r\n'.encode())
    recv3 = clientsocket.recv(1024).decode()
    # print(recv3)
    if '334' != recv3[:3]:
        print('服务器未响应验证字符串')
    clientsocket.sendall((username + '\r\n').encode())
    recvname = clientsocket.recv(1024).decode()#响应数据
    # print(recvname)
    if '334' != recvname[:3]:
        print('服务器未响应验证字符串')
    clientsocket.sendall((password + '\r\n').encode())
    recvpass = clientsocket.recv(1024).decode()
    # print(recvpass)
    if '235' != recvpass[:3]:
        print('权限验证失败')
    else:
        print('已经连接上smtp服务')

    # toaddress = input("请输入收件人邮箱地址:")
    toaddress='15572261989@163.com'
    # toaddress=receiver
    def juestemail(address):
        pattern = r'^[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}$'
        adr = address
        while 1:
            if re.match(pattern, adr):
                print("邮箱地址有效")
                break
            else:
                adr = input("邮箱地址无效,请重新输入:")
        return adr

    toaddress = juestemail(toaddress)

    # 发送MAIL
    clientsocket.sendall(('MAIL FROM: <' + fromaddress + '>\r\n').encode())
    recvfrom = clientsocket.recv(1024).decode()
    # print(recvfrom)
    if '250' != recvfrom[:3]:
        print('服务器没有收到邮件')

    # 发送一个或者多个rcpt命令,收到ok响应表示服务器愿意帮用户发送邮件
    clientsocket.sendall(('RCPT TO: <' + toaddress + '> \r\n').encode())
    recvto = clientsocket.recv(1024).decode()
    # print(recvto)
    if '250' != recvto[:3]:
        print('服务器未收到邮件')

    # 发送DATA,返回354，以“.”结束
    clientsocket.sendall('DATA\r\n'.encode())
    recvdata = clientsocket.recv(1024).decode()
    # print(recvdata)
    if '354' != recvdata[:3]:
        print('暂时不可以发生邮件内容')
    else:
        # print('请填写邮件内容')
        print("")

    # 标题
    Subject = input("请输入标题:")
    # Subject=header
    # 请求和响应中媒体类型消息
    contentType = 'text/plain'
    # contentType = 'image/jpg'
    masg = input("请输入正文内容:")
    # masg=content
    message = 'from: ' + fromaddress + '\r\n'
    message += 'to: ' + toaddress + '\r\n'
    message += 'subject: ' + Subject + '\r\n'
    message += 'Content-Type: ' + contentType + '\t\n'
    message += '\r\n' + masg
    clientsocket.sendall(message.encode())

    # 结束。以“.”结束返回250
    clientsocket.sendall('\r\n.\r\n'.encode())
    recvend = clientsocket.recv(1024).decode()
    # print(recvend)
    if '550' == recvend[:3]:
        print('发送失败，邮件地址不存在')
    elif '554 ' == recvend[:3]:
        print('邮件被认定服务器为垃圾邮件')

    elif '250' == recvend[:3]:
        print('发送成功')
    clientsocket.sendall('QUIT\r\n'.encode())
    clientsocket.close()


temp=[]
def print_info(msg, indent=0):

    if indent == 0:
        for header in ["From", "To", "Subject"]:
            value = msg.get(header, "")
            if value:
                if header == "Subject":
                    value = decode_str(value)
                    global temp
                    temp.append(value)
                else:
                    hdr, addr = parseaddr(value)
                    name = decode_str(hdr)
                    value = f"{name} <{addr}>"
            print(f"{'  ' * indent}{header}: {value}")
    if msg.is_multipart():
        parts = msg.get_payload()
        for n, part in enumerate(parts):
            print(f"{'  ' * indent}part {n}")
            print(f"{'  ' * indent}--------------------")
            print_info(part, indent + 1)
    else:
        content_type = msg.get_content_type()
        if content_type == "text/plain" or content_type == "text/html":
            content = msg.get_payload(decode=True)
            charset = guess_charset(msg)
            if charset:
                content = content.decode(charset)
            print(f"{'  ' * indent}Text: {content}")
            temp.append(content)
        else:
            print(f"{'  ' * indent}Attachment: {content_type}")


def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value


def guess_charset(msg):
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
    return charset


def recive():
    # 输入邮件地址, 口令和POP3服务器地址:
    email = '1657299258@qq.com'
    password = 'alyxvzpugztccbdb'
    pop3_server = 'pop.qq.com'

    # 连接到POP3服务器:
    server = poplib.POP3_SSL(pop3_server)
    # 可以打开或关闭调试信息:
    server.set_debuglevel(1)
    # 身份认证:
    server.user(email)
    server.pass_(password)
    # list()返回所有邮件的编号:
    resp, mails, octets = server.list()
    # 获取最新一封邮件, 注意索引号从end开始:
    index = len(mails)
    resp, lines, octets = server.retr(index)
    # lines存储了邮件的原始文本的每一行,
    # 可以获得整个邮件的原始文本:
    msg_content = b'\r\n'.join(lines).decode('utf-8')
    print("msg_content",msg_content)
    # 稍后解析出邮件:
    msg = Parser().parsestr(msg_content)
    # print("-------------------------------------------------------------------------------------------------------------")
    print("msg",msg)
    # print("-------------------------------------------------------------------------------------------------------------")
    print_info(msg)
    # print("var", var)
    # 解析
    # 可以根据邮件索引号直接从服务器删除邮件:
    # server.dele(index)
    # 关闭连接:
    server.quit()
    return


print("1.发邮件        2.收邮件        0.退出")

while 1:
    sendorrecive = input("请输入功能号：")
    if sendorrecive == '1':
        send()
    elif sendorrecive == '2':
        recive()
        # print('temp',temp)
    else:
        break

var=recive()

