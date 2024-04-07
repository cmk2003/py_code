n,i=input().split()
n=int(n)
i=float(i)
str=input().split()
total=0
for j in range(n+1):
    total+=int(str[j])*pow(1+i,-j)
    # print(total)
print("%.3f"%total)