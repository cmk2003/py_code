class Solution:
    def validateBookSequences(self, putIn, takeOut) -> bool:
        chushiStack=[]
        pos=0

        for i in putIn:
            chushiStack.append(i)
            while chushiStack and chushiStack[-1]==takeOut[pos]:
                print('11')
                chushiStack.pop()
                pos=pos+1
        return not chushiStack


so=Solution()
print(so.validateBookSequences([1,2,3,4,5],[4,5,3,2,1]))