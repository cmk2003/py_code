class Solution:
    def myAtoi(self, str) -> int:
        str=str.strip()
        if str=='' :return
        res,sign,i=0,1,1
        int_max, int_min, bndry = 2 ** 31 - 1, -2 ** 31, 2 ** 31 // 10
        if(str[0]=='-'):sign=-1
        elif(str[0]!='+'):#说明是正数
            i=0
        for c in str[i:]:
            if not '0'<=c<='9':
                #不是数字就退出
                break
            if res > bndry or res == bndry and c > '7': return int_max if sign == 1 else int_min  # 数字越界处理
            res=10*res+ord(c)-ord('0')

        print(sign*res)


if __name__=="__main__":
    so = Solution()
    str=so.myAtoi("   42")