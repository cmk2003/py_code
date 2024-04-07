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

#计算Q*k的转置*w
res=[]
for i in range(n):
    templine=[]
    for j in range(n):
        temp = 0
        for k in range(d):
            temp+=juzhengQ[i][k]*juzhengK_t[k][j]
        # print(temp)
        templine.append(temp)
    for w in range(len(templine)):
        templine[w]*=xiangliangw[i]
    res.append(templine)

#计算 res*V
res1=[]
for i in range(n):
    templine=[]
    for j in range(d):
        temp = 0
        for k in range(n):
            temp+=res[i][k]*juzhengV[k][j]
        # print(temp)
        templine.append(temp)
    res1.append(templine)

for i in range(len(res1)):
    for j in range(len(res1[i])):
        print(res1[i][j],end=" ")
    print()