#encoding=utf-8
'''
Created on 2016年12月22日
@author: heyker
'''
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        r=0
        for i in nums:
            r^=i
        r&=-r
        r1=0;r2=0;
        for i in nums:
            if r&i==0:
                r1^=i
            else:
                r2^=i
        return [r1,r2]
if __name__ == '__main__':
    s=Solution()
    preorder=[2,1,2,3,4,1]
    print s.singleNumber(preorder)
    pass