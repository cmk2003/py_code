def mul_poly(poly1, poly2):
    i = 0
    while i < len(poly1) and poly1[i] == 0:
        i += 1

    poly1 = poly1[i:]
    i = 0
    while i < len(poly1) and poly2[i] == 0:
        i += 1

    poly2 = poly2[i:]

    m = len(poly1)
    n = len(poly2)
    result = [0] * (m + n - 1)

    for i in range(m):
        for j in range(n):
            result[i + j] += poly1[i] * poly2[j]
    result = [x % 2 for x in result]
    result = [0] * (9 - len(result)) + result
    return result

def sub_poly(poly1, poly2):
    i = 0
    while i < len(poly1) and poly1[i] == 0:
        i += 1

    poly1 = poly1[i:]
    i = 0
    while i < len(poly1) and poly2[i] == 0:
        i += 1

    poly2 = poly2[i:]
    result = []
    max_length = max(len(poly1), len(poly2))

    # 补齐多项式长度
    poly1 = [0] * (max_length - len(poly1)) + poly1
    poly2 = [0] * (max_length - len(poly2)) + poly2

    # 逐项相减
    for coeff1, coeff2 in zip(poly1, poly2):
        result.append(coeff1 - coeff2)

    result = [x % 2 for x in result]
    result = [0] * (9 - len(result)) + result
    return result

def add_poly(poly1,poly2):
    poly1 = [0] * (9 - len(poly1)) + poly1
    poly2 = [0] * (9 - len(poly2)) + poly2
    result=[x + y for x, y in zip(poly1, poly2)]
    result = [x % 2 for x in result]
    i = 0
    while i < len(result) and result[i] == 0:
        i += 1

    result = result[i:]
    result = [x % 2 for x in result]
    result = [0] * (9 - len(result)) + result
    return result
def arr_to_poly(poly1):
    i = 0
    while i < len(poly1) and poly1[i] == 0:
        i += 1

    poly1 = poly1[i:]
    n= len(poly1)
    # print(n)
    str=""
    for i in range(0,n):
        if i<n-1 and poly1[i]!=0:
            str+=f"{poly1[i]}*x^{n-1-i} + "
        if i==n-1:
            str += f"{poly1[i]}"
    print(str)

def div_poly(a,b):

    #1、计算q
    pos1,pos2=0,0
    # 遍历列表，如果找到第一个值为 1 的元素，返回它的下标
    for i, x in enumerate(a):
        if x == 1:
            pos1=i
            # print(i)  # 输出下标
            break  # 找到第一个值为 1 的元素后直接退出循环
    for i, x in enumerate(b):
        if x == 1:
            pos2=i
            # print(i)  # 输出下标
            break  # 找到第一个值为 1 的元素后直接退出循环
    q=pos2-pos1
    #扩展成多项式
    # print("pos_q=",q)
    n = 9  # 数组长度
    q = [0] * (n - q - 1) + [1] + [0] * q
    # print("q=",q)
    #2、计算qb
    qb=mul_poly(q,b)
    # print("a=",a)
    # print("b=", b)
    # print("qb=",qb)
    t=sub_poly(a,qb)
    # print("t=",t)

    #判断t和b谁大
    while 1:
        pos1, pos2 = 0, 0
        # 遍历列表，如果找到第一个值为 1 的元素，返回它的下标
        for i, x in enumerate(t):
            if x == 1:
                pos1 = i
                # print(i)  # 输出下标
                break  # 找到第一个值为 1 的元素后直接退出循环
        for i, x in enumerate(b):
            if x == 1:
                pos2 = i
                # print(i)  # 输出下标
                break  # 找到第一个值为 1 的元素后直接退出循环
        if pos1<=pos2:
            # print(1)
            # print("t=", t)
            # print("b=", b)
            pos_m=pos2-pos1
            # print("pos_m=",pos_m)
            # 扩展成多项式
            n = 9  # 数组长度
            m = [0] * (n - pos_m - 1) + [1] + [0] * pos_m
            # print("m=",m)
            mb=mul_poly(m,b)
            # print("t=",t)
            # print("mb=",mb)
            t=sub_poly(t,mb)
            # print("tt=",t)
            if all(x == 0 for x in t):
                print("最后的结果是：", b)
                print("因式为：", end=" ")
                arr_to_poly(b)
                return b

        else:#是ok的
            # print(2)
            yushu=t
            # print("yushu=",yushu)
            div_poly(b,yushu)
            break

