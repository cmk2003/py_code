import string
#if语句
#a=int(input("请输入a: "))
#b=int(input("请输入b: "))
a=5
b=4
c=10
if a>b and c>11:
    print("a>b")
elif a<b:
    print("a<b")
else:
    print("a=b")

#while循环
i=1
while i<7:
    print(i,end=" ")
    i +=1
print()
i=0
while i<7:
    i += 1
    if i == 4 :
        continue
    if i == 5 :
        break
    print(i,end=" ")
print()
#for循环
#列表
fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)
#   if x == "banana":
#     break
# for x in "bananxxx":
#     print(x,end=' ')
#
# for x in range(10):
#     print(x,end=' ')
print(fruits[-2:])
fruits.append(123)
fruits1=fruits
print(fruits)
del fruits[1]
print(fruits)
