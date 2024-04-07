class MinStack:

    def __init__(self):
        self.stack=[]
        self.minStack=[]


    def push(self, x: int) -> None:
        self.stack.append(x)
        if len(self.minStack)==0:
            self.minStack.append(x)
        else:
            if x<=self.minStack[-1]:
                self.minStack.append(x)


    def pop(self) -> None:
        temp=self.stack.pop()
        if temp==self.minStack[-1]:
            self.minStack.pop()

    def top(self) -> int:
        temp=self.stack.pop()
        self.stack.append(temp)
        return temp

    def getMin(self) -> int:
        if len(self.minStack)!=0:
            return self.minStack[-1]



# Your MinStack object will be instantiated and called as such:
obj = MinStack()
min=obj.getMin()
print(min)
obj.push(-2)
obj.push(2)
obj.push(-3)
print("11111")
print(obj.minStack)
min=obj.getMin()
print(min)
obj.pop()
param_3 = obj.top()
print(param_3)
min=obj.getMin()
print(min)
print(obj.stack)

# param_4 = obj.getMin()