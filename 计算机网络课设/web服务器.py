import socket
import os
def handle_request(client_socket):
    request_data = client_socket.recv(1024).decode()  # 接收客户端请求数据

    # 解析请求数据，获取请求方法和URL
    request_lines = request_data.split("\r\n")
    print(request_lines)
    request_line = request_lines[0]
    print(request_line)
    method, url, protocol = request_line.split(" ")
    # 处理请求，根据URL获取文件内容
    if method == "GET":
        if url == "/":
            filename = "index.html"  # 默认主页文件
        else:
            filename = url[1:]  # 去除URL中的"/"，获取实际文件名
            print("filename=",filename)

        if os.path.exists(filename):
            with open(filename, "rb") as file:
                response_data = file.read()
            response_header = "HTTP/1.1 200 OK\r\n\r\n".encode()
        else:
            with open("404.html", "rb") as file:
                response_data = file.read()
            response_header = "HTTP/1.1 404 Not Found\r\n\r\n".encode()
    elif method == "POST":
        # Extract the request body
        body_start = request_data.index("\r\n\r\n") + 4 #找到请求体的具体位置
        request_body = request_data[body_start:]#
        print("Request Body:", request_body)#
        for i in range(0,len(request_body)-2):
            # print(request_body[i])
            if request_body[i]=="=":
                request_body=request_body[i+1:]
                break
        if os.path.exists(request_body):
            with open(request_body, "rb") as file:
                response_data = file.read()
            response_header = "HTTP/1.1 200 OK\r\n\r\n".encode()
        else:
            with open("404.html", "rb") as file:
                response_data = file.read()
            # response_header = "HTTP/1.1 200 OK\r\n\r\n".encode()
            # response_data = b"<html><body ><h1>404 NOT FOUND</h1></body></html>"
            response_header = "HTTP/1.1 404 Not Found\r\n\r\n".encode()
    else:
        response_data = b""
        response_header = "HTTP/1.1 501 Not Implemented\r\n\r\n".encode()


    # 发送响应数据
    client_socket.send(response_header + response_data)
    client_socket.close()

def run_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("127.0.0.1", 8600))  # 绑定服务器地址和端口
    server_socket.listen(50)  # 监听连接请求，最大连接数为5

    print("目标网站： http://127.0.0.1:8600")

    while True:
        client_socket, addr = server_socket.accept()  # 接受客户端连接请求
        handle_request(client_socket)

if __name__ == "__main__":
    run_server()
