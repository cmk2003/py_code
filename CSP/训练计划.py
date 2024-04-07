n, m = map(int, input().split())
res1 = [i for i in map(int, input().split())]
res2 = [i for i in map(int, input().split())]
# 最早时间
res3 = []
# 最晚时间
res4 = []
# 最早开始时间
for i in range(m):
    res3.append(0)
for i in range(m):
    res4.append(0)

# 最早开始时间
for i in range(m):
    if res1[i] == 0:
        # print(1,end=" ")
        res3[i] = 1
    else:
        res3[i] = res2[res1[i] - 1] + res3[res1[i] - 1]
print(*res3)

# 最晚开始的时间
for i in range(m):
    if res1[i] == 0:
        res4[i] = n + 1 - res2[i]
    else:
        pass
for i in range(m):
    if res1[i] == 0:
        res4[i] = n + 1 - res2[i]
    else:
        res4[i]=n+1-res2[i]
    value = 0
    temp = 366
    #寻找是否有依赖于该科目的科目
    for k in range(m):
        #i=0,k=1,find 1
        if res1[k] == i + 1:
            temp = min(temp, res4[j])

    if tmp != []:
        value = max(tmp)
    #寻找依赖链

    res4[i] = res4[i] - value
    # if res4[i]<=res4[res1[i]-1] and i>0:
    #     break


print(*res4)
