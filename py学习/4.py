#类对象
class father:
    x=5
    #内置的_init_()函数
    #每次使用类创建新对象时，都会自动调用 __init__() 函数。
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printname(self):
        print(self.name," ",self.age)
class child(father):#子的 __init__() 函数会覆盖对父的 __init__() 函数的继承。
    def __init__(self,name,age,father):
        self.name = name
        self.age = age


c1 = father("cmk",18)
c1.printname()

