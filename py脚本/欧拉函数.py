import math


def phi(n):
    amount = 0
    for k in range(1, n + 1):
        if math.gcd(n, k) == 1:
            amount += 1
    return amount


if __name__ == '__main__':

    print(phi(int(2022)))
    print("1",(90+84+140)%105)
    print(math.gcd(7854,2145))
    print(11*2145-3*7854)
    print("12",6**4%41)


    for i in range(999,1101):
        if(i%3==2 and i%5==4 and i%7==6):
            print(i)

    print(((0.2*2+0.19*2+0.5*3+0.11*4)*0.96))