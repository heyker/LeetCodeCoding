#encoding=utf-8
'''
Created on 2016年12月22日
@author: heyker
'''
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret=0
        curidx=0
        maxidx=0
        ll=len(nums)
        for i in range(ll):
            if curidx<i:
                ret+=1
                curidx=maxidx
            k=nums[i]+i
            if k>maxidx:
                maxidx=k
        return ret
if __name__ == '__main__':
    s=Solution()
    A = [2,3,1,1,4]
    print s.jump(A)
    pass