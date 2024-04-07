class Solution:
    def dynamicPassword(self, password, target):
        # tmp_str = password[:target]
        # tmp_1_str = password[target:]
        # new_str=tmp_1_str+tmp_str
        # return str(password)
        res=[]
        for i in range(target,len(password)):
            res.append(password[i-1])
        for i in range(target):
            res.append(password[i])
        tmp=''.join(res)
        print(tmp)



if __name__=="__main__":
    so = Solution()
    str=so.dynamicPassword("passwd",5)