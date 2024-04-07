n,a,b=map(int,input().split())

#每个矩形的坐标
juxing_pos=[]
sum=0
for i in range(n):
    x_1,y_1,x_2,y_2=map(int,input().split())
    # temp=[[x_1,y_1],[x_2,y_1],[x_2,y_2],[x_1,y_2],"未知"]#记录坐标位置
    temp=[[x_1,x_2],[y_1,y_2]]
    juxing_pos.append(temp)

#计算重合的长度0 a  0 b
for i in range(len(juxing_pos)):
    #算X的长度
    x1,x2=0,0
    x_len=0
    if juxing_pos[i][0][0]<=0:
        x1=0
        if a>=juxing_pos[i][0][1]>=0:
            x2=juxing_pos[i][0][1]
            x_len=x2-x1
        if juxing_pos[i][0][1]>a:
            x2=a
            x_len=x2-x1
    if 0<juxing_pos[i][0][0]<=a:
        x1=juxing_pos[i][0][0]
        if a>=juxing_pos[i][0][1]>=0:
            x2=juxing_pos[i][0][1]
            x_len=x2-x1
        if juxing_pos[i][0][1]>a:
            x2=a
            x_len=x2-x1

    # print(x_len)
    #计算y

    x11, x21 = 0, 0
    y_len = 0
    if juxing_pos[i][1][0] <= 0:
        x11 = 0
        if b >= juxing_pos[i][1][1] >= 0:
            x21 = juxing_pos[i][1][1]
            y_len = x21 - x11
        if juxing_pos[i][1][1] > b:
            x21 = b
            y_len = x21 - x11
    if 0 < juxing_pos[i][1][0] <= b:
        x11 = juxing_pos[i][1][0]
        if b >= juxing_pos[i][1][1] >= 0:
            x21 = juxing_pos[i][1][1]
            y_len = x21 - x11
        if juxing_pos[i][1][1] > b:
            x21 = b
            y_len = x21 - x11
    sum+=x_len*y_len

    # print(y_len)
    # print("====")

print(sum)

