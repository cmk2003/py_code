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
    poly1 = [0] * (max_length - len(poly1))+poly1
    poly2 = [0] * (max_length - len(poly2))+poly2
    print("p1",poly1)
    print("p2",poly2)
    # 逐项相减
    for coeff1, coeff2 in zip(poly1, poly2):
        print(coeff1,"  ",coeff2)
        result.append(coeff1 - coeff2)

    # # 去除结果中末尾的零系数
    # while len(result) > 0 and result[-1] == 0:
    #     result.pop()
    print("result=",result)
    result = [x % 2 for x in result]
    result = [0] * (9 - len(result)) + result
    return result


x1 = [0, 0, 0, 0, 1, 1, 1, 0, 1]
x2 = [0, 0, 0, 0, 0, 0, 1, 0, 0]
print(mul_poly(x1,x2))

t= [0, 0, 0, 0, 0, 1, 1, 0, 1]
mb= [0, 0, 0, 0, 0, 1, 0, 0, 0]
t=sub_poly(t,mb)
print("tt=",t)