for i in range(17):
    if 8*i%17==1:
        print(i)


def ModReverse(a, m):
    # Extended Euclidean Algorithm to find modular inverse
    m0, x0, x1 = m, 0, 1

    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0

    return x1 + m0 if x1 < 0 else x1

def Dot_add(x,y):
    if (x!=y):
        k=(((y[1]-x[1])%17)*ModReverse((y[0]-x[0])%17,17))%17
    else:
        k=(((3*pow(x[0],2) + 1)%17)*ModReverse((2*x[1])%17,17))%17
        print(k)
    Rx = (pow(k, 2) - x[0] - y[0])%17
    Ry = (k * (x[0] - Rx) - x[1])%17
    z=[Rx,Ry]
    return z

p=[8,4]
p2=Dot_add(p,p)
p3=Dot_add(p2,p)
p4=Dot_add(p2,p2)
p7=Dot_add(p4,p3)
print(p7)