n,d=map(int,input().split())
# print(n,d)
juzhengQ=[]
for i in range(n):
    hang=[]
    for i in input().split():
        hang.append(int(i))
    juzhengQ.append(hang)

juzhengK=[]
for i in range(n):
    hang=[]
    for i in input().split():
        hang.append(int(i))
    juzhengK.append(hang)

juzhengV=[]
for i in range(n):
    hang=[]
    for i in input().split():
        hang.append(int(i))
    juzhengV.append(hang)
xiangliangw=[]
for i in input().split():
    xiangliangw.append(int(i))

# k的转置
juzhengK_t=[]
for i in range(d):
    templine=[]
    for j in range(n):
        templine.append(juzhengK[j][i])
    juzhengK_t.append(templine)

#计算k的转置*V
res=[]
for i in range(d):
    templine=[]
    for j in range(d):
        temp = 0
        for k in range(n):
            temp+=juzhengK_t[i][k]*juzhengV[k][j]
        # print(temp)
        templine.append(temp)
    res.append(templine)

#计算w*Q*res
res1=[]
for i in range(n):
    templine=[]
    for j in range(d):
        temp = 0
        for k in range(d):
            temp+=juzhengQ[i][k]*res[k][j]
        # print(temp)
        templine.append(temp)
    for w in range(len(templine)):
        templine[w] *= xiangliangw[i]
        # print(templine[w])
        # print(w)
    res1.append(templine)







for i in range(len(res1)):
    for j in range(len(res1[i])):
        print(res1[i][j],end=" ")
    print()