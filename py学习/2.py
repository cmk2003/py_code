#包含随机数的库
import random
import string
#type
num = 10
print(type(num))
list_a = ["1","2","3"]
print(type(list_a))

#强制类型转换
x = 10

print(x)
print(type(x))
#随机数
cmk_age=random.randrange(14,20)
print(cmk_age)

#使用三个双引号定义一个多行的变量
a = """  AAAAaaaa Python is a widely used general-purpose, high level programming language. 
It was initially designed by Guido van Rossum in 1991 
and developed by Python Software Foundation. 
It was mainly developed for emphasis on code readability, 
and its syntax allows programmers to express concepts in fewer lines of code   .    """
print(a)
print(a[0:2])#从0到1，不包括1，
print("字符串长度为：%.i"%len(a),end='  ')
print("zif",len(a))
x=3.2
#有精度的输出
print("字符串长度为1：%.2f"%x)
#输出大小写
print('小写',a.lower())
print("大写",a.upper())
#输出把前后的空格给去掉
print('去掉空格',a.strip())

#字符串拆解
b = a.split(' ')
print(b)
#删除元素
del b[0]
print(b)
#构造和b一样的数组
bb=b.copy()
#or
bbb=list(b)
#数组排序
#print()
b.sort()
print("升序  ",b)
bb.sort(reverse=True)
print("降序",bb)

#字符串查找,返回bool类型
c = "Py" in a
print(c)
c= a.index("Python")
print(c)
d = "Py" not in a
print(d)

#运算符
e=3**4#幂
f=e//5#整除
print(e)
print(f)