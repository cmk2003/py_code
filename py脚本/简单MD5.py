import hashlib

def md5(str):
    m=hashlib.md5()

    m.update(str.encode("utf-8"))

    return m.hexdigest()

str1="/fllllllllllllag"
str2="a9e5390d-4a90-4d74-9b45-f98edb9f2447"+md5(str1)
print(str2)
print(md5(str2))
# for i in range(0,60000):
#     m=str(i)#把数字转换成字符串
#     k=md5(m)[-6:]#后6位，之后根据要求可以改
#     print(k)
#     if k=='8b184b':
#         print(i)
#         break
#
# while 1:
#     m=input("输入值")
#     k=md5(m)
#     print(k)