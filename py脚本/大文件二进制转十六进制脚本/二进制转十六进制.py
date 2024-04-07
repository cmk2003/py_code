#line = input("请输入一个二进制数：")
# 将二进制数转换为十六进制数
with open('output.txt', 'r') as file:
    data = file.read(8)
    while data:
        #print(data)
        str = hex(int(data, 2))
        str = str.replace('0x', '')
        if str=="0":
            str="0"+str
        if str=="1":
            str="0"+str
        if len(str)==1:
            str = "0" + str
        print(str,end=" ")
        data = file.read(8)



