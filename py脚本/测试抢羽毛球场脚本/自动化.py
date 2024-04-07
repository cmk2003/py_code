import json

# 原始JSON数据
json_data = '{"stockdetail":{"12731":"123534","12732":"123553"},"serviceid":"1","stockid":"12732,","remark":""}'
#json_data = '{"stockdetail": { "12708": "123100", "12709": "123119"}, "serviceid": "1", "stockid": "12709,", "remark": ""}'

###两个小时变成三个小时
data = json.loads(json_data)
stock_id_12703 = data.get("stockid").strip(",")
modified_value = str(int(stock_id_12703) - 2)
print(modified_value)

value_122983 = str(int(data["stockdetail"][stock_id_12703])-38)
print("value_122983",value_122983)

data["stockdetail"][str(modified_value)] = value_122983

# 按照stockdetail字典的键进行排序
sorted_stockdetail = {k: data["stockdetail"][k] for k in sorted(data["stockdetail"])}

# 更新data字典中的stockdetail键
data["stockdetail"] = sorted_stockdetail

# 将字典转换为JSON字符串
sorted_json_data = json.dumps(data)

# 打印更新后的JSON字符串
print(sorted_json_data)


# # 循环遍历stockdetail字典，将所有值加一
# for key in data['stockdetail']:
#     data['stockdetail'][key] = str(int(data['stockdetail'][key]) + 1)
# encoded_string1 = json.dumps(data)
# print('456',encoded_string1)
#
# for key in data['stockdetail']:
#     data['stockdetail'][key] = str(int(data['stockdetail'][key]) + 1)
# encoded_string2 = json.dumps(data)
# print('789',encoded_string2)
###一个场变成三个场
data = json.loads(sorted_json_data)
print(data)
encoded_string = json.dumps(data)
print('123',encoded_string)
payload = []
payload.append(encoded_string)
for i in range(3):
    for key in data['stockdetail']:
        data['stockdetail'][key] = str(int(data['stockdetail'][key]) + 1)
    encoded_string1 = json.dumps(data)
    payload.append(encoded_string1)
    print(encoded_string1)

for i in payload:
    print("kkkk",i)
# print('hhhh',payload)