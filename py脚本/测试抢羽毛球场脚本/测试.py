import requests

# 定义请求的参数
date = "2023-10-19"  # 示例日期
serviceid = "1"  # 替换为您的服务ID
coordinatedes = ""  # 替换为您的协调描述

# 构建请求的参数字典
param = {
    "s_dates": date,
    "serviceid": serviceid,
    "coordinatedes": coordinatedes
}

# 发送GET请求模拟AJAX请求
url = "http://http://ydfwpt.cug.edu.cn//product/getarea"  # 替换为实际的URL
response = requests.get(url, params=param)

# 如果请求成功 (HTTP状态码为200)
if response.status_code == 200:
    # 处理响应内容
    response_content = response.content
    # 在这里处理响应内容，可以是HTML或者其他数据格式
    print(response_content)
else:
    print("AJAX request failed with status code:", response.status_code)
