
sentence="&#102;&#108;&#97;&#103;&#123;&#97;&#49;&#55;&#98;&#49;&#99;&#101;&#102;&#50;&#102;&#101;&#51;&#100;&#98;&#99;&#97;&#101;&#53;&#48;&#100;&#102;&#101;&#51;&#57;&#99;&#100;&#56;&#53;&#101;&#53;&#98;&#48;&#125;"

#sentence = "这是一句话；包含了分号；需要被去除。"
new_sentence = sentence.replace(";", " ")
print(new_sentence)
new_sentence = new_sentence.replace("&", "")
new_sentence = new_sentence.replace("#", "")
#new_sentence = new_sentence.replace(" ", "")
print(new_sentence)#转换成以空格为分界的字符串//输出的格式为str 要类型转换的话需要int一下
l=new_sentence.split()
print(l)
text=""
for ascii_val in l:
    char = chr(int(ascii_val))
    text += char

print("ASCII码对应的字符串为：", text)

lst = [int(x) for x in new_sentence.split()]
print(lst)
for ascii_val in lst:
    char = chr(ascii_val)
    text += char

print("ASCII码对应的字符串为：", text)


