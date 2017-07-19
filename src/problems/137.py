#encoding=utf-8
'''
Created on 2016年12月22日
@author: heyker
'''
class Solution(object):
    def int_overflow(self,val):  
        maxint = 2147483647  
        if not -maxint-1 <= val <= maxint:  
            val = (val + (maxint + 1)) % (2 * (maxint + 1)) - maxint - 1  
        return val 
    def singleNumber1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret=0
        #bitnum=[0]*32
        for i in range(0,32):
            bn=0
            for j in nums:
                bn+=((j>>i)&1)
            if bn%3==1:
                ret|=(1<<i)
        return self.int_overflow(ret)
    def singleNumber(self, nums):
        r1=0;r2=0;r3=0;
        for i in nums:
            r2|=(r1&i);r1^=i;r3=r1&r2;
            r1&=~r3;r2&=~r3;
        return r1
if __name__ == '__main__':
    s=Solution()
    preorder=[-2,-2,1,1,-3,1,-3,-3,-4,-2]
    print s.singleNumber(preorder)
    pass