#import math

# 计算 a^b (mod m)
def modPow(a, b, m):

    result = 1
    a = a % m

    while b > 0:
        if b % 2 == 1:
            result = (result * a) % m

        a = (a * a) % m
        b //= 2

    return result
def modee(a: int, b: int, x1: int, x2: int, x3: int, x4: int, judge: int, mod: int) -> int:
    t = 0

    if judge == 1:
        x1, x2 = 1, 0
        t = a  # t = a * x1 + b * x2

        x3, x4 = 0, 1
        t = b  # t = a * x3 + b * x4

    q = a // b
    t = a - q * b
    x1 -= q * x3
    x2 -= q * x4

    if t == 1:
        if x1 < 0:
            x1 += mod
        return x1

    return modee(b, t, x3, x4, x1, x2, 2, mod)
# print(modee(e,m,1,0,0,1,1))

target=[5272281348, 21089283929, 3117723025, 26844144908, 22890519533, 26945939925, 27395704341, 2253724391, 1481682985, 2163791130, 13583590307, 5838404872, 12165330281, 501772358, 7536755222]
m=[]
p = 187963
q = 163841
e = 48611
phi=(p-1)*(q-1)
n=p*q
print(phi)
d=0

d=modee(e,phi,1,0,0,1,1,phi)
print("d=",d)
for i in range(0,len(target)):
    s=modPow(target[i],d,n)
    m.append(s)
print(m)

result = []

for num in m:
    num_str = str(num)
    digits = [int(num_str[i:i+2]) for i in range(0, len(num_str), 2)]
    result.extend(digits)
print(result)

x = [num - 11 for num in result]
print(x)

b = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
s = ""
for i in x:
    s+=b[i]
print(s)

print("mathematics is the queen of science and number theory is the queen of mathematics. c.f. gauss.")
print()
#选做题
def stein_gcd(m, n):
    if m < n:
        return stein_gcd(n, m)

    if n == 0:
        return m

    if m % 2 == 0 and n % 2 == 0:
        return 2 * stein_gcd(m // 2, n // 2)

    if m % 2 == 0 and n % 2 == 1:
        return stein_gcd(m // 2, n)

    if m % 2 == 1 and n % 2 == 0:
        return stein_gcd(m, n // 2)

    return stein_gcd(n, m - n)
result = stein_gcd(48, 18)
result1 = stein_gcd(24, 9)
print("gcd(48, 18)=",result,"gcd(24, 9)=",result1," gcd(48, 18)=2*gcd(24, 9)，当 m 为偶数且 n 为偶数时，gcd(m, n)=2*gcd(m/2, n/2)")  # 输出：6
result = stein_gcd(24, 9)
result1 = stein_gcd(12, 9)
print("gcd(24, 9)=",result,"gcd(12, 9)=",result1," gcd(24, 9)=gcd(12, 9),当 m 为偶数且 n 为奇数时，gcd(m, n)=gcd(m/2, n)")  # 输出：6
result = stein_gcd( 9,24)
result1 = stein_gcd( 9,12)
print("gcd(9,24)=",result,"gcd(9,12)=",result1," gcd(9,24)=gcd( 9,12),当 m 为奇数且 n 为偶数时，gcd(m, n)=gcd(m, n/2)")  # 输出：6
result = stein_gcd( 5,3)
result1 = stein_gcd( 3,2)
print("gcd(5,3)=",result,"gcd(3,2)=",result1," gcd(5,3)=gcd( 3,2),当 m 为奇数且 n 为奇数时，gcd(m, n)=gcd(n, m-n)")  # 输出：6

print()

