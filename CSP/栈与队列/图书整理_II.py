class CQueue:

    def __init__(self):
        self.A, self.B = [], []

    def appendTail(self, value: int) -> None:
        self.A.append(value)

    def deleteHead(self) -> int:
        if len(self.A)==0:
            #A是空，判断B空不空
            if(len(self.B)==0):
                return -1
            return self.B.pop()
        elif len(self.B)==0:
            while self.A:self.B.append(self.A.pop())
        return self.B.pop()



# Your CQueue object will be instantiated and called as such:
obj = CQueue()
obj.appendTail(10)
obj.appendTail(20)
obj.appendTail(30)
param_2 = obj.deleteHead()
print(param_2)
param_3 = obj.deleteHead()
print(param_3)
param_3 = obj.deleteHead()
print(param_3)
param_3 = obj.deleteHead()
print(param_3)