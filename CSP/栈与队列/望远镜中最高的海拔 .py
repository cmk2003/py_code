import collections
from typing import List
class Solution:
    def maxAltitude(self, heights, limit: int) -> List[int]:
        dqune=collections.deque()
        res=[]
        for i,j in zip(range(1-limit,len(heights)),range(len(heights))):
            print(i,j)
            if i>0 and dqune[0]==heights[i-1]:dqune.popleft()#滑动窗口没有这个数字了
            # while dqune and heights[j]>dqune[-1]:dqune.pop()#如果来了一个小的，那么就往后加，万一这个小的是后面大的
            # dqune.append(heights[j])
            if dqune and heights[j]>dqune[-1] :
                while dqune:
                    dqune.pop()
                dqune.append(heights[j])
            else:dqune.append(heights[j])
            if i>=0:
                res.append(dqune[0])

        return res




so=Solution()
print(so.maxAltitude([1,3,1,2,0,5],1))
