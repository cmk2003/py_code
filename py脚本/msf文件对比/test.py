with open('1.list', 'r') as file:
    # 读取原始文件的所有行
    lines = file.readlines()

# 获取奇数行的内容
odd_lines = [line.strip() for index, line in enumerate(lines, start=1) if index % 2 != 0]

# 打开新文件并写入奇数行的内容
with open('msf.list', 'w') as new_file:
    # 将奇数行的内容写入新文件
    for line in odd_lines:
        new_file.write(line + '\n')

