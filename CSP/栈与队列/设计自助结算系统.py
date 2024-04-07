import collections
from typing import List
class Checkout:

    def __init__(self):
        self.queue=collections.deque()
        self.maxQueue=collections.deque()#递减的序列

    def get_max(self) -> int:
        if self.maxQueue:
            return self.maxQueue[0]
        return -1

    def add(self, value: int) -> None:
        self.queue.append(value)
        while self.maxQueue and value>self.maxQueue[-1]:
            self.maxQueue.pop()
        self.maxQueue.append(value)



    def remove(self) -> int:
        if len(self.queue)==0: return -1
        if self.maxQueue[0]==self.queue[0] :
            self.maxQueue.popleft()
        return self.queue.popleft()



# Your Checkout object will be instantiated and called as such:
obj = Checkout()
param_1 = obj.get_max()
print(param_1)
obj.add(4)
obj.add(3)
obj.add(7)
obj.add(9)
obj.add(8)
obj.add(6)
obj.add(7)
obj.add(9)
print(obj.queue)
print(obj.maxQueue)
param_1 = obj.get_max()
print(param_1)
param_3 = obj.remove()
print("remove",param_3)
print(obj.queue)
print(obj.maxQueue)

param_3 = obj.remove()
print(obj.queue)
print(obj.maxQueue)
param_1 = obj.get_max()
print(param_1)

param_3 = obj.remove()
print(obj.queue)
print(obj.maxQueue)
param_1 = obj.get_max()
print(param_1)

param_3 = obj.remove()
print(obj.queue)
print(obj.maxQueue)
param_1 = obj.get_max()
print(param_1)