#encoding=utf-8
'''
Created on 2016年12月27日

@author: heyker
'''
class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        remainder={0:-1}
        csum=0
        if k<0:
            k*=-1
        for i in range(0,len(nums)):
            csum+=nums[i]
            r=csum
            if k>0:
                r=csum%k 
            if r in remainder:
                if i-remainder[r]>1:
                    #print i,remainder[r],r
                    return True
            else:
                remainder[r]=i
            #print i,csum,remainder
        return False
if __name__ == '__main__':
    s=Solution()
    nums=[23, 2, 6, 4, 7];  k=6
    print s.checkSubarraySum([1,0],0)
    pass

