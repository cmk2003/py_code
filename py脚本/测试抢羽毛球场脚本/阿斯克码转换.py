# 原始字符串
str_original = "7H:Z>6Y+"

print(ord(char) for char in str_original)
# 将每个字符的ASCII码值加上25，并构建新的字符串
str_modified = ''.join(chr(ord(char) + 25) for char in str_original)

# 输出修改后的字符串
print("修改后的字符串:", str_modified)

# 输出修改后的ASCII码值
print("修改后的ASCII码值:")
for char in str_modified:
    print(char, ":", ord(char))