def inverse_poly(a,b,x1,x2,x3,x4,judge,mod):
    # print("开始")
    t=[]
    if judge==1:
        x1=[0]*8+[1]
        x2=[0]*9
        t=add_poly(mul_poly(a,x1),mul_poly(b,x2))
        # print(t)
        x3 = [0] * 9
        x4 = [0] * 8 + [1]
        t = add_poly(mul_poly(a, x3), mul_poly(b, x4))
        # print(t)
    #计算q
    pos1, pos2 = 0, 0
    # 遍历列表，如果找到第一个值为 1 的元素，返回它的下标
    for i, x in enumerate(a):
        if x == 1:
            pos1 = i
            # print(i)  # 输出下标
            break  # 找到第一个值为 1 的元素后直接退出循环
    for i, x in enumerate(b):
        if x == 1:
            pos2 = i
            # print(i)  # 输出下标
            break  # 找到第一个值为 1 的元素后直接退出循环
    q = pos2 - pos1
    # 扩展成多项式
    # print("pos_q=", q)
    n = 9  # 数组长度
    q = [0] * (n - q - 1) + [1] + [0] * q
    # print("q=", q)
    # 2、计算qb
    qb = mul_poly(q, b)
    # print("a=", a)
    # print("b=", b)
    # print("qb=", qb)
    t=sub_poly(a,qb)
    # print("t",t)
    tx1=sub_poly(x1,mul_poly(q,x3))
    # print("tx1=",tx1)
    tx2=sub_poly(x2,mul_poly(q,x4))
    # print("tx2",tx2)
    # 判断t和b谁大
    while 1:
        pos1, pos2 = 0, 0
        # 遍历列表，如果找到第一个值为 1 的元素，返回它的下标
        for i, x in enumerate(t):
            if x == 1:
                pos1 = i
                # print(i)  # 输出下标
                break  # 找到第一个值为 1 的元素后直接退出循环
        for i, x in enumerate(b):
            if x == 1:
                pos2 = i
                # print(i)  # 输出下标
                break  # 找到第一个值为 1 的元素后直接退出循环
        if pos1 <= pos2:
            # print("不正常")
            # print("t=", t)
            # print("b=", b)
            pos_m = pos2 - pos1
            # print("pos_m=", pos_m)
            # 扩展成多项式
            n = 9  # 数组长度
            m = [0] * (n - pos_m - 1) + [1] + [0] * pos_m
            # print("m=", m)
            mb = mul_poly(m, b)
            mx1=mul_poly(m,x3)
            # print("mx1=",mx1)
            mx2=mul_poly(m,x4)
            # print("mx2=", mx2)
            t=sub_poly(t,mb)
            tx1=sub_poly(tx1,mx1)
            tx2 = sub_poly(tx2, mx2)
            # print("tt=", t)
            # print("mb=", mb)
            # print("tx1=",tx1)
            # print("tx2=",tx2)
            #t=[0, 0, 0, 0, 0, 0, 0, 0, 1]
            m=[0, 0, 0, 0, 0, 0, 0, 0, 1]
            if t==m:
                print("乘法逆元为：",tx2)
                arr_to_poly(tx2)
                # break
                return tx1

        else:
            # print("正常")
            x1=tx1
            x2=tx2
            inverse_poly(b,t,x3,x4,x1,x2,2,mod)
            break




x1 = [1, 0, 0, 0, 1, 1, 0, 1, 1]
x2 = [0, 1, 0, 0, 0, 0, 0, 1, 1]

# arr_to_poly(x2)
div_poly(x1,x2)

x1 = [0, 0, 1, 1, 1, 1, 1, 1, 1]
x2 = [0, 0, 0, 0, 1, 0, 1, 1, 1]

# arr_to_poly(x2)
div_poly(x1,x2)

x1 = [1, 0, 0, 0, 1, 1, 0, 1, 1]
x2 = [0, 1, 0, 0, 0, 0, 0, 1, 1]
inverse_poly(x1,x2,[0]*8+[1],[0]*9,[0]*9,[0]*8+[1],1,x2)


# m=[0, 0, 1, 0, 0, 0, 1, 1, 1]
# n=[0, 1, 0, 0, 0, 0, 0, 1, 1]
# print(mul_poly(m,n))
# arr_to_poly(mul_poly(m,n))
# # div_poly(m,n)
# m=[1,2,1]
# n=[1,1]
# div_poly(m,n)