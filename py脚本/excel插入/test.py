from datetime import datetime

# 给定的日期字符串
date_string = "2004-06-01 00:00:00"

# 将字符串解析为日期对象
date_object = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")

# 提取年份和月份
year = date_object.year
month = date_object.month

# 将年份和月份拼接成所需的格式
formatted_date = f"{year}年{month}月"

# 输出结果
print(formatted_date)
