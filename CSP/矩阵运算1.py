import numpy as np

n,d=map(int,input().split())

juzhengQ=[]
for i in range(n):
    hang=[]
    for i in input().split():
        hang.append(int(i))
    juzhengQ.append(hang)
matrixQ=np.array(juzhengQ)
juzhengK=[]
for i in range(n):
    hang=[]
    for i in input().split():
        hang.append(int(i))
    juzhengK.append(hang)
matrixK=np.array(juzhengK)
juzhengV=[]
for i in range(n):
    hang=[]
    for i in input().split():
        hang.append(int(i))
    juzhengV.append(hang)
matrixV=np.array(juzhengV)

xiangliangw=[]
for i in input().split():
    xiangliangw.append(int(i))

#w矩阵转置
juzhengK_T=[]
for j in range(d):#列
    templine=[]
    for i in range(n):#行
        templine.append(juzhengK[i][j])
    juzhengK_T.append(templine)
matrixk_T=np.array(juzhengK_T)

#乘法
res=np.dot(matrixQ,matrixk_T)

for i in range(n):
    res[i]=res[i]*xiangliangw[i]

res=np.dot(res,matrixV)


for i in range(len(res)):
    for j in range(len(res[i])):
        print(res[i][j],end=" ")
    print()