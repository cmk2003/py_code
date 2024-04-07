# 定义一个变量
import random
import math
random1=[]
for i in range(100):

    if len(random1)==4:
        break
    temp=random.randint(2,31)
    if temp== 24 or temp==25:
        continue
    if temp in random1:
        continue
    else:random1.append(temp)

print(random1," ")

a=math.getprime(100)
print(a)
# print(pow(2,1024,))
