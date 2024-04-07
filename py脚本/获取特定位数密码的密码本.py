import random

# 生成长度为5的随机密码
for i in range(1,10000):
    password = ''.join(random.sample('0123456789', 5))
    # 打印生成的随机密码
    print(password)