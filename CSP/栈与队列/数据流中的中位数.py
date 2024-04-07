import queue

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.init_queue=[]#原始队列
        self.sort_queue=[]#排序队列





    def addNum(self, num: int) -> None:
        temp_queue=queue.deque()
        self.init_queue.append(num)
        if not self.sort_queue:
            self.sort_queue.append(num)
            return
        while  self.sort_queue and num > self.sort_queue[-1]:
            temp_queue.append(self.sort_queue.pop())
        self.sort_queue.append(num)
        temp_queue.reverse()
        self.sort_queue+=temp_queue



    def findMedian(self) -> float:
        #求中位数
        if len(self.sort_queue)%2==0:
            #是一个偶数
            pos=int(len(self.sort_queue)/2)
            return float((self.sort_queue[pos]+self.sort_queue[pos-1])/2)
        else:return self.sort_queue[int((len(self.sort_queue)-1)/2)]



# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
obj.addNum(3)
print(obj.sort_queue)
param_2 = obj.findMedian()
print(param_2)