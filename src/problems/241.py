#encoding=utf-8
'''
Created on 2016年12月27日

@author: heyker
'''
class Solution(object):
    def productExceptSelf(self, inp):
        """
        :type input: str
        :rtype: List[int]
        """
        ret=[]
        ret.append(1)
        for i in range(1,len(inp)):
            ret.append(inp[i-1]*ret[i-1])

        rt=1
        for i in range(len(inp)-1,-1,-1):
            ret[i]*=rt
            rt*=inp[i]
        return ret
            
            
if __name__ == '__main__':
    s=Solution()
    inp=[1,2,3,4]
    print s.productExceptSelf(inp)
    pass

