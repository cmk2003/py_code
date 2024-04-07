n, m = map(int, input().split())
p = [0] + [i for i in map(int, input().split())]
t = [0] + [i for i in map(int, input().split())]
earliest = [0 for _ in range(m + 1)]
latest = [0 for _ in range(m + 1)]
mark = 1
# 将每个科目的最早时间确定
for i in range(1, m + 1):
    if p[i] == 0:
        earliest[i] = 1
    else:
        earliest[i] = earliest[p[i]] + t[p[i]]
    # 判断所有科目最早开始的情况是否可以完成所有科目
    if earliest[i] + t[i] - 1 > n:
        mark = 0
# 输出每项科目的最早开始时间
print(*earliest[1:])

# 判断是否可以完成项目
# if mark == 1:
    # 将确定每个科目的最晚，从最后的科目往前推，需要把依赖该科目的科目所消耗时间算上
for i in range(m, 0, -1):
    temp = 366
    for j in range(i + 1, m + 1):
        # 寻找是否有依赖该科目的科目
        if p[j] == i:
            temp = min(temp, latest[j])
    # 如果没有被依赖，那么最晚开始时间 = 最后期限 - 持续时间的时刻
    if temp == 366:
        latest[i] = n - t[i] + 1
    # 如果有被依赖，那么最晚开始时间 = 依赖它的科目的最晚开始的时刻最小的科目 - 本身的持续时间的时刻
    else:
        latest[i] = temp - t[i]
# 输出每项科目的最早开始时间
print(*latest[1:])