import urllib.parse
import json

# 给定的URL编码字符串
encoded_string = "%7B%22stockdetail%22%3A%7B%2212986%22%3A%22125837%22%2C%2212987%22%3A%22125856%22%7D%2C%22serviceid%22%3A%221%22%2C%22stockid%22%3A%2212987%2C%22%2C%22remark%22%3A%22%22%7D"

# 解码URL编码字符串
decoded_string = urllib.parse.unquote(encoded_string)

# 解析JSON字符串
parsed_json = json.loads(decoded_string)

# 将字典对象转换为JSON字符串，替换单引号为双引号
json_with_double_quotes = json.dumps(parsed_json)

# 打印解析结果
print(json_with_double_quotes)
# {"stockdetail": {"12875": "124303", "12876": "124315"}, "serviceid": "3", "stockid": "12876,", "remark": ""}
# {"stockdetail": {"12675": "122469", "12676": "122488"}, "serviceid": "1", "stockid": "12676,", "remark": ""}
#{"stockdetail": {"12674": "122451","12675": "122470", "12676": "122489"}, "serviceid": "1", "stockid": "12676,", "remark": ""}
#{"stockdetail": {"12674": "122452","12675": "122471", "12676": "122490"}, "serviceid": "1", "stockid": "12676,", "remark": ""}