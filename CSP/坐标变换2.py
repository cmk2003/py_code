import math

n, m = map(int, input().split());
# print(n,m)
tmp = []


def lashen(x, y, k):
    x = x * k;
    y = y * k;
    return x, y


def xuanzhaun(x, y, th):
    x_new = x * math.cos(th) - y * math.sin(th)
    y_new = x * math.sin(th) + y * math.cos(th)
    return x_new, y_new


for i in range(n):
    op, k_or_th = input().split();
    op = int(op)
    k_or_th = float(k_or_th)
    tmp.append([op, k_or_th])

# print(tmp)
x_new = 0
y_new = 0;
for k in range(m):
    i, j, x, y = map(int, input().split())
    op, k_or_th = tmp[i - 1]
    if i == j:
        if (op == 1):
            # k倍
            x_new, y_new = lashen(x, y, k_or_th)
        if (op == 2):
            # 旋转
            x_new, y_new = xuanzhaun(x, y, k_or_th)
        print(x_new, y_new)
        continue

    if (op == 1):
        # k倍
        x_new, y_new = lashen(x, y, k_or_th)
    if (op == 2):
        # 旋转
        x_new, y_new = xuanzhaun(x, y, k_or_th)
    op, k_or_th = tmp[j - 1]
    if (op == 1):
        # k倍
        x_new, y_new = lashen(x_new, y_new, k_or_th)
    if (op == 2):
        # 旋转
        x_new, y_new = xuanzhaun(x_new, y_new, k_or_th)
    print(x_new, y_new)
