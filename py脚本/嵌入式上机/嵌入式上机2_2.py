import socket
import ssl

class client_ssl:
    def send(self,):
        # 生成SSL上下文
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
        # 加载信任根证书
        context.load_verify_locations('ca.crt')

        #与服务端建立socket连接
        with socket.create_connection(('172.20.10.5', 7777)) as sock:
        # 将socket打包成SSL socket
        # 一定要注意的是这里的server_hostname不是指服务端IP，而是#指服务端证书中设置的ip。当然，由于实验中证书是由服务端生成的，此处#的ip与服务端ip一致。
            with context.wrap_socket(sock, server_hostname='server') as ssock:
                while True:
            #msg = "do i connect with server ?".encode("utf-8")
                #ssock.send(msg)
            # 接收服务端返回的信息
                #msg = ssock.recv(1024).decode("utf-8")
                #print(f"receive msg from server : {msg}")
                #ssock.close()
                    sendData = input("输入你要发送的消息：")
                    en_sendData=sendData.encode("utf-8")
                    if sendData=="quit":
                        ssock.send(sendData.encode("utf-8"))
                        ssock.close()
                        break
                    ssock.send(en_sendData)
                    recvData = ssock.recv(1024).decode("utf-8")
                    if recvData=="quit":
                        ssock.close()
                        break
                    print("接受到服务器传来的消息：{0}".format(recvData))
if __name__ == "__main__":
    client = client_ssl()
    client.send()